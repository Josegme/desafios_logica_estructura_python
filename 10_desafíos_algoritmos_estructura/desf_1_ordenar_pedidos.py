"""
Optimización de procesos
Problema: Tenés una lista de pedidos de una tienda online y necesitás procesarlos en orden de prioridad.

Desafío: ¿Cómo ordenarías los pedidos según urgencia sin afectar el rendimiento del sistema?

Pistas:

Usá colas de prioridad para que los pedidos más urgentes se procesen primero.
Considerá estructuras de datos eficientes, como heap (montículo).
No bloquees el sistema, implementá una solución que procese pedidos en tiempo real.

"""

import heapq

# Lista de pedidos con prioridades (prioridad, pedido)
pedidos = [
    (3, "Pedido A"),
    (2, "Pedido B"),
    (4, "Pedido C"),
    (2, "Pedido D"),
]

# Convertir la lista en un heap (montículo)
heapq.heapify(pedidos)

print("Procesando pedidos en orden de prioridad:")

# Procesar pedidos en orden de prioridad
while pedidos:
    prioridad, pedido = heapq.heappop(pedidos)  # Extrae el pedido con menor prioridad numérica
    print(f'Procesando {pedido} con prioridad {prioridad}')
