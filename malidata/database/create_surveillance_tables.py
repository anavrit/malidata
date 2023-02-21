import psycopg2
from connection import cursor, conn

sql1 = """
        CREATE TABLE meningite (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql1)
# \copy meningite FROM '/Users/amitprasad/Documents/mali/malidata/database/data/meningite.csv' DELIMITER ',' CSV HEADER

sql2 = """
        CREATE TABLE region_meningite (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql2)
# \copy region_meningite FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_meningite.csv' DELIMITER ',' CSV HEADER

sql3 = """
        CREATE TABLE rougeole (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql3)
# \copy rougeole FROM '/Users/amitprasad/Documents/mali/malidata/database/data/rougeole.csv' DELIMITER ',' CSV HEADER

sql4 = """
        CREATE TABLE region_rougeole (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql4)
# \copy region_rougeole FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_rougeole.csv' DELIMITER ',' CSV HEADER

sql5 = """
        CREATE TABLE fievre_jaune (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql5)
# \copy fievre_jaune FROM '/Users/amitprasad/Documents/mali/malidata/database/data/fievre_jaune.csv' DELIMITER ',' CSV HEADER

sql6 = """
        CREATE TABLE region_fievre_jaune (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql6)
# \copy region_fievre_jaune FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_fievre_jaune.csv' DELIMITER ',' CSV HEADER

sql7 = """
        CREATE TABLE cholera (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql7)
# \copy cholera FROM '/Users/amitprasad/Documents/mali/malidata/database/data/cholera.csv' DELIMITER ',' CSV HEADER

sql8 = """
        CREATE TABLE region_cholera (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql8)
# \copy region_cholera FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_cholera.csv' DELIMITER ',' CSV HEADER

sql9 = """
        CREATE TABLE rage_humaine (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql9)
# \copy rage_humaine FROM '/Users/amitprasad/Documents/mali/malidata/database/data/rage_humaine.csv' DELIMITER ',' CSV HEADER

sql10 = """
        CREATE TABLE region_rage_humaine (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql10)
# \copy region_rage_humaine FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_rage_humaine.csv' DELIMITER ',' CSV HEADER

sql11 = """
        CREATE TABLE charbon (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql11)
# \copy charbon FROM '/Users/amitprasad/Documents/mali/malidata/database/data/charbon.csv' DELIMITER ',' CSV HEADER

sql12 = """
        CREATE TABLE region_charbon (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql12)
# \copy region_charbon FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_charbon.csv' DELIMITER ',' CSV HEADER

sql13 = """
        CREATE TABLE piqures_serpents (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql13)
# \copy piqures_serpents FROM '/Users/amitprasad/Documents/mali/malidata/database/data/piqures_serpents.csv' DELIMITER ',' CSV HEADER

sql14 = """
        CREATE TABLE region_piqures_serpents (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql14)
# \copy region_piqures_serpents FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_piqures_serpents.csv' DELIMITER ',' CSV HEADER

sql15 = """
        CREATE TABLE morssures_chien (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql15)
# \copy morssures_chien FROM '/Users/amitprasad/Documents/mali/malidata/database/data/morssures_chien.csv' DELIMITER ',' CSV HEADER

sql16 = """
        CREATE TABLE region_morssures_chien (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql16)
# \copy region_morssures_chien FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_morssures_chien.csv' DELIMITER ',' CSV HEADER

sql17 = """
        CREATE TABLE piqures_scorpion (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql17)
# \copy piqures_scorpion FROM '/Users/amitprasad/Documents/mali/malidata/database/data/piqures_scorpion.csv' DELIMITER ',' CSV HEADER

sql18 = """
        CREATE TABLE region_piqures_scorpion (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql18)
# \copy region_piqures_scorpion FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_piqures_scorpion.csv' DELIMITER ',' CSV HEADER

sql19 = """
        CREATE TABLE diarhee_rouge (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql19)
# \copy diarhee_rouge FROM '/Users/amitprasad/Documents/mali/malidata/database/data/diarhee_rouge.csv' DELIMITER ',' CSV HEADER

sql20 = """
        CREATE TABLE region_diarhee_rouge (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql20)
# \copy region_diarhee_rouge FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_diarhee_rouge.csv' DELIMITER ',' CSV HEADER

sql21 = """
        CREATE TABLE diarhee_rouge (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql21)
# \copy diarhee_rouge FROM '/Users/amitprasad/Documents/mali/malidata/database/data/diarhee_rouge.csv' DELIMITER ',' CSV HEADER

sql22 = """
        CREATE TABLE region_diarhee_rouge (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql22)
# \copy region_diarhee_rouge FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_diarhee_rouge.csv' DELIMITER ',' CSV HEADER

sql23 = """
        CREATE TABLE covid19 (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        isocode CHAR(21) NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator)
        );
      """
cursor.execute(sql23)
# \copy covid19 FROM '/Users/amitprasad/Documents/mali/malidata/database/data/covid19.csv' DELIMITER ',' CSV HEADER

sql24 = """
        CREATE TABLE region_covid19 (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        indicator char(5) NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator)
        );
      """
cursor.execute(sql24)
# \copy region_covid19 FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_covid19.csv' DELIMITER ',' CSV HEADER

sql25 = """
        CREATE TABLE pfa (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, semaine)
        );
      """
cursor.execute(sql25)
# \copy pfa FROM '/Users/amitprasad/Documents/mali/malidata/database/data/pfa.csv' DELIMITER ',' CSV HEADER

sql26 = """
        CREATE TABLE region_pfa (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, semaine)
        );
      """
cursor.execute(sql26)
# \copy region_pfa FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_pfa.csv' DELIMITER ',' CSV HEADER

sql27 = """
        CREATE TABLE dcd_maternel (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, semaine)
        );
      """
cursor.execute(sql27)
# \copy dcd_maternel FROM '/Users/amitprasad/Documents/mali/malidata/database/data/dcd_maternel.csv' DELIMITER ',' CSV HEADER

sql28 = """
        CREATE TABLE region_dcd_maternel (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, semaine)
        );
      """
cursor.execute(sql28)
# \copy region_dcd_maternel FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_dcd_maternel.csv' DELIMITER ',' CSV HEADER

sql29 = """
        CREATE TABLE dcd_nn (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, semaine)
        );
      """
cursor.execute(sql29)
# \copy dcd_nn FROM '/Users/amitprasad/Documents/mali/malidata/database/data/DCD_NN.csv' DELIMITER ',' CSV HEADER

sql30 = """
        CREATE TABLE region_dcd_nn (
        region_id SMALLINT NOT NULL,
        year INT,
        population INT,
        semaine SMALLINT NOT NULL,
        value FLOAT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, semaine)
        );
      """
cursor.execute(sql30)
# \copy region_dcd_nn FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_DCD_NN.csv' DELIMITER ',' CSV HEADER

sql31 = """
        CREATE TABLE tnn (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        year INT,
        indicator VARCHAR(4),
        semaine SMALLINT NOT NULL,
        value INT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator, semaine)
        );
      """
cursor.execute(sql31)
# \copy tnn FROM '/Users/amitprasad/Documents/mali/malidata/database/data/TNN.csv' DELIMITER ',' CSV HEADER

sql32 = """
        CREATE TABLE region_tnn (
        region_id SMALLINT NOT NULL,
        year INT,
        indicator VARCHAR(4),
        semaine SMALLINT NOT NULL,
        value INT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator, semaine)
        );
      """
cursor.execute(sql32)
# \copy region_tnn FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_TNN.csv' DELIMITER ',' CSV HEADER

sql33 = """
        CREATE TABLE mort_ne (
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        year INT,
        indicator VARCHAR(5),
        semaine SMALLINT NOT NULL,
        value INT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (region_id, cercle_id, year, indicator, semaine)
        );
      """
cursor.execute(sql33)
# \copy mort_ne FROM '/Users/amitprasad/Documents/mali/malidata/database/data/mort_ne.csv' DELIMITER ',' CSV HEADER

sql34 = """
        CREATE TABLE region_mort_ne (
        region_id SMALLINT NOT NULL,
        year INT,
        indicator VARCHAR(5),
        semaine SMALLINT NOT NULL,
        value INT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator, semaine)
        );
      """
cursor.execute(sql34)
# \copy region_mort_ne FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_mort_ne.csv' DELIMITER ',' CSV HEADER

sql35 = """
        CREATE TABLE region_palu (
        region_id SMALLINT NOT NULL,
        year INT,
        indicator VARCHAR(12),
        semaine SMALLINT NOT NULL,
        value INT,
        FOREIGN KEY (region_id) REFERENCES region (id),
        PRIMARY KEY (region_id, year, indicator, semaine)
        );
      """
cursor.execute(sql35)
# \copy region_palu FROM '/Users/amitprasad/Documents/mali/malidata/database/data/region_palu.csv' DELIMITER ',' CSV HEADER
