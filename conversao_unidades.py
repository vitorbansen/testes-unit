def converter_massa_lunar(massa_terrestre):
    return massa_terrestre / 6

def converter_massa_marte(massa_terrestre):
    gravidade_terra = 9.81
    gravidade_marte = 3.71
    return (gravidade_terra / gravidade_marte) * massa_terrestre

# Testes
def testar_conversoes():
    assert converter_massa_lunar(12) == 2
    assert converter_massa_marte(12) == 31.86
    print("Testes de conversão passaram.")

testar_conversoes()
