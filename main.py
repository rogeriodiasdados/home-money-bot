import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da API do Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Instruções do sistema (A "personalidade" e regras do robô)
INSTRUCOES_SISTEMA = """
Você é o assistente virtual da loja 'Home Money Modas'.
Seu objetivo é atender clientes no WhatsApp de forma cortês, rápida e objetiva.

Regras de Atendimento:
1. Responda em no máximo 3 frases (formato ideal para WhatsApp).
2. Horário de funcionamento: Segunda a Sexta, das 8h às 18h.
3. Formas de pagamento: Pix, Cartão de Crédito e Boleto.
4. Se o cliente perguntar algo fora do escopo da loja, redirecione educadamente para um atendente humano.
"""

def responder_cliente(mensagem_cliente: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=mensagem_cliente,
            config=types.GenerateContentConfig(
                system_instruction=INSTRUCOES_SISTEMA,
                temperature=0.3, # Respostas mais precisas e diretas
            )
        )
        return response.text
    except Exception as e:
        return "Desculpe, estou passando por uma manutenção rápida. Um atendente humano responderá em breve!"

# Teste local via Terminal (Simulação do WhatsApp)
if __name__ == "__main__":
    print("--- ASSISTENTE DE ATENDIMENTO IA (SIMULADOR DE WHATSAPP) ---")
    print("Digite 'sair' para encerrar o teste.\n")
    
    while True:
        entrada_usuario = input("Cliente: ")
        if entrada_usuario.lower() == "sair":
            break
            
        resposta = responder_cliente(entrada_usuario)
        print(f"Bot: {resposta}\n")