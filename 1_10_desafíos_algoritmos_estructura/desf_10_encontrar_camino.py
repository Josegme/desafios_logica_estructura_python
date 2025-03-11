"""
🚀 Desafío 10 - Encontrar el Camino Más Corto en un Mapa con Dijkstra
📌 Problema: Tenés un mapa representado como un grafo, donde los nodos son ciudades y las aristas son caminos con una distancia específica. Querés encontrar la ruta más corta entre dos ciudades usando el algoritmo de Dijkstra.

💡 Desafío: ¿Cómo diseñarías un sistema que permita calcular la ruta óptima desde una ciudad de origen hasta un destino?

✅ Pistas:
🔹 Representá el mapa con un diccionario de Python, donde cada ciudad tiene una lista de conexiones y distancias.
🔹 Usá una cola de prioridad (heapq) para optimizar la búsqueda del camino más corto.
🔹 Mantené un diccionario de distancias para registrar la ruta más eficiente.

"""
#creamos un grafo y aplicamos el algoritmo de Dijkstra para encontrar la ruta mas corta
import heapq
#tenemos que definir el mapa como un diccionario de ciudades y distancias
mapa = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
}

def dijkstra(mapa, inicio, destino):
    #hacemos una cola de prioridad para explorar los caminos mas cortos primero
    cola = [(0, inicio)]
    distancias = {ciudad: float('inf') for ciudad in mapa}
    distancias[inicio] = 0
    camino = {}

    while cola:
        costo_actual, ciudad_actual = heapq.heappop(cola)

        if ciudad_actual == destino:
            break

        for vecino, costo in mapa[ciudad_actual].items():
            nueva_distancia = costo_actual + costo
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
                camino[vecino] = ciudad_actual 

    ruta = []
    ciudad = destino
    while ciudad in camino:
        ruta.append(ciudad)
        ciudad = camino[ciudad]
    ruta.append(inicio)
    ruta.reverse()

    return ruta, distancias[destino]

origen = 'A'
destino = 'E'
ruta, costo = dijkstra(mapa, origen, destino)

print(f"Ruta mas corta: {' -> '.join(ruta)} con un costo de {costo}")
