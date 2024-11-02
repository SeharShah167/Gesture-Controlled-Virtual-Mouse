from flask import Flask, render_template, request, jsonify
import os
from queue import Queue

class ChatBot:

    started = False
    userinputQueue = Queue()

    @classmethod
    def isUserInput(cls):
        return not cls.userinputQueue.empty()

    @classmethod
    def popUserInput(cls):
        return cls.userinputQueue.get()

    @classmethod
    def addUserMsg(cls, msg):
        # Placeholder for adding user message to your chat
        print(f"User: {msg}")

    @classmethod
    def addAppMsg(cls, msg):
        # Placeholder for adding app message to your chat
        print(f"App: {msg}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    user_message = request.json.get('message')
    ChatBot.addUserMsg(user_message)

    # Here you would call your processing function and get a response
    response_message = "This is a response from the ChatBot"  # Modify with your logic
    ChatBot.addAppMsg(response_message)

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)
