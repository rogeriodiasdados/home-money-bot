from google import genai

# 1. Configuração da API do Gemini (Coloque a sua chave aqui)
client = genai.Client(api_key='')

# 2. MÓDULO 2: Lendo o arquivo do sensor
with open("sensor_temperatura.txt", "r", encoding="utf-8") as arquivo:
    dados_sensor = arquivo.read()

# MÓDULO 1: Extraindo e convertendo a temperatura para FLOAT (Número Decimal)
# (Aqui estamos pegando o valor de 94.5 que estava no arquivo)
temperatura = 62.5 

print(f"Temperatura atual lida: {temperatura}°C")

# 3. MÓDULO 3: Tomada de decisão com IF, ELIF, ELSE
if temperatura > 90.0:
    print("⚠️ STATUS: CRÍTICO! Solicitando análise urgente da IA...")
    
    # Criamos o prompt para a IA montar a Ordem de Serviço
    prompt = f"""
    Você é um Engenheiro de Manutenção Preditiva.
    O sensor do transformador disparou um alerta CRÍTICO.
    
    Dados do Sensor:
    {dados_sensor}
    
    Gere uma Ordem de Serviço (OS) de emergência contendo:
    1. Ação imediata que a equipe de turno deve tomar.
    2. Possíveis causas para esse aumento de temperatura.
    """
    
    # Chamando a IA do Google
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    # MÓDULO 2: Salvando a Ordem de Serviço em um arquivo novo ("w")
    with open("ordem_de_servico_urgente.txt", "w", encoding="utf-8") as os_file:
        os_file.write(resposta.text)
        
    print("✅ Ordem de serviço criada e salva em 'ordem_de_servico_urgente.txt'!")

elif temperatura > 75.0:
    print("⚠️ STATUS: ATENÇÃO! Temperatura elevada. Registrando no histórico...")
    
    # MÓDULO 2: Registrando no histórico sem apagar o anterior ("a" de Append)
    with open("historico_alertas.txt", "a", encoding="utf-8") as hist:
        hist.write(f"Alerta moderado: {temperatura}°C no Transformador TR-02\n")

else:
    print("✅ STATUS: NORMAL. Equipamento operando com segurança.")