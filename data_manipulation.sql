-- These are some Database Manipulation queries for a partially implemented Project Website 
-- using the cookbooks database.
-- These are ALL the queries required to implement ALL the functionalities listed in the Project Specs.

--INSERTS
--when a user clicks the add button on the recipe screen at the top of the page
--inserts user input into the ingredients table
INSERT INTO `Ingredients` (name, type)
VALUES(:name_input, :type_input);

--when the user clicks the save new recipe button at the bottom right of the build recipe page
--all the info on the right side of the page gets put into the recipes table
INSERT INTO `Recipes` (name, instruction, total_cook_time, genre)
VALUES(:name_input, :instruction_input, :cook_time_input, :genre_input)

--When the user clicks the add genre button on the genre pages
--inserts the users new genre into the table
INSERT INTO `Genres` (name)
VALUES(:name_input);

INSERT INTO `Cookbooks` (book_name)
VALUES(:book_name_input);

--SELECT
--when you click the filter or add! button this gets all the names of the ingredient
--from the ingredient table
SELECT :name_input
FROM `Ingredients`


--UPDATE
--when the user clicks the edit genre button on the your genres page
--this button gets the name of the genre that is going to be edited
UPDATE 'Genres'
SET name = :name_input
WHERE name = :name_input;

--when the user clicks the edit recipe button on the view your cookbook page
--this button gets the informatmtion of the recipes that way it can be edited
UPDATE `Recipes`
SET name = :name_input AND instruction = :instruction_input AND total_cook_time = :cook_time_input AND genre = :genre_input
WHERE :name_input AND instruction = :instruction_input AND total_cook_time = :cook_time_input AND genre = :genre_input;

--When the user clicks the update button on the build your recipes page (the button hasnt been added yet)
UPDATE 'Ingredients'
SET type = :type_input
WHERE type = :type_input;


--WHen the user hits the add new cookbook button on the home screen (the button hasnt been added yet)
UPDATE `Cookbooks`
SET book_name = :book_name_input
WHERE book_name = :book_name_input;

--DELETE
--when the user hits the delete button on the genres page
DELETE FROM `Genres`
WHERE name = :name_input;

--when the user clicks the delete button on the View your Cookbook!
DELETE FROM `Recipes`
WHERE total_cook_time = :cook_time_input;

--When the user clicks the delete button on the build your recipe page (the button hasnt been added yet)
DELETE FROM 'Ingredients'
WHERE name = :name_input;

--When the user clicks the delete button on the welcome page (the button hasnt been added yet)
DELETE FROM `Cookbooks`
WHERE book_name = :book_name_input;







