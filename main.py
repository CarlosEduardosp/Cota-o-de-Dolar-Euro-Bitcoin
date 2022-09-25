import functions

cotacao = functions.cotar()
result = functions.pegar_cota(cotacao)
result = functions.mudar(result[0], result[1], result[2])
functions.mostrar(result[0], result[1], result[2])
carteira = float(input('\nDigite o valor de sua carteira: '))
calculo = functions.calculo(carteira, result[0], result[1], result[2])
carteira = functions.moeda(carteira)
functions.mostrar_atual(carteira, calculo[0], calculo[1], calculo[2])















