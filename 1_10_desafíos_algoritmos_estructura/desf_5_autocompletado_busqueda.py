"""
📌 Problema: Estás creando un buscador y necesitás 
sugerir palabras mientras el usuario escribe.

💡 Desafío: ¿Cómo implementarías un autocompletado eficiente?

✅ Pistas:

Usá una estructura de árbol (trie) para almacenar palabras.
Buscá coincidencias en tiempo real mientras se escribe.
Optimizá para búsquedas rápidas en grandes volúmenes de datos.
"""
#para la solución utilizo Trie

class TrieNode:
    def __init__(self):
        self.hijos = {}
        self.es_fin = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def insertar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = TrieNode()
            nodo = nodo.hijos[letra]
        nodo.es_fin = True

    def buscar_prefix(self, prefix):
        nodo = self.raiz
        for letra in prefix:
            if letra not in nodo.hijos:
                return []
            nodo = nodo.hijos[letra]
        return self.obtener_palabras(nodo, prefix)
    
    def obtener_palabras(self, nodo, prefix):
        resultados = []
        if nodo.es_fin:
            resultados.append(prefix)
        for letra, hijo in nodo.hijos.items():
            resultados.extend(self.obtener_palabras(hijo, prefix + letra))
        return resultados

#para probar
trie = Trie()
palabras = ["hola", "hoja", "hormiga", "hogar", "hombre"]
for palabra in palabras:
    trie.insertar(palabra)

#vamos a buscar una sugerencia -> prefijo "ho"
print(trie.buscar_prefix('ho'))

"""
TrieNote alamcena letras y referencias a otras letras
buscar_prefix() encuentra palabras en base a un prefijo

"""