from fastapi import FastAPI
from llm_configurator import LlmConfigurator
from query_processor import QueryProcessor

app = FastAPI()

@app.get("/ask/{question}")
def ask_llm(question: str):
    return {"question": question,
        "answer": "answer"}

if __name__ == "__main__":
    configurator = LlmConfigurator()
    llm = configurator.get_llm()
    lora = configurator.get_lora()
    tokenizer = configurator.get_tokenizer()

    prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"

    processor = QueryProcessor(prompt, llm, tokenizer, lora)
    answer = processor.run()
