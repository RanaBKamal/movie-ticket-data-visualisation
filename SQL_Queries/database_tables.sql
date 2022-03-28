-- query to create Users table
CREATE TABLE IF NOT EXISTS Users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	full_name VARCHAR(40) NOT NULL,
	username VARCHAR(20) NOT NULL UNIQUE,
	email VARCHAR(40) NOT NULL UNIQUE,
	password VARCHAR(40) NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);