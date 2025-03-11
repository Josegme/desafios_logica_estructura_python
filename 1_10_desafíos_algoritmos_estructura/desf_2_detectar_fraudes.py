"""
📌 Problema: Un banco necesita detectar movimientos sospechosos en tiempo real.

💡 Desafío: ¿Cómo detectarías si una transacción es fraudulenta basándote en el historial del usuario?

✅ Pistas:

Analizá montos inusuales respecto a compras previas.
Usá un desviación estándar para detectar anomalías.
Considerá la frecuencia de transacciones en cortos períodos de tiempo 
(utilizaos numpy para detectar anomalías)
"""
import numpy as np

#historial de transacciones
transacciones = [50,45,60,55,70,2000] #Puse la última como transacción sospechosa

#calculamos la media y la desviación estándar
media = np.mean(transacciones[:-1])
desviacion = np.std(transacciones[:-1])

#detectamos si la última transacción es sospechosa
ultima = transacciones[-1]
es_fraude = ultima > media + 3*desviacion

print(f'Última transacción: ${ultima}')
print('FRAUDE DETECTADO' if es_fraude else 'Transacción Normal.')

"""
numpy.mean() y numply.std() calculan el comportamiento normal de gastos
se usa la regla 3 sigmas para idetificar valores fuera de lo normal
tiempo de ejecucion 0(1) excelente para deteccion en tiempo real.

"""
