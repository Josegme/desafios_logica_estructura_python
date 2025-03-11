"""
🚀 Desafío 3 - Generador de contraseñas seguras
📌 Problema: Necesitás crear contraseñas fuertes que sean difíciles de hackear.

💡 Desafío: ¿Cómo generarías una contraseña aleatoria con alto nivel de seguridad?

✅ Pistas:

Usá caracteres mayúsculas, minúsculas, números y símbolos.
Asegurate de que la contraseña tenga al menos 12 caracteres.
Implementá una opción para generar múltiples contraseñas.
"""
#solución usando secrets & string

import secrets
import string
#definimos una función para generar la contraseña
def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ' '.join(secrets.choice(caracteres) for _ in range(longitud))

#generaramos y mostramos la contraseña segura
print(f'Contraseña generada: {generar_contraseña()}')

"""
secrets.choice() Mas seguro que random.choice() para criptografía 
ser usan todos los tipos de caracteres para mayor seguridad ascii_letter + digits + punctuation

"""