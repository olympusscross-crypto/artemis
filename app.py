import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Studio Artemis - Gestão",
    page_icon="✨",
    layout="wide"
)

# Estilo visual (Escuro + Dourado)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #121212;
    }
    [data-testid="stSidebar"] * {
        color: #F3E5AB !important;
    }
    h1, h2, h3 {
        color: #D4AF37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Navegação
with st.sidebar:
    st.markdown("# ✨ Studio Artemis")
    st.markdown("---")
    pagina = st.radio(
        "Navegação",
        [
            "📊 Dashboard de Evolução",
            "👤 Fichas de Alunas",
            "🏆 Gestão de Níveis",
            "📖 Biblioteca de Movimentos",
            "⚙️ Configurações"
        ]
    )

# Páginas
if pagina == "📊 Dashboard de Evolução":
    st.title("Dashboard de Evolução - Studio Artemis")
    st.write("Visão geral de progresso técnico e métricas do estúdio.")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Alunas", "35")
    col2.metric("Nível Básico", "15")
    col3.metric("Nível Intermédio", "12")
    col4.metric("Nível Avançado", "8")

    st.markdown("---")
    st.subheader("📌 Alunas Prontas para Avaliação de Nível")
    
    dados_alunas = {
        "Nome da Aluna": ["Ana Silva", "Beatriz Costa", "Carla Mendes"],
        "Nível Atual": ["Básico 1", "Básico 2", "Intermédio 1"],
        "Pendências": ["Nenhuma (Pronta para teste)", "1 Figura (Climb)", "1 Transição"],
        "Status": ["Aguardando Avaliação", "Em Progresso", "Em Progresso"]
    }
    df = pd.DataFrame(dados_alunas)
    st.dataframe(df, use_container_width=True)

elif pagina == "👤 Fichas de Alunas":
    st.title("Fichas das Alunas")
    st.info("Módulo em desenvolvimento.")

elif pagina == "🏆 Gestão de Níveis":
    st.title("Gestão de Níveis e Transições")
    st.info("Módulo em desenvolvimento.")

elif pagina == "📖 Biblioteca de Movimentos":
    st.title("Biblioteca de Movimentos")
    st.info("Módulo em desenvolvimento.")

elif pagina == "⚙️ Configurações":
    st.title("Configurações")
    st.info("Módulo em desenvolvimento.")
