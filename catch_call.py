from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()

    response.say("Hello. Here could be your advertisement")

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
