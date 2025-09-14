import time

# Decorator que mede o tempo de execução da função
def tempo_execucao(func):
    def wrapper():
        inicio = time.time()  # marca o início
        func()  # executa a função
        fim = time.time()  # marca o fim
        duracao = fim - inicio
        print(f"\nA função demorou {duracao:.2f} segundos.")

    return wrapper

# Função que imprime mensagens e usa sleep
@tempo_execucao
def espera():
    print("Esperando por 2 segundos...")
    time.sleep(2)
    print("Esperando por 3 segundos...")
    time.sleep(3)
    print("Fim")

# Chamada da função Saudacao
espera()