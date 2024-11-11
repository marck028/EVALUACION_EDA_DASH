import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
data = pd.read_excel("C:\\Users\\Marco\\Downloads\\economia_financiera.xlsx")

# Configurar el título y la estructura del dashboard
st.title("Dashboard Interactivo de Análisis Financiero y Demográfico")
st.sidebar.header("Filtros")

# Configurar filtros
genero = st.sidebar.multiselect("Género", options=data['Genero'].unique(), default=data['Genero'].unique())
edad = st.sidebar.multiselect("Rango de Edad", options=data['Rango_Edad'].unique(), default=data['Rango_Edad'].unique())
socieconomico = st.sidebar.multiselect("Nivel Socioeconómico", options=data['nivel_socieconomico'].unique(), default=data['nivel_socieconomico'].unique())
laboral = st.sidebar.multiselect("Situación Laboral", options=data['Situacion_Laboral'].unique(), default=data['Situacion_Laboral'].unique())
distrito = st.sidebar.multiselect("Distrito", options=data['Distrito'].unique(), default=data['Distrito'].unique())

# Aplicar filtros
filtered_data = data[
    (data['Genero'].isin(genero)) &
    (data['Rango_Edad'].isin(edad)) &
    (data['nivel_socieconomico'].isin(socieconomico)) &
    (data['Situacion_Laboral'].isin(laboral)) &
    (data['Distrito'].isin(distrito))
]

# Gráfico de Barras: Distribución de niveles socioeconómicos por género
st.subheader("Distribución de Niveles Socioeconómicos por Género")
bar_chart = px.bar(filtered_data, x='Genero', color='nivel_socieconomico', barmode='group')
st.plotly_chart(bar_chart, use_container_width=True)

# Gráfico de Torta: Distribución de Situación Laboral
st.subheader("Distribución de Situación Laboral")
pie_chart = px.pie(filtered_data, names='Situacion_Laboral', title="Situación Laboral")
st.plotly_chart(pie_chart, use_container_width=True)

# Gráfico de Barras Apiladas: Uso de Productos Financieros por Nivel Socioeconómico
st.subheader("Uso de Productos Financieros por Nivel Socioeconómico")
stacked_bar_chart = px.histogram(filtered_data, x='nivel_socieconomico', color='tarjeta_debito', barmode='stack')
st.plotly_chart(stacked_bar_chart, use_container_width=True)

# Gráfico de Dispersión: Relación entre menores y mayores de edad en el grupo familiar
st.subheader("Relación entre Menores y Mayores de Edad en el Grupo Familiar")
scatter_plot = px.scatter(filtered_data, x='menores_edad', y='mayores_edad', color='Genero')
st.plotly_chart(scatter_plot, use_container_width=True)

# Mapa de Calor: Nivel de educación y uso de tarjeta de crédito
st.subheader("Nivel de Educación y Uso de Tarjeta de Crédito")
heatmap_data = pd.crosstab(filtered_data['Nivel_educacion'], filtered_data['tarjeta_credito'])
heatmap = px.imshow(heatmap_data, labels=dict(x="Uso de Tarjeta de Crédito", y="Nivel de Educación"), color_continuous_scale="Viridis")
st.plotly_chart(heatmap, use_container_width=True)

# Gráfico de Área: Conceptos de ahorro e inversión a través de diferentes niveles socioeconómicos
st.subheader("Conceptos de Ahorro e Inversión por Nivel Socioeconómico")
line_chart = px.area(filtered_data, x='nivel_socieconomico', y='conceptos_ahorro_inversion', color='nivel_socieconomico')
st.plotly_chart(line_chart, use_container_width=True)

# Gráfico de Columnas Apiladas con Filtro: Distribución de productos financieros por rango de edad
st.subheader("Distribución de Productos Financieros por Rango de Edad")
stacked_column_chart = px.histogram(filtered_data, x='Rango_Edad', color='depositos_cuentas_ahorro', barmode='stack')
st.plotly_chart(stacked_column_chart, use_container_width=True)


st.subheader("Distribución de Clientes por Rango de Edad")
hist_chart = px.histogram(filtered_data, x='Rango_Edad', nbins=10, title="Distribución de Edad de los Clientes")
st.plotly_chart(hist_chart, use_container_width=True)

st.subheader("Distribución de Ingresos por Nivel de Educación")
box_plot = px.box(filtered_data, x='Nivel_educacion', y='plan_economico_mensual', color='Nivel_educacion', title="Ingresos según Nivel de Educación")
st.plotly_chart(box_plot, use_container_width=True)

st.subheader("Uso de Préstamos según Situación Laboral")
stacked_bar_chart = px.histogram(filtered_data, x='Situacion_Laboral', color='prestamos_personales', barmode='stack', title="Uso de Préstamos por Situación Laboral")
st.plotly_chart(stacked_bar_chart, use_container_width=True)

st.subheader("Familiaridad con Préstamos vs Nivel Socioeconómico")
scatter_plot = px.scatter(filtered_data, x='nivel_socieconomico', y='prestamos_personales', color='nivel_socieconomico', title="Familiaridad con Préstamos por Nivel Socioeconómico")
st.plotly_chart(scatter_plot, use_container_width=True)
