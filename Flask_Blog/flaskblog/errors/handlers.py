from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)



@errors.app_errorhandler(404) #handles 404 errors
def error_404(error):
    return render_template('errors/404.html'), 404 #second value is status note default value is 200


@errors.app_errorhandler(403) #handles 404 errors
def error_403(error):
    return render_template('errors/403.html'), 403 #second value is status note default value is 200

@errors.app_errorhandler(500) #handles 500 errors
def error_500(error):
    return render_template('errors/500.html'), 500 #second value is status note default value is 200
