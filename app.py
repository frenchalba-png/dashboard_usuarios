import streamlit as st
import pandas as pd

# --- Título y descripción ---
st.set_page_config(page_title="Dashboard de Usuarios", layout="wide")
st.title("Dashboard de Usuarios")
st.markdown("Visualización de datos desde archivo CSV con información de personas XY.")

# --- Cargar datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("personas_data.csv")
    return df

df = cargar_datos()

# --- Mostrar datos ---
st.subheader("Vista general de los datos")
st.dataframe(df, use_container_width=True)

# --- Métricas principales ---
st.subheader("Métricas generales")
col1, col2, col3 = st.columns(3)
col1.metric("Total de registros", len(df))
col2.metric("Edad promedio", round(df["edad"].mean(), 1))
col3.metric("Nacionalidades únicas", df["nacionalidad"].nunique())

# --- Filtros ---
st.subheader("Filtrar por nacionalidad")
nacionalidades = st.multiselect("Selecciona una o varias nacionalidades:", df["nacionalidad"].unique())
if nacionalidades:
    df = df[df["nacionalidad"].isin(nacionalidades)]

# --- Visualizaciones ---
st.subheader("Distribución de edades")
st.bar_chart(df["edad"])

st.subheader("Conteo por nacionalidad")
st.bar_chart(df["nacionalidad"].value_counts())

st.markdown("---")
st.caption("Creado por Alba F. 🚀✨ | Datos de ejemplo")
