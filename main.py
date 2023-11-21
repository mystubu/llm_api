from fastapi import FastAPI
from llm_controller import LlmController
from peft_controller import PeftController
import torch

app = FastAPI()

@app.get("/ask/{question}")
def ask_llm(question: str):
    controller = LlmController()
    controller.load_model()
    answer = controller.ask(question)
    return {"question": question,
        "answer": "answer"}

if __name__ == "__main__":
    llm_controller = LlmController()
    llm_controller.set_bnb_config()
    llm_controller.load_tokenizer()
    llm_controller.load_model()
    # answer = controller.ask("How can I effectively gather functional requirements for a software system when working with a single stakeholder?")
    # print(answer)
    peft_controller = PeftController()

    ft_model = peft_controller.ft_model
    tokenizer = llm_controller.tokenizer

    model_input = tokenizer("How can I effectively gather functional requirements for a software system when working with a single stakeholder?", return_tensors="pt").to("cuda")

    ft_model.eval()
    with torch.no_grad():
        print(tokenizer.decode(ft_model.generate(**model_input, max_new_tokens=512, repetition_penalty=1.15)[0], skip_special_tokens=True))
