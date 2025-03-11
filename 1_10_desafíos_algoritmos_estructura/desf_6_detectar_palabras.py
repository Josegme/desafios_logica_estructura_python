"""
Problema: Necesitás analizar un texto y contar cuántas veces aparece cada palabra.

💡 Desafío: ¿Cómo harías para que la solución sea eficiente incluso con textos muy largos?

✅ Pistas:
🔹 Usá estructuras como diccionarios (hashmaps) para contar palabras rápidamente.
🔹 Limpiá el texto eliminando puntuaciones y convirtiéndolo a minúsculas.
🔹 Considerá palabras clave para filtrar términos irrelevantes.

"""

from collections import Counter
import re

def contar_palabras(texto):
    texto = re.sub(r'[^\w\s]', '', texto).lower() #eliminamos la puntuacion y convertimos a minuscula
    palabras = texto.split()
    return Counter(palabras)

texto = "El sol brilla en el cielo. El cielo es azul y el sol es brillante."
#llamamos a la funcion y le asignamos a una variable para poder imprimir
frecuencia = contar_palabras(texto)
print(frecuencia)

"""
usamos el Counter de collections para contar palabras
importamos el re (REGEX) para eliminar caracteres no deseados y lo pasamos a minuscula con .lower
el resultado mostramos como un diccionario con la frecuencia de cada palabra.

"""