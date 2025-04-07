palavra_secreta = "girafa"
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6

# Desenho da forca por etapas
desenhos = [
    """
       ------
       |    |
       O    |
            |
            |
            |
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    """
]

while tentativas > 0 and "_" in letras_acertadas:
    print(desenhos[6 - tentativas])  # Mostra o estado atual da forca
    print(" ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[index] = letra
    else:
        tentativas -= 1
        print(f"Você errou! Você tem {tentativas} tentativas restantes.")

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print(desenhos[-1])  # Exibe o desenho final da forca
    print("Que pena, você perdeu. A palavra era:", palavra_secreta)
