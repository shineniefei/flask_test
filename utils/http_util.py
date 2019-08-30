#!/usr/bin/env python3
# coding: utf-8

from urllib import request
import requests


class HttpUtil():
    def __init__(self):
        self.timeout = 30
        self.headers_dict = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Connection':
            'keep-alive',
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8"
        }

    def do_get(self, url, params, headers):
        try:
            r = requests.get(
                url=url, params=params, headers=headers, timeout=self.timeout)
            print(r.raise_for_status())
            return r.text
        except Exception as e:
            print(e)
            return "do_get model exception: {}".format(e)

    def do_post(self, url, data, headers):
        try:
            r = requests.post(
                url=url, data=data, headers=headers, timeout=self.timeout)
            print(r.raise_for_status())
            return r.text
        except Exception as e:
            print(e)
            return "do_post model exception: {}".format(e)

    def do_transmit(self, method, url, data, headers):
        if method == 'GET':
            return self.do_get(url, data, headers)
        elif method == 'POST':
            return self.do_post(url, data, headers)
        else:
            return 'do_transmit model exception: method must be GET or POST'

    def do_put(self, url):
        r = requests.put(url=url)
        r.raise_for_status()

    def do_delete(self, url):
        r = requests.delete(url=url)
        r.raise_for_status()

    def do_options(self, url):
        r = requests.options(url=url)
        r.raise_for_status()

    def do_head(self, url):
        r = requests.head(url=url)
        r.raise_for_status()


def doPost(url, data):
    print('Post to: ' + url + ', send data: ' + data)
    data = bytes(data, 'utf-8')
    req = request.Request(url)
    req.add_header('Content-Type', 'application/json')
    print(req.get_header('Content-Type'))
    with request.urlopen(req, data=data) as f:
        print('响应结果 status: ', f.status, f.reason)
        print(f.getheader('Content-Type'))
        back = f.read().decode('utf-8')
        print('get data: ' + back)
    return back


def doGet(url, data):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
    }
    params = "?"
    if data != '':
        for key in data:
            params = params + key + "=" + data[key] + "&"
    else:
        params = ''
    print('Get to: ' + url + ', send data: ' + params)
    req = request.Request(url=url + params, headers=headers)
    with request.urlopen(req) as f:
        print('响应结果 status: ', f.status, f.reason)
        back = f.read().decode('utf-8')
        print('get data: ' + back)
    return back


if __name__ == '__main__':
    HttpUtil = HttpUtil()
