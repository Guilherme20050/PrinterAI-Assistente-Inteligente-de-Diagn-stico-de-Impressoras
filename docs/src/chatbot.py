import json

# Carregar base de conhecimento
with open("../data/problemas.json", "r") as f:
    base = json.load(f)

def responder(pergunta):
    pergunta = pergunta.lower()

    for item in base:
        if item["problema"] in pergunta:
            return item["solucao"]

    return "Não tenho informação suficiente para responder com segurança."

def iniciar_chat():
    print("📌 PrinterAI iniciado!")
    print("Digite sua dúvida ou 'sair' para encerrar.\n")

    while True:
        user = input("Você: ")

        if user.lower() == "sair":
            print("Encerrando atendimento...")
            break

        resposta = responder(user)
        print(f"Assistente: {resposta}\n")

if __name__ == "__main__":
    iniciar_chat()
