#encoding=utf8

import os
import sys
import logging
logging.basicConfig(level=logging.INFO)

def get_osinfo():
    
    os_name = os.name
    pyfile = "Index('https://pypi.douban.com/')"

    if os.name == "posix":
        pass
    elif os.name == "nt":
        pass

        
    

    # if os_info == 'nt'
def get_env_path():
    version_info = sys.version_info[0]
    if version_info == 3:
        pre_path = input("type the virtualenv path :")
    elif version_info == 2:
        pre_path = raw_input("type the virtualenv path :")
    return pre_path

def get_pre():
    len_argv = len(sys.argv)
    if len_argv == 1:
        pre_path = get_env_path()
    elif len_argv > 1:
        pre_path = sys.argv[1]
    return pre_path

def main():
    """ main func """
    # 获取文件所在目录
    # 定位的需要更改的那一行
    # 执行更改
    pre_path = get_pre()
    index = "index.py"
    b_path = "Lib\\site-packages\\pip\\models\\"
    full_path = os.path.join(pre_path, b_path)
    index_file = os.path.join(full_path, index)
    with open(index_file, "r") as f:
        lines = f.readlines()
        
        
        
    print(full_path)
    a = "123"
    a.replace
if __name__ == '__main__':
    main()
