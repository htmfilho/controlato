defmodule ControlatoWeb.ProcessController do
    use ControlatoWeb, :controller

    def index(conn, _params) do
        render(conn, "index.html")
    end
end