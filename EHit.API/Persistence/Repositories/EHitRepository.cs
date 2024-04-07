using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EHit.API.Entities;
using Microsoft.EntityFrameworkCore;

namespace EHit.API.Persistence.Repositories
{
    public class EHitRepository : IEHitRepository
    {
        private readonly EHitDbContext _context;

        public EHitRepository(EHitDbContext context) => _context = context;

        public void Delete(Artista artista)
        {
            _context.Artistas.Remove(artista);
            _context.SaveChanges();
        }

        public List<Artista> GetAll()
        {
            return _context.Artistas.Include(m => m.Musicas).AsNoTracking().ToList();
        }

        public List<Musica> GetAllMusic()
        {
            return _context.Musicas.AsNoTracking().ToList();
        }

        public Artista GetById(int id)
        {
            var artista = _context.Artistas.Include(m => m.Musicas).SingleOrDefault(x => x.Id == id);
            return artista!;
        }

        public void Post(Artista artista)
        {
            _context.Artistas.Add(artista);
            _context.SaveChanges();
        }

        public void PostMusic(Musica musica)
        {
            _context.Musicas.Add(musica);
            _context.SaveChanges();
        }

        public void Put(Artista artista)
        {
            _context.Artistas.Update(artista);
            _context.SaveChanges();
        }

    }
}