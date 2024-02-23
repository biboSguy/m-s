def calculadora():
    print("Calculadora legal de metros por segundo 2023 atualizada")
    while True:
        try:
            def vm(distancia, tempo):
                if tempo != 0:
                    return distancia / tempo
                else:
                    return "Erro"

            print("Velocidade Média")
            distancia = float(input('''
Qual a distância?
(em metros): '''))
            print("Distância:", distancia)
            tempo = float(input('''
Qual é o tempo? 
(em segundos): '''))
            print("Tempo:", tempo)

            resultado = vm(distancia, tempo)
            print("A velocidade média é:", resultado)

        except ValueError:
            print("Por favor, digite números válidos.")
calculadora()
