"""
📌Problema: Un estudiante quiere aprender nuevos temas 
y necesita sugerencias basadas en sus cursos previos.

💡 Desafío: ¿Cómo recomendarías cursos relevantes según su historial?

✅ Pistas:

Usá un sistema de similitud de contenido.
Compará palabras clave en los cursos completados.
Implementá distancia coseno para medir similitudes.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cursos = [
    "Python para Data Science",
    "Machine Learning con Python",
    "Desarrollo Web con JavaScript",
    "Ciencia de Datos con Pandas"
]

vectorizador = TfidfVectorizer()
matriz = vectorizador.fit_transform(cursos)

similitudes = cosine_similarity(matriz)

print('Similitudes entre cursos: \n', similitudes)

"""

TfidfVectorizer() transforma texto en datos numéricos
cosine_similarity() encuentra cursos con contenido similar
se puede aplicar en recomendaciones de libros, peliculas y otros

¿Como interpretar el rusultado ->
Cada fila y cada columna representan un curso. La intersección de una fila y una columna muestra cuán similares son esos dos cursos.

La diagonal principal es siempre 1, porque cada curso es idéntico a sí mismo.
Los valores fuera de la diagonal indican la similitud entre cursos distintos:
0.1877 → El curso 0 y el curso 1 tienen una similitud del 18.77%.

"""