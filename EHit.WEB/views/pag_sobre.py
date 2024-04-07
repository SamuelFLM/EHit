import streamlit as st
from api import API
from utilidades import *

def sobre():
    api = API()
    artista = api.obter_por_id(st.session_state.id)
    try:
        if artista["foto"]:
            st.image(artista["foto"], caption=f"Idade: {artista["idade"]} anos.",width=350)
        else:
            st.image("", caption=f"Idade: {artista["idade"]} anos.",width=350)
    except:
        pass
    
    st.header(artista["nome"], divider="violet")
    
    st.markdown(artista["biografia"])
    
    st.header("Músicas", divider='violet')

    st.text("")

    st.button("Adicionar", on_click=mudar_pagina, args=("adicionar_musica",))

    st.text("")
    
    for musica in artista["musicas"]:
        with st.expander(musica["nome"]):
            col1, col2, col3, col4 = st.columns([0.3, 0.3, 0.3, 0.3])
            col1.button(f"{musica["nome"]}", use_container_width=True, key=f"unique_{musica["nome"]}_{id}", type='primary')
            col2.button(f"Gênero: {musica["genero"]}", use_container_width=True, key=f"unique_{musica["genero"]}_{id}_{musica["nome"]}", type='primary')
            col3.button(f"Nota: {float(musica["nota"])}", use_container_width=True, key=f"editar_{musica["nota"]}_{id}_{musica["nome"]}", type='primary')
            col4.button(f"Duração: {musica["duracao"]} s", use_container_width=True, key=f"excluir_{musica["duracao"]}_{id}_{musica["nome"]}", type='primary')
