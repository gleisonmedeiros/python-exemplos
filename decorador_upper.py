# Decorator que transforma o resultado
# da função em maiúsculo e imprime
def upper_decorator(func):
    def wrapper():
        resultado = func()
        print(resultado.upper())

    return wrapper

# Função que retorna uma frase, será impressa
# em maiúsculo pelo decorator
@upper_decorator
def frase():
    return "Esta frase ficará em maiúsculo."

# Chamada da função frase
frase()