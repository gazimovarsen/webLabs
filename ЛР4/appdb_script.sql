create table contactrequests (
	id integer PRIMARY KEY autoincrement, 
	firstname varchar(255) NOT NULL, 
	first_message varchar(255), 
	second_message varchar(255),
	cratedAt datetime, 
	updatedAt datetime
);
