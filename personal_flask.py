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

@app.route('/feature_teacher_pres')
def feature_teacher_pres():
    return flask.send_file("static/pdfs/feature_teacher_pres.pdf")


@app.route('/feature_teacher')
def feature_teacher():
    url = "http://nbviewer.jupyter.org/github/dkarapetyan/feature_teacher/blob/master/feature_teacher.ipynb"
    return flask.redirect(url, code=302)




if __name__ == '__main__':
    app.run(debug=True)
