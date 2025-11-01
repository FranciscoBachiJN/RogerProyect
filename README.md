# 🧠 Simulación de la Ley de Snell con Tkinter + Matplotlib

**Autores:**
- Francisco Díaz González  
- Osvaldo Antonio Valencia García  
- Ezequiel Isaí Ramos Gutiérrez  
- Mendoza Castillo Edsel Anuar  
- Emilio Martínez Quintanar  

---

## 🧩 Descripción general
Esta aplicación interactiva muestra la **Ley de Snell**, visualizando los rayos **incidente, reflejado y refractado**, así como el fenómeno de **Reflexión Interna Total (TIR)**.  
Permite modificar en tiempo real el **ángulo de incidencia (θ₁)** y los **índices de refracción (n₁, n₂)** de ambos medios mediante *sliders*, mostrando los cambios de forma visual e intuitiva.

---

## ⚙️ Tecnologías utilizadas
- **Python 3.13+**
- **Tkinter** — interfaz gráfica de usuario
- **Matplotlib** — renderizado del plano y los rayos
- **Math** — funciones trigonométricas para los cálculos físicos

---

## 🎯 Funcionalidades principales

✅ **Interfaz interactiva:**
- Control de **ángulo de incidencia (θ₁)** con deslizador.
- Control independiente de **índices de refracción n₁ y n₂**.
- Cálculo y visualización dinámica del **ángulo refractado (θ₂)**.

✅ **Visualización completa:**
- Dibujo de los rayos **incidente**, **reflejado** y **refractado**.
- Representación de la **normal** y del **plano separador** entre medios.
- Arcos y etiquetas de los ángulos **θ₁**, **θ₂** y **θc**.

✅ **Análisis automático:**
- Cálculo del **ángulo crítico (θc)** cuando n₁ > n₂.
- Detección de **Reflexión Interna Total (TIR)** con aviso visual en color rojo.

✅ **Experiencia de usuario mejorada:**
- Fondo oscuro para contraste óptimo.
- Escala y cuadrícula visibles.
- Confirmación al cerrar la ventana para evitar cierres accidentales.

---

## 🧮 Fórmulas empleadas

### Ley de Snell
\[
n_1 \sin(\theta_1) = n_2 \sin(\theta_2)
\]

### Ángulo crítico
\[
\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)
\quad (\text{sólo si } n_1 > n_2)
\]

---

## 💡 Requisitos

Instalar dependencias necesarias con:
```bash
pip install matplotlib
```

> **Nota:** Tkinter viene incluido por defecto con Python en la mayoría de las distribuciones.

---

## ▶️ Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/FranciscoBachiJN/SnellCalculator_v1.2
   cd SnellCalculator_v1.2
   ```

2. Ejecutar el programa:
   ```bash
   python main.py
   ```

3. Ajusta los valores con los *sliders* y observa cómo cambia la dirección de los rayos.

---

## 📊 Resultados esperados
- Si **n₁ < n₂**, el rayo refractado se acerca a la normal.  
- Si **n₁ > n₂**, se aleja de la normal y puede producirse **TIR**.  
- Al superar el ángulo crítico, desaparece el rayo refractado y se muestra un aviso de **Reflexión Interna Total**.

---
## 🎥 Demostración en video

[![Ver demostración en YouTube](https://img.youtube.com/vi/iEcdB9d64R8/hqdefault.jpg)](https://www.youtube.com/watch?v=iEcdB9d64R8)

## 🧠 Bitácora de desarrollo

### 🔹 Etapa 1: Diseño del entorno gráfico
- Se implementó la interfaz con **Tkinter**, configurando sliders y botones.
- Se añadieron etiquetas y valores dinámicos de los parámetros físicos.

### 🔹 Etapa 2: Cálculo físico y validación
- Se implementaron las ecuaciones de la **Ley de Snell** y **ángulo crítico**.
- Se añadieron condiciones para evitar errores de dominio y detectar **TIR**.

### 🔹 Etapa 3: Visualización y estilo
- Se integró **Matplotlib** para el dibujo vectorial de los rayos.
- Se aplicó un esquema de colores oscuros y se añadieron arcos y etiquetas con notación LaTeX.

### 🔹 Etapa 4: Optimización y compilación
- Se ajustaron escalas, cuadrículas y eventos de actualización.
- Se agregó una función de salida segura y se compiló el ejecutable con `pyinstaller`.

---

## 🧑‍💻 Créditos

Proyecto desarrollado por estudiantes para la visualización interactiva de la **Ley de Snell** en el marco de la materia de **Física General**.

---

## 🗂️ Estructura del proyecto

```
SnellCalculator_v1.2/
│
├── main.py         # Código fuente principal
├── README.md       # Guía de uso y documentación
└── dist/           # Ejecutable compilado
```

---

