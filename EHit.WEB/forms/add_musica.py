import streamlit as st
from utilidades import *
from api import API


def forms_musica():
    api = API()
    st.header("Adicionar Música", divider="violet")
    with st.form("Adicionar_Musica", border=True):
        st.write("Preencher os dados da música do artista")

        nome = st.text_input("Nome", max_chars=50, placeholder="Diamonds")

        espaco_entre_componente(2)

        genero = st.text_input("Gênero", max_chars=10, placeholder="Pop")

        espaco_entre_componente(2)

        nota = st.text_input(
            "Nota",
            placeholder="10",
        )

        espaco_entre_componente(2)

        duracao = st.text_input(
            "Duração",
            placeholder="220",
        )

        espaco_entre_componente(2)

        col1, col2 = st.columns([0.3, 1])
        btn_adicionar = col1.form_submit_button(
            "Adicionar",
            use_container_width=True,
        )

        espaco_entre_componente(2)
        if btn_adicionar:
            musica = {
                "nome": str(nome),
                "genero": str(genero),
                "nota": int(nota),
                "duracao": str(duracao),
            }
            api.adicionar_musica(st.session_state.id, musica)
            st.toast(f"Sucesso", icon="✅")
            st.success("Artista cadastrado com sucesso.")


def espaco_entre_componente(n_espaco):
    for i in range(n_espaco):
        st.write("")
