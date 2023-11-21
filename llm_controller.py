from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

class LlmController:
    def __init__(self, path_or_model_id) -> None:
        self.path = path_or_model_id # "HuggingFaceH4/zephyr-7b-beta"
        self.bnb_config = None
        self.tokenizer = None
        self.model = None
        self.model_inputs = None

    def set_bnb_config(self):
        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
            )

    def load_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.path, add_boss_token=True, trust_remote_code=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def load_model(self):
        self.model = AutoModelForCausalLM.from_pretrained(
            self.path,
            quantization_config=self.bnb_config, 
            device_map="auto",
            trust_remote_code=True, 
            use_auth_token=False)

    def _set_model_inputs(self, text):
        self.model_inputs = self.tokenizer([text], return_tensors="pt".to("cuda"))

    def ask(self, question):
        self._set_model_inputs(question)
        answer_ids = self.model.generate(**self.model_inputs, max_length=512)
        return self.tokenizer.batch_decode(answer_ids, skip_special_tokens=True)[0]
    