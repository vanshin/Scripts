#!/home/vanshin/.pyenv/shims/python
#coding=utf8

'''各种各样的小工具'''

import os
import sys
import datetime
import click

from requests import get,post

@click.command()
def title():
    now = datetime.datetime.now()
    isoweekday = now.isoweekday()
    title = now.strftime('%Y年%m月%d日 第%W周')
    print(title)
    return title

@click.group()
def main():
    pass

main.add_command(title)

if __name__ == '__main__':
    main()
