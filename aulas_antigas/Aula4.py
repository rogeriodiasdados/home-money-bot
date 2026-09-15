# Definindo a voltagem do painel
tensao = 105

# Testando as opções
if tensao < 110:
    print("Alerta: Tensão muito baixa!")
elif tensao == 220:
    print("Sucesso: Tensão nominal de 220V detectada! Sistema seguro.")
else:
    print("Alerta: Tensão acima do esperado!")