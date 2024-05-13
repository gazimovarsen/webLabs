create table logins ( 
	id integer PRIMARY KEY autoincrement, 
	username varchar(255) NOT NULL UNIQUE, 
	email varchar(255) NOT NULL UNIQUE, 
	password varchar(255) NOT NULL UNIQUE,
	PRAGMA foreign_keys=ON
); 
