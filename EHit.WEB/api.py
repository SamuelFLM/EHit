from dotenv import load_dotenv
import os
import requests, json


class API:
    load_dotenv()

    def __init__(self) -> None:
        self.url = os.environ["URL_BASE"]
        self.headers = {"Content-Type": "application/json"}

    def obter(self):
        try:
            resposta = requests.get(self.url)
            if resposta.status_code:
                return resposta.json()
        except Exception:
            return ""

    def obter_musicas(self, id):
        try:
            resposta = requests.get(f"{self.url}/{id}/musica")
            if resposta.status_code:
                return resposta.json()
        except Exception:
            return ""

    def obter_por_id(self, id):
        try:
            resposta = requests.get(f"{self.url}/{id}")
            return resposta.json()
        except Exception:
            return ""

    def adicionar_artista(self, artista):
        try:
            resposta = requests.post(url=self.url, json=artista, headers=self.headers)
            return resposta.json()
        except Exception:
            return ""

    def adicionar_musica(self, id, musica):
        try:
            resposta = requests.post(
                url=f"{self.url}/{id}/musica", json=musica, headers=self.headers
            )
            return resposta.json()
        except Exception:
            return ""

    def alterar(self, id, artista):
        try:
            resposta = requests.put(
                url=f"{self.url}/{id}", json=artista, headers=self.headers
            )
            return resposta.json()
        except Exception:
            return ""

    def deletar(self, id):
        try:
            requests.delete(url=f"{self.url}/{id}")
        except Exception:
            return ""
