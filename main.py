# We will start with RTE from SuperGlue as our task
# Template is from Webson 2021 and experiments will be to varying the labels

# Code should be able to extend templates easily
# code should be easy to add more tasks from glue or more datasets
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


name = "bigscience/bloom-3b"
text = "Hello my name is"
max_new_tokens = 20

def generate_from_model(model, tokenizer):
  encoded_input = tokenizer(text, return_tensors='pt')
  output_sequences = model.generate(input_ids=encoded_input['input_ids'].cuda())
  return tokenizer.decode(output_sequences[0], skip_special_tokens=True)


print('loading model')
model_8bit = AutoModelForCausalLM.from_pretrained(name, device_map="auto", load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(name)

print("loaded the model")
out = generate_from_model(model_8bit, tokenizer)
print(out)