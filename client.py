from openai import OpenAI

client=OpenAI(
    api_key="")
completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
      {
          "role": "you are a virtual assistant name neko skilled in general task alexa and google",
          "content": "What is coding"
      }
  ]
)

print(completion.choices[0].message.content)