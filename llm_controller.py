# from llm import Llm
# from peft import Peft
import torch

class LlmController:
    def __init__(self, llm, peft) -> None:
        self.llm = llm
        self.peft = peft

    def configure_llm(self):
        self.llm.set_bnb_config()
        self.llm.load_tokenizer()
        self.llm.load_model()

    def run(self, question):
        ft_model = self.peft.ft_model
        tokenizer = self.llm.tokenizer
        model_input = tokenizer(question, return_tensors="pt").to("cuda")

        ft_model.eval()
        with torch.no_grad():
            answer = ft_model.generate(**model_input, max_new_tokens=512, repetition_penalty=1.15)[0]
            return tokenizer.decode(answer, skip_special_tokens=True)
