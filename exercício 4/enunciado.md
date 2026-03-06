Exercício 4:
 Uma empresa de Streaming precisa alocar servidores para processar um lote de vídeos. Eles utilizam três tipos de instâncias: Instância G (processa 100 vídeos), 
Instância M (processa 10 vídeos) e Instância P (processa 1 vídeo). O custo é cobrado por instância aberta, 
então o sistema deve sempre usar o máximo possível das maiores antes de passar para as menores.

Dado um número total de vídeos no buffer, calcule o plano de alocação de servidores e o custo total, sabendo que: G custa R$ 150, M custa R$ 20 e P custa R$ 5.
Casos de teste (vídeos no buffer → saída):

253 -> 2 Instâncias G, 5 Instâncias M, 3 Instâncias P. Custo: R$ 415.

10 -> 0 Instâncias G, 1 Instância M, 0 Instâncias P. Custo: R$ 20.

108 -> 1 Instância G, 0 Instâncias M, 8 Instâncias P. Custo: R$ 190.