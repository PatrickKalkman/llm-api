from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.5,
    model="anymodel.gguf",
    openai_api_base="http://localhost:8000",
    openai_api_key="ey"
)


try:
    for chunk in llm.stream("Write me a python script that validates an email address"):
        if chunk.content:
            print(chunk.content, end="", flush=True)
except Exception as e:
    print(f"An error occurred: {e}")
