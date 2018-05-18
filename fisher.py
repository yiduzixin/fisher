"""
Created by 逗蛆 on 2018/5/6

"""
from app import create_app

__author__ = "逗蛆"

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'], threaded=True)  # threaded开启多线程
