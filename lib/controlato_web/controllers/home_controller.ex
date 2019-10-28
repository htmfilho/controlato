defmodule ControlatoWeb.HomeController do
  use ControlatoWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
