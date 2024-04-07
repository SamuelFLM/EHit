import streamlit as st
from utilidades import *
from api import API


def forms_editar_artista():
    api = API()
    st.header("Editar Artista", divider="violet")
    artista = api.obter_por_id(st.session_state.id)
    with st.form("Editar", border=True):
        st.write("Editar artista favorito")

        nome = st.text_input("Nome", max_chars=50, value=artista["nome"])

        espaco_entre_componente(2)

        idade = st.text_input("Idade", max_chars=2, value=artista["idade"])

        espaco_entre_componente(2)

        foto = st.text_input(
            "Foto",
            value=artista["foto"],
        )

        espaco_entre_componente(2)

        biografia = st.text_area(
            "Biografia",
            value=artista["biografia"],
        )

        espaco_entre_componente(2)

        col1, col2 = st.columns([0.3, 1])
        btn_adicionar = col1.form_submit_button(
            "Salvar",
            use_container_width=True,
        )

        espaco_entre_componente(2)
        if btn_adicionar:
            artista = {
                "nome": str(nome),
                "biografia": str(biografia),
                "idade": int(idade),
                "foto": str(foto),
            }
            api.alterar(st.session_state.id, artista)
            st.toast(f"Sucesso", icon="✅")
            st.success("Artista alterado com sucesso.")


def espaco_entre_componente(n_espaco):
    for i in range(n_espaco):
        st.write("")
