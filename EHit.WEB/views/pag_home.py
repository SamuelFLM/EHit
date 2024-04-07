import streamlit as st


def home():
    st.header("EHit")
    st.markdown(
        "EHit é um aplicativo inovador e intuitivo que oferece uma plataforma para gerenciar artistas e suas respectivas músicas online. Aqui está uma descrição mais detalhada:"
    )
    categoria(
        "Cadastro de Artistas",
        "O EHit permite que você cadastre artistas de forma eficiente. Você pode inserir informações relevantes sobre os artistas, como nome, gênero musical, biografia, entre outros.",
    )
    categoria(
        "Gerenciamento de Músicas",
        "Além de cadastrar artistas, o EHit também permite que você adicione as músicas de cada artista. Você pode inserir detalhes como o título da música, o álbum ao qual pertence, o ano de lançamento, entre outros.",
    )

    categoria(
        "Edição e Exclusão",
        "O EHit oferece a flexibilidade de editar e excluir informações. Se você cometeu um erro ao inserir detalhes ou se as informações de um artista ou música mudaram, você pode facilmente editar essas informações. Além disso, se um artista ou música não estiver mais disponível, você pode excluir essas informações do sistema.",
    )

    categoria(
        "Interface Amigável",
        "O EHit tem uma interface amigável que torna a navegação e o uso do aplicativo uma experiência agradável. As informações são organizadas de maneira clara e lógica, tornando fácil encontrar o que você está procurando.",
    )

    categoria(
        "Acesso Online",
        "Como o EHit é um aplicativo online, você pode acessar as informações de qualquer lugar, a qualquer momento. Tudo que você precisa é de uma conexão com a internet.",
    )


def categoria(titulo, texto):
    st.subheader(titulo, divider="violet")
    st.markdown(texto)
