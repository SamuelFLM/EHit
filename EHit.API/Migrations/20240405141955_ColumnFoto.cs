using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace EHit.API.Migrations
{
    /// <inheritdoc />
    public partial class ColumnFoto : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Foto",
                table: "Artistas",
                type: "nvarchar(max)",
                nullable: true);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Foto",
                table: "Artistas");
        }
    }
}
