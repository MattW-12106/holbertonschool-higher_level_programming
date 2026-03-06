-- creates the table id_not_null
IF NOT EXISTS id_not_null (
    id INT = 1,
    name VARCHAR(256) NOT NULL
);