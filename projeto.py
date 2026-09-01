from google import genai

# 1. O Python se conecta com o sistema da IA do Google
# (Como estamos testando, ele usa uma chave interna do sistema)
client = genai.Client(api_key="")

# 2. O Python abre o arquivo de texto e lê o relatório da falha elétrica
with open("ocorrencia.txt", "r", encoding="utf-8") as arquivo:
    relatorio_falha = arquivo.read()

# 3. Criamos a pergunta detalhada para a IA (o Prompt)
# Juntamos a nossa instrução com o texto que lemos do arquivo!
pergunta = f"""
Você é um especialista em Engenharia Elétrica e Segurança Industrial.
Analise o seguinte relato de falha e forneça:
1. Uma hipótese do que causou o problema.
2. Três passos de segurança que o técnico deve seguir antes de mexer no painel.

Relato da Falha:
{relatorio_falha}
"""

print("Enviando os dados para a Inteligência Artificial analisar...")

# 4. O Python envia a pergunta para o modelo de IA (Gemini) e recebe a resposta
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=pergunta,
)

# 5. O Python exibe na tela o que a IA respondeu
print("\n--- DIAGNÓSTICO DA IA ---")
print(resposta.text)