def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   categoria TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   imagem_url TEXT NOT NULL
                   )""")
        print("Banco de dados criado!!")


init_db()