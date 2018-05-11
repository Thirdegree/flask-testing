import flask
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return  flask.render_template('base.html.j2')


if __name__ == '__main__':
    app.run()
