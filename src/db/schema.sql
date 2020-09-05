CREATE TABLE tropical_cyclone (
	tropical_cyclone_id serial PRIMARY KEY,
	place VARCHAR(255) DEFAULT '',
	description_text VARCHAR(255) DEFAULT '',
	image VARCHAR(255) DEFAULT '',
	created_by TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_by TIMESTAMP NOT NULL DEFAULT NOW()
);