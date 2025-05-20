def calcular_engajamento(curtidas, comentarios, compartilhamentos, seguidores, alcance, impressoes):
    engajamento_por_seguidores = (curtidas + comentarios + compartilhamentos) / seguidores * 100 if seguidores else 0
    engajamento_por_alcance = (curtidas + comentarios + compartilhamentos) / alcance * 100 if alcance else 0
    engajamento_por_impressoes = (curtidas + comentarios + compartilhamentos) / impressoes * 100 if impressoes else 0

    return engajamento_por_seguidores, engajamento_por_alcance, engajamento_por_impressoes

# Solicitar dados do usuário
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))
seguidores = int(input("Digite o número de seguidores: "))
alcance = int(input("Digite o número de pessoas alcançadas: "))
impressoes = int(input("Digite o número de impressões: "))

# Calcular engajamento
eng_seguidores, eng_alcance, eng_impressoes = calcular_engajamento(curtidas, comentarios, compartilhamentos, seguidores, alcance, impressoes)

# Exibir resultados
print(f"\nEngajamento por seguidores: {eng_seguidores:.2f}%")
print(f"Engajamento por alcance: {eng_alcance:.2f}%")
print(f"Engajamento por impressões: {eng_impressoes:.2f}%")
