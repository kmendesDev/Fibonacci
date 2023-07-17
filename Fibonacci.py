import time

fibonacci = [1, 1]  # Cria a lista
# inicia as variáveis para guardar os 2 números anteriores que serão calculados
a2 = 1
a1 = 1
n = int(input("Digite a quantidade de iteracoes para o Fibonacci ser calculado: "))
# Verifica o horário em que o código começa a rodar:
ini = time.time()
print("Tempo inicial:" + str(ini))
i = 1
soma = 0
# Loop para calcular a sequência. É usado n-1 pelo fato do índice da lista ser 1 a menos que o número de iterações
while i < n - 1:
    atual = a1 + a2
    # Adiciona ao final da lista:
    fibonacci.append(atual)
    a1 = a2
    a2 = atual
    i += 1
for x in fibonacci:
    soma = soma + x
# Imprime o nº escolhido na tela:
print("Numero Fibonacci solicitado: " + str(fibonacci[n - 1]))
print("Soma de Fibonacci: " + str(soma))
# Verifica o horário em que o código termina de rodar:
fim = time.time()
print(fim)
# Apresenta o tempo total de duração do código:
print("tempo total: " + str(fim - ini))
