import psycopg2
from connection import cursor, conn

sql1 = """
        CREATE TABLE source (
        id SERIAL,
        source VARCHAR(350) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql1)

sql2 = """
        CREATE TABLE iso3 (
        id SERIAL,
        iso3 CHAR(3) UNIQUE,
        country VARCHAR(128) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql2)

sql3 = """
        CREATE TABLE indicator (
        id SERIAL,
        ind VARCHAR(32) UNIQUE,
        short_name VARCHAR(64) UNIQUE,
        medium_name VARCHAR(256) UNIQUE,
        transformed_name VARCHAR(128) UNIQUE,
        long_name VARCHAR (512) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql3)

sql4 = """
        CREATE TABLE gpw13 (
        iso3 INTEGER REFERENCES iso3(id) ON DELETE CASCADE,
        year INTEGER,
        indicator INTEGER REFERENCES indicator(id) ON DELETE CASCADE,
        value FLOAT,
        lower FLOAT,
        upper FLOAT,
        source INTEGER REFERENCES source(id) ON DELETE CASCADE,
        type VARCHAR(10),
        region VARCHAR(4),
        billion CHAR(3)
        );
      """
cursor.execute(sql4)

conn.commit()
conn.close()
