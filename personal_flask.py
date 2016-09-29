import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return flask.render_template("layout.html", page_to_insert="about.html")


@app.route('/publications')
def publications():
    return flask.send_file("static/pdfs/publications.pdf")


@app.route('/resume')
def resume():
    return flask.send_file("static/pdfs/resume.pdf")

@app.route('/feature_teacher')
def feature_teacher():
    return flask.redirect("https://github.com/dkarapetyan/feature-teacher/blob/master/feature-teacher.ipynb", code=302)



if __name__ == '__main__':
    app.run(debug=True)
