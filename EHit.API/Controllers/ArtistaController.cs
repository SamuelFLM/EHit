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
    [Route("api/artista")]
    public class ArtistaController : ControllerBase
    {

        private readonly IEHitRepository _repository;

        public ArtistaController(IEHitRepository repository) => _repository = repository;

        [HttpGet]
        public IActionResult GetAll()
        {
            var artistas = _repository.GetAll();
            return Ok(artistas);
        }
        [HttpGet("{id}")]
        public IActionResult GetById(int id)
        {
            var artista = _repository.GetById(id);

            if (artista is null)
                return NotFound();

            return Ok(artista);
        }

        [HttpPost]
        public IActionResult Post(AddArtistaDTO model)
        {
            Artista artista = new Artista(model.Nome, model.Idade, model.Biografia, model.Foto);

            _repository.Post(artista);

            return CreatedAtAction(nameof(GetById), new { id = artista.Id }, artista);
        }

        [HttpPut("{id}")]
        public IActionResult Put(int id, UpdateArtistaDTO model)
        {

            var artista = _repository.GetById(id);

            if (artista is null)
                return NotFound();

            artista.Atualizar(model.Nome, model.Idade, model.Biografia, model.Foto);

            _repository.Put(artista);

            return NoContent();
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var artista = _repository.GetById(id);

            if (artista is null)
                return NotFound();

            _repository.Delete(artista);

            return NoContent();
        }

    }
}