defmodule Controlato.Repo do
  use Ecto.Repo,
    otp_app: :controlato,
    adapter: Ecto.Adapters.Postgres
end
