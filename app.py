import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.title("🧮 Resolver Ecuación Cuadrática")
st.write("Ingresa los coeficientes a, b y c para resolver ax² + bx + c = 0")

a = st.number_input("Coeficiente a (≠ 0)", value=1.0)
b = st.number_input("Coeficiente b", value=0.0)
c = st.number_input("Coeficiente c", value=0.0)

if a == 0:
    st.error("El valor de 'a' no puede ser cero.")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        st.success("Raíces reales distintas")
        st.write(f"Raíz 1: {raiz1:.4f}")
        st.write(f"Raíz 2: {raiz2:.4f}")
    elif discriminante == 0:
        raiz = -b / (2 * a)
        st.info("Raíces reales coincidentes")
        st.write(f"Raíz doble: {raiz:.4f}")
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
        st.warning("Raíces complejas distintas")
        st.write(f"Raíz 1: {parte_real:.4f} ± {parte_imaginaria:.4f}i")

    # Graficar
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"f(x) = {a:.2f}x² + {b:.2f}x + {c:.2f}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    ax.set_title("Gráfica de la función cuadrática")
    st.pyplot(fig)