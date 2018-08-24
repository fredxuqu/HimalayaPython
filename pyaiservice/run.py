"""
    create by Fred on 2018/8/22
"""
from app.app import create_app

__author__ = 'Fred'

app = create_app()

app.config.from_object('app.config.secure')
app.config.from_object('app.config.settings')

if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.config['DEBUG'], None)