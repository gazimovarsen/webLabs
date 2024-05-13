create table contactrequests (
	id integer PRIMARY KEY autoincrement, 
	firstname varchar(255) NOT NULL, 
	lastname varchar(255), 
	email varchar(255), 
	reqtype varchar(255), 
	reqtext varchar(255), 
	cratedAt datetime, 
	updatedAt datetime
);
