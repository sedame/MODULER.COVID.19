DROP TABLE IF EXISTS `Communiques`;
DROP TABLE IF EXISTS `Localite`;

CREATE TABLE Localite(
    nom_Localite VARCHAR(50) ,
    nombre_cas int(10)  
) ;


CREATE TABLE Communiques (
  id_communique int(5) PRIMARY KEY,
  date_communique varchar(50) DEFAULT 'NULL',
  nb_tests int(5) NOT NULL DEFAULT 0,
  nb_cas int(5) NOT NULL DEFAULT 0,
  nb_cas_contact int(5) NOT NULL DEFAULT 0,
  nb_cas_communautaire int(5) NOT NULL DEFAULT 0,
  nb_gueris int(5) NOT NULL DEFAULT 0,
  nb_deces int(5) NOT NULL DEFAULT 0,
  date_extraction varchar(10)  DEFAULT NULL
) ;

