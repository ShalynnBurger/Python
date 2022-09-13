SELECT * FROM dojos_and_ninjas_schema.dojos;
INSERT INTO dojos (name)
VALUES ('Shay');
INSERT INTO dojos (name)
VALUES ('Maverick'), ('Jenna');

INSERT INTO dojos (name)
VALUES ('Shay'), ('Maverick'), ('Jenna');

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Shalynn', 'Burger', 27, 4), ('Trevor', 'Hawksworth', 27, 4), ('Jennifer', 'Mattheis', 35, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Kyva', 'Ray', 3, 5), ('Wheely', 'Handsome', 5, 5), ('Leo', 'Lib', 6, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Christian', 'Hutto', 30, 6), ('Danielle', 'Irwin', 25, 6), ('Anna', 'Wagle', 26, 6);

SELECT * FROM dojos WHERE id = 4;
SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 6;
SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT name FROM dojos WHERE dojo_id = 6;

SELECT dojo_id FROM ninjas WHERE id=12; 
SELECT * FROM dojos