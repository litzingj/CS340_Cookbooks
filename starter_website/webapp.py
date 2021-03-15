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
        query = 'SELECT ing_id, name, type FROM Ingredients'
        result = execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('ingredient.html', i_rows = result)

    elif request.method == 'POST':
        print("Add new ingredient!")
        ing_name = request.form['ing_name']
        ing_type = request.form['type']
        query = 'INSERT INTO Ingredients (name, type) VALUES (\'' + ing_name + '\', \'' + ing_type + '\')'
        execute_query(db_connection, query)
        query = "SELECT ing_id, name, type from Ingredients ORDER BY ing_id ASC;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('ingredient.html', i_rows=result)



@webapp.route('/edit_ingredient/<int:id>', methods=['POST', 'GET'])
def edit_ingredient(id):
        print('In the function')
        db_connection = connect_to_database()
#display existing data
        if request.method == 'GET':
            print('The GET request')
            query = 'SELECT ing_id, name, type from Ingredients WHERE ing_id = %s'  % (id)
            result = execute_query(db_connection, query).fetchone()

            if result == None:
                return "No such person found!"

            print('Returning')
            return render_template('edit_ingredients.html', info = result)

        elif request.method == 'POST':
            print('The POST request')
            ing_name = request.form['ing_name']
            ing_type = request.form['type']
            query = "UPDATE Ingredients SET name = %s, type = %s WHERE ing_id = %s"
            data = (ing_name, ing_type, id)
            result = execute_query(db_connection, query, data)
            print(str(result.rowcount) + " row(s) updated")
            return redirect('/ingredient')


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


@webapp.route('/delete_genre/<int:id>')
def delete_genre(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Genres WHERE g_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/browse_genre')

@webapp.route('/delete_ingredient/<int:id>')
def delete_ingredients(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Ingredients WHERE ing_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/ingredient')    
