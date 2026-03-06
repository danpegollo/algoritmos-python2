massa = float(input("Coloque a massa do carro em kg: "))
desaceleracao = float(input("Coloque a taxa de desaceleração do carro em metros por segundo ao quadrado: "))
forca = massa * desaceleracao
print("A força necessária para desacelarar um carro de", massa, "quilos é de", forca, "newtons")