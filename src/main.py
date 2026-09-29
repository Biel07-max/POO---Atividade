from guerreiro import Guerreiro
from inimigo import Inimigo
from orc import Orc
from dragao import Dragao
from item import PocaoDeVida
from batalha import Batalha


def main():

    jogador = Guerreiro("Arthur")
    # Para jogar com outra classe:
    #   from mago import Mago;         jogador = Mago("Merlin")
    #   from arqueiro import Arqueiro; jogador = Arqueiro("Robin")

    for _ in range(3):
        jogador.adicionar_item(PocaoDeVida())

    inimigos = [
        Inimigo(nome="Goblin", vida=100, ataque=15, defesa=5),
        Orc(),
        Dragao(),  # chefe final
    ]

    for inimigo in inimigos:
        resultado = Batalha(jogador, inimigo).iniciar()

        if resultado != "vitoria":
            print("Fim de jogo.")
            return

    print("\nParabéns! Você derrotou o chefe final e salvou o reino!")


if __name__ == "__main__":
    main()