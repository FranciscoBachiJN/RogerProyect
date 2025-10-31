# 🧠 Simulación de la Ley de Snell con Tkinter + Matplotlib

**Autores:**
- Francisco Díaz González  
- Osvaldo Antonio Valencia García  
- Ezequiel Isaí Ramos Gutiérrez  
- Mendoza Castillo Edsel Anuar  
- Emilio Martínez Quintanar  

---

## 🧩 Descripción general
Esta aplicación interactiva permite visualizar el fenómeno de **refracción y reflexión** de la luz según la **Ley de Snell**.  
El usuario puede ajustar el ángulo de incidencia y los índices de refracción de ambos medios para observar cómo cambia el rayo refractado o reflejado.

---

## ⚙️ Tecnologías utilizadas
- **Python 3.13+**
- **Tkinter** (interfaz gráfica)
- **Matplotlib** (visualización de rayos)
- **Math** (cálculos trigonométricos)

---

## 🎯 Funcionalidades principales
✅ Interfaz gráfica con sliders para:
- Ángulo de incidencia (θ₁)
- Índice de refracción del medio 1 (n₁)
- Índice de refracción del medio 2 (n₂)

✅ Dibujo dinámico:
- Rayo incidente  
- Rayo reflejado  
- Rayo refractado  
- Normal y plano divisorio  

✅ Cálculos en tiempo real:
- Ángulo de refracción (θ₂)
- Verificación del ángulo crítico
- Detección de **TIR** (Reflexión Interna Total)

✅ Botón para cerrar el programa correctamente.

---

## 🧮 Fórmulas empleadas

### Ley de Snell:
\[
n_1 \sin(\theta_1) = n_2 \sin(\theta_2)
\]

### Ángulo crítico:
\[
\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)
\quad (\text{sólo si } n_1 > n_2)
\]

---

## 💡 Requisitos
Instalar dependencias con:
```bash
pip install matplotlib
```

---

## ▶️ Ejecución
Ejecutar el archivo principal:
```bash
python main.py
```

---

## 🧑‍💻 Créditos
Proyecto desarrollado por estudiantes para la visualización interactiva de la **Ley de Snell**.

## Programa compilado
Se encuentra en dist.
