from langchain_groq import ChatGroq
from pydantic import BaseModel

class EarningsSummary(BaseModel):
    company: str
    eps: float
    summary: str

llm = ChatGroq(
    model_name="openai/gpt-oss-120b"
)

llm_with_output = llm.with_structured_output(EarningsSummary)

response = llm_with_output.invoke("Nvidia reported quarterly EPS of 2.3. Summarize in one line.")

# 6. Access structured fields
print("Company:", response.company)
print("EPS:", response.eps)
print("Summary:", response.summary)
