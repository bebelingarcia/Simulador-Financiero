# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i-aGuK06Db-ri_7Khqsa2-iS5fjD5iJL
"""

#A) Simulador de Ahorro con Interés Compuesto (Pagaré Bancario)
# Función para calcular el monto final con interés compuesto
def interes_compuesto(P, r, n, t):
    M = P * (1 + r/n) ** (n * t)
    return M

# Ejemplo de uso:
P = 10000  # Monto inicial
r = 0.065  # Tasa de interés anual del 6.5%
n = 1  # Interés compuesto anual
t = 5  # 5 años

monto_final = interes_compuesto(P, r, n, t)
monto_final

# Función para calcular el pago mensual de un préstamo
def pago_prestamo(P, r, n):
    A = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return A

# Ejemplo de uso:
P_prestamo = 20000  # Monto del préstamo
r_mensual = 0.065 / 12  # Tasa de interés mensual
n_pagos = 60  # 5 años de pagos mensuales

pago_mensual = pago_prestamo(P_prestamo, r_mensual, n_pagos)
pago_mensual

# Simulador de Afores y Siefore basado en rendimiento promedio de 5 años
def rendimiento_siefore(monto, rendimiento_promedio, años):
    monto_final = monto * (1 + rendimiento_promedio) ** años
    return monto_final

# Ejemplo de uso:
monto_inicial = 50000  # Monto inicial del usuario
rendimiento_promedio_siefore = 0.05  # 5% de rendimiento anual
años = 20  # 20 años hasta el retiro

monto_final_siefore = rendimiento_siefore(monto_inicial, rendimiento_promedio_siefore, años)
monto_final_siefore

import yfinance as yf
import matplotlib.pyplot as plt

# Empresas tecnológicas en BMV y BIVA
empresas_bmv = ['AMX.MX', 'TLEVISACPO.MX', 'KOFUBL.MX', 'GFNORTEO.MX']  # Empresas en la Bolsa Mexicana
empresas_biva = ['CEMEX.MX', 'SOFTTEK.MX', 'ALSEA.MX', 'VITRO.MX']  # Empresas en la Bolsa Institucional de Valores

# Fechas de análisis de los últimos 5 años
inicio = '2019-01-01'
fin = '2024-01-01'

# Graficar acciones de BMV y BIVA
plt.figure(figsize=(14, 7))

# Graficar acciones de BMV
for accion in empresas_bmv:
    try:
        datos_bmv = yf.download(accion, start=inicio, end=fin)['Close']
        plt.plot(datos_bmv, label=f'BMV - {accion}')
    except Exception as e:
        print(f"No se pudieron obtener los datos para {accion} de BMV: {e}")

# Graficar acciones de BIVA
for accion in empresas_biva:
    try:
        datos_biva = yf.download(accion, start=inicio, end=fin)['Close']
        plt.plot(datos_biva, label=f'BIVA - {accion}')
    except Exception as e:
        print(f"No se pudieron obtener los datos para {accion} de BIVA: {e}")

# Agregar título y etiquetas a la gráfica
plt.title('Comparativa de Acciones (BMV vs BIVA)')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre (MXN)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

!git clone https://github.com/bebelingarcia/Simulador-Financiero.git

# Commented out IPython magic to ensure Python compatibility.
# %cd Simulador-Financiero

!git add .

!git commit -m "Actualización con cambios en el simulador bursátil"

!git push origin main