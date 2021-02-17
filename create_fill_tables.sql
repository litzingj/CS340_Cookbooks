--create tables--

CREATE TABLE `Ingredients` 
(`ing_id` INT NOT NULL AUTO_INCREMENT UNIQUE, `name` VARCHAR(255) NOT NULL UNIQUE, `type` VARCHAR(255) NOT NULL, PRIMARY KEY (`ing_id`));

CREATE TABLE `Genres`
(`g_id` INT UNIQUE NOT NULL AUTO_INCREMENT, `name` VARCHAR(255) UNIQUE NOT NULL, PRIMARY KEY (`g_id`));

CREATE TABLE `Recipes`
(`recipe_id` INT UNIQUE NOT NULL AUTO_INCREMENT, `name` VARCHAR(255) UNIQUE NOT NULL, `instruction` VARCHAR(255) NOT NULL, `total_cook_time` INT NOT NULL, `genre` INT, PRIMARY KEY (`recipe_id`), FOREIGN KEY (`genre`) REFERENCES `Genres` (`g_id`));

CREATE TABLE `Cookbooks`
(`cookbook_id` INT UNIQUE NOT NULL AUTO_INCREMENT, `book_name` VARCHAR(255) UNIQUE NOT NULL,`chef` VARCHAR(255), `note` VARCHAR(255), PRIMARY KEY (`cookbook_id`));

--create intersection tables for many-to-many relationships--

CREATE TABLE `Ingredients_Recipes` 
(`ing_id` INT NOT NULL, `recipe_id` INT NOT NULL, 
PRIMARY KEY (ing_id, recipe_id), FOREIGN KEY (ing_id) REFERENCES `Ingredients` (ing_id), FOREIGN KEY (recipe_id) REFERENCES `Recipes` (recipe_id));

CREATE TABLE `Cookbooks_Recipes` 
(`cookbook_id` INT NOT NULL, `recipe_id` INT NOT NULL,
PRIMARY KEY (cookbook_id, recipe_id), FOREIGN KEY (cookbook_id) REFERENCES `Cookbooks` (cookbook_id), FOREIGN KEY (recipe_id) REFERENCES `Recipes` (recipe_id));

--fill in tables--

INSERT INTO `Ingredients` (name, type) VALUES ('Onion', 'Vegetable'), ('Potato', 'Vegetable'), ('Apples', 'Fruit'), ('Milk', 'Dairy'), ('Flour', 'Grain'), ('Egg', 'Protein'), ('Water', 'Liquid'), ('Salt', 'Seasoning'), ('Butter', 'Dairy'),
('French Bread', 'Carb'), ('Garlic', 'Vegetable'), ('Parsley', 'Seasoning'), ('Parmesan Cheese', 'Dairy'), ('Oregano', 'Seasoning'), ('Basil', 'Seasoning');

INSERT INTO `Genres` (name) VALUES ('Italian'), ('American'), ('Chinese'), ('French'), ('Indian'), ('Thai'), ('Moroccan'), ('Mexican'), ('Japanese'), ('None of the above');

INSERT INTO `Recipes` (name, genre, instruction, total_cook_time) VALUES
('Crepes', (SELECT g_id FROM Genres WHERE name='French'), 'Make the batter and cook in thin layers on a griddle 2 mins per side', 30),
('Garlic Bread', (SELECT g_id FROM Genres WHERE name='Italian'), 'Cover bread with butter and herbs and broil for 5 mins', 15);

INSERT INTO `Cookbooks` (book_name, note) VALUES 
('Breakfast for Dinner', 'ideas for breakfast for dinner'),
('FOOB', 'only tasty foob here');

--fill in intersection tables--
INSERT INTO `Cookbooks_Recipes` (cookbook_id, recipe_id) VALUES (1, 1), (2, 2);

--fill in garlic bread--
INSERT INTO `Ingredients_Recipes` (ing_id, recipe_id) VALUES (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2);

--fill in crepes--
INSERT INTO `Ingredients_Recipes` (ing_id, recipe_id) VALUES (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1);