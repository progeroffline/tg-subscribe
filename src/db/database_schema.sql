CREATE TABLE IF NOT EXISTS "Users" (
	"id"	INTEGER,
	"telegram_id"	INTEGER,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"username"	TEXT,
	"days_sub_end"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Payments" (
	"id"	INTEGER,
	"txid"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
