def generate_response(incoming_msg):
    if "oi" in incoming_msg:
        return "Olá! Como posso te ajudar?"
    elif "cardápio" in incoming_msg:
        return "Aqui está nosso cardápio: \n1️⃣ Pizza \n2️⃣ Hambúrguer \n3️⃣ Bebidas"
    else:
        return "Desculpe, não entendi. Digite 'cardápio' para ver as opções."
