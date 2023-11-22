from fastapi import FastAPI
from llm_configurator import LlmConfigurator
from query_processor import QueryProcessor
from contextlib import asynccontextmanager

configurator = None
llm = None
lora = None
tokenizer = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    configurator = LlmConfigurator()
    llm = configurator.get_llm()
    lora = configurator.get_lora()
    tokenizer = configurator.get_tokenizer()
    yield
    configurator = None
    llm = None
    lora = None
    tokenizer = None

app = FastAPI(lifespan=lifespan)

@app.get("/ask/{question}")
def ask_llm(question: str):
    processor = QueryProcessor(question, llm, tokenizer, lora)
    answer = processor.run()
    return {"question": question,
            "answer": answer}

# prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"
