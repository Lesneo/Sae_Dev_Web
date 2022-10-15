CREATE TABLE mytable(
   Administrée INTEGER  NOT NULL PRIMARY KEY 
  ,Nom         VARCHAR(8) NOT NULL
  ,Prénom      VARCHAR(7) NOT NULL
  ,Naissance   DATE  NOT NULL
  ,Adresse     VARCHAR(22) NOT NULL
  ,Code_Postal VARCHAR(6) NOT NULL
  ,Ville       VARCHAR(17) NOT NULL
  ,Tel         VARCHAR(14) NOT NULL
  ,Aliment1    INTEGER  NOT NULL
  ,Aliment2    INTEGER  NOT NULL
  ,Aliment3    INTEGER  NOT NULL
  ,Aliment4    INTEGER  NOT NULL
  ,Aliment5    INTEGER  NOT NULL
  ,Aliment6    INTEGER  NOT NULL
  ,Aliment7    INTEGER  NOT NULL
  ,Aliment8    INTEGER  NOT NULL
  ,Aliment9    INTEGER  NOT NULL
  ,Aliment10   INTEGER  NOT NULL
);
INSERT INTO mytable(Administrée,Nom,Prénom,Naissance,Adresse,Code_Postal,Ville,Tel,Aliment1,Aliment2,Aliment3,Aliment4,Aliment5,Aliment6,Aliment7,Aliment8,Aliment9,Aliment10) VALUES (10,'CAUCHARD','Georges','01/08/1995','2 bis, rue Quatrefages','14 110','CONDE SUR NOIREAU','02 46 32 16 42',36037,76081,13431,25957,23588,20103,19666,25203,12763,6254);
