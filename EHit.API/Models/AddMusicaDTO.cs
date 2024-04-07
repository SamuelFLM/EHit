using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EHit.API.Models
{
    public record AddMusicaDTO(string? Nome,
         string? Genero,
         int Nota,
         int Duracao,
         int IdArtista)
    {

    }
}