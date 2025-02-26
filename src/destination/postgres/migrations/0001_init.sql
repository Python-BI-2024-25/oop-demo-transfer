CREATE TABLE user_info
(
    id   SERIAL PRIMARY KEY,
    source TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    sex  VARCHAR(50)
);
