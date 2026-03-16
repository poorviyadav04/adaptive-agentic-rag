from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-opus-4-6",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""
)


generation_chain = prompt | llm | StrOutputParser()