DROP TABLE IF EXISTS inctype;

CREATE TABLE inctype (
    sample_id TEXT PRIMARY KEY,
    rep_type TEXT,
    rep_type_accession TEXT,
    predicted_mobility TEXT,
    organism TEXT,
    taxid INTEGER
)

