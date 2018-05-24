#!/home/vanshin/.pyenv/shims/python
#coding=utf8

'''各种各样的小工具'''

import os
import sys
import datetime
import click

from requests import get,post

def change(dest_fn, other):
    file_directory = '/etc/supervisor/conf.d/'
    dest_name = dest_fn.split('.')[0]
    source_file = os.path.join(file_directory, )
    source_file = '/etc/supervisor/conf.d/ads_api.conf'
    with open(source_file, 'r') as sf, open(dest_fn, 'w+') as df:
        data = []
        for i in sf.readlines():
            if source_name in i:
                i = i.replace(source_name, dest_name)
            data.append(i)
        df.writelines(data)

@click.command()
def title():
    now = datetime.datetime.now()
    isoweekday = now.isoweekday()
    title = now.strftime('%Y年%m月%d日 第%W周')
    title2 = now.strftime('%Y-%m-%d-%Ww')
    print(title)
    print(title2)
    return title

@click.command()
@click.option('--name', type=click.STRING, prompt='name:')
def sconf():
    source_fn = '/etc/supervisor/conf.d/apollo.conf'
    change(source_fn, de)
    return title

@click.group()
def main():
    pass

main.add_command(title)

if __name__ == '__main__':
    main()
