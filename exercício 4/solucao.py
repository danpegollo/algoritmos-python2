videos = int(input("Coloque o total de vídeos: "))

instanciaG = videos // 100
resto = videos % 100
instanciaM = resto // 10
instanciaP = resto % 10

total = (instanciaG * 150) + (instanciaM * 20) + (instanciaP * 5)

print("Vídeos:", videos)
print("Instâncias G:", instanciaG)
print("Instâncias M:", instanciaM)
print("Instâncias P:", instanciaP)
print("Custo total: R$", total)