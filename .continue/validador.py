import re

def validar_contraseña(contraseña):
    """
    Valida que la contraseña tenga al menos 8 caracteres,
    una mayúscula, una minúscula y un número.
    """
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(patron, contraseña))