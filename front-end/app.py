import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de produtos", page_icon="📦🧾")
st.title("📦 Estoque de produtos ")

menu = st.sidebar.radio("Navegação", ["Estoque", "Registrar produto", "Atualizar registro", "Deletar registro"])

if menu == "Estoque":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/listar_produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("❌ Não há produtos registrados")
    else:
        st.error("❌ Erro ao acessar a API")
    
