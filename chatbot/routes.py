from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import app
from chatbot.responses import generate_response
from chatbot.openai_service import get_openai_response

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()
    
    if "oi" in incoming_msg:
        msg.body("Olá! Como posso te ajudar?")
    elif "cardápio" in incoming_msg:
        msg.body("Aqui está nosso cardápio: \n1️⃣ Pizza \n2️⃣ Hambúrguer \n3️⃣ Bebidas")
    else:
        ai_response = get_openai_response(incoming_msg)
        msg.body(ai_response)
    
    return str(response)
