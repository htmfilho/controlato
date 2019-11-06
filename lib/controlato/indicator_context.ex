defmodule Controlato.IndicatorContext do
  use Ecto.Schema
  import Ecto.Changeset

  schema "indicator_context" do
    field :cron_expression, :string
    field :description, :string
    field :name, :string
    field :status, :string
    field :trend, :string

    timestamps()
  end

  @doc false
  def changeset(indicator_context, attrs) do
    indicator_context
    |> cast(attrs, [:name, :description, :cron_expression, :trend, :status])
    |> validate_required([:name, :description, :cron_expression, :trend, :status])
  end
end
