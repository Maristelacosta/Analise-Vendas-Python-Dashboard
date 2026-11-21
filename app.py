import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard Comercial",
    page_icon="📊",
    layout="wide"
)

# Base de dados
df = pd.DataFrame({
    "Produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Impressora"],
    "Vendas": [5000, 800, 3000, 1200, 2500],
    "Região": ["Sul", "Sudeste", "Sul", "Nordeste", "Sudeste"]
})

# Barra lateral
st.sidebar.header("Filtros")

regiao = st.sidebar.selectbox(
    "Selecione a região",
    ["Todas"] + list(df["Região"].unique())
)

# Filtro
if regiao != "Todas":
    df_filtrado = df[df["Região"] == regiao]
else:
    df_filtrado = df

# Indicadores
faturamento = df_filtrado["Vendas"].sum()
media_vendas = df_filtrado["Vendas"].mean()
maior_venda = df_filtrado["Vendas"].max()

# Título
st.title("📊 Painel Comercial")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Faturamento", f"R$ {faturamento:,.2f}")

with col2:
    st.metric("📈 Média de Vendas", f"R$ {media_vendas:,.2f}")

with col3:
    st.metric("🏆 Maior Venda", f"R$ {maior_venda:,.2f}")

st.divider()

# Gráfico de barras
fig_bar = px.bar(
    df_filtrado,
    x="Produto",
    y="Vendas",
    color="Região",
    title="Vendas por Produto",
    text_auto=True
)

st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de pizza
fig_pizza = px.pie(
    df_filtrado,
    names="Região",
    values="Vendas",
    title="Participação por Região"
)

st.plotly_chart(fig_pizza, use_container_width=True)

st.divider()

# Tabela
st.subheader("📋 Base de Dados")
st.dataframe(df_filtrado, use_container_width=True)