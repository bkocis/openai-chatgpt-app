import time
import openai
import logging
from bokeh.layouts import column, row
from bokeh.plotting import curdoc
from bokeh.models.widgets import TextInput, Div, Button

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
messages = [{"role": "system",
             "content": "You are a helpful assistant."}]


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        reply, messages = method(*args, **kw)
        te = time.time()
        timing = te - ts
        logging.info(f"{method.__name__}  {te - ts} sec")
        print(f"{timing} sec")
        return reply, messages, timing
    return timed


def format_reply(reply):
    reply = reply.replace("```", '<pre><code class="python">', 1)
    reply = reply.replace("```", "</code></pre>", 1)
    return reply


def message_counter(messages):
    question_count = 0
    for message in messages:
        if message["role"] == "user" and message["content"] != "":
            question_count += 1
    return question_count


@timeit
def call_openai(new):
    messages.append(
        {"role": "user", "content": new},
    )
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        stream=True
    )
    # use message.content for the case of stream=False
    # reply = chat_completion.choices[0].message.content
    # return reply, messages
    reply = []
    for chunk in chat_completion:
        if chunk is not None:
            # print(chunk.choices[0].delta.get("content"))
            reply.append(chunk.choices[0].delta.get("content"))
    # print(reply)
    return " ".join(reply[1:-1]), messages


def update_div(attrname, old, new):
    reply, messages, timing = call_openai(new)

    logging.info(f"A: {reply}")
    print(f"A: {reply}")
    message_count = message_counter(messages)

    messages.append({"role": "assistant", "content": reply})

    if new != "":
        div.text += f"<br>Q{message_count}: {new}"
        div.text += f"<br><dd>{format_reply(reply)}</dd>"

        text_input.value = ""
        # div.styles = {'color': '#6ed44d',
        #               'font-family': 'monospace',
        #               'background': '#111111'}
        div.text += f"<br>{timing}"
        div.text += "<hr>"


def stream_div():
    messages.append(
        {"role": "user", "content": text_input.value},
    )
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        stream=True
    )
    # reply = []
    for chunk in chat_completion:
        if chunk is not None:
            div.text += f'{(chunk.choices[0].delta.get("content"))}'
            # reply.append(chunk.choices[0].delta.get("content"))
    # print(reply)
    # return " ".join(reply[1:-1]), messages

    # logging.info(f"A: {reply}")
    # print(f"A: {reply}")
    # message_count = message_counter(messages)

    # messages.append({"role": "assistant", "content": reply})

    # if new != "":
    #     # div.text += f"<br>Q{message_count}: {new}"
    #     # div_Q.text += f"<br>{new}"
    #     div.text += f"<br><dd>{format_reply(reply)}</dd>"
    #     # div_A.text += f"<br>{format_reply(reply)}"
    #
    #     text_input.value = ""
    #     # div.styles = {'color': '#6ed44d',
    #     #               'font-family': 'monospace',
    #     #               'background': '#111111'}
    #     #div.text += f"<br>{timing}"
    #     div.text += "<hr>"


def clear_input_filed(attrname, old, new):
    text_input.disabled = True


def new_chat_button():
    messages.clear()
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    div.text = ""


def take_the_text_input():
    print(text_input.value)
    # stream_div("value", "", text_input.value)
    update_div("value", "", text_input.value)


# List of widgets
text_input = TextInput(width=900, prefix="😋")
button = Button(label="New Chat", button_type="success")
enter_button = Button(label="Enter", button_type="success")
div = Div(text=f"{text_input.value}",
          width=900,
          styles={'font-size': '100%',
                  'color': '#6ed44d',
                  'font-family': 'monospace',
                  'background': '#0a0a0a'})

# List of callbacks
text_input.on_change("value", update_div)
# text_input.on_change("value", stream_div)
button.on_click(new_chat_button)
enter_button.on_click(take_the_text_input)

# Layout
layout = column(div,
                column(row(text_input, enter_button), button, align="start"),
                )

# Add to document
curdoc().add_root(layout)
# curdoc().add_periodic_callback(stream_div, 1000)
# curdoc().add_periodic_callback(update_div, 1000)
curdoc().title = "openai-chatgpt-app"
