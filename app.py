import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------------------------------------
# 1. Configuração da Página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Studio Artemis - Management",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. Estilização Visual Avançada (Dark & Gold Artemis)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Fundo geral escuro */
    .stApp {
        background-color: #0f0f0f;
        color: #e5e5e5;
    }

    /* Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #2a2211;
    }
    [data-testid="stSidebar"] * {
        color: #d4af37 !important;
    }

    /* Títulos e Cabeçalhos */
    h1 {
        color: #d4af37 !important;
        font-family: 'Georgia', serif;
        font-weight: 700;
        font-size: 1.8rem;
        letter-spacing: 0.5px;
    }
    h3 {
        color: #d4af37 !important;
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }

    /* Containers de Blocos (Cards) */
    .artemis-card {
        background-color: #161616;
        border: 1px solid #2a2211;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }

    /* Logotipo da Barra Lateral (Crescente Dourado) */
    .logo-container {
        text-align: center;
        padding: 1.5rem 0;
    }
    .logo-circle {
        width: 90px;
        height: 90px;
        border: 2px solid #d4af37;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        background: radial-gradient(circle, #1a170e 0%, #121212 100%);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    .logo-text {
        font-size: 2.2rem;
        color: #d4af37;
    }
    .logo-title {
        font-size: 0.8rem;
        letter-spacing: 3px;
        color: #d4af37;
        margin-top: 0.5rem;
        font-weight: bold;
    }

    /* Estilização de Tabelas */
    [data-testid="stDataFrame"] {
        border: 1px solid #2a2211;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Sidebar (Menu Lateral com Logotipo)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div class="logo-container">
            <div class="logo-circle">
                <div class="logo-text">🏹</div>
            </div>
            <div class="logo-title">STUDIO ARTEMIS</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    pagina = st.radio(
        "Navegação",
        [
            "Dashboard",
            "Fichas de Alunas",
            "Gestão de Níveis",
            "Biblioteca de Movimentos",
            "Configurações"
        ]
    )
    
    st.markdown("---")
    # Logotipo inferior na sidebar igual ao design
    st.markdown("""
        <div style="text-align: center; opacity: 0.7; margin-top: 2rem;">
            <div style="font-size: 1.5rem;">🌙</div>
            <div style="font-size: 0.65rem; letter-spacing: 2px; color: #d4af37;">ARTEMIS</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. Conteúdo Principal - Dashboard
# ---------------------------------------------------------
if pagina == "Dashboard":
    
    st.title("Dashboard de Evolução - Studio Artemis")
    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    # Linha Superior: Gestão de Níveis e Gráfico de Rosca
    col_top1, col_top2 = st.columns(2)

    with col_top1:
        st.markdown('<div class="artemis-card">', unsafe_allow_html=True)
        st.subheader("Gestão de Níveis e Figuras")
        st.write("Overall distribuição de alunas por nível:")
        
        # Barra visual de progresso de níveis
        st.markdown("""
            <div style="background-color: #222; border-radius: 6px; height: 14px; width: 100%; display: flex; overflow: hidden; margin: 15px 0 10px 0;">
                <div style="width: 35%; background-color: #7a6522;" title="Básico 1"></div>
                <div style="width: 30%; background-color: #bfa142;" title="Básico 2"></div>
                <div style="width: 25%; background-color: #d4af37;" title="Inter 1"></div>
                <div style="width: 10%; background-color: #f3e5ab;" title="Avançado"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #aaa;">
                <span>Básico 1</span>
                <span>Básico 2</span>
                <span>Inter 1</span>
                <span>Avançado</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_top2:
        st.markdown('<div class="artemis-card">', unsafe_allow_html=True)
        st.subheader("Progresso Técnico por Aluna")
        
        # Gráfico de Rosca (Donut Chart) com Altair
        source = pd.DataFrame({
            'Categoria': ['Finalizado', 'Em progresso', 'Aguardando Avaliação'],
            'Valor': [55, 30, 15],
            'Cor': ['#222222', '#bfa142', '#d4af37']
        })
        
        donut_chart = alt.Chart(source).mark_arc(innerRadius=50, outerRadius=80).encode(
            theta=alt.Theta(field="Valor", type="quantitative"),
            color=alt.Color(field="Categoria", type="nominal", 
                            scale=alt.Scale(domain=['Finalizado', 'Em progresso', 'Aguardando Avaliação'],
                                            range=['#333333', '#c2a13e', '#e6c55c']),
                            legend=alt.Legend(orient="right", title=None))
        ).properties(width=300, height=140)
        
        st.altair_chart(donut_chart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Linha Intermediária: Tabelas de Alunas e Requisitos
    col_mid1, col_mid2 = st.columns(2)

    with col_mid1:
        st.markdown('<div class="artemis-card">', unsafe_allow_html=True)
        st.subheader("Alunas para Progressão de Nível")
        
        df_prog = pd.DataFrame({
            "Nome": ["Ana Silva", "Beatriz Costa", "Carla Mendes"],
            "Nível Atual": ["Básico 1", "Básico 2", "Básico"],
            "Pendentes": [0, 0, 0]
        })
        
        # Exibição simulando a tabela com botão
        st.dataframe(df_prog, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_mid2:
        st.markdown('<div class="artemis-card">', unsafe_allow_html=True)
        st.subheader("Mapeamento de Requisitos Técnicos")
        
        df_req = pd.DataFrame({
            "Figura": ["Básico 1", "Básico 2", "Básico 3", "Inter 1", "Inter 1", "Avançado", "Avançado"],
            "Requisitos Técnicos": [
                "Figura 1 → Requisitos Técnicos",
                "Figura 2 → Requisitos Técnicos",
                "Figura 1 → Aguardando Avaliação",
                "Figura 2 → Requisitos Técnicos",
                "Figura 2 → Requisitos Técnicos",
                "Trançado → Aguardando Técnicos",
                "Figura 2 → Avançado"
            ]
        })
        
        st.dataframe(df_req, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Linha Inferior: Registros Rápidos e Frequência
    st.markdown('<div class="artemis-card">', unsafe_allow_html=True)
    st.subheader("Registros Rápidos")
    
    col_bot1, col_bot2 = st.columns([1, 1])
    with col_bot1:
        st.write("Frequência e Acompanhamento de Aula")
        st.date_input("Data da Aula", value=pd.to_datetime("2023-01-11"))
    with col_bot2:
        st.info("Painel rápido de controle de presenças e lançamentos diários das professoras.")
        
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Fichas de Alunas":
    st.title("Fichas de Alunas")
    st.info("Módulo detalhado de fichas individuais.")

elif pagina == "Gestão de Níveis":
    st.title("Gestão de Níveis")
    st.info("Módulo de configuração de níveis.")

elif pagina == "Biblioteca de Movimentos":
    st.title("Biblioteca de Movimentos")
    st.info("Catálogo de figuras.")

elif pagina == "Configurações":
    st.title("Configurações")
    st.info("Painel de ajustes.")
