import openai
import logging
from bokeh.layouts import column
from bokeh.plotting import curdoc
from bokeh.models.widgets import TextInput, Div, Button

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

text_input = TextInput(width=900, prefix="😋")
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
        div.text += "<hr>"
        text_input.value = ""
        div.styles = {'background': '#222221'}


def clear_input_filed(attrname, old, new):
    text_input.disabled = True


def new_chat_button():
    messages.clear()
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    div.text = ""


button = Button(label="New Chat", button_type="success")

# Attach the callback function to the text input widget
text_input.on_change("value", update_div)
button.on_click(new_chat_button)

div = Div(text=f"{text_input.value}",
          width=900,
          styles={'font-size': '100%',
                  'color': '#6ed44d',
                  'font-family': 'monospace',
                  'background': '#0a0a0a'})

layout = column(div, column(text_input, button, align="end"))
curdoc().add_root(layout)
