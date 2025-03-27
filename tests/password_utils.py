import random
import string

def gerar_senha(tamanho=12):
    """gera uma senha forte com letras números e caracteres especiais."""
    if tamanho <8:
        raise ValueError("O tamanho mínimo de senha deve ser 8 caracteres.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha =''.join(random.choice(caracteres)
            for _ in
       range(tamanho))
    return senha

def validar_senha(senha):
    "verifica se a senha é forte:"
    "-pelo menos 8 caracteres"
    "contem letra maiuscula,minuscula,número e símbolo"
    if len(senha)<8:
        return False
    if not any(c.islower()for c in senha):
        return False
    
    if not any(c.isupper()for c in senha):
        return False
    
    if not any(c.isdigit()for c in senha):
        return False
    
    if not any(c in string.punctuation for c in senha):
        return False
    return True



    
    
        
        

    
