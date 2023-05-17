Create database if not exists Tris;

CREATE TABLE IF NOT EXISTS Users(
    username varchar(10) PRIMARY KEY,
    partite_vinte int(6) DEFAULT 0,
    partite_perse int(6) DEFAULT 0,
    partite_giocate int(6) DEFAULT 0,
    email varchar(50) NOT NULL,
    password varchar(512) NOT NULL,
);