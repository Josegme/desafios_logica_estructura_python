"""
🚀 Desafío 9 - Optimizar la carga de imágenes en una galería web
📌 Problema: Necesitás que las imágenes de una galería se carguen de forma eficiente sin afectar la velocidad de la web.

💡 Desafío: ¿Qué estrategias aplicarías para mejorar la carga sin afectar la experiencia del usuario?

✅ Pistas:
🔹 Implementá "lazy loading" para cargar imágenes solo cuando sean visibles.
🔹 Usá formatos optimizados como WebP para reducir el tamaño.
🔹 Aplicá compresión sin perder calidad.
EN ESTE TUVE QUE INVESTIGAR UN POCO Y RECIBÍN AYUDA DE MI PROFE LUIS

"""
#PRIMERO HAY QUE INSTALAR pip isntall pillow
#una vez instalado -> esrcribir un script para convertir imágenes JPG-PNG-WebP

from PIL import Image
#para abrir la img y convertirla a WebP
image = Image.open("imagen.jpg")  #cambiar por la img que tengas
image.save("imagen.webp", "WEBP", quality=80) #guardar en WebP con la calidad 80 para este caso

print("Imagen convertida a WebP con éxito")

#si quiereo mostrar imágenes en una web sin recargarlas todas de golpe, usamos FLASK
#instalar -> pip install flask
#creamos un servidor que muestre las imagenes
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/imagen')
def mostrar_imagen():
    return send_file("imagen.webp", mimetype='image/webp')

if __name__ == '__main__':
    app.run(debug=True)
#esto tiene que servir la img solamente cuando alguien solicita

#esto iría en HTML
"""
<img src="http://127.0.0.1:5000/imagen" loading="lazy" alt="Imagen optimizada">
con esta etiqueta se carga solo cuando uno necesita
entonces
converitmos imágenes a WebP con Pilow
Creamos un servidor básico con Flask para servir imagenes
usamos lazy loading en HTML para mejorar la velocidad de la web

"""