import streamlit as st
from api import API


def inicializar():
    if not "pagina_atual" in st.session_state:
        st.session_state.pagina_atual = "home"

    if not "artista" in st.session_state:
        st.session_state.artista = ""

    if not "add_artista" in st.session_state:
        st.session_state.add_artista = ""

    if not "id" in st.session_state:
        st.session_state.id = ""


def mudar_pagina(pag):
    st.session_state.pagina_atual = pag


def excluir():
    api = API()
    api.deletar(st.session_state.id)
    st.toast("Artista Excluído.", icon="❌")
