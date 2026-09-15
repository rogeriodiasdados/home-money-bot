from google import genai

# ==========================================
# 1. CONEXÃO COM A IA
# ==========================================
client = genai.Client(api_key="SUA_CHAVE_AQUI")

# ==========================================
# 2. DADOS DOS SENSORES (Móduo 1 & 4: Tipos e Listas)
# ==========================================
motores = [
    {"nome": "Motor 01 - Esteira", "temp": "82.5"},
    {"nome": "Motor 02 - Compressores", "temp": "95.0"},
    {"nome": "Motor 03 - Prensa", "temp": "DADO_CORROMPIDO"}, # Sensor com defeito!
    {"nome": "Motor 04 - Resfriador", "temp": "45.0"}
]

motores_criticos = []

print("--- INICIANDO RONDA DE INSPEÇÃO INTELIGENTE ---\n")

# ==========================================
# 3. RONDA DE INSPEÇÃO (Módulo 4: Loop 'for')
# ==========================================
for item in motores:
    nome_motor = item["nome"]
    leitura_crua = item["temp"]
    
    # Módulo 5: O Disjuntor (Try / Except)
    try:
        # Módulo 1: Convertendo texto para número decimal (float)
        temperatura = float(leitura_crua)
        
        # Módulo 3: Tomada de Decisão (if / elif / else)
        if temperatura > 90.0:
            print(f"🔴 {nome_motor} | {temperatura}°C -> ALERTA CRÍTICO!")
            motores_criticos.append(f"{nome_motor} ({temperatura}°C)")
            
        elif temperatura > 75.0:
            print(f"🟡 {nome_motor} | {temperatura}°C -> Atenção: Temperatura elevada.")
            
        else:
            print(f"🟢 {nome_motor} | {temperatura}°C -> Normal.")

    except:
        # Se o dado do sensor for inviável (ex: "DADO_CORROMPIDO"), o disjuntor atua aqui!
        print(f"⚠️ {nome_motor} | Leitura: '{leitura_crua}' -> FALHA NO SENSOR! Verifique a fiação.")

# ==========================================
# 4 e 5. CHAMA A IA E SALVA NO ARQUIVO (Módulo 2)
# ==========================================
if len(motores_criticos) > 0:
    print("\n--- GERANDO RELATÓRIO TÉCNICO COM A IA ---")
    
    prompt = f"""
    Você é um Engenheiro de Manutenção Preditiva.
    Na inspeção de hoje, identificamos motores em estado CRÍTICO:
    {motores_criticos}
    
    Por favor, gere um laudo com:
    1. Ações imediatas de segurança.
    2. Diagnóstico provável do problema.
    """
    
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    # Módulo 2: Gravando o arquivo no computador ("w")
    with open("relatorio_final.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(resposta.text)
        
    print("✅ Relatório gerado com sucesso em 'relatorio_final.txt'!")
else:
    print("\n✅ Todos os motores funcionando dentro da normalidade.")

print("\n--- FIM DA EXECUÇÃO ---")