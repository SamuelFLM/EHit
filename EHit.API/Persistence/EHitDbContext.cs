using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EHit.API.Entities;
using Microsoft.EntityFrameworkCore;

namespace EHit.API.Persistence
{
    public class EHitDbContext : DbContext
    {
        public EHitDbContext(DbContextOptions<EHitDbContext> options) : base(options) { }


        public DbSet<Artista> Artistas { get; set; }
        public DbSet<Musica> Musicas { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Artista>(e =>
                {
                    e.HasKey(i => i.Id);

                    e.HasMany(i => i.Musicas)
                    .WithOne()
                    .HasForeignKey(i => i.IdArtista);
                }
            );


            modelBuilder.Entity<Musica>(e =>
            {
                e.HasKey(i => i.Id);
            });
        }
    }
}