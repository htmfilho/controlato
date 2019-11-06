defmodule Controlato.Repo.Migrations.CreateIndicatorContext do
  use Ecto.Migration

  def change do
    create table(:indicator_context) do
      add :name, :string
      add :description, :string
      add :cron_expression, :string
      add :trend, :string
      add :status, :string

      timestamps()
    end

  end
end
