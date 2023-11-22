import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

def get_default_llm():
    base_model_id = "HuggingFaceH4/zephyr-7b-beta"
    
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        use_auth_token=False
    )

    tokenizer = AutoTokenizer.from_pretrained(
        base_model_id,
        add_bos_token=True,
        trust_remote_code=True,
    )

    tokenizer.pad_token = tokenizer.eos_token

    return {"default_base_model": base_model,
            "tokenizer": tokenizer}

def get_default_lora(base_model):
    return PeftModel.from_pretrained(base_model, "Fransver/zephyr-hboi-sb").to("cuda")

class LlmConfigurator():
    default_llm = get_default_llm()["default_base_model"]
    default_tokenizer = get_default_llm()["tokenizer"]
    default_lora = get_default_lora(default_llm)

    def __init__(self, llm=default_llm, tokenizer=default_tokenizer, lora=default_lora) -> None:
        self.llm = llm
        self.tokenizer = tokenizer
        self.lora = lora

    def get_llm(self):
        return self.llm
    
    def get_tokenizer(self):
        return self.tokenizer
    
    def get_loar(self):
        return self.lora
