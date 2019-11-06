defmodule Controlato.Scale do
  use Ecto.Schema
  import Ecto.Changeset

  schema "scale" do
    field :acronym, :string
    field :factor, :decimal
    field :name, :string
    field :range_max, :integer
    field :range_min, :integer

    timestamps()
  end

  @doc false
  def changeset(scale, attrs) do
    scale
    |> cast(attrs, [:name, :acronym, :range_min, :range_max, :factor])
    |> validate_required([:name, :acronym, :range_min, :range_max, :factor])
  end
end
