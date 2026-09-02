from google import genai

# 1. Configuração da API
client = genai.Client(api_key="")

# 2. Dados da ronda de inspeção
medicoes_motores = [
    {"motor": "Motor 01 - Exaustor", "temp": 55.0},
    {"motor": "Motor 02 - Esteira", "temp": 92.3},
    {"motor": "Motor 03 - Prensa", "temp": 78.0},
    {"motor": "Motor 04 - Compressor", "temp": 96.1},
    {"motor": "Motor 05 - Bomba D'água", "temp": 40.0}
]

# Lista em branco onde o Python vai guardar apenas os motores críticos
motores_criticos = []

print("--- ANALISANDO A LINHA DE PRODUÇÃO ---")

# 3. O Loop 'for' faz a varredura
for item in medicoes_motores:
    nome = item["motor"]
    temperatura = item["temp"]
    
    if temperatura > 90.0:
        print(f"🔴 {nome} | {temperatura}°C -> PERIGO!")
        # Adiciona o motor crítico na nossa lista especial
        motores_criticos.append(f"{nome} ({temperatura}°C)")

# 4. Se a lista de críticos NÃO estiver vazia, acionamos a IA!
if len(motores_criticos) > 0:
    print("\n⚠️ Enviando lista de motores críticos para a IA gerar o plano...")
    
    prompt = f"""
    Você é um Engenheiro de Manutenção Preditiva.
    Na ronda de hoje, os seguintes motores apresentaram temperatura crítica:
    {motores_criticos}
    
    Crie um plano de ação prioritário indicando:
    1. Qual motor deve ser checado primeiro e por quê.
    2. Duas medidas imediatas para conter o superaquecimento antes de desligar a linha.
    """
    
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    # Salvando o relatório da ronda
    with open("plano_contingencia_ronda.txt", "w", encoding="utf-8") as arq:
        arq.write(resposta.text)
        
    print("✅ Plano de contingência gerado e salvo em 'plano_contingencia_ronda.txt'!")