import json
import os

def carregar_historia(arquivo):
    """Carrega a história do arquivo JSON."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
        exit()
    except json.JSONDecodeError:
        print(f"Erro: Problema ao ler o arquivo {arquivo}. Verifique a formatação JSON.")
        exit()

def limpar_tela():
    """Limpa a tela do terminal para melhor experiência do usuário."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_trecho(trecho):
    """Exibe um trecho da história e as opções disponíveis."""
    limpar_tela()
    print("\n📖", trecho["texto"], "\n")
    
    for i, opcao in enumerate(trecho["opcoes"], start=1):
        print(f"  [{i}] {opcao['descricao']}")
    
    print("\n[0] Sair do jogo.")

def iniciar_jogo():
    historia = carregar_historia("data/historia.json")
    trecho_atual = historia["inicio"]

    while True:
        mostrar_trecho(trecho_atual)
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "0":
            print("\n🎮 Obrigado por jogar! Até a próxima!")
            break
        
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(trecho_atual["opcoes"]):
                proximo_id = trecho_atual["opcoes"][escolha - 1]["proximo"]
                trecho_atual = historia.get(proximo_id, {"texto": "Erro: Caminho inválido.", "opcoes": []})
            else:
                print("⚠️ Opção inválida! Escolha um número válido.")
        else:
            print("⚠️ Entrada inválida! Digite apenas números.")

if __name__ == "__main__":
    iniciar_jogo()
