import json
import os
import pygame  # Importando a biblioteca de áudio

# Inicializando o mixer do pygame (módulo de áudio)
pygame.mixer.init()

def tocar_som(arquivo):
    """Toca um efeito sonoro."""
    pygame.mixer.Sound(arquivo).play()

def tocar_musica(arquivo):
    """Toca música de fundo em loop."""
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play(-1)  # -1 significa que tocará em loop

def parar_musica():
    """Para a música de fundo."""
    pygame.mixer.music.stop()

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

    # Começa a tocar a música de fundo
    tocar_musica("assets/music.mp3")

    while True:
        mostrar_trecho(trecho_atual)
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "0":
            tocar_som("assets/sair.mp3")
            print("\n🎮 Obrigado por jogar! Até a próxima!")
            parar_musica()  # Para a música antes de sair
            break
        
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(trecho_atual["opcoes"]):
                tocar_som("assets/escolha.mp3")  # Som ao escolher opção
                proximo_id = trecho_atual["opcoes"][escolha - 1]["proximo"]
                trecho_atual = historia.get(proximo_id, {"texto": "Erro: Caminho inválido.", "opcoes": []})
            else:
                tocar_som("assets/erro.mp3")  # Som de erro
                print("⚠️ Opção inválida! Escolha um número válido.")
        else:
            tocar_som("assets/erro.mp3")  # Som de erro
            print("⚠️ Entrada inválida! Digite apenas números.")

if __name__ == "__main__":
    iniciar_jogo()
