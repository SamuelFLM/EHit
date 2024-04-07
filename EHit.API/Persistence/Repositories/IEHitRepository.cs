using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EHit.API.Entities;

namespace EHit.API.Persistence.Repositories
{
    public interface IEHitRepository
    {
        List<Artista> GetAll();
        Artista GetById(int id);
        void Post(Artista artista);

        void Put(Artista artista);

        void Delete(Artista artista);

        List<Musica> GetAllMusic();

        void PostMusic(Musica musica);

    }
}