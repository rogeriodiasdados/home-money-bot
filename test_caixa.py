# Arquivo: test_caixa.py
import pytest
from caixa import processar_saque

def test_saque_com_letras_deve_falhar():
    # O 'with pytest.raises' é a nossa aposta de que o erro vai acontecer
    with pytest.raises(ValueError):
        processar_saque("ABC_FALHA_TECLADO")