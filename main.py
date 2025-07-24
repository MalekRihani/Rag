from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate  
from vector import retriever


model = OllamaLLM(model="llama3.2")

Template="""
you are expert in answering questions about pizza
here same relevant reviews about pizza:{reviews}
here is the question: {question}"""

Prompt = PromptTemplate.from_template(Template)
chain = Prompt | model

while True:
    print("\n\n-----------------------------------------------------------------")
    question = input("Enter your question : ")
    print("\n\n")
    if question == "q":
        break
    reviews = retriever.invoke(question)
    result= chain.invoke({"reviews": [], "question": question})
    print(result)