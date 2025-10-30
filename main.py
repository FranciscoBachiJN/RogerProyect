import tkinter as tk
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

root = tk.Tk()
root.geometry("805x700")
root.title("Simulación Ley de Snell")
root.configure(bg="#1e1e1e")  # Fondo oscuro

TamañoVec = 10
vector = None
vectorReflejo = None
VectorAtravieza = None
arc1 = None
arc2 = None
Tetona1 = None
Tetona2 = None
def Borra():
    global vector, vectorReflejo, VectorAtravieza,arc1,arc2,Tetona1,Tetona2
    if vector is not None:
        vector.remove()
        vector = None
    if vectorReflejo is not None:
        vectorReflejo.remove()
        vectorReflejo = None
    if VectorAtravieza is not None:
        VectorAtravieza.remove()
        VectorAtravieza = None
    if arc1 is not None:
        arc1.remove()
        arc1 = None
    if arc2 is not None:
        arc2.remove()
        arc2 = None
    if Tetona1 is not None:
        Tetona1.remove()
        Tetona1 = None
    if Tetona2 is not None:
        Tetona2.remove()
        Tetona2 = None
def Actualizar(value=None):
    global vector, vectorReflejo, VectorAtravieza,arc1,arc2,Tetona1,Tetona2
    Borra()
    Teta = math.radians(Slider.get())+math.radians(90)
    VectOriginal = ((math.cos(Teta)*TamañoVec),(math.sin(Teta)*TamañoVec))
    VectorRebote = (VectOriginal[0], VectOriginal[1])
    theta2 = math.asin(math.sin(Teta)/Slider2.get()) + math.radians(270)
    xR = math.cos(theta2)*TamañoVec
    yR = math.sin(theta2)*TamañoVec

    vector = ax.quiver(
        VectOriginal[0],
        VectOriginal[1],
        0-VectOriginal[0],
        0-VectOriginal[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color='#ff4444')
    vectorReflejo = ax.quiver(
        0,
        0,
        0-VectorRebote[0],
        VectorRebote[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color='#4488ff')
    if (Slider2.get() != 1):
        VectorAtravieza = ax.quiver(0, 0, xR, yR, angles='xy', scale_units='xy', scale=1, color='#ffaa00')
        arc2 = patches.Arc(
            (0, 0),
            4, 4,
            theta1=270,            
            theta2=math.degrees(theta2),  
            color='yellow',
            lw=2
            )
        ax.add_patch(arc2)
        angulo_medio2 = theta2 - math.radians(10)
        x_texto2 = 3 * math.cos(angulo_medio2)
        y_texto2 = 3 * math.sin(angulo_medio2)

        # Agrega texto sobre el arco
        Tetona2 = ax.text(x_texto2, y_texto2, r'$\theta$₂ =' +f"{math.degrees(theta2) - 270:.2f}", fontsize=10, color='white')
        
    canvas.draw()
    
    arc1 = patches.Arc(
    (0, 0),              # centro del arco
    4, 4,                # ancho y alto del arco
    theta1=90,            # ángulo inicial (en grados)
    theta2=Slider.get()+90,  # ángulo final
    color='yellow',
    lw=2
    )

    ax.add_patch(arc1)
    angulo_medio1 = Teta - math.radians(10)
    x_texto1 = 3 * math.cos(angulo_medio1)
    y_texto1 = 3 * math.sin(angulo_medio1)

    # Agrega texto sobre el arco
    Tetona1 = ax.text(x_texto1, y_texto1, r'$\theta$₁ =' +f"{math.degrees(Teta) - 90:.2f}", fontsize=10, color='white')
    canvas.draw()


# --- Crear figura de Matplotlib ---
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor('#0e0e0e')  # Fondo del plano
fig.patch.set_facecolor('#1e1e1e')  # Fondo del canvas
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.tick_params( colors="#ffffff")
ax.axhline(0, color="#ffffff")  
ax.axvline(0, color="#ffffff")  
ax.grid(True, linestyle='--', alpha=0.3, color='white')

cuadro = patches.Rectangle((-10, -10), 20, 10, edgecolor='black', facecolor='white', alpha=0.1)
ax.add_patch(cuadro)

# --- Sliders personalizados ---
Slider = tk.Scale(
    root,
    resolution= 0.1,
    from_=1, to=89,
    label="Ángulo de incidencia θ",
    orient="horizontal",
    command=Actualizar,
    bg="#1e1e1e",
    fg="#ffffff",
    troughcolor="#333333",
    highlightbackground="#1e1e1e",
    activebackground="#00ffaa",
    sliderrelief='flat'
)
Slider.place(x=50, y=600, width=300)
Slider.set(45)

Slider2 = tk.Scale(
    root,
    from_=1, to=5,
    label="Índice de refracción",
    resolution=0.01,
    orient="horizontal",
    command=Actualizar,
    bg="#1e1e1e",
    fg="#ffffff",
    troughcolor="#333333",
    highlightbackground="#1e1e1e",
    activebackground="#ffaa00",
    sliderrelief='flat'
)
Slider2.place(x=400, y=600, width=300)
Slider2.set(2.5)


# --- Insertar figura en Tkinter ---
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=0, y=0)
canvas.draw()

root.mainloop()
