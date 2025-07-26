# 🌀 Poética Visual V2.2 – Algorítmica del Infinito

Explora cómo diferentes constantes matemáticas transforman un texto literario en un poema generado algorítmicamente. Esta aplicación convierte decimales infinitos en caminos poéticos que atraviesan un corpus de palabras, generando **Tankas visuales** y flujos de lectura con sentido estético y matemático.

---

## ✨ ¿Qué hace esta app?

- Lee un texto `.txt` cargado por el usuario.
- Extrae todas las palabras únicas y las indexa.
- Utiliza los decimales de una constante matemática como coordenadas para recorrer el texto.
- Genera un poema y una serie de **Tankas** (estrofas de 5 versos con estructura japonesa).
- Muestra un flujo numérico de lectura y permite descargar el resultado.

---

## 📐 Números generadores disponibles

Puedes elegir entre los siguientes números irracionales e infinitos como generadores poéticos:

- π (pi) – 3.1415…
- e (Euler) – 2.7182…
- φ (número áureo) – 1.6180…
- √2 – 1.4142…
- √3 – 1.7320…
- τ (2π) – 6.2831…
- Champernowne – 0.12345678910111213…

---

## 🎛️ Parámetros ajustables

- **Modo de lectura:** directo, inverso, espaciado o modular.
- **Tamaño del bloque:** 3, 4 o 5 cifras decimales.
- **Inicio y salto:** controla el punto de partida y el ritmo de lectura.

---

## 📥 Uso local

### 1. Clona este repositorio
```bash
git clone https://github.com/tu_usuario/poetica-visual-v22.git
cd poetica-visual-v22
```

### 2. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecuta la app
```bash
streamlit run app.py
```

---

## 📤 Despliegue en Streamlit Cloud

1. Sube este repositorio a GitHub.
2. Ve a [https://share.streamlit.io](https://share.streamlit.io)
3. Selecciona tu repositorio y el archivo `app.py`.
4. Asegúrate de incluir todos los archivos `.txt` de constantes.

---

## 📁 Estructura del proyecto

```
📦 poetica-visual-v22
 ┣ 📜 app.py
 ┣ 📜 pi_decimals.txt
 ┣ 📜 e_decimals.txt
 ┣ 📜 phi_decimals.txt
 ┣ 📜 sqrt2_decimals.txt
 ┣ 📜 sqrt3_decimals.txt
 ┣ 📜 tau_decimals.txt
 ┣ 📜 champernowne.txt
 ┗ 📜 requirements.txt
```

---

## 📦 requirements.txt sugerido

```txt
streamlit
sympy
mpmath
```

---

## 🧠 Inspiración

Esta aplicación es parte de un proyecto más amplio de investigación poética, algorítmica y estética. Combina principios de ecología simbólica, matemáticas y creación literaria computacional.

> “El número es natural y el cielo, un artificio.”

---

## ✍️ Autor

**Dédalo Toro Rivadeneira**  
Investigador en ecopoesía, estética del número y filosofía de la creación.

---

## 🌀 Licencia

Este proyecto es de código abierto y puede ser adaptado para fines artísticos, académicos y educativos. Siempre que menciones la autoría, el infinito será generoso contigo.
