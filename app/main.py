from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.llm_configurator import LlmConfigurator
from app.query_processor import QueryProcessor


configurator = None
llm = None
lora = None
tokenizer = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global configurator, llm, lora, tokenizer    
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
    return {"answer": answer}

# prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"
