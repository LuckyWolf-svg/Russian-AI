from gpt4all import GPT4All
model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='gpu')
#You can change this model to another, not official gpt4all

character_description = "Ты пират"

print('Test 1/2 | Success')

def gpt (text):
    answer = model.generate(prompt=text) #you can add method 'max_tokens=1024', tokens your cpu\gpu giving you
    print('answer: ' + answer)
    return answer