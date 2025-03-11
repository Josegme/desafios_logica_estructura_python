"""
Problema: Necesitás mostrar una lista de productos ordenados según la cantidad en stock y la demanda del mercado.

💡 Desafío: ¿Cómo ordenarías los productos para mostrar primero los más demandados y con menos stock disponible?

✅ Pistas:
🔹 Usá sorted() con una función clave personalizada.
🔹 Definí una métrica combinada entre demanda y stock.
🔹 Priorizá productos con mayor demanda y menor stock.

"""
productos = [
    {"nombre": "Laptop", "stock": 10, "demanda": 100},
    {"nombre": "Mouse", "stock": 50, "demanda": 300},
    {"nombre": "Teclado", "stock": 5, "demanda": 200},
    {"nombre": "Monitor", "stock": 8, "demanda": 150}
]
#ordenamos por demanda/stock (mas demanda y menos stock primero)
productos_ordenados = sorted(productos, 
                             key=lambda p: p["demanda"]/ p["stock"],
                             reverse=True)
for p in productos_ordenados:
    print(f"{p['nombre']} - Stock: {p['stock']}, Demanda: {p['demanda']}")

"""
cada producto es un diccionario con tres claves: nombre, stock y demanda

como queremos priorizar los productos que tienen ALTA demanda y tiene BAJO stock
usamos la metrica de demanda/stock:
si un producto tiene mucha demanda y poco stock, el valor será mas alto.
si un producto tiene mucho stock y poca demanda, el valor será mas bajo.

uso del SORTED en Python es para ordenar las listas 
    sorted(iterable, key=función, reverse=True) 
iterable -> la lista que queremos ordenar, para el caso PRODUCTOS
key -> Una función que define como comprar los elementos de la lista (lambda)
reverse = True -> queremos ordenar de mayor a menor 
"""