Create database if not exists trisdb;

CREATE TABLE IF NOT EXISTS utenti(
    username varchar(50) PRIMARY KEY,
    email varchar(50) NOT NULL,
    password varchar(512) NOT NULL,
    color varchar(7) NULL
);

alter table utenti drop column partite_vinte, drop column partite_perse, drop column partite_giocate;

Create TABLE if not exists match_history(
    id int(6) AUTO_INCREMENT PRIMARY KEY,
    username_p1 varchar(50) NULL,
    username_p2 varchar(50) NULL,
    match_grid JSON,
    endstatus int(1),
    FOREIGN KEY (username_p1) REFERENCES Utenti(username),
    FOREIGN KEY (username_p2) REFERENCES Utenti(username)
);