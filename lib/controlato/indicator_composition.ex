defmodule Controlato.IndicatorComposition do
  use Ecto.Schema
  import Ecto.Changeset

  schema "indicator_composition" do
    field :description, :string
    field :name, :string

    timestamps()
  end

  @doc false
  def changeset(indicator_composition, attrs) do
    indicator_composition
    |> cast(attrs, [:name, :description])
    |> validate_required([:name, :description])
  end
end
