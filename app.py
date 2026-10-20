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

# Estilização limpa e profissional idêntica ao design solicitado
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
    .card-box {
        background-color: #1a1a1a;
        border: 1px solid #2e2614;
        border-radius: 6px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .card-title {
        color: #d4af37;
        font-family: 'Georgia', serif;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    # Exibe a sua logo real carregada no GitHub (substitui qualquer símbolo)
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.warning("Carregue a imagem 'logo.png' no GitHub para exibir a marca.")
    
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

# ---------------------------------------------------------
# CONTEÚDO PRINCIPAL: DASHBOARD
# ---------------------------------------------------------
if pagina == "Dashboard":
    
    st.markdown("<h2 style='color: #ffffff; font-family: Georgia;'>Dashboard de Evolução - Studio Artemis</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #2e2614; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

    # LINHA 1: Gestão de Níveis & Progresso Técnico
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Gestão de Níveis e Figuras</div>', unsafe_allow_html=True)
        st.write("Overall distribuição de alunas:")
        
        st.markdown("""
            <div style="background-color: #222; border-radius: 4px; height: 12px; width: 100%; display: flex; overflow: hidden; margin: 15px 0 10px 0;">
                <div style="width: 35%; background-color: #615220;"></div>
                <div style="width: 30%; background-color: #9c812d;"></div>
                <div style="width: 25%; background-color: #c4a135;"></div>
                <div style="width: 10%; background-color: #f3e5ab;"></div>
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

    # LINHA 2: Tabelas Exatas da Imagem
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

    # LINHA 3: Registros Rápidos
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Registros Rápidos</div>', unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        st.write("Atendência da classe")
        st.date_input("Data de Seleção", value=pd.to_datetime("2023-01-11"), label_visibility="collapsed")
    with r2:
        st.write("Controle de Presença e Lançamentos")
        st.caption("Painel operacional rápido para o registo diário das turmas.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Fichas de Alunas":
    st.title("Fichas de Alunas")
elif pagina == "Gestão de Níveis":
    st.title("Gestão de Níveis")
elif pagina == "Biblioteca de Movimentos":
    st.title("Biblioteca de Movimentos")
elif pagina == "Configurações":
    st.title("Configurações")
