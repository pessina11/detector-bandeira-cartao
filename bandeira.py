import re

def identificar_bandeira(numero):
    numero = numero.replace(" ", "").replace("-", "")
    
    padroes = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$"
    }

    for bandeira, regex in padroes.items():
        if re.match(regex, numero):
            return bandeira

    return "Bandeira não identificada"

