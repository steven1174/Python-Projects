-- 0. Drop table INSTRUCTOR in case it already exists
DROP TABLE INSTRUCTOR;

-- 1. Create a table INSTRUCTOR
CREATE TABLE INSTRUCTOR(
	ins_id INTEGER PRIMARY KEY NOT NULL,
	lastname VARCHAR(15) NOT NULL,
	firstname VARCHAR(15) NOT NULL,
	city VARCHAR(15), 
	country CHAR(2)
	);

-- 2. Insert rows
INSERT INTO  INSTRUCTOR (ins_id, lastname, firstname, city, country)
VALUES
(1, 'Ahuja', 'Rav', 'Toronto', 'CA'),
(2, 'Chong', 'Raul', 'Toronto', 'CA'),
(3, 'Vasudevan', 'Hima', 'Chicago', 'US');

-- 3. Select all rows in the table
SELECT * from INSTRUCTOR;

-- 3b. Select firstname, lastname and country where city is Toronto
SELECT firstname, lastname, country from INSTRUCTOR where city = 'Toronto';

-- 4. Change the city for Rav to Markham
UPDATE INSTRUCTOR
	SET city = 'Markham' 
	where  ins_id = 1;

-- 5. Delete the row for Raul Chong from the table
DELETE from INSTRUCTOR WHERE ins_id = 2;

-- 5b. Retrieve all rows from the table
SELECT * from INSTRUCTOR;