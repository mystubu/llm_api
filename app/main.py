from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.llm_configurator import LlmConfigurator
from app.query_processor import QueryProcessor
from app.question import Question


configurator = None
llm = None
lora = None
tokenizer = None
question = None

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

@app.post("/question/")
async def create_question(q: Question):
    global question 
    question = q
    return q

@app.get("/ask/{question}")
async def ask_llm(question: str):
    processor = QueryProcessor(question.question, llm, tokenizer, lora)
    answer = processor.run()
    return {"answer": answer}

# prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"
