using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EHit.API.Entities
{
    public class Artista
    {
        public Artista(string? nome, int idade, string? biografia, string? foto)
        {
            Nome = nome;
            Idade = idade;
            Biografia = biografia;
            Foto = foto;
        }
        public int Id { get; private set; }
        public string? Nome { get; set; }
        public int Idade { get; private set; }
        public string? Biografia { get; set; }
        public string? Foto { get; private set; }

        public List<Musica> Musicas { get; set; } = null!;


        public void Atualizar(string? nome, int idade, string? biografia, string? foto)
        {
            Nome = nome;
            Idade = idade;
            Biografia = biografia;
            Foto = foto;
        }
    }
}