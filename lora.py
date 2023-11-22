from peft import PeftModel

class Lora:
    def __init__(self, basemodel, peft) -> None:
        self.ft_model = PeftModel(basemodel, peft).to("cuda")
