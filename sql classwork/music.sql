
CREATE TABLE artist (
  id serial PRIMARY KEY,
  name varchar,
  band varchar
);

CREATE TABLE album (
  id serial PRIMARY KEY,
  name varchar,
  artist varchar,
  writer varchar
);

CREATE TABLE song (
  id serial PRIMARY KEY,
  artist varchar,
  album varchar,
  writer varchar
);

CREATE TABLE writer (
  id serial PRIMARY KEY,
  name varchar
);