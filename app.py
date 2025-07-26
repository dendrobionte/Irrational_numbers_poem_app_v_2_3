
import streamlit as st
import re
from collections import OrderedDict

st.set_page_config(page_title="Poética visual – Versión 2_2", layout="wide")

# --- ESTILO VISUAL PERSONALIZADO ---
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
        background-color: #f4f1ec;
        color: #2f2f2f;
    }
    .tanka-block {
        padding: 1.2em;
        margin-bottom: 1.5em;
        border-top: 2px dotted #bfae9c;
        border-bottom: 2px dotted #bfae9c;
        text-align: center;
        font-size: 1.1em;
        line-height: 1.6em;
    }
    .symbol {
        font-size: 1.3em;
        color: #a07d52;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌀 Poética visual – Versión 2_2")
st.markdown("Explora cómo distintas constantes matemáticas transforman un texto en Tankas numerados con estilo.")

def limpiar_texto(texto):
    palabras = re.findall(r"\b[a-záéíóúüñ]+\b", texto.lower())
    return list(OrderedDict.fromkeys(palabras))

@st.cache_data
def cargar_decimales(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        return f.read().strip().replace("\n", "")

def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman += syms[i]
            n -= val[i]
        i += 1
    return roman

def generar_versos(palabras, longitud=7):
    return [palabras[i:i+longitud] for i in range(0, len(palabras), longitud) if len(palabras[i:i+longitud]) == longitud]

def transformar_en_tanka(verso, i):
    if len(verso) != 7:
        return None
    numero = to_roman(i)
    return f"<div class='tanka-block'><div class='symbol'>{numero}</div>{verso[0]}<br>{verso[1]} {verso[2]}<br>{verso[3]}<br>{verso[4]} {verso[5]}<br>{verso[6]}</div>"

archivo = st.file_uploader("📄 Sube un archivo .txt", type="txt")

if archivo:
    texto = archivo.read().decode("utf-8")
    palabras = limpiar_texto(texto)
    total = len(palabras)
    st.success(f"✔️ Texto cargado con {total} palabras únicas.")

    st.sidebar.header("🔧 Parámetros de generación")
    número_generador = st.sidebar.selectbox("Número generador", ["π", "e", "φ", "√2", "√3", "τ", "Champernowne"])
    modo = st.sidebar.selectbox("Modo de lectura", ["Directo", "Inverso", "Espaciado", "Modular"])
    tam_bloque = st.sidebar.selectbox("Tamaño del bloque (cifras)", [3, 4, 5], index=1)
    inicio = st.sidebar.slider("Punto de inicio", 0, 10000, 0)
    salto = st.sidebar.slider("Salto entre bloques (solo para 'Espaciado')", 1, 20, 1)

    archivos = {
        "π": "pi_decimals.txt",
        "e": "e_decimals.txt",
        "φ": "phi_decimals.txt",
        "√2": "sqrt2_decimals.txt",
        "√3": "sqrt3_decimals.txt",
        "τ": "tau_decimals.txt",
        "Champernowne": "champernowne.txt"
    }

    decimales = cargar_decimales(archivos[número_generador])

    if modo == "Inverso":
        decimales = decimales[::-1]
    elif modo == "Espaciado":
        decimales = ''.join(decimales[i] for i in range(inicio, len(decimales), salto))

    usados = set()
    resultado = []
    registros = []
    i = inicio if modo != "Espaciado" else 0

    while len(usados) < total and i + tam_bloque <= len(decimales):
        bloque = int(decimales[i:i+tam_bloque])
        idx = bloque % total if modo == "Modular" else bloque - 1
        if 0 <= idx < total and idx not in usados:
            palabra = palabras[idx]
            resultado.append(palabra)
            usados.add(idx)
            registros.append((i, decimales[i:i+tam_bloque], idx + 1, palabra))
        i += tam_bloque

    st.sidebar.markdown("### 📊 Flujo de lectura")
    if registros:
        vista = registros[:5]
        resumen = "\n".join([f"{b} → {p}" for (_, b, _, p) in vista])
        st.sidebar.text(resumen)

    poema = " ".join(resultado)
    st.markdown("### ✨ Poema generado")
    st.text_area("Texto:", poema, height=200)
    st.download_button("💾 Descargar poema", poema, file_name="poema.txt", mime="text/plain")

    versos = generar_versos(resultado)
    tankas = [transformar_en_tanka(v, idx+1) for idx, v in enumerate(versos) if transformar_en_tanka(v, idx+1)]

    if tankas:
        st.markdown("### 🌸 Tankas visuales")
        for t in tankas:
            st.markdown(t, unsafe_allow_html=True)
        texto_tankas = "\n\n".join([re.sub('<[^<]+?>', '', t) for t in tankas])
        st.download_button("💾 Descargar tankas", texto_tankas, file_name="tankas.txt", mime="text/plain")

    if registros:
        st.markdown("### 🔍 Tabla de flujo")
        st.dataframe({
            "Posición": [r[0] for r in registros],
            "Bloque": [r[1] for r in registros],
            "Índice resultado": [r[2] for r in registros],
            "Palabra": [r[3] for r in registros]
        }, use_container_width=True)
else:
    st.info("📥 Sube un archivo para comenzar.")
