CREATE TABLE binary_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    binary_name TEXT NOT NULL,
    architecture VARCHAR(10),
    compiler TEXT,
    compiler_version VARCHAR(10)
);



CREATE TABLE function_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    function_name TEXT NOT NULL
);


CREATE TABLE function_disassambly (
    function_id INTEGER,
    disassambly TEXT NOT NULL,
    FOREIGN KEY(function_id) REFERENCES function_name(id)
);



CREATE TABLE binary_function_mapping (
    binary_id INTEGER NOT NULL,
    function_id INTEGER NOT NULL,
    FOREIGN KEY(binary_id) REFERENCES binary_name(id),
    FOREIGN KEY(function_id) REFERENCES function_name(id)
);





