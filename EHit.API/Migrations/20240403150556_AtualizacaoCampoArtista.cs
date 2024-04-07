using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace EHit.API.Migrations
{
    /// <inheritdoc />
    public partial class AtualizacaoCampoArtista : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Biografia",
                table: "Artistas",
                type: "nvarchar(max)",
                nullable: true);

            migrationBuilder.AddColumn<int>(
                name: "Idade",
                table: "Artistas",
                type: "int",
                nullable: false,
                defaultValue: 0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Biografia",
                table: "Artistas");

            migrationBuilder.DropColumn(
                name: "Idade",
                table: "Artistas");
        }
    }
}
