import streamlit as st
import requests
import os
import json
from dotenv import load_dotenv
from utilidades import *
from forms.add_artista import *
from api import API

def button_clicked(artist_id, pagina):
  st.session_state.id = artist_id
  mudar_pagina(pagina)

def artista():
    
    load_dotenv()
    
    api = API()
    artistas = api.obter()    
    st.header("Artistas", divider='violet')
    pesquisar = st.text_input("Pesquisar Artista", max_chars=20, placeholder="Samuel")

    st.title("")
    col1, col2, col3, col4 = st.columns([0.7, 0.3, 0.3, 0.3])
    col4.button("➕ Adicionar", use_container_width=True, on_click=mudar_pagina, args=("adicionar_artista",))
    st.header("", divider="violet")
    st.text("")
    try:
        for i, artista in enumerate(artistas):
            id = artista["id"]   
            col1, col2, col3, col4,col5 = st.columns([0.7, 0.3, 0.3, 0.3,0.3])
            col1.button(f"{artistas[i]["nome"]}", use_container_width=True, key=f"unique_{artistas[i]["nome"]}", type='primary', on_click=button_clicked, args=(id,"artista_sobre"))
            col4.button("✏️ Editar", use_container_width=True, key=f"editar_{artistas[i]["nome"]}", on_click=button_clicked, args=(id,"editar_artista",))
            col5.button("❌ Excluir", use_container_width=True, key=f"excluir_{artistas[i]["nome"]}", on_click=button_clicked, args=(id,"excluir_musica",))
    except:
        pass
    st.header("", divider="violet")


if __name__ == "__main__":
    artista()
