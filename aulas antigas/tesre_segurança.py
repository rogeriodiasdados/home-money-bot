dado_do_sensor = "ERRO_LEITURA"

try:
    # O Python "TENTA" executar esta linha
    temperatura = float(dado_do_sensor)
    print(f"Temperatura lida com sucesso: {temperatura}°C")

except:
    # Se der erro lá no 'try', o "DISJUNTOR ATUA" e entra aqui sem quebrar o programa!
    print("🚨 ALERTA DE SENSOR: Falha ao ler a temperatura! Verifique os cabos do sensor.")