import sqlite3

with sqlite3.connect("formula.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS escuderias(
                        nombre TEXT PRIMARY KEY,
                        anno_fundacion INTEGER,
                        titulos_constructor INTEGER,
                        team_principal TEXT
                    )
                   ''')
    """ cursor.execute('''
                    INSERT INTO escuderias (nombre, anno_fundacion, titulos_constructor, team_principal) VALUES
                        ('Ferrari', 1939, 16, 'Fred Vasseur'),
                        ('McLaren', 1963, 10, 'Andrea Stella'),
                        ('Mercedes', 1954, 8, 'Toto Wolff'),
                        ('Aston Martin', 1959, 0, 'Andy Cowell'),
                        ('Alpine', 1985, 0, 'Flavio Briatore'),
                        ('Red Bull Racing', 2005, 6, 'Laurent Mekies'),
                        ('Williams', 1977, 9, 'James Vowles'),
                        ('Racing Bulls', 2024, 0, 'Alan Permane'),
                        ('Haas', 2016, 0, 'Ayao Komatsu'),
                        ('Kick Sauber', 1993, 0, 'Jonathan Wheatley');
                    ''') """
    
    cursor.execute("UPDATE escuderias SET titulos_constructor = 1 WHERE nombre == 'Kick Sauber'")

    cursor.execute("SELECT * FROM escuderias")

    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
