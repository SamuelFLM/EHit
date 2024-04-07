using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EHit.API.Entities
{
    public class Musica
    {
        public Musica(string? nome, string? genero, int nota, int duracao, int idArtista)
        {
            Nome = nome;
            Genero = genero;
            Nota = nota;
            Duracao = duracao;
            IdArtista = idArtista;
        }
        public int Id { get; private set; }
        public string? Nome { get; private set; }
        public string? Genero { get; private set; }
        public int Nota { get; private set; }
        public int Duracao { get; private set; }
        public int IdArtista { get; private set; }

    }
}