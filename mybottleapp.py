from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Python'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/humans/<id:int>')
def human_details(id):
    assert isinstance(id, int)
    
    return "Human Here!"

run(host='localhost', port=8080, debug=True)
