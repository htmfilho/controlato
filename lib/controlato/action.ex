defmodule Controlato.Action do
  use Ecto.Schema
  import Ecto.Changeset

  schema "action" do
    field :name, :string

    timestamps()
  end

  @doc false
  def changeset(action, attrs) do
    action
    |> cast(attrs, [:name])
    |> validate_required([:name])
  end
end
