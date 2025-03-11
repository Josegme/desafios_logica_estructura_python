"""
Desafío 8 - Implementar un sistema FIFO y LIFO
📌 Problema: Necesitás manejar datos en una estructura de tipo cola (FIFO) y pila (LIFO).

💡 Desafío: ¿Cómo diseñarías un sistema que permita procesar elementos en estos dos modos?

✅ Pistas:
🔹 FIFO (First In, First Out) se implementa con deque de collections.
🔹 LIFO (Last In, First Out) se puede manejar con listas o deque.
🔹 Usá append() y pop() para simular ambas estructuras.

"""
from collections import deque
#fifo - cola (first in/first out)
cola = deque(["Tarea1", "Tarea2", "Tarea3"])
cola.append("Tarea4")
print(cola.popleft()) #elimina y muestra la Tarea1

#lifo - pila (last in/first out)
pila = ["Acción1", "Acción2", "Acción3"]
pila.append("Acción4")
print(pila.pop()) #elimina y muestra la Acción4

"""
Usamos deque para mejorar el rendimiento en FIFO, 
la pila funciona con listas y pop()
"""