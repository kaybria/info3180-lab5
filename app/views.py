"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, url_for,send_from_directory
import os
from app.models import Movie
from app.forms import MovieForm
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_wtf.csrf import generate_csrf
###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/movies', methods=['POST'])
def movies():    
    movieform = MovieForm()
    if movieform.validate_on_submit():
        title= movieform.title.data
        description = movieform.description.data
        poster = movieform.poster.data
        created_at = datetime.utcnow()
        pname=secure_filename(poster.filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'],pname))

        newmovie = Movie(title,description,pname,created_at)
        db.session.add(newmovie)
        db.session.commit()
        
        movieresult = {
            "message": 'Movie Successfully added',
            "title": title,
            "poster": pname,
            "description": description}
        return jsonify(data = movieresult)
    return jsonify(errors =form_errors(movieform))

    

@app.route('/api/v1/movies', methods=['GET'])
def getmovies():
    movies = Movie.query.all()
    allmovies = []
    for m in movies:
        allmovies.append({
            "id":m.id,
            "title" :m.title,
            "description":m.description,
            "poster": url_for('getimages',filename = m.poster)
        })
    return jsonify(movies=allmovies)

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/v1/poster/<filename>')
def getimages(filename):
    #rootdir = os.getcwd()
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404