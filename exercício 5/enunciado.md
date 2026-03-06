Exercício 5:
 Drones de entrega operam com coordenadas baseadas em uma "Grade de Navegação" de alta precisão. O GPS envia a posição em Milímetros (inteiro), mas o painel do operador precisa visualizar a distância em Quilômetros, Metros e Centímetros.
O aluno deve ler a distância total em milímetros e decompor o valor para as unidades maiores. A dificuldade aqui é a escala decimal e a manutenção da precisão sem arredondamentos flutuantes indesejados.

Casos de Teste (Distância em mm -> Saída):

1200550 -> 1 km, 200 m, 5 cm. (Sobram 0 mm).

50020 -> 0 km, 50 m, 2 cm. (Sobram 0 mm).

3000000 -> 3 km, 0 m, 0 cm. (Sobram 0 mm).