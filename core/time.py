from datetime import datetime

def get_mensagem_principal():
    agora = datetime.now()
    hora = agora.hour()

    if hora >= 5 and hora < 12:
        mensagem = 'Bom dia'
    elif hora >= 12 and hora < 18:
        mensagem = 'Boa tarde'
    else:
        mensagem = 'Boa noite'
    return mensagem
