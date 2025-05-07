from bandeira import identificar_bandeira

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    print("Bandeira detectada:", identificar_bandeira(numero))

