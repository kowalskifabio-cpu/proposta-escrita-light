import streamlit as st
from streamlit_option_menu import option_menu

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Labor OS | Escrita Contabilidade", layout="wide", page_icon="📈")

# --- ESTILIZAÇÃO CSS (Padrão Labor Business) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { max-width: 1100px; margin: 0 auto; }
    .titulo-capa { color: #2c3e50; font-size: 38px; font-weight: bold; line-height: 1.2; }
    .sub-capa { color: #ff9900; font-size: 20px; font-weight: 500; margin-bottom: 30px; }
    .secao-header { color: #2c3e50; border-bottom: 2px solid #ff9900; padding-bottom: 5px; margin-top: 30px; margin-bottom: 20px; font-size: 26px; font-weight: bold; }
    .pilar-header { color: #ff9900; font-size: 18px; font-weight: bold; margin-top: 15px; }
    .card-cronograma { background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 5px solid #ff9900; margin-bottom: 10px; }
    .entrega-box { background-color: #e3f2fd; padding: 10px; border-radius: 5px; border: 1px solid #bbdefb; color: #1565c0; font-weight: 500; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- MENU LATERAL ---
with st.sidebar:
    try:
        st.image("tela inicial.png", use_container_width=True)
    except:
        st.error("Imagem 'tela inicial.png' não encontrada.")
    
    selected = option_menu(
        menu_title="Plano Light - 12 Meses",
        options=["Contexto", "Objetivos", "Pilares do Escopo", "Cronograma 12 meses", "Modelo e Investimento"],
        icons=["info-circle", "target", "diagram-3", "calendar-check", "cash-stack"],
        menu_icon="layers", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.write("**Cliente:** Escrita Contabilidade")
    st.write("**Projeto:** Labor OS")

# --- CONTEÚDO ---

if selected == "Contexto":
    st.markdown('<p class="titulo-capa">Labor OS — Governança, Precificação e Gestão</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-capa">PROPOSTA COMERCIAL — PLANO LIGHT (12 MESES)</p>', unsafe_allow_html=True)
    
    st.image("tela inicial.png", use_container_width=True)
    
    st.markdown('<div class="secao-header">1) Contexto e Motivação</div>', unsafe_allow_html=True)
    st.write("A Escrita possui uma base relevante (~800 clientes), mas o crescimento e a previsibilidade ficam limitados quando:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Falta método de precificação alinhado ao custo real")
        st.error("❌ Comercial opera sem governança de contratos")
        st.error("❌ Decisões com baixa rastreabilidade de indicadores")
    with col2:
        st.warning("⚠️ Centros de custos não suportam análise por cliente")
        st.warning("⚠️ Crescimento acelerado pode comprometer a qualidade")
    
    st.info("**Diretriz:** Crescer com segurança, preservando qualidade e capacidade do time.")

elif selected == "Objetivos":
    st.markdown('<div class="secao-header">2) Objetivo do Projeto</div>', unsafe_allow_html=True)
    st.write("Implantar, em 12 meses, um sistema de gestão e governança que permita:")
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("🎯 Precificar corretamente")
        st.markdown("🎯 Estruturar plano de contas")
    with cols[1]:
        st.markdown("🎯 Gestão por cliente (Centro de Resultado)")
        st.markdown("🎯 Gestão de contratos (SLA + Escopo)")
    with cols[2]:
        st.markdown("🎯 Pipeline comercial sustentável")
        st.markdown("🎯 Indicadores simples e auditáveis")

    st.markdown('<div class="secao-header">3) Entregáveis Finais (O que muda na prática)</div>', unsafe_allow_html=True)
    st.write("Ao final dos 12 meses, a Escrita terá:")
    st.success("✅ Política de precificação com critérios claros")
    st.success("✅ Estrutura gerencial com lucro real por cliente/segmento")
    st.success("✅ Modelo de contrato com limites de escopo e reajuste")
    st.success("✅ Fluxo comercial → operação com handoff e checklists")

elif selected == "Pilares do Escopo":
    st.markdown('<div class="secao-header">4) Escopo do PLANO LIGHT (Pilares)</div>', unsafe_allow_html=True)
    
    pilar = st.selectbox("Selecione um Pilar para ver os detalhes:", 
                        ["Pilar A - Estratégia de Precificação", 
                         "Pilar B - Método de Custeio e Contas", 
                         "Pilar C - Cliente como Centro de Resultado",
                         "Pilar D - Gestão de Contratos",
                         "Pilar E - Comercial Enxuto",
                         "Pilar F - Indicadores e Gestão"])

    if "Pilar A" in pilar:
        st.markdown('<p class="pilar-header">Estratégia de Precificação (Prioridade Máxima)</p>', unsafe_allow_html=True)
        st.write("- Revisão de portfólio, definição de preço mínimo sustentável e regras de reajuste.")
        st.markdown('<div class="entrega-box">Entregável: Playbook de Precificação + Tabela de pacotes.</div>', unsafe_allow_html=True)

    elif "Pilar B" in pilar:
        st.markdown('<p class="pilar-header">Método de Custeio + Plano de Contas</p>', unsafe_allow_html=True)
        st.write("- Adequação gerencial do plano de contas e definição de centros de custo.")
        st.markdown('<div class="entrega-box">Entregável: Modelo gerencial para custo e margem consistentes.</div>', unsafe_allow_html=True)

    elif "Pilar C" in pilar:
        st.markdown('<p class="pilar-header">Cliente como Centro de Resultado</p>', unsafe_allow_html=True)
        st.write("- Classificação de rentabilidade: rentáveis, neutros e deficitários.")
        st.markdown('<div class="entrega-box">Entregável: Matriz de rentabilidade por cliente e segmento.</div>', unsafe_allow_html=True)

    elif "Pilar D" in pilar:
        st.markdown('<p class="pilar-header">Gestão de Contratos Integrada</p>', unsafe_allow_html=True)
        st.write("- Padronização de propostas, SLAs e regras para serviços fora do pacote.")
        st.markdown('<div class="entrega-box">Entregável: Kit Contratual + checklist de onboarding e handoff.</div>', unsafe_allow_html=True)

    elif "Pilar E" in pilar:
        st.markdown('<p class="pilar-header">Comercial Enxuto (Governança)</p>', unsafe_allow_html=True)
        st.write("- Funil simples Lead → Onboarding, com definição de capacidade mensal (slots).")
        st.markdown('<div class="entrega-box">Entregável: Funil mínimo viável + regras de capacidade.</div>', unsafe_allow_html=True)

    elif "Pilar F" in pilar:
        st.markdown('<p class="pilar-header">Indicadores e Rotina de Gestão</p>', unsafe_allow_html=True)
        st.write("- Painel semanal com entradas/saídas, conversão, ticket médio e margem.")
        st.markdown('<div class="entrega-box">Entregável: Rotina semanal + indicadores acionáveis.</div>', unsafe_allow_html=True)

elif selected == "Cronograma 12 meses":
    st.markdown('<div class="secao-header">6) Cronograma Macro (12 meses)</div>', unsafe_allow_html=True)
    
    cronograma = [
        ("Mês 1", "Diagnóstico e Arquitetura", "Modelo desenhado e aprovado."),
        ("Meses 2-3", "Precificação e Pacotes", "Vender com preço certo e regra clara."),
        ("Meses 4-5", "Centro de Resultado por Cliente", "Enxergar lucro real por cliente."),
        ("Meses 6-7", "Contratos e Handoff", "Parar de vender contrato 'solto'."),
        ("Meses 8-9", "Comercial Enxuto e Sustentável", "Crescimento lento, porém saudável."),
        ("Meses 10-12", "Consolidação e Governança", "Modelo continua sem depender do consultor.")
    ]
    
    for mes, foco, marco in cronograma:
        st.markdown(f'<div class="card-cronograma"><strong>{mes}: {foco}</strong><br>🎯 Marco: {marco}</div>', unsafe_allow_html=True)

elif selected == "Modelo e Investimento":
    st.markdown('<div class="secao-header">5) Modelo de Trabalho (Light e Sustentável)</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("💻 **Reunião Online Semanal:** 60 a 90 min.")
        st.write("🏢 **Reunião Presencial Mensal:** 1 dia (opcional).")
    with col2:
        st.write("📱 **Suporte Assíncrono:** WhatsApp/Email para dúvidas.")
        st.write("⚠️ **Foco:** Estruturar o time, não substituir.")

    st.markdown('<div class="secao-header">9) Investimento (Novo Modelo Light)</div>', unsafe_allow_html=True)
    st.metric("Fixo Mensal", "R$ 5.000,00 / mês", "12 meses")
    st.info("**Success Fee:** 10% sobre receita recebida de clientes novos.")

    st.markdown('<div class="secao-header">8) Limites do Escopo</div>', unsafe_allow_html=True)
    st.write("Não inclui: Prospecção diária (SDR), gestão de equipe, tráfego pago ou promessas de volume de vendas.")
    
    st.divider()
    if st.button("Aprovar Proposta Escrita Contabilidade"):
        st.balloons()
        st.success("Proposta aceita! Próximo passo: Reunião de Kick-off.")

# --- RODAPÉ ---
st.divider()
st.caption("Labor Business - Governança Comercial e Gestão de Capacidade")
