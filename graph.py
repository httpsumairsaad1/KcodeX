from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="openai/gpt-oss-120b"
)
response = llm.invoke("What is LangGraph? in 1 sentence")
print(response.content)