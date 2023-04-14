#!/usr/bin/env python3

import requests
import sys


def request_change_css(command):
    url = 'http://127.0.0.1:5000/update_css'
    data = {'command': command}
    response = requests.post(url, data=data)
    print(response.json())


def main():
    #command = sys.argv[1]
    #command = "背景换成橙色"
    command = "背景换成蓝色"
    command = "随机"
    request_change_css(command)


if __name__ == "__main__":
    main()
