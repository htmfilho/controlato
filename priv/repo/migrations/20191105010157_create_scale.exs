defmodule Controlato.Repo.Migrations.CreateScale do
  use Ecto.Migration

  def change do
    create table(:scale) do
      add :name, :string
      add :acronym, :string
      add :range_min, :integer
      add :range_max, :integer
      add :factor, :decimal

      timestamps()
    end

  end
end
