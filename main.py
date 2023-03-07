import openai
import logging
from bokeh.layouts import column
from bokeh.plotting import curdoc
from bokeh.models.widgets import TextInput, Div

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

text_input = TextInput(title="Ask me a question", width=700, prefix="😋")
messages = [{"role": "system",
             "content": "You are a helpful assistant."}]


def format_reply(reply):
    reply = reply.replace("```", '<pre><code class="python">', 1)
    reply = reply.replace("```", "</code></pre>", 1)
    return reply


def update_div(attrname, old, new):
    # Update the text in the div with the new input value
    messages.append(
        {"role": "user", "content": new},
    )
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat_completion.choices[0].message.content
    # logging.info(f"A: {reply}")
    print(f"A: {reply}")

    messages.append({"role": "assistant", "content": reply})

    if new != "":
        div.text += f"<br>Q: {new}"
        div.text += f"<br>A: {format_reply(reply)}"
        text_input.value = ""


# Attach the callback function to the text input widget
text_input.on_change("value", update_div)

div = Div(text=f"{text_input.value}", styles={'font-size': '100%', 'color': 'blue'})

layout = column(div, text_input)
curdoc().add_root(layout)
