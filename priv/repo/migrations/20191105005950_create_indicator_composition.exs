defmodule Controlato.Repo.Migrations.CreateIndicatorComposition do
  use Ecto.Migration

  def change do
    create table(:indicator_composition) do
      add :name, :string
      add :description, :string

      timestamps()
    end

  end
end
