# ============================================================
#  Simulación de la Ley de Snell con Tkinter + Matplotlib
#  First Programer: Francisco Diaz Gonzalez
#  other programer:
#       Osvaldo Antonio Valencia Garcia 
#       Ezequiel Isai Ramos Gutierrez 
#       Mendoza Castillo Edsel Anuar
#       emilio martinez quintanar
# Descripción:
#     Visualiza la refracción, reflexión y reflexión total interna
#     según los índices de refracción y el ángulo de incidencia.
# ============================================================

import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

# ============================================================
#  CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================================

root = tk.Tk()
root.geometry("805x1000")
root.title("Simulación Ley de Snell")
root.configure(bg="#1e1e1e")  # Fondo oscuro

# ============================================================
#  VARIABLES GLOBALES
# ============================================================

TamañoVec = 10
vector = None
vectorReflejo = None
VectorAtravieza = None
arc1 = None
arc2 = None
Tetona1 = None
Tetona2 = None

# ============================================================
#  FUNCIÓN PARA BORRAR ELEMENTOS ANTERIORES DEL PLANO
# ============================================================

def Borra():
    """Elimina los vectores, arcos y textos anteriores del gráfico."""
    global vector, vectorReflejo, VectorAtravieza, arc1, arc2, Tetona1, Tetona2

    elementos = [vector, vectorReflejo, VectorAtravieza, arc1, arc2, Tetona1, Tetona2]
    for e in elementos:
        if e is not None:
            e.remove()

    vector = vectorReflejo = VectorAtravieza = None
    arc1 = arc2 = Tetona1 = Tetona2 = None

# ============================================================
#  FUNCIÓN PRINCIPAL DE ACTUALIZACIÓN
# ============================================================

def Actualizar(value=None):
    """
    Calcula y dibuja los rayos incidente, reflejado y refractado
    según los valores actuales de los sliders.
    """
    global vector, vectorReflejo, VectorAtravieza, arc1, arc2, Tetona1, Tetona2

    Borra()
    Bandera = False  # Indica si hay reflexión total interna

    # --- Limpia textos anteriores del ángulo crítico ---
    for artist in ax.texts:
        artist.remove()

    # --- Lectura de valores desde los sliders ---
    theta1 = math.radians(Slider.get())
    n1 = Slider3.get()  # Índice del medio de origen
    n2 = Slider2.get()  # Índice del medio al que pasa

    # ========================================================
    #  CÁLCULO DEL ÁNGULO CRÍTICO
    # ========================================================
    if n1 > n2:
        theta_c = math.degrees(math.asin(n2 / n1))
        textoCritico = f"θc = {theta_c:.2f}°"
    else:
        theta_c = None
        textoCritico = "No existe ángulo crítico (n₁ ≤ n₂)"

    # ========================================================
    #  VECTOR DEL RAYO INCIDENTE
    # ========================================================
    Teta = theta1 + math.radians(90)
    VectOriginal = (math.cos(Teta) * TamañoVec, math.sin(Teta) * TamañoVec)

    # ========================================================
    #  VERIFICACIÓN DE REFLEXIÓN TOTAL INTERNA (TIR)
    # ========================================================
    if (n1 / n2) * math.sin(theta1) > 1:
        Bandera = True  # Ocurre TIR → no hay rayo refractado
    else:
        theta2 = math.asin((n1 / n2) * math.sin(theta1))      # Ángulo físico
        theta2_grafico = theta2 + math.radians(270)           # Ajuste visual (debajo del eje)
        xR = math.cos(theta2_grafico) * TamañoVec
        yR = math.sin(theta2_grafico) * TamañoVec

    # ========================================================
    #  DIBUJO DE RAYOS
    # ========================================================

    # --- Rayo incidente ---
    vector = ax.quiver(
        VectOriginal[0], VectOriginal[1],
        -VectOriginal[0], -VectOriginal[1],
        angles='xy', scale_units='xy', scale=1, color='#ff4444')

    # --- Rayo reflejado ---
    vectorReflejo = ax.quiver(
        0, 0,
        -VectOriginal[0], VectOriginal[1],
        angles='xy', scale_units='xy', scale=1, color='#4488ff')

    # --- Rayo refractado ---
    if not Bandera:
        VectorAtravieza = ax.quiver(0, 0, xR, yR, angles='xy',
                                    scale_units='xy', scale=1, color='#ffaa00')

        # Arco del ángulo refractado
        arc2 = patches.Arc(
            (0, 0), 4, 4,
            theta1=270,
            theta2=math.degrees(theta2_grafico),
            color='yellow', lw=2)
        ax.add_patch(arc2)

        # Texto θ₂
        angulo_medio2 = theta2_grafico - math.radians(10)
        x_texto2 = 3 * math.cos(angulo_medio2)
        y_texto2 = 3 * math.sin(angulo_medio2)
        Tetona2 = ax.text(
            x_texto2, y_texto2,
            r'$\theta$₂ =' + f"{math.degrees(theta2):.2f}°",
            fontsize=10, color='white')

    # ========================================================
    #  ARCO Y TEXTO DEL ÁNGULO DE INCIDENCIA
    # ========================================================
    arc1 = patches.Arc(
        (0, 0), 4, 4,
        theta1=90,
        theta2=Slider.get() + 90,
        color='yellow', lw=2)
    ax.add_patch(arc1)

    # Texto θ₁
    angulo_medio1 = Teta - math.radians(10)
    x_texto1 = 3 * math.cos(angulo_medio1)
    y_texto1 = 3 * math.sin(angulo_medio1)
    Tetona1 = ax.text(
        x_texto1, y_texto1,
        r'$\theta$₁ =' + f"{math.degrees(theta1):.2f}°",
        fontsize=10, color='white')

    # ========================================================
    #  MOSTRAR INFORMACIÓN DE ÁNGULO CRÍTICO
    # ========================================================
    color_texto = 'red' if Bandera else 'white'
    ax.text(-9.5, 9, textoCritico, fontsize=11, color=color_texto, ha='left', va='top')

    if Bandera and theta_c is not None:
        ax.text(-9.5, 8, "Reflexión total interna",
                fontsize=11, color='red', ha='left', va='top')

    # Actualiza el gráfico
    canvas.draw()

# ============================================================
#  CONFIGURACIÓN DE LA FIGURA MATPLOTLIB
# ============================================================

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('#0e0e0e')
fig.patch.set_facecolor('#1e1e1e')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.tick_params(colors="#ffffff")
ax.axhline(0, color="#ffffff")
ax.axvline(0, color="#ffffff")
ax.grid(True, linestyle='--', alpha=0.3, color='white')

# Zona inferior (medio donde se refracta)
cuadro = patches.Rectangle((-10, -10), 20, 10,
                           edgecolor='black', facecolor='white', alpha=0.1)
ax.add_patch(cuadro)

# ============================================================
#  CONTROLES (SLIDERS)
# ============================================================

Slider = tk.Scale(
    root, from_=1, to=89, resolution=0.1,
    label="Ángulo de incidencia θ₁",
    orient="horizontal", command=Actualizar,
    bg="#1e1e1e", fg="#ffffff", troughcolor="#333333",
    highlightbackground="#1e1e1e", activebackground="#00ffaa",
    sliderrelief='flat')
Slider.place(x=50, y=600, width=300)
Slider.set(45)

Slider3 = tk.Scale(
    root, from_=1, to=5, resolution=0.01,
    label="Índice de refracción n₁ (medio de origen)",
    orient="horizontal", command=Actualizar,
    bg="#1e1e1e", fg="#ffffff", troughcolor="#333333",
    highlightbackground="#1e1e1e", activebackground="#ffaa00",
    sliderrelief='flat')
Slider3.place(x=50, y=800, width=300)
Slider3.set(2.5)

Slider2 = tk.Scale(
    root, from_=1, to=5, resolution=0.01,
    label="Índice de refracción n₂ (medio de destino)",
    orient="horizontal", command=Actualizar,
    bg="#1e1e1e", fg="#ffffff", troughcolor="#333333",
    highlightbackground="#1e1e1e", activebackground="#ffaa00",
    sliderrelief='flat')
Slider2.place(x=400, y=600, width=300)
Slider2.set(2.5)

# ============================================================
#  INSERCIÓN DE FIGURA EN TKINTER
# ============================================================

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=0, y=0)
canvas.draw()

# ============================================================
#  FUNCIÓN DE CIERRE CONTROLADO
# ============================================================

def al_cerrar():
    """Confirma el cierre del programa."""
    if messagebox.askokcancel("Salir", "¿Seguro que quieres cerrar el programa?"):
        root.destroy()
        exit()

root.protocol("WM_DELETE_WINDOW", al_cerrar)

# ============================================================
#  EJECUCIÓN DEL PROGRAMA
# ============================================================

root.mainloop()
