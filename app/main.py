from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from contextlib import asynccontextmanager
from app.llm_configurator import LlmConfigurator
from app.query_processor import QueryProcessor
from app.question import Question
import app.authenticator as authenticator
from fastapi import HTTPException
import runpod
import uvicorn

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
# app = FastAPI()

@app.post("/token", response_model=authenticator.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticator.authenticate_user(authenticator.db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = authenticator.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=authenticator.User)
async def read_users_me(current_user: authenticator.User = Depends(authenticator.get_current_user)):
    return current_user

@app.post("/question", response_model=authenticator.User)
async def create_question(q: Question):
    global question 
    question = q
    return q

@app.get("/ask/{question}", response_model=authenticator.User)
async def ask_llm(question: str):
    processor = QueryProcessor(question.question, llm, tokenizer, lora)
    answer = processor.run()
    return {"answer": answer}

# prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"

def run_api():
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

runpod.serverless.start({"handler": run_api})
