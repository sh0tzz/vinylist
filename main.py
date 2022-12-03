import sqlite3

# testiranje baze

conn = sqlite3.connect('catalog.db')
c = conn.cursor()

QUERY = '''
CREATE TABLE Menart (
    PlocaIme    TEXT        NOT NULL,
    PlocaSlika  TEXT        NOT NULL,
    PlocaKn     REAL        NOT NULL,
    PlocaEUR    REAL        NOT NULL
);
'''
c.execute(QUERY)

QUERY = '''
INSERT INTO Menart VALUES
    ('ploca1', 1.23, 2.23),
    ('ploca2', 54.53 ,25.34),
    ('ploca4', 542.542, 54);
'''
c.execute(QUERY)
conn.commit()

QUERY = '''
SELECT * FROM Menart;
'''
print(c.execute(QUERY).fetchall())