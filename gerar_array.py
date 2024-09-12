import random

def gerar_array(tamanho, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

# Teste
array = gerar_array(20000, -999999, 999999)
print("Array gerado com sucesso. Número de elementos:", len(array))
