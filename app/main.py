#Модуль входа в приложение
from app import app
from app import db

from posts.blueprint import posts, post_detail, tag_detail

import view

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()
