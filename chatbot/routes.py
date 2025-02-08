from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import app
from chatbot.responses import generate_response

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()
    
    msg.body(generate_response(incoming_msg))
    
    return str(response)
