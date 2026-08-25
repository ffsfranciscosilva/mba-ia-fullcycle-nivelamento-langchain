from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]
    return { "square_result": x * x }

question_template = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me aboult the number {square_result}",
)

model = ChatOpenAI(model_name="gpt-5-mini", temperature=0.5)
chain = square | question_template | model

result = chain.invoke({"x": 5})
print(result.content)