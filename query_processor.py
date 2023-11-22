import torch

class QueryProcessor:
    def __init__(self, prompt, llm, tokenizer, lora) -> None:
        self.prompt = prompt
        # prompt template
        self.llm = llm
        self.tokenizer = tokenizer
        self.lora = lora

    def _tokenize_input(self):
        return self.tokenizer(self.prompt, return_tensors="pt").to("cuda")

    def _get_llm_output(self, model_input):
        return self.lora.generate(**model_input, max_new_tokens=512, repetition_penalty=1.15)[0]
    
    def _decode_output(self, output):
        return self.tokenizer.decode(output, skip_special_tokens=True)
    
    def run(self):
        tokenized_input = self._tokenize_input()
        with torch.no_grad():
            llm_output = self._get_llm_output(tokenized_input)
            decoded_output = self._decode_output(llm_output)
            return decoded_output
    