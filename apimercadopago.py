import mercadopago

def gerar_link_pagamento():
    # Substitua esse token por uma variável de ambiente em produção
    sdk = mercadopago.SDK("TEST-350643946761775-050510-0ed480303e3a560971f909449bd346cd-472206845")

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "Camisa",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 0.99
            }
        ],
        "back_urls": {
            "success": "https://127.0.0.1:5000/compracerta",
            "failure": "https://127.0.0.1:5000/compraerrada",
            "pending": "https://127.0.0.1:5000/compraerrada"
        },
        "auto_return": "all"
    }

    try:
        result = sdk.preference().create(payment_data)

        if result.get("status") != 201:
            print("Erro ao criar preferência:", result)
            return "Erro: não foi possível gerar o link de pagamento."

        payment = result.get("response", {})
        link_iniciar_pagamento = payment.get("init_point")

        if not link_iniciar_pagamento:
            print("init_point não encontrado na resposta:", payment)
            return "Erro: link de pagamento não disponível."

        return link_iniciar_pagamento

    except Exception as e:
        print("Exceção ao criar preferência:", str(e))
        return "Erro: exceção ao gerar link de pagamento."
