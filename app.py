import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

# Configuración inicial de la página
st.set_page_config(page_title="Ecuación Cuadrática", page_icon="🧮")

# Logo y encabezado
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Factorio_1.0.0_logo.svg/512px-Factorio_1.0.0_logo.svg.png ", width=100)
st.title("🧮 Resolver Ecuación Cuadrática")
st.markdown("### Desarrollado por: Marco Almeida | Correo: ingeltecservice@gmail.com")
st.markdown("Esta aplicación permite resolver ecuaciones cuadráticas, graficar funciones y exportar resultados.")

# Campos de entrada del usuario
a = st.number_input("Coeficiente a (≠ 0)", value=1.0)
b = st.number_input("Coeficiente b", value=0.0)
c = st.number_input("Coeficiente c", value=0.0)

# Rango de x personalizado
st.sidebar.header("Configuración de gráfica")
xmin = st.sidebar.number_input("Rango inicial de x:", value=-10.0)
xmax = st.sidebar.number_input("Rango final de x:", value=10.0)

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

    # Graficar función
    x = np.linspace(xmin, xmax, 400)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"f(x) = {a:.2f}x² + {b:.2f}x + {c:.2f}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    ax.set_title("Gráfica de la función cuadrática")
    st.pyplot(fig)

    # Botón para descargar gráfica como imagen
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=300)
    buf.seek(0)
    st.download_button(
        label="📥 Descargar gráfica como PNG",
        data=buf,
        file_name="grafica_cuadratica.png",
        mime="image/png"
    )

    # Generar tabla de datos
    df = pd.DataFrame({
        "x": x,
        "f(x)": y
    })

    # Botón para exportar a CSV
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📄 Exportar puntos a CSV",
        data=csv_data,
        file_name="tabla_datos_cuadraticos.csv",
        mime="text/csv"
    )

    # Mostrar los datos generados
    with st.expander("👁️ Ver tabla de valores"):
        st.dataframe(df)
