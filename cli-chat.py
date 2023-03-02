import openai

messages = [
    # system message first, it helps set the behavior of the assistant
    {"role": "system", "content": "You are a helpful assistant."},
]
while True:
    message = input("Q: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    reply = chat_completion.choices[0].message.content
    print(f"A: {reply}")
    messages.append({"role": "assistant", "content": reply})
