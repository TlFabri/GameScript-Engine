import json

def carregar_historia(arquivo):
    """Carrega a história do arquivo JSON."""
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_trecho(trecho):
    """Exibe um trecho da história e as opções disponíveis."""
    print("\n" + trecho["texto"])
    
    for i, opcao in enumerate(trecho["opcoes"], start=1):
        print(f"{i}. {opcao['descricao']}")

def iniciar_jogo():
    historia = carregar_historia("data/historia.json")
    trecho_atual = historia["inicio"]

    while True:
        mostrar_trecho(trecho_atual)
        
        escolha = input("Escolha uma opção: ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(trecho_atual["opcoes"]):
                proximo_id = trecho_atual["opcoes"][escolha - 1]["proximo"]
                trecho_atual = historia[proximo_id]
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Digite um número válido.")

if __name__ == "__main__":
    iniciar_jogo()

