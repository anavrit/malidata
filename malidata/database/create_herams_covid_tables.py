import psycopg2
from connection import cursor, conn

sql1 = """
        CREATE TABLE baco1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql1)
# \copy baco1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_BACO1x_1_categories.csv' DELIMITER ',' CSV HEADER

sql2 = """
        CREATE TABLE baen1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql2)
# \copy baen1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_BAEN1x_1_categories.csv' DELIMITER ',' CSV HEADER

sql3 = """
        CREATE TABLE basa1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql3)
# \copy basa1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_BASA1x_1_categories.csv' DELIMITER ',' CSV HEADER

sql4 = """
        CREATE TABLE bawa1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql4)
# \copy bawa1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_BAWA1x_1_categories.csv' DELIMITER ',' CSV HEADER

sql5 = """
        CREATE TABLE bawm2x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql5)
# \copy bawm2x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_BAWM2x_1_categories.csv' DELIMITER ',' CSV HEADER

sql6 = """
        CREATE TABLE condb (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql6)
# \copy condb (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_CONDB_categories.csv' DELIMITER ',' CSV HEADER

sql7 = """
        CREATE TABLE condbx (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql7)
# \copy condbx (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_CONDBx_1_categories.csv' DELIMITER ',' CSV HEADER

sql8 = """
        CREATE TABLE geo5 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql8)
# \copy geo5 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_GEO5_categories.csv' DELIMITER ',' CSV HEADER

sql9 = """
        CREATE TABLE hfacc (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql9)
# \copy hfacc (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFACC_categories.csv' DELIMITER ',' CSV HEADER

sql10 = """
        CREATE TABLE hfaccx (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql10)
# \copy hfaccx (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFACCx_1_categories.csv' DELIMITER ',' CSV HEADER

sql11 = """
        CREATE TABLE hffunct (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql11)
# \copy hffunct (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFFUNCT_categories.csv' DELIMITER ',' CSV HEADER

sql12 = """
        CREATE TABLE hffunctx (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql12)
# \copy hffunctx (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFFUNCTx_1_categories.csv' DELIMITER ',' CSV HEADER

sql13 = """
        CREATE TABLE hfgaps1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql13)
# \copy hfgaps1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFGAPS1_1_categories.csv' DELIMITER ',' CSV HEADER

sql14 = """
        CREATE TABLE hfinp1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql14)
# \copy hfinp1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFINP1_SQ001_categories.csv' DELIMITER ',' CSV HEADER

sql15 = """
        CREATE TABLE hfinp1y (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql15)
# \copy hfinp1y (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFINP1y_categories.csv' DELIMITER ',' CSV HEADER

sql16 = """
        CREATE TABLE herams_covid_dbcolnames (
        id SERIAL,
        long_name VARCHAR(500) UNIQUE,
        short_name VARCHAR(50) UNIQUE,
        dbcol_name VARCHAR(50) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql16)
# \copy herams_covid_dbcolnames (long_name, short_name, dbcol_name) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_covid_dbcolumn_names.csv' DELIMITER ',' CSV HEADER

sql17 = """
        CREATE TABLE hfipc3x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql17)
# \copy hfipc3x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFIPC3x_1_categories.csv' DELIMITER ',' CSV HEADER

sql18 = """
        CREATE TABLE hfman (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql18)
# \copy hfman (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFMAN_categories.csv' DELIMITER ',' CSV HEADER

sql19 = """
        CREATE TABLE hfsup1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql19)
# \copy hfsup1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_HFSUP1_categories.csv' DELIMITER ',' CSV HEADER

sql20 = """
        CREATE TABLE imst1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql20)
# \copy imst1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_IMST1_categories.csv' DELIMITER ',' CSV HEADER

sql21 = """
        CREATE TABLE info1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql21)
# \copy info1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_INFO1x_categories.csv' DELIMITER ',' CSV HEADER

sql22 = """
        CREATE TABLE lab1x (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql22)
# \copy lab1x (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_LAB1x_1_categories.csv' DELIMITER ',' CSV HEADER

sql23 = """
        CREATE TABLE mosd3 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql23)
# \copy mosd3 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_MoSD3_categories.csv' DELIMITER ',' CSV HEADER

sql24 = """
        CREATE TABLE mosd4 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql24)
# \copy mosd4 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_MoSD4_categories.csv' DELIMITER ',' CSV HEADER

sql25 = """
        CREATE TABLE mosd5 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql25)
# \copy mosd5 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_MoSD5_categories.csv' DELIMITER ',' CSV HEADER

sql26 = """
        CREATE TABLE mosd7 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql26)
# \copy mosd7 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_MoSD7_categories.csv' DELIMITER ',' CSV HEADER

sql27 = """
        CREATE TABLE scren1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql27)
# \copy scren1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_SCREN1_categories.csv' DELIMITER ',' CSV HEADER

sql28 = """
        CREATE TABLE triage1 (
        id SERIAL,
        categories VARCHAR(200) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql28)
# \copy triage1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_TRIAGE1_categories.csv' DELIMITER ',' CSV HEADER

sql29 = """
        CREATE TABLE herams_covid_colnames (
        id SERIAL,
        long_name VARCHAR(500) UNIQUE,
        short_name VARCHAR(50) UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql29)
# \copy herams_covid_colnames (long_name, short_name) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_covid_column_names.csv' DELIMITER ',' CSV HEADER

sql30 = """
        CREATE TABLE herams_geo6 (
        geo6_index SMALLINT UNIQUE,
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        geo6 VARCHAR(100) NOT NULL,
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (geo6_index)
        );
      """
cursor.execute(sql30)
# \copy herams_geo6 (geo6_index, region_id, cercle_id, geo6) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/herams_GEO6_localite.csv' DELIMITER ',' CSV HEADER

sql31 = """
        CREATE TABLE herams_covid (
        external_id INT PRIMARY KEY,
        last_synced TIMESTAMP,
        record_date TIMESTAMP,
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        geo6_id SMALLINT NOT NULL,
        mosd2 VARCHAR(100),
        mosd3 SMALLINT NOT NULL,
        mosd3_other VARCHAR(50),
        mosd4 SMALLINT,
        mosd5 SMALLINT,
        mosd6 VARCHAR(200),
        lat FLOAT,
        lon FLOAT,
        mosdpop INT,
        mosd7 SMALLINT,
        hffunct SMALLINT,
        hffunctx1 SMALLINT,
        hffunctx2 SMALLINT,
        imst1 SMALLINT,
        scren1 SMALLINT,
        scren1x1 SMALLINT,
        scren1x2 SMALLINT,
        scren1x3 SMALLINT,
        triage1 SMALLINT,
        hfinp3 SMALLINT,
        hfinp1_sq1 SMALLINT,
        hfinp1_sq2 SMALLINT,
        hfinp1_sq3 SMALLINT,
        hfinp1y SMALLINT,
        hfinp1x_sq1_tlt INT,
        hfinp1x_sq1_ocp1 INT,
        hfinp1x_sq1_ocp2 INT,
        hfinp1x_sq2_tlt INT,
        hfinp1x_sq2_ocp1 INT,
        hfinp1x_sq2_ocp2 INT,
        hfinp1x_sq3_tlt INT,
        hfinp1x_sq3_ocp1 INT,
        hfinp1x_sq3_ocp2 INT,
        hfinp2_sq1 INT,
        hfinp2_sq2 INT,
        hfcapcom VARCHAR(400),
        lab1 SMALLINT,
        lab1x1 SMALLINT,
        lab1x2 SMALLINT,
        lab1x3 SMALLINT,
        lab1x4 SMALLINT,
        lab2_sq1 INT,
        lab2_sq2 INT,
        diag1 SMALLINT,
        diag1x1 SMALLINT,
        diag1x2 SMALLINT,
        diag1x3 SMALLINT,
        diag1x4 SMALLINT,
        diag2 SMALLINT,
        diag2x1 SMALLINT,
        diag2x2 SMALLINT,
        diag3 SMALLINT,
        diag3x1 SMALLINT,
        diag3x2 SMALLINT,
        diag3x3 SMALLINT,
        diag3x4 SMALLINT,
        labcom VARCHAR(400),
        hfeqp1dv CHAR(14),
        hfeqp1_sq1 SMALLINT,
        hfeqp1_sq2 SMALLINT,
        hfeqp1_sq3 SMALLINT,
        hfeqp1_sq4 SMALLINT,
        hfeqp1_sq5 SMALLINT,
        hfeqp1y SMALLINT,
        hfeqp1x_sq4_use INT,
        hfeqp1x_sq4_tlt INT,
        hfeqp1x_sq5_use INT,
        hfeqp1x_sq5_tlt INT,
        hfeqp1x_sq1_use INT,
        hfeqp1x_sq1_tlt INT,
        hfeqp1x_sq2_use INT,
        hfeqp1x_sq2_tlt INT,
        hfeqp1x_sq3_use INT,
        hfeqp1x_sq3_tlt INT,
        hfoxy1 SMALLINT,
        hfoxy2_sq1 SMALLINT,
        hfoxy2_sq2 SMALLINT,
        hfoxy3 INT,
        hfeqpcom VARCHAR(400),
        hrcap1dv CHAR(29),
        hrcap1_sq1 SMALLINT,
        hrcap1_sq2 SMALLINT,
        hrcap1_sq3 SMALLINT,
        hrcap1_sq4 SMALLINT,
        hrcap1_sq5 SMALLINT,
        hrcap1_sq6 SMALLINT,
        hrcap1_sq7 SMALLINT,
        hrcap1_sq8 SMALLINT,
        hrcap1_sq9 SMALLINT,
        hrcap1_sq10 SMALLINT,
        hrcap1y SMALLINT,
        hrcap1x_sq5_tlt INT,
        hrcap1x_sq5_wrk INT,
        hrcap1x_sq5_cmipc INT,
        hrcap1x_sq5_icu INT,
        hrcap1x_sq6_tlt INT,
        hrcap1x_sq6_wrk INT,
        hrcap1x_sq6_cmipc INT,
        hrcap1x_sq6_icu INT,
        hrcap1x_sq4_tlt INT,
        hrcap1x_sq4_wrk INT,
        hrcap1x_sq4_cmipc INT,
        hrcap1x_sq4_icu INT,
        hrcap1x_sq2_tlt INT,
        hrcap1x_sq2_wrk INT,
        hrcap1x_sq2_cmipc INT,
        hrcap1x_sq2_icu INT,
        hrcap1x_sq3_tlt INT,
        hrcap1x_sq3_wrk INT,
        hrcap1x_sq3_cmipc INT,
        hrcap1x_sq3_icu INT,
        hrcap1x_sq1_tlt INT,
        hrcap1x_sq1_wrk INT,
        hrcap1x_sq1_cmipc INT,
        hrcap1x_sq1_icu INT,
        hrcap1x_sq7_tlt INT,
        hrcap1x_sq7_wrk INT,
        hrcap1x_sq7_cmipc INT,
        hrcap1x_sq7_icu INT,
        hrcap1x_sq8_tlt INT,
        hrcap1x_sq8_wrk INT,
        hrcap1x_sq8_cmipc INT,
        hrcap1x_sq8_icu INT,
        hrcap1x_sq9_tlt INT,
        hrcap1x_sq9_wrk INT,
        hrcap1x_sq9_cmipc INT,
        hrcap1x_sq9_icu INT,
        hrcap1x_sq10_tlt INT,
        hrcap1x_sq10_wrk INT,
        hrcap1x_sq10_cmipc INT,
        hrcap1x_sq10_icu INT,
        hrcapcom VARCHAR(400),
        hfipc2dv CHAR(26),
        hfipc1 SMALLINT,
        hfipc1x1 SMALLINT,
        hfipc1x2 SMALLINT,
        hfipc1x3 SMALLINT,
        hfipc1x4 SMALLINT,
        hfipc2_sq1 SMALLINT,
        hfipc2_sq2 SMALLINT,
        hfipc2_sq3 SMALLINT,
        hfipc2_sq4 SMALLINT,
        hfipc2_sq5 SMALLINT,
        hfipc2_sq6 SMALLINT,
        hfipc2_sq7 SMALLINT,
        hfipc2_sq9 SMALLINT,
        hfipc2_sq8 SMALLINT,
        hfipc2y SMALLINT,
        hfipc2x_sq1 INT,
        hfipc2x_sq2 INT,
        hfipc2x_sq3 INT,
        hfipc2x_sq4 INT,
        hfipc2x_sq5 INT,
        hfipc2x_sq6 INT,
        hfipc2x_sq7 INT,
        hfipc2x_sq8 INT,
        hfipc2x_sq9 INT,
        hfipc3 SMALLINT,
        hfipc3x1 SMALLINT,
        hfipc3x2 SMALLINT,
        hfipc3x3 SMALLINT,
        hfipccom VARCHAR(400),
        morgue1 SMALLINT,
        morgue1x1 SMALLINT,
        morgue1x2 SMALLINT,
        morgue1x3 SMALLINT,
        morgue1x4 SMALLINT,
        morgue1x5 SMALLINT,
        morgue2 SMALLINT,
        morgue3 INT,
        morguecom VARCHAR(400),
        hfgaps1_1 SMALLINT,
        hfgaps1_2 SMALLINT,
        hfgaps1_3 SMALLINT,
        hfgaps2 VARCHAR(400),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        FOREIGN KEY (geo6_id) REFERENCES herams_geo6 (geo6_index),
        FOREIGN KEY (mosd3) REFERENCES mosd3 (id),
        FOREIGN KEY (mosd4) REFERENCES mosd4 (id),
        FOREIGN KEY (mosd5) REFERENCES mosd5 (id),
        FOREIGN KEY (mosd7) REFERENCES mosd7 (id),
        FOREIGN KEY (hffunct) REFERENCES hffunct (id),
        FOREIGN KEY (hffunctx1) REFERENCES hffunctx (id),
        FOREIGN KEY (hffunctx2) REFERENCES hffunctx (id),
        FOREIGN KEY (imst1) REFERENCES imst1 (id),
        FOREIGN KEY (scren1) REFERENCES scren1 (id),
        FOREIGN KEY (scren1x1) REFERENCES oui_non (id),
        FOREIGN KEY (scren1x2) REFERENCES oui_non (id),
        FOREIGN KEY (scren1x3) REFERENCES oui_non (id),
        FOREIGN KEY (triage1) REFERENCES triage1 (id),
        FOREIGN KEY (hfinp3) REFERENCES oui_non (id),
        FOREIGN KEY (hfinp1_sq1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfinp1_sq2) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfinp1_sq3) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfinp1y) REFERENCES hfinp1y (id),
        FOREIGN KEY (lab1) REFERENCES hfinp1 (id),
        FOREIGN KEY (lab1x1) REFERENCES lab1x (id),
        FOREIGN KEY (lab1x2) REFERENCES lab1x (id),
        FOREIGN KEY (lab1x3) REFERENCES lab1x (id),
        FOREIGN KEY (lab1x4) REFERENCES lab1x (id),
        FOREIGN KEY (diag1) REFERENCES hfinp1 (id),
        FOREIGN KEY (diag1x1) REFERENCES lab1x (id),
        FOREIGN KEY (diag1x2) REFERENCES lab1x (id),
        FOREIGN KEY (diag1x3) REFERENCES lab1x (id),
        FOREIGN KEY (diag1x4) REFERENCES lab1x (id),
        FOREIGN KEY (diag2) REFERENCES triage1 (id),
        FOREIGN KEY (diag2x1) REFERENCES lab1x (id),
        FOREIGN KEY (diag2x2) REFERENCES lab1x (id),
        FOREIGN KEY (diag3) REFERENCES triage1 (id),
        FOREIGN KEY (diag3x1) REFERENCES lab1x (id),
        FOREIGN KEY (diag3x2) REFERENCES lab1x (id),
        FOREIGN KEY (diag3x3) REFERENCES lab1x (id),
        FOREIGN KEY (diag3x4) REFERENCES lab1x (id),
        FOREIGN KEY (hfeqp1_sq1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfeqp1_sq2) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfeqp1_sq3) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfeqp1_sq4) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfeqp1_sq5) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfeqp1y) REFERENCES hfinp1y (id),
        FOREIGN KEY (hfoxy1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfoxy2_sq1) REFERENCES oui_non (id),
        FOREIGN KEY (hfoxy2_sq2) REFERENCES oui_non (id),
        FOREIGN KEY (hrcap1_sq1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq2) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq3) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq4) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq5) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq6) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq7) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq8) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq9) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1_sq10) REFERENCES hfinp1 (id),
        FOREIGN KEY (hrcap1y) REFERENCES hfinp1y (id),
        FOREIGN KEY (hfipc1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc1x1) REFERENCES lab1x (id),
        FOREIGN KEY (hfipc1x2) REFERENCES lab1x (id),
        FOREIGN KEY (hfipc1x3) REFERENCES lab1x (id),
        FOREIGN KEY (hfipc1x4) REFERENCES lab1x (id),
        FOREIGN KEY (hfipc2_sq1) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq2) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq3) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq4) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq5) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq6) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq7) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq9) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2_sq8) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc2y) REFERENCES hfinp1y (id),
        FOREIGN KEY (hfipc3) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfipc3x1) REFERENCES hfipc3x (id),
        FOREIGN KEY (hfipc3x2) REFERENCES hfipc3x (id),
        FOREIGN KEY (hfipc3x3) REFERENCES hfipc3x (id),
        FOREIGN KEY (morgue1) REFERENCES hfinp1 (id),
        FOREIGN KEY (morgue1x1) REFERENCES lab1x (id),
        FOREIGN KEY (morgue1x2) REFERENCES lab1x (id),
        FOREIGN KEY (morgue1x3) REFERENCES lab1x (id),
        FOREIGN KEY (morgue1x4) REFERENCES lab1x (id),
        FOREIGN KEY (morgue1x5) REFERENCES lab1x (id),
        FOREIGN KEY (morgue2) REFERENCES hfinp1 (id),
        FOREIGN KEY (hfgaps1_1) REFERENCES hfgaps1 (id),
        FOREIGN KEY (hfgaps1_2) REFERENCES hfgaps1 (id),
        FOREIGN KEY (hfgaps1_3) REFERENCES hfgaps1 (id)
        );
      """
cursor.execute(sql31)
# \copy herams_covid FROM '/Users/amitprasad/Documents/mali/malidata/database/data/HeRAMS_Mali_COVID_Normalized.csv' DELIMITER ',' CSV HEADER