import pytest
from password_utils import gerar_senha,validar_senha

def test_gerar_senha():
    senha = gerar_senha(12)
    assert isinstance(senha,str) #*verifica se retorna string

    assert len(senha)==12 #*verifica se o tamanho está correto
    
    assert any(c.islower()for c in senha)

    assert any(c.isupper()for c in senha)

    assert any(c.isdigit()for c in senha)

    assert any(c in "!@#%^&*()_+-=[]{}|;:'\",.<>?/"for c in senha) #*deve ter símbolo
    

def test_gerar_senha_tamanho_minimo():
    with pytest.raises(ValueError,match="O tamanho mínimo de senha deve ser 8 caracteres."):
        gerar_senha(6)

def test_validar_senha():
    assert validar_senha("Aa1@5678")==True #*senha forte

    assert validar_senha("abcdefg")==False #!senha fraca

    assert validar_senha("2117289")==False #!senha fraca

    assert validar_senha("Aa1Y56B8")==False #!senha sem símbolos


    
    

    