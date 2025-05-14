from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# documents = [
#     "This is a test document.",
#     "This is another test document.",
#     "This is yet another test document."
# ]
# vector = embedding.embed_documents(documents)
# print(str(vector))

text = "This is a test document."

vector = embedding.embed_query(text)
print(str(vector))