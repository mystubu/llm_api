from peft import PeftModel

class PeftController:
    def __init__(self, basemodel, peft) -> None:
        self.ft_model = PeftModel(basemodel, peft).to("cuda")
