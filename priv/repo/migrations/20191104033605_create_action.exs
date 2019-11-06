defmodule Controlato.Repo.Migrations.CreateAction do
  use Ecto.Migration

  def change do
    create table(:action) do
      add :name, :string

      timestamps()
    end

  end
end
