import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Dashboard Comercial",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Dashboard Comercial")

# Base de dados
dados = {
    "Produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Impressora"],
    "Vendas": [5000, 800, 3000, 1200, 2500],
    "Regiao": ["Sul", "Sudeste", "Sul", "Nordeste", "Sudeste"]
}

df = pd.DataFrame(dados)

# Filtro
regiao = st.sidebar.selectbox(
    "Selecione a região",
    ["Todas"] + list(df["Regiao"].unique())
)

if regiao != "Todas":
    df = df[df["Regiao"] == regiao]

# Indicadores
faturamento = df["Vendas"].sum()
media = df["Vendas"].mean()
maior = df["Vendas"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Faturamento",
        f"R$ {faturamento:,.2f}"
    )

with col2:
    st.metric(
        "📈 Média de Vendas",
        f"R$ {media:,.2f}"
    )

with col3:
    st.metric(
        "🏆 Maior Venda",
        f"R$ {maior:,.2f}"
    )

st.divider()

# Tabela
st.subheader("📋 Base de Dados")
st.dataframe(df)

# Gráfico
st.subheader("📊 Vendas por Produto")
st.bar_chart(
    df.set_index("Produto")["Vendas"]
)

# Ranking
st.subheader("📈 Ranking de Produtos")

ranking = df.sort_values(
    by="Vendas",
    ascending=False
)

st.dataframe(ranking)

# Produto destaque
st.subheader("🏅 Produto Destaque")

produto_top = df.loc[df["Vendas"].idxmax()]

st.success(
    f"O produto líder em vendas é "
    f"{produto_top['Produto']} "
    f"com faturamento de "
    f"R$ {produto_top['Vendas']:,.2f}"
)