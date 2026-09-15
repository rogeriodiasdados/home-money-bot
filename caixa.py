# Arquivo: caixa.py

def processar_saque(valor_digitado):
    # Se a conversão falhar, o Python gera um ValueError naturalmente
    valor = float(valor_digitado)
    
    if valor > 1500.0:
        return "Saldo Insuficiente"
    return "Saque Aprovado"