from llm_configurator import LlmConfigurator
from query_processor import QueryProcessor
from question import Question
import runpod
   
configurator = LlmConfigurator()
llm = configurator.get_llm()
lora = configurator.get_lora()
tokenizer = configurator.get_tokenizer()

def ask_llm(job):
    print(job)
    question = job['input']['question']
    processor = QueryProcessor(question, llm, tokenizer, lora)
    answer = processor.run()
    return {"answer": answer}

def ping(job):
    return "pong"

# prompt = "How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"

runpod.serverless.start({"handler": ask_llm})
