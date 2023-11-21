from peft import PeftModel

class Peft:
    def __init__(self, basemodel, peft) -> None:
        self.ft_model = PeftModel(basemodel, peft).to("cuda")
