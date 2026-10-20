import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. Configuração da Página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Studio Artemis - Pole Dance & Movement",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. Design Personalizado e Estilização CSS (Dark & Gold)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Fundo principal escuro da Artemis */
    .stApp {
        background-color: #0d0d0d;
        color: #e0e0e0;
    }

    /* Estilo do Menu Lateral */
    [data-testid="stSidebar"] {
        background-color: #141414 !important;
        border-right: 1px solid #2a2415;
    }
    
    [data-testid="stSidebar"] * {
        color: #e5cb7a !important;
    }

    /* Títulos e Destaques em Dourado Métalico */
    h1, h2, h3, h4 {
        color: #d4af37 !important;
        font-family: 'Georgia', serif;
        font-weight: 600;
        letter-spacing: 0.8px;
    }

    /* Subtítulos e Textos Secundários */
    .sub-header-text {
        color: #aaaaaa;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }

    /* Cartões de Métricas Estilizados */
    .metric-card {
        background: linear-gradient(145deg, #181818, #111111);
        border: 1px solid #332a15;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    .metric-title {
        color: #aaaaaa;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        color: #f3e5ab;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 0.3rem;
    }

    /* Divisores Elegantes */
    hr {
        border-color: #2a2415 !important;
        margin: 1.5rem 0;
    }

    /* Estilo para Tabelas e Containers */
    [data-testid="stDataFrame"] {
        border: 1px solid #2a2415;
        border-radius: 8px;
        background-color: #121212;
    }

    /* Símbolo do Cabeçalho da Barra Lateral */
    .sidebar-brand {
        text-align: center;
        padding: 1rem 0;
    }
    .sidebar-brand-symbol {
        font-size: 2.8rem;
        color: #d4af37;
        line-height: 1;
    }
    .sidebar-brand-title {
        font-size: 1.3rem;
        font-weight: bold;
        letter-spacing: 2px;
        color: #d4af37;
        margin-top: 0.5rem;
    }
    .sidebar-brand-subtitle {
        font-size: 0.75rem;
        color: #888888;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Menu Lateral
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-brand-symbol">🌙✨</div>
            <div class="sidebar-brand-title">ARTEMIS</div>
            <div class="sidebar-brand-subtitle">Pole Dance Studio</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    pagina = st.radio(
        "Menu do Sistema",
        [
            "📊 Dashboard Geral",
            "👤 Fichas das Alunas",
            "🏆 Gestão de Níveis",
            "📖 Biblioteca de Movimentos",
            "⚙️ Configurações"
        ]
    )
    
    st.markdown("---")
    st.caption("Studio Artemis v1.0 • Sistema Pedagógico")

# ---------------------------------------------------------
# 4. Conteúdo Principal - Dashboard Geral
# ---------------------------------------------------------
if pagina == "📊 Dashboard Geral":
    
    # Cabeçalho Principal com Símbolo
    col_head1, col_head2 = st.columns([1, 10])
    with col_head1:
        st.markdown("<h1 style='text-align: center; margin: 0;'>🏹</h1>", unsafe_allow_html=True)
        
    with col_head2:
        st.title("Studio Artemis — Gestão Pedagógica")
        st.markdown("<p class='sub-header-text'>Visão geral do progresso técnico, turmas e avaliações pendentes.</p>", unsafe_allow_html=True)

    # Cartões de Métricas Estilizados em Dourado
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Alunas Ativas</div>
                <div class="metric-value">35</div>
            </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Nível Básico</div>
                <div class="metric-value">15</div>
            </div>
        """, unsafe_allow_html=True)
        
    with m3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Nível Intermédio</div>
                <div class="metric-value">12</div>
            </div>
        """, unsafe_allow_html=True)
        
    with m4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Nível Avançado</div>
                <div class="metric-value">8</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Seção: Avaliações Pendentes
    st.subheader("📌 Alunas Prontas para Exame de Nível")
    st.write("Alunas que completaram a frequência mínima e requisitos técnicos para transição:")

    dados_alunas = {
        "Aluna": ["Ana Silva", "Beatriz Costa", "Carla Mendes", "Diana Rocha"],
        "Nível Atual": ["Básico 1", "Básico 2", "Intermédio 1", "Básico 1"],
        "Requisitos Concluídos": ["100% (Pronta)", "85% (Falta Climb)", "90% (Falta Trava)", "100% (Pronta)"],
        "Status de Avaliação": ["🟢 Exame Agendado", "🟡 Em Treino", "🟡 Em Treino", "🟢 Aguardando Marcação"]
    }
    
    df_alunas = pd.DataFrame(dados_alunas)
    st.dataframe(df_alunas, use_container_width=True, hide_index=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Resumo Rápido da Biblioteca de Movimentos
    col_bottom1, col_bottom2 = st.columns(2)
    
    with col_bottom1:
        st.subheader("📖 Figuras Cadastradas")
        st.info("Total de 84 figuras e 32 transições registradas na Biblioteca do Studio.")

    with col_bottom2:
        st.subheader("📅 Próximas Avaliações")
        st.success("Exames de Mudança de Nível marcados para esta semana: 3 alunas.")

elif pagina == "👤 Fichas das Alunas":
    st.title("👤 Fichas e Histórico das Alunas")
    st.info("Módulo em estruturação técnica.")

elif pagina == "🏆 Gestão de Níveis":
    st.title("🏆 Requisitos e Matriz de Níveis")
    st.info("Módulo em estruturação técnica.")

elif pagina == "📖 Biblioteca de Movimentos":
    st.title("📖 Catálogo e Biblioteca de Movimentos")
    st.info("Módulo em estruturação técnica.")

elif pagina == "⚙️ Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.info("Módulo em estruturação técnica.")
