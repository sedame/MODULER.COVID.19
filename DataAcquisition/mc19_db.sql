--creation de la base de donnees

CREATE DATABASE Projet_Covid  character set = "utf8";

use Projet_Covid;

--DIFFENT TABLES DE LA BASE projet_C


--Departement
CREATE TABLE Departement (

    Id_departement int(10) not null,
    Nom_departement VARCHAR(50) NOT NULL,
    Position_departement CHAR(25) NOT NULL
    PRIMARY KEY(Id_departement)
    constraint Depa_K FOREIGN KEY (id_statut) REFERENCES statut(Id_statut)

) ENGINE=InnoDB


--statut de la population
CREATE Table statut(

    id_statut int(10) not null,
    Date_statut date,
    Source varchar(30) not null,
    Nombre_teste int(15) not null,
    Nombre_cas int(15) not null,
    Nombre_cas_grave int(15) not null,
    Nombre_gueri int (15) not null,
    Cas_commautaire int(15) not null,
    Mort int(15) not null 
    primary key(id_statut)
    constraint stat_k FOREIGN KEY (id_t) REFERENCES temps(Id_t)

) ENGINE=InnoDB

--situation temporaire
create table temps(

    Id_t int(10) not null,
    date_moment date


) ENGINE=InnoDB
