from flask import Flask, request, redirect

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_send():
    response = MessagingResponse()
    response.message("We got your messsage")

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
