from fastapi import FastAPI
from llm import Llm
from peft import Peft
from llm_controller import LlmController
import torch

app = FastAPI()

@app.get("/ask/{question}")
def ask_llm(question: str):
    return {"question": question,
        "answer": "answer"}

if __name__ == "__main__":
    llm = Llm("HuggingFaceH4/zephyr-7b-beta")
    peft = Peft(llm, "Fransver/zephyr-hboi-sb")
    controller = LlmController(llm, peft)
    controller.configure_llm()
    llm_response = controller.run("What is the meaning of life?")
