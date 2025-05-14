from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Print the environment variable to check if it's loaded
print("HUGGINGFACEHUB_API_TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

result = llm.invoke("What is the capital of India?")
print(result)