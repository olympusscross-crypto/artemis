import streamlit as st
import pandas as pd
import altair as alt

# Configuração da página
st.set_page_config(
    page_title="Studio Artemis - Management",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS fiel ao design escuro com detalhes dourados
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    [data-testid="stSidebar"] {
        background-color: #161616 !important;
        border-right: 1px solid #2a2211;
    }
    [data-testid="stSidebar"] * {
        color: #d4af37 !important;
    }
    h1 {
        color: #222222 !important;
        font-family: 'Georgia', serif;
        font-size: 1.8rem;
        font-weight: bold;
    }
    /* Estilo de Cartões/Containers */
    .card-box {
        background-color: #1a1a1a;
        border: 1px solid #2e2614;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .card-title {
        color: #d4af37;
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    /* Logo Circular na Sidebar */
    .sidebar-logo-container {
        text-align: center;
        padding: 1.5rem 0;
    }
    .sidebar-logo-circle {
        width: 100px;
        height: 100px;
        border: 2px solid #d4af37;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        background: radial-gradient(circle, #221d10 0%, #121212 100%);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.25);
    }
    .sidebar-logo-text {
        font-size: 2.2rem;
        line-height: 1;
    }
    .sidebar-logo-sub {
        font-size: 0.55rem;
        letter-spacing: 2px;
        color: #d4af37;
        margin-top: 4px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div class="sidebar-logo-container">
            <div class="sidebar-logo-circle">
                <div class="sidebar-logo-text">💃</div>
                <div class="sidebar-logo-sub">ARTEMIS</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    pagina = st.radio(
        "Menu Principal",
        [
            "Dashboard",
            "Fichas de Alunas",
            "Gestão de Níveis",
            "Biblioteca de Movimentos",
            "Configurações"
        ]
    )
    
    st.markdown("---")
    # Logotipo inferior da sidebar igualzinho à foto
    st.markdown("""
        <div style="text-align: center; padding-top: 1rem;">
            <div style="font-size: 1.8rem; color: #d4af37;">🏹</div>
            <div style="font-size: 0.7rem; letter-spacing: 3px; color: #d4af37; font-weight: bold;">ARTEMIS</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTEÚDO PRINCIPAL: DASHBOARD
# ---------------------------------------------------------
if pagina == "Dashboard":
    
    st.markdown("<h1>Dashboard de Evolução - Studio Artemis</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #2e2614; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

    # LINHA 1: Gestão de Níveis & Progresso Técnico (Lado a Lado)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Gestão de Níveis e Figuras</div>', unsafe_allow_html=True)
        st.write("Overall distribuição de alunas:")
        
        # Barra de distribuição por nível
        st.markdown("""
            <div style="background-color: #222; border-radius: 4px; height: 12px; width: 100%; display: flex; overflow: hidden; margin: 15px 0 10px 0;">
                <div style="width: 35%; background-color: #615220;" title="Básico 1"></div>
                <div style="width: 30%; background-color: #9c812d;" title="Básico 2"></div>
                <div style="width: 25%; background-color: #c4a135;" title="Inter 1"></div>
                <div style="width: 10%; background-color: #f3e5ab;" title="Avançado"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #999;">
                <span>Básico 1</span>
                <span>Básico 2</span>
                <span>Inter 1</span>
                <span>Avançado</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Progresso Técnico por Aluna</div>', unsafe_allow_html=True)
        
        # Gráfico de Rosca (Donut Chart)
        df_donut = pd.DataFrame({
            'Status': ['Finalizado', 'Em progresso', 'Aguardando Avaliação'],
            'Valor': [60, 25, 15]
        })
        
        donut = alt.Chart(df_donut).mark_arc(innerRadius=45, outerRadius=75).encode(
            theta=alt.Theta(field="Valor", type="quantitative"),
            color=alt.Color(field="Status", type="nominal",
                            scale=alt.Scale(domain=['Finalizado', 'Em progresso', 'Aguardando Avaliação'],
                                            range=['#2c2c2c', '#b39436', '#e0c765']),
                            legend=alt.Legend(orient="right", title=None))
        ).properties(width=280, height=130)
        
        st.altair_chart(donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # LINHA 2: Alunas para Progressão & Mapeamento de Requisitos
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Alunas para Progressão de Nível</div>', unsafe_allow_html=True)
        
        df_alunas = pd.DataFrame({
            "Nome": ["Nome Nome", "Nome Nome", "Nome Nome"],
            "Nível Atual": ["Básico 1", "Básico 2", "Básico"],
            "Pendentes": [0, 0, 0]
        })
        st.dataframe(df_alunas, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Mapeamento de Requisitos Técnicos</div>', unsafe_allow_html=True)
        
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

    # LINHA 3: Registros Rápidos e Frequência
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Registros Rápidos</div>', unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        st.write("Atendência da classe")
        st.date_input("Data de Seleção", value=pd.to_datetime("2023-01-11"), label_visibility="collapsed")
    with r2:
        st.write("Controle de Presença e Lançamentos")
        st.caption("Painel operacional rápido para o registo diário das turmas do estúdio.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Fichas de Alunas":
    st.title("Fichas de Alunas")
    st.info("Módulo em construção.")
elif pagina == "Gestão de Níveis":
    st.title("Gestão de Níveis")
    st.info("Módulo em construção.")
elif pagina == "Biblioteca de Movimentos":
    st.title("Biblioteca de Movimentos")
    st.info("Módulo em construção.")
elif pagina == "Configurações":
    st.title("Configurações")
    st.info("Módulo em construção.")
