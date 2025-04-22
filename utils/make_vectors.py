import faiss
import pickle
import os


def make_vectors(model, docs_folder, res_folder="db"):
    os.makedirs(res_folder, exist_ok=True)
    
    docs = []
    for filename in os.listdir(docs_folder):
        file_path = os.path.join(docs_folder, filename)
        if not os.path.isfile(file_path):
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            docs.append(f.read())

    

    embeddings = model.encode(docs, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open(res_folder + "/docs.pkl", "wb") as f:
        pickle.dump(docs, f)
    faiss.write_index(index, res_folder +  "/index.faiss")
