from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('/app/project/model/default/model_20190204-222950')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('/app/project/model/dialogue', interpreter=interpreter)

def chatlogs_html(messages):
    messages_html = "".join(["<p>{}</p>".format(m) for m in messages])
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html


while True:
    print(chatlogs_html(messages))
    time.sleep(0.3)
    a = input()
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        messages.append(r.get("text"))
