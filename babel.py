from flask_babel import Babel
babel = Babel 

LANGUAGES = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish'
}

def configure(app):
    babel.init_app(app)
    app.config['LANGUAGES'] = LANGUAGES