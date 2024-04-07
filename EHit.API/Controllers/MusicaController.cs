using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EHit.API.Entities;
using EHit.API.Models;
using EHit.API.Persistence.Repositories;
using Microsoft.AspNetCore.Mvc;

namespace EHit.API.Controllers
{
    [ApiController]
    [Route("api/artista/{id}/musica")]
    public class MusicaController : ControllerBase
    {

        private readonly IEHitRepository _repository;

        public MusicaController(IEHitRepository repository) => _repository = repository;

        [HttpGet]
        public IActionResult Get()
        {
            var musicas = _repository.GetAllMusic();
            return Ok(musicas);
        }

        [HttpPost]
        public IActionResult Post(int id, AddMusicaDTO model)
        {
            Musica musica = new Musica(model.Nome, model.Genero, model.Nota, model.Duracao, id);

            _repository.PostMusic(musica);

            return NoContent();
        }

    }
}