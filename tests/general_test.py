import pytest
from password_utils import gerar_senha,validar_senha
import time


    #*TESTE DE UNIDADE 1
  
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




    
def test_gerar_senha_tamanho():
        senha = gerar_senha(12)
        assert len(senha)== 12 #verifica se a senha gerada tem o tamanho correto


    
    

   
    #*TESTE DE PERFORMANCE

def test_performance():
    start_time = time.time()
    for _ in range(1000):
        gerar_senha(12)
    end_time = time.time()
    assert (end_time - start_time) < 2, "A geração de 1000 senhas deve ser rápida"



  

#*Teste de Regressão - Verifica se uma alteração no código não quebrou funcionalidades anteriores

def test_regressao():
    senha = gerar_senha(12)
    assert len(senha) == 12
    assert validar_senha(senha) is True


#* Teste de Integração - Geração e validação da senha juntas
def test_geracao_e_validacao():
    senha = gerar_senha(10)
    assert validar_senha(senha), "A senha gerada deve ser válida"



#*Teste de Sistema - Simula um uso real, gerando senhas a cada 5 minutos"
def test_senha_temporaria():
    senha1 = gerar_senha(12)
    time.sleep(2)  # Simula o tempo entre trocas de senha (reduzido para testes)
    senha2 = gerar_senha(12)
    assert senha1 != senha2, "As senhas devem ser diferentes a cada geração"