import pickle
from sentence_transformers import SentenceTransformer
import faiss

from generator.deepseek import Deepseek


model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("db/index.faiss")

model_service = Deepseek()

with open("db/docs.pkl", "rb") as f:
    docs = pickle.load(f)

def make_finale_prompt(query):
    q_embedding = model.encode([query])
    D, I = index.search(q_embedding, k=6)

    retrieved = [docs[i] for i in I[0]]

    # print(retrieved)
    context = "\n---\n".join(retrieved)

    prompt = f"""
    Ответь на вопрос, используя информацию ниже.

    Контекст:
    {context}

    Вопрос (если в контексте нет нужной информации, ответь сам, но упомняни, что отвечаешь по данным из интернета. Помимо ответа ничего не пиши): {query}
    Ответ (должен звучать как живая речь учителя. Справка. Не делай сравнений. Без заголовков, без упоминаний книги.:
    """

    return prompt


async def get_answer(prompt: str, articles: str = ''):
        """
        Обработка словаря текстов формата {'1': 'текст1', '2': 'текст2', ...}
        """
        try:
            if len(articles) == 0:
                prompt += "Также я дам тебе товарный ряд. Постарайся предлагать людям наши товары, если это возможно: "
            response = model_service.generate_text(prompt, model="deepseek-reasoner")
            # print(response)
            return response.get("data", "{}")
                
        except Exception as e:
            return {
                "error": str(e),
                "summary": "",
                "sentiment": "neutral",
                "key_points": [],
                "entities": []
            }


async def get_answer_from_query(query: str):
    prompt = make_finale_prompt(query)
    return await get_answer(prompt)