from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='deepseek-r1:7b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky disgusting?',
  },
])
print(response.message.content, end='', flush=True )
# for chunk in response:
#     print(chunk[0]['message']['content'], end='', flush=True)