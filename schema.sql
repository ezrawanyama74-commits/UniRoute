DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS admin;

CREATE TABLE platforms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    is_free_option BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform_id INTEGER,
    title TEXT NOT NULL,
    provider_institution TEXT,
    credential_type TEXT NOT NULL,
    is_accredited BOOLEAN NOT NULL DEFAULT 0,
    cost_status TEXT NOT NULL,
    price_detail TEXT,
    direct_link TEXT NOT NULL,
    FOREIGN KEY(platform_id) REFERENCES platforms(id)
);

CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
