from bottle import route, run, template, get, post, request, static_file, \
     redirect
import sqlite3

conn = sqlite3.connect('human_data')

humans = []

@get('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root="./")

@route('/')
@route('/hello/<name>')
def greet(name='Python'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/humans/<id:int>')
def human_details(id):
    assert isinstance(id, int)

    human = humans[id]

    return template("<div>Name: {{name}}, color: {{color}}",
        name=human['name'], color=human['color'])


@get('/humans') # or @route('/login')
def show_humans():
    human_list = ""

    c = conn.cursor()
    c.execute("SELECT * FROM humans")

    humans = c.fetchall()
    conn.commit()

    for human in humans:
        human_list = human_list + template("<div>Name: {{name}}, color: {{color}}",
            name=human[1], color=human[2])

    return human_list + '''
    <form action="/humans" method="post">
            Human name: <input name="name" type="text" />
            Human's favorite color: <input name="color" type="text" />
            <input value="Add Human" type="submit" />
        </form>
    '''

@post('/humans') # or @route('/login', method='POST')
def show_humans():
    name = request.forms.get('name')
    color = request.forms.get('color')

    c = conn.cursor()
    c.execute("INSERT INTO humans (name, color) VALUES (?, ?)", (name, color))

    conn.commit()

#    humans.append( { "name": name, "color": color } )

    return redirect("/humans")

@get('/humans.json')
def humans_json():
    return { "humans": humans }

run(host='localhost', port=8080, debug=True)
