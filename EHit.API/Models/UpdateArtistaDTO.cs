using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EHit.API.Models
{
    public record UpdateArtistaDTO(string? Nome, int Idade, string? Biografia, string? Foto)
    {

    }
}