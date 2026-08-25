from langchain_core.runnables import RunnableLambda

def paser_number(text:str) -> int:
    return int(text.strip())

parse_runnable = RunnableLambda(paser_number)

number = parse_runnable.invoke("  42  ")
print(number)