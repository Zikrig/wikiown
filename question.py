import pickle
from sentence_transformers import SentenceTransformer
import faiss


model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("db/index.faiss")


while True:
    query = input("Введите запрос: ")
    # query = "Расскажи про масла с апельсином"

    q_embedding = model.encode([query])
    D, I = index.search(q_embedding, k=10)

    with open("db/docs.pkl", "rb") as f:
        docs = pickle.load(f)

    retrieved = [docs[i] for i in I[0]]
    context = "\n---\n".join(retrieved)

    prompt = f"""
    Ответь на вопрос, используя информацию ниже.

    Контекст:
    {context}

    Вопрос (если в контексте нет нужной информации, ответь сам, но упомяни об этом в конце. Помимо ответа ничего не пиши): {query}
    Ответ (должен звучать как живая речь учителя. Справка. Не делай сравнений. Без заголовков, без упоминаний книги. Имей в виду, что мы продаем духи и ароматические свечи. Возможно, мы сможем сделать кастомный продукт на заказ.):
    """

    print(prompt)