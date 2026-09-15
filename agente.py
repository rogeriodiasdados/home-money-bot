import os
import google.generativeai as genai
from dotenv import load_dotenv
from banco import buscar_resposta_faq

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a chave de API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Instruções de comportamento da IA quando ela precisar gerar respostas livres
SYSTEM_INSTRUCTION = """
Você é um assistente virtual atencioso e profissional da empresa Home Money.
Sua missão é ajudar os clientes de forma clara, educada e direta.
Caso não saiba uma informação específica sobre valores ou horários, peça para o cliente aguardar o atendimento humano.
"""

# Inicializa o modelo da IA
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

def responder_cliente(mensagem_cliente):
    # 1. Tentar buscar uma resposta fixa/oficial no banco SQL
    # Simplificação: verifica se palavras-chave conhecidas estão na mensagem
    resposta_banco = None
    if "horario" in mensagem_cliente.lower() or "hora" in mensagem_cliente.lower():
        resposta_banco = buscar_resposta_faq("horario")
    elif "preco" in mensagem_cliente.lower() or "valor" in mensagem_cliente.lower() or "quanto" in mensagem_cliente.lower():
        resposta_banco = buscar_resposta_faq("precos")

    # Se encontrou no banco de dados, entrega a SUA resposta oficial
    if resposta_banco:
        print("[Origem da Resposta: Banco de Dados SQL]")
        return resposta_banco

    # 2. Se não encontrou no banco, a IA gera a resposta dinamicamente
    print("[Origem da Resposta: Inteligência Artificial Gemini]")
    resposta_ia = model.generate_content(mensagem_cliente)
    return resposta_ia.text

if __name__ == "__main__":
    print("--- Testando o Agente de Atendimento ---")
    
    # Teste 1: Pergunta que DEVE vir do banco de dados SQL
    pergunta1 = "Qual é o horário de vocês?"
    print(f"\nCliente: {pergunta1}")
    print(f"Agente: {responder_cliente(pergunta1)}")

    # Teste 2: Pergunta livre que a IA deve responder sozinha
    pergunta2 = "Olá! Como vocês podem me ajudar com minhas finanças?"
    print(f"\nCliente: {pergunta2}")
    print(f"Agente: {responder_cliente(pergunta2)}")