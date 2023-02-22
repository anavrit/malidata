import psycopg2
from connection import cursor, conn

sql1 = """
        CREATE TABLE region (
        id SERIAL,
        region VARCHAR(20) UNIQUE NOT NULL,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql1)
# \copy region (region) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/regions.csv' DELIMITER ',' CSV HEADER

sql2 = """
        CREATE TABLE cercle (
        id SERIAL,
        cercle VARCHAR(30) NOT NULL,
        region_id SMALLINT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (region_id) REFERENCES region (id)
        );
      """
cursor.execute(sql2)
# \copy cercle (cercle, region_id) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/cercle.csv' DELIMITER ',' CSV HEADER

sql3 = """
        CREATE TABLE commune (
        id SERIAL,
        commune VARCHAR(100) NOT NULL,
        cercle_id SMALLINT NOT NULL,
        region_id SMALLINT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        FOREIGN KEY (region_id) REFERENCES region (id)
        );
      """
cursor.execute(sql3)
# \copy commune (commune, cercle_id, region_id) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/commune.csv' DELIMITER ',' CSV HEADER

sql4 = """
        CREATE TABLE pop2020 (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        commune_id SMALLINT NOT NULL,
        masculin INT,
        feminin INT,
        PRIMARY KEY (region_id, cercle_id, commune_id),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        FOREIGN KEY (commune_id) REFERENCES commune (id)
        );
      """
cursor.execute(sql4)
# \copy pop2020 (region_id, cercle_id, commune_id, masculin, feminin) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/population.csv' DELIMITER ',' CSV HEADER

sql5 = """
        CREATE TABLE service_sigle (
        id SERIAL,
        sigle VARCHAR(100) UNIQUE NOT NULL,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql5)
# \copy service_sigle (sigle) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/sigle.csv' DELIMITER ',' CSV HEADER

sql6 = """
        CREATE TABLE service_typologie (
        id SERIAL,
        typologie VARCHAR(50) UNIQUE NOT NULL,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql6)
# \copy service_typologie (typologie) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/typology.csv' DELIMITER ',' CSV HEADER

sql7 = """
        CREATE TABLE service_etat (
        id SERIAL,
        etat VARCHAR(50) UNIQUE NOT NULL,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql7)
# \copy service_etat (etat) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/etat.csv' DELIMITER ',' CSV HEADER

sql8 = """
        CREATE TABLE oui_non (
        id SERIAL,
        oui_non VARCHAR(20) UNIQUE NOT NULL,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql8)
# \copy oui_non (oui_non) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/yesno.csv' DELIMITER ',' CSV HEADER

sql9 = """
        CREATE TABLE aire_sante (
        id SERIAL PRIMARY KEY,
        aire_sante VARCHAR(200) NOT NULL,
        cercle_id SMALLINT NOT NULL,
        region_id SMALLINT NOT NULL,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id)
        );
      """
cursor.execute(sql9)
# \copy aire_sante (aire_sante, cercle_id, region_id) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/aire_sante.csv' DELIMITER ',' CSV HEADER

sql10 = """
        CREATE TABLE service_availability (
        id SERIAL,
        typologie SMALLINT,
        nom VARCHAR (200),
        sigle SMALLINT NOT NULL,
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        aire_sante_id SMALLINT NOT NULL,
        hopital SMALLINT NOT NULL,
        csref SMALLINT NOT NULL,
        cscom SMALLINT NOT NULL,
        psa SMALLINT NOT NULL,
        equipe_mobile SMALLINT NOT NULL,
        soins_de SMALLINT NOT NULL,
        urenam SMALLINT NOT NULL,
        urenas SMALLINT NOT NULL,
        ureni SMALLINT NOT NULL,
        population FLOAT,
        lat FLOAT,
        lon FLOAT,
        etat SMALLINT NOT NULL,
        urgence SMALLINT NOT NULL,
        transition SMALLINT NOT NULL,
        developpement SMALLINT NOT NULL,
        FOREIGN KEY (sigle) REFERENCES service_sigle (id),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        FOREIGN KEY (aire_sante_id) REFERENCES aire_sante (id),
        FOREIGN KEY (hopital) REFERENCES oui_non (id),
        FOREIGN KEY (csref) REFERENCES oui_non (id),
        FOREIGN KEY (cscom) REFERENCES oui_non (id),
        FOREIGN KEY (psa) REFERENCES oui_non (id),
        FOREIGN KEY (equipe_mobile) REFERENCES oui_non (id),
        FOREIGN KEY (soins_de) REFERENCES oui_non (id),
        FOREIGN KEY (urenam) REFERENCES oui_non (id),
        FOREIGN KEY (urenas) REFERENCES oui_non (id),
        FOREIGN KEY (ureni) REFERENCES oui_non (id),
        FOREIGN KEY (etat) REFERENCES service_etat (id),
        FOREIGN KEY (urgence) REFERENCES oui_non (id),
        FOREIGN KEY (transition) REFERENCES oui_non (id),
        FOREIGN KEY (developpement) REFERENCES oui_non (id)
        );
      """
cursor.execute(sql10)
# \copy service_availability (typologie, nom, sigle, region_id, cercle_id, aire_sante_id, hopital, csref, cscom, psa, equipe_mobile, soins_de, urenam, urenas, ureni, population, lat, lon, etat, urgence, transition, developpement) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/service_availability.csv' DELIMITER ',' CSV HEADER
