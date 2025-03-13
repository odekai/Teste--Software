import random
import string

def gerer_senha(tamanho=12):
    """gera uma senha forte com letras números e caracteres especiais."""
    if tamanho <8:
        raise ValueError("o tamanho ,mínimo de senha deve ser 8 caracteres.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
         senha =
    ''.join(random.choice(caracteres)
            for _ in
       range(tamanho))
    return senha