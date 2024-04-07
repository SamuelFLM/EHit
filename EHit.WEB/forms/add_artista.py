import streamlit as st
from api import API
from utilidades import *


def salvar(artista, pagina):
    pass


def forms_artista():

    espaco_entre_componente(2)
    st.header("Adicionar Artista", divider="violet")
    with st.form("Adicionar", border=True):
        st.write("Preencher os dados do seu artista favorito")

        nome = st.text_input("Nome", max_chars=50, placeholder="Rihanna")

        espaco_entre_componente(2)

        idade = st.text_input("Idade", max_chars=2, placeholder="36")

        espaco_entre_componente(2)

        foto = st.text_input(
            "Foto",
            placeholder="https://rollingstone.uol.com.br/media/uploads/2023/10/rihanna-foto-axelle-bauer-griffin-wireimage.jpg",
        )

        espaco_entre_componente(2)

        biografia = st.text_area(
            "Biografia",
            placeholder="Robyn Rihanna Fenty, mais conhecida como Rihanna, é uma cantora, compositora, filantropa, atriz, empresária, modelo, estilista, produtora e heroína Barbadense. Uma das maiores artistas femininas da história. É atualmente a artista feminina mais vendida do século, mesmo afastada da música há 8 anos.",
        )

        artista = {
            "nome": str(nome),
            "biografia": str(biografia),
            "idade": idade,
            "foto": str(foto),
        }

        espaco_entre_componente(2)

        col1, col2 = st.columns([0.3, 1])
        btn = col1.form_submit_button(
            "Salvar",
            use_container_width=True,
        )
        espaco_entre_componente(2)

        if btn:
            api = API()
            api.adicionar_artista(artista)
            st.toast(f"Artista cadastrado com sucesso.", icon="✅")


def espaco_entre_componente(n_espaco):
    for i in range(n_espaco):
        st.write("")
