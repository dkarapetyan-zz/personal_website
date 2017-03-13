import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return flask.render_template("layout.html", page_to_insert="news.html")


@app.route('/about')
def about():
    return flask.render_template("layout.html", page_to_insert="about.html")


@app.route('/music')
def music():
    return flask.render_template("layout.html", page_to_insert="music.html")


@app.route('/events')
def events():
    return flask.render_template("layout.html", page_to_insert="events.html")


@app.route('/contact')
def contact():
    return flask.render_template("layout.html", page_to_insert="contact.html")


if __name__ == '__main__':
    app.run(debug=False)
