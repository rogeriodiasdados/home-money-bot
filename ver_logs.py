import sqlite3

def visualizar_historico():
    conexao = sqlite3.connect("atendimento.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cliente_id, mensagem_cliente, resposta_agente, data_hora 
        FROM historico_atendimento 
        ORDER BY id DESC
    """)
    
    registros = cursor.fetchall()
    conexao.close()

    print("=== HISTÓRICO DE ATENDIMENTOS GRAVADOS ===")
    if not registros:
        print("Nenhum registro encontrado.")
        return

    for reg in registros:
        print(f"\n[ID: {reg[0]}] Data/Hora: {reg[4]}")
        print(f"Cliente ({reg[1]}): {reg[2]}")
        print(f"Agente: {reg[3]}")
        print("-" * 40)

if __name__ == "__main__":
    visualizar_historico()