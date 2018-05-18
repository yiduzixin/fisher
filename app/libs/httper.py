"""
Created by 逗蛆 on 2018/5/6

"""
import requests

__author__ = "逗蛆"


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
