import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("atendimento.db")
    cursor = conexao.cursor()

    # Tabela de respostas oficiais (FAQ)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS respostas_faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assunto TEXT UNIQUE NOT NULL,
            resposta TEXT NOT NULL
        )
    """)

    # Tabela de histórico de mensagens
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_atendimento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT NOT NULL,
            mensagem_cliente TEXT NOT NULL,
            resposta_agente TEXT NOT NULL,
            data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()

def cadastrar_resposta_faq(assunto, resposta):
    """Cadastra ou atualiza uma resposta oficial no banco de dados."""
    conexao = sqlite3.connect("atendimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO respostas_faq (assunto, resposta)
        VALUES (?, ?)
        ON CONFLICT(assunto) DO UPDATE SET resposta=excluded.resposta
    """, (assunto.lower(), resposta))
    conexao.commit()
    conexao.close()
    print(f"Resposta para '{assunto}' cadastrada com sucesso!")

def buscar_resposta_faq(assunto):
    """Busca uma resposta cadastrada pelo assunto."""
    conexao = sqlite3.connect("atendimento.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT resposta FROM respostas_faq WHERE assunto = ?", (assunto.lower(),))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado else None

if __name__ == "__main__":
    inicializar_banco()
    
    # Exemplo: Cadastrando suas respostas padrão
    cadastrar_resposta_faq("horario", "Nosso horario de atendimento e de segunda a sexta, das 08h as 18h.")
    cadastrar_resposta_faq("precos", "Nossos planos comecam a partir de R$ 99,00 mensais.")