distancia = int(input("Coloque a distância em mm: "))
distanciaInicial = distancia

km = distancia//1000000
distancia = distancia % 1000000

m = distancia//1000
distancia = distancia % 1000

cm = distancia//10
mm = distancia % 10


print(f"{distanciaInicial} => {km} km {m} m {cm} cm e sobram {mm} mm")