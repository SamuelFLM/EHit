import streamlit as st
from utilidades import *
from streamlit_option_menu import option_menu
from views.pag_artista import *
from views.pag_home import *
from views.pag_sobre import *
from forms.add_artista import forms_artista
from forms.upd_artista import forms_editar_artista
from forms.add_musica import forms_musica
from api import API

st.set_page_config("EHit", page_icon="🎶", layout="wide")

inicializar()
api = API()

st.sidebar.button(
    "Home", on_click=mudar_pagina, args=("home",), use_container_width=True
)
st.sidebar.button(
    "Artistas", on_click=mudar_pagina, args=("artista",), use_container_width=True
)

if st.session_state.artista != "":
    api.adicionar_artista(st.session_state.artista)

if st.session_state.pagina_atual == "home":
    home()

elif st.session_state.pagina_atual == "artista":
    artista()

elif st.session_state.pagina_atual == "adicionar_artista":
    forms_artista()

elif st.session_state.pagina_atual == "editar_artista":
    forms_editar_artista()

elif st.session_state.pagina_atual == "artista_sobre":
    sobre()

elif st.session_state.pagina_atual == "adicionar_musica":
    forms_musica()

elif st.session_state.pagina_atual == "salvar_artista":
    artista()

elif st.session_state.pagina_atual == "excluir_musica":
    excluir()
    artista()
