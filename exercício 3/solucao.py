velocidade = float(input("Coloque a velocidade inicial do trem em metros por segundo: "))
desaceleracao = float(input("Coloque a desaceleração do trem em metros por segundo ao quadrado: "))
tempo = float(input("Coloque o tempo de frenagem em segundos: "))

aceleracao = -desaceleracao 
distancia = (velocidade * tempo) + (aceleracao * tempo ** 2) / 2

print(f"A distância percorrida durante a frenagem é de {distancia:.2f} metros")