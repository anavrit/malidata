import psycopg2
from connection import cursor, conn

sql1 = """
        CREATE TABLE sex (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql1)
# \copy sex (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/sex.csv' DELIMITER ',' CSV HEADER

sql2 = """
        CREATE TABLE test_result (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql2)
# \copy test_result (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/measles_test.csv' DELIMITER ',' CSV HEADER

sql3 = """
        CREATE TABLE measles_classify (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql3)
# \copy measles_classify (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/measles_final_class.csv' DELIMITER ',' CSV HEADER

sql4 = """
        CREATE TABLE in_out (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql4)
# \copy in_out (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/in_out_patient.csv' DELIMITER ',' CSV HEADER

sql5 = """
        CREATE TABLE patient_outcome (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql5)
# \copy patient_outcome (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/patient_outcome.csv' DELIMITER ',' CSV HEADER

sql6 = """
        CREATE TABLE specimen_condition (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql6)
# \copy specimen_condition (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/specimen_condition.csv' DELIMITER ',' CSV HEADER

sql7 = """
        CREATE TABLE urban_rural (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql7)
# \copy urban_rural (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/urban_rural.csv' DELIMITER ',' CSV HEADER

sql8 = """
        CREATE TABLE specimen_source (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql8)
# \copy specimen_source (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/specimen_source.csv' DELIMITER ',' CSV HEADER

sql9 = """
        CREATE TABLE boolean (
        id SERIAL,
        categories VARCHAR(5) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql9)
# \copy boolean (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/boolean.csv' DELIMITER ',' CSV HEADER

sql10 = """
        CREATE TABLE polio_casecontact (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql10)
# \copy polio_casecontact (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_casecontact.csv' DELIMITER ',' CSV HEADER

sql11 = """
        CREATE TABLE polio_relationtoindex (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql11)
# \copy polio_relationtoindex (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_relationtoindex.csv' DELIMITER ',' CSV HEADER

sql12 = """
        CREATE TABLE polio_periodofexposure (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql12)
# \copy polio_periodofexposure (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_periodofexposure.csv' DELIMITER ',' CSV HEADER

sql13 = """
        CREATE TABLE polio_stoolcondition (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql13)
# \copy polio_stoolcondition (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_stoolcondition.csv' DELIMITER ',' CSV HEADER

sql14 = """
        CREATE TABLE polio_findingsatfollowup (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql14)
# \copy polio_findingsatfollowup (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_findingsatfollowup.csv' DELIMITER ',' CSV HEADER

sql15 = """
        CREATE TABLE polio_finalclassification (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql15)
# \copy polio_finalclassification (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_finalclassification.csv' DELIMITER ',' CSV HEADER

sql16 = """
        CREATE TABLE polio_injectionsite (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql16)
# \copy polio_injectionsite (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_injectionsite.csv' DELIMITER ',' CSV HEADER

sql17 = """
        CREATE TABLE polio_reasoncontact (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql17)
# \copy polio_reasoncontact (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_reasoncontact.csv' DELIMITER ',' CSV HEADER

sql18 = """
        CREATE TABLE polio_cellculture (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql18)
# \copy polio_cellculture (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_cellculture.csv' DELIMITER ',' CSV HEADER

sql19 = """
        CREATE TABLE polio_v1 (
        id SERIAL,
        categories VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql19)
# \copy polio_v1 (categories) FROM '/Users/amitprasad/Documents/mali/malidata/database/data/polio_v1.csv' DELIMITER ',' CSV HEADER

sql20 = """
        CREATE TABLE measles (
        id VARCHAR(25) NOT NULL UNIQUE,
        facility VARCHAR(100),
        date_received DATE,
        age FLOAT,
        sex SMALLINT,
        place SMALLINT,
        date_seen DATE,
        date_notified DATE,
        date_onset DATE,
        vaccine_doses INT,
        date_last_vacc DATE,
        in_out SMALLINT,
        outcome SMALLINT,
        final_class SMALLINT,
        date_sent_form DATE,
        date_rec_form DATE,
        date_spec_collected DATE,
        date_spec_sentlab DATE,
        date_spec_reclab DATE,
        spec_cond SMALLINT,
        measles_test SMALLINT,
        rubella_test SMALLINT,
        other_result VARCHAR(100),
        date_lab_sentdist DATE,
        date_dist_reclab DATE,
        unique_key INT UNIQUE NOT NULL,
        region_id SMALLINT NOT NULL,
        report_cercle SMALLINT NOT NULL,
        resid_cercle SMALLINT NOT NULL,
        FOREIGN KEY (sex) REFERENCES sex (id),
        FOREIGN KEY (place) REFERENCES urban_rural (id),
        FOREIGN KEY (in_out) REFERENCES in_out (id),
        FOREIGN KEY (outcome) REFERENCES patient_outcome (id),
        FOREIGN KEY (final_class) REFERENCES measles_classify (id),
        FOREIGN KEY (spec_cond) REFERENCES specimen_condition (id),
        FOREIGN KEY (measles_test) REFERENCES test_result (id),
        FOREIGN KEY (rubella_test) REFERENCES test_result (id),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (report_cercle) REFERENCES cercle (id),
        FOREIGN KEY (resid_cercle) REFERENCES cercle (id),
        PRIMARY KEY (unique_key)
        );
      """
cursor.execute(sql20)
# \copy measles FROM '/Users/amitprasad/Documents/mali/malidata/database/data/Measles_Cases.csv' DELIMITER ',' CSV HEADER

sql21 = """
        CREATE TABLE yellow_fever (
        facility VARCHAR(100),
        date_rec_nat DATE,
        date_rec_dist DATE,
        id VARCHAR(25) UNIQUE NOT NULL,
        age FLOAT,
        sex SMALLINT,
        place SMALLINT,
        date_notified DATE,
        vaccine_doses INT,
        date_seen DATE,
        date_last_vacc DATE,
        date_onset DATE,
        in_out SMALLINT,
        outcome SMALLINT,
        final_class SMALLINT,
        date_sent_form DATE,
        date_spec_collected DATE,
        spec_source SMALLINT,
        date_spec_sentlab DATE,
        date_spec_reclab DATE,
        spec_cond SMALLINT,
        yf_test SMALLINT,
        date_rec_result DATE,
        other_result VARCHAR(100),
        date_lab_sentdist DATE,
        unique_key INT UNIQUE NOT NULL,
        region_id SMALLINT NOT NULL,
        report_cercle SMALLINT NOT NULL,
        resid_cercle SMALLINT NOT NULL,
        FOREIGN KEY (sex) REFERENCES sex (id),
        FOREIGN KEY (place) REFERENCES urban_rural (id),
        FOREIGN KEY (in_out) REFERENCES in_out (id),
        FOREIGN KEY (outcome) REFERENCES patient_outcome (id),
        FOREIGN KEY (final_class) REFERENCES measles_classify (id),
        FOREIGN KEY (spec_source) REFERENCES specimen_source (id),
        FOREIGN KEY (spec_cond) REFERENCES specimen_condition (id),
        FOREIGN KEY (yf_test) REFERENCES test_result (id),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (report_cercle) REFERENCES cercle (id),
        FOREIGN KEY (resid_cercle) REFERENCES cercle (id),
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql21)
# \copy yellow_fever FROM '/Users/amitprasad/Documents/mali/malidata/database/data/YF_Cases.csv' DELIMITER ',' CSV HEADER

sql22 = """
        CREATE TABLE polio (
        id VARCHAR(25) UNIQUE NOT NULL,
        date_rec DATE,
        contact SMALLINT NOT NULL,
        facility VARCHAR(100),
        sex SMALLINT,
        date_notified DATE,
        date_investigated DATE,
        reason_contact SMALLINT,
        date_contact DATE,
        relation_index SMALLINT,
        period_exposure SMALLINT,
        ll SMALLINT,
        ra SMALLINT,
        admit_hospital SMALLINT,
        admit_date DATE,
        la SMALLINT,
        rl SMALLINT,
        date_onset DATE,
        fever_onset SMALLINT,
        progress_3days SMALLINT,
        asymmetrical SMALLINT,
        sudden_paralysis SMALLINT,
        true_afp SMALLINT,
        polio_doses INT,
        date_birth_dose DATE,
        date_second_dose DATE,
        date_fourth_dose DATE,
        date_first_dose DATE,
        date_third_dose DATE,
        date_last_dose DATE,
        date_first_stool DATE,
        date_second_stool DATE,
        date_stool_tolab DATE,
        stool_cond SMALLINT,
        date_final_cell DATE,
        date_rec_nat DATE,
        final_cell_culture SMALLINT,
        date_rec_dist DATE,
        v1 SMALLINT,
        v2 SMALLINT,
        v3 SMALLINT,
        date_reg_lab_sent DATE,
        date_nat_lab_sent DATE,
        vdpv1 SMALLINT,
        vdpv2 SMALLINT,
        vdpv3 SMALLINT,
        rnev SMALLINT,
        rnpent SMALLINT,
        date_follow_up DATE,
        lafup BOOLEAN NOT NULL,
        rafup BOOLEAN NOT NULL,
        finding_follow_up SMALLINT,
        final_class SMALLINT,
        rlfup BOOLEAN NOT NULL,
        llfup BOOLEAN NOT NULL,
        doses_sia INT,
        doses_ri INT,
        doses_risia INT,
        date_last_risia DATE,
        vdpv_serotype SMALLINT,
        immunocomp SMALLINT,
        date_sent_dist DATE,
        date_seq_results DATE,
        pain_sensitive SMALLINT,
        inject_before_onset SMALLINT,
        date_isolate_seq DATE,
        inject_rsite SMALLINT,
        inject_lsite SMALLINT,
        date_sent_nat DATE,
        date_spec_rec_nat DATE,
        week_onset INT,
        opvnopvsia INT,
        opvnopvri INT,
        ipv_doses_sia INT,
        ipv_doses_ri INT,
        age FLOAT,
        region_id SMALLINT NOT NULL,
        cercle_id SMALLINT NOT NULL,
        FOREIGN KEY (contact) REFERENCES polio_casecontact (id),
        FOREIGN KEY (sex) REFERENCES sex (id),
        FOREIGN KEY (reason_contact) REFERENCES polio_reasoncontact (id),
        FOREIGN KEY (relation_index) REFERENCES polio_relationtoindex (id),
        FOREIGN KEY (period_exposure) REFERENCES polio_periodofexposure (id),
        FOREIGN KEY (ll) REFERENCES oui_non (id),
        FOREIGN KEY (ra) REFERENCES oui_non (id),
        FOREIGN KEY (la) REFERENCES oui_non (id),
        FOREIGN KEY (rl) REFERENCES oui_non (id),
        FOREIGN KEY (fever_onset) REFERENCES oui_non (id),
        FOREIGN KEY (progress_3days) REFERENCES oui_non (id),
        FOREIGN KEY (asymmetrical) REFERENCES oui_non (id),
        FOREIGN KEY (sudden_paralysis) REFERENCES oui_non (id),
        FOREIGN KEY (true_afp) REFERENCES oui_non (id),
        FOREIGN KEY (stool_cond) REFERENCES polio_stoolcondition (id),
        FOREIGN KEY (final_cell_culture) REFERENCES polio_cellculture (id),
        FOREIGN KEY (v1) REFERENCES polio_v1 (id),
        FOREIGN KEY (v2) REFERENCES polio_v1 (id),
        FOREIGN KEY (v3) REFERENCES polio_v1 (id),
        FOREIGN KEY (vdpv1) REFERENCES polio_v1 (id),
        FOREIGN KEY (vdpv2) REFERENCES polio_v1 (id),
        FOREIGN KEY (vdpv3) REFERENCES polio_v1 (id),
        FOREIGN KEY (rnev) REFERENCES oui_non (id),
        FOREIGN KEY (rnpent) REFERENCES oui_non (id),
        FOREIGN KEY (finding_follow_up) REFERENCES polio_findingsatfollowup (id),
        FOREIGN KEY (final_class) REFERENCES polio_finalclassification (id),
        FOREIGN KEY (immunocomp) REFERENCES oui_non (id),
        FOREIGN KEY (pain_sensitive) REFERENCES oui_non (id),
        FOREIGN KEY (inject_before_onset) REFERENCES oui_non (id),
        FOREIGN KEY (inject_rsite) REFERENCES polio_injectionsite (id),
        FOREIGN KEY (inject_lsite) REFERENCES polio_injectionsite (id),
        FOREIGN KEY (region_id) REFERENCES region (id),
        FOREIGN KEY (cercle_id) REFERENCES cercle (id),
        PRIMARY KEY (id)
        );
      """
cursor.execute(sql22)
# \copy polio FROM '/Users/amitprasad/Documents/mali/malidata/database/data/Polio_Cases.csv' DELIMITER ',' CSV HEADER