from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
def hello():
    return "Hello World!"

@webapp.route('/browse_genre')
#the name of this function is just a cosmetic thing
def browse_genre():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT g_id, name from Genres ORDER BY g_id ASC;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('genre.html', g_rows=result)

@webapp.route('/edit_genre/<int:id>', methods=['POST', 'GET'])
#the name of this function is just a cosmetic thing
def edit_genre(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        query = 'SELECT g_id, name from Genres WHERE g_id = %s'  % (id)
        result = execute_query(db_connection, query).fetchone()

        if result == None:
            return "No such person found!"

        print('Returning')
        return render_template('edit_genre.html', info = result)

    elif request.method == 'POST':
        print('The POST request')
        gname = request.form['gname']

        query = "UPDATE Genres SET name = %s WHERE g_id = %s"
        data = (gname, id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_genre')



@webapp.route('/view_cookbook')
#the name of this function is just a cosmetic thing
def browse_cb():
    print("Fetching and rendering cookbook web page")
    db_connection = connect_to_database()
    query = "SELECT recipe_id, name, instruction, total_cook_time, genre from Recipes;" #is just reading all recipes, not recipes in that cookbook, need to also read ingredients
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Cookbook.HTML', r_rows=result)

@webapp.route('/recipe')
#the name of this function is just a cosmetic thing
def recipe():
    print("Fetching and rendering recipe web page")
    db_connection = connect_to_database()
    query = "SELECT name from Genres ORDER BY g_id ASC;"
    genre_names = execute_query(db_connection, query).fetchall()
    query = "SELECT ing_id, name, type FROM Ingredients"
    ingredients = execute_query(db_connection, query).fetchall()
    print(genre_names)
    print(ingredients)
    return render_template('recipe.html', g_rows=genre_names, i_rows=ingredients)

@webapp.route('/add_new_genre', methods=['POST','GET'])
def add_new_genre():
    db_connection = connect_to_database()
    if request.method == 'GET':
        print("Fetching and rendering people web page")
        db_connection = connect_to_database()
        query = "SELECT g_id, name from Genres ORDER BY g_id ASC;"
        result = execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('genre.html', g_rows=result)

    elif request.method == 'POST':
        print("Add new genres!")
        gname = request.form['gname']
        query = 'INSERT INTO Genres (name) VALUES (\'' + gname + '\')'
        execute_query(db_connection, query)
        query = "SELECT g_id, name from Genres ORDER BY g_id ASC;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('genre.html', g_rows=result)

@webapp.route('/ingredient')
#the name of this function is just a cosmetic thing
def browse_ingredients():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT ing_id, name, type from Ingredients;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('ingredient.html', i_rows=result)

@webapp.route('/ingredients', methods=['POST','GET'])
def add_new_ingredients():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT id, name, type from Ingredients'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('ingredient.html', ingredient = result)
    elif request.method == 'POST':
        print("Add new ingredient!")
        ing_id = request.form['ing_id']
        name = request.form['name']
        type = request.form['type']

        query = 'INSERT INTO Ingredients (ing_id, name, type) VALUES (%s,%s,%s)'
        data = (ing_id, name, type)
        execute_query(db_connection, query, data)
        return ('Ingredient added!')

@webapp.route('/')
def index():
    print("Fetching and rendering cookbook web page")
    db_connection = connect_to_database()
    query = "SELECT cookbook_id, book_name, chef, note from Cookbooks;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('index.html', c_rows=result)

@webapp.route('/home')
def home():
    db_connection = connect_to_database()
    #query = "DROP TABLE IF EXISTS diagnostic;"
    #execute_query(db_connection, query)
    #query = "CREATE TABLE `Genres` (`g_id` INT UNIQUE NOT NULL AUTO_INCREMENT, `name` VARCHAR(255) UNIQUE NOT NULL, PRIMARY KEY (`g_id`));"
    #execute_query(db_connection, query)
    #query = "INSERT INTO diagnostic (text) VALUES ('MySQL is working');"
    #execute_query(db_connection, query)
    query = "SELECT * from Genres;"
    result = execute_query(db_connection, query)
    for r in result:
        print(f"{r[0]}, {r[1]}")
    return render_template('home.html', result = result)

@webapp.route('/db_test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s'  % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall()

        print('Returning')
        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print('The POST request')
        character_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
