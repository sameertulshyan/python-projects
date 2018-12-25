/* Data source: https://www.kaggle.com/cdc/brfss-tobacco-use */

DROP TABLE IF EXISTS tobacco;
CREATE TABLE tobacco (
    data_year integer,
    data_state text,
    data_everyday real,
    data_some real,
    data_former real,
    data_never real
);