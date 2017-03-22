#encoding=utf8

import os
import sys
import logging
logging.basicConfig(level=logging.INFO)

def get_osinfo():
    
    os_name = os.name
    pyfile = "Index('https://pypi.douban.com/')"

    

def get_env_path():
    """ 23兼容 """
    version_info = sys.version_info[0:2]
    if version_info[0] == 3:
        pre_path = input("type the virtualenv path, end with //:")
    elif version_info[0] == 2:
        pre_path = raw_input("type the virtualenv path, end with //:")
    return pre_path

def get_bpath():
    """ 系统兼容 """
    version_info = sys.version_info[0:2]
    if os.name == "posix":
        python_version = "python" + version_info[0] + '.' + version_info[1]
        b_path = "Lib\\" + python_version + "\\site-packages\\pip\\models\\index.py"
    elif os.name == "nt":
        b_path = "Lib\\site-packages\\pip\\models\\index.py"
    return b_path

def get_pre():
    """ 获取虚拟环境路径 """
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
    b_path = get_bpath()
    full_path = os.path.join(pre_path, b_path)
    with open(full_path, "r+") as f:
        # 读取文件的所有内容
        lines = f.readlines()
        # 将文件的偏移量设置为开始
        f.seek(0)
        # 将文件的内容全部删除
        f.truncate()
        d = ''
        for line in lines:
            # 将需要更改的地方更改
            d = d+line.replace("python.org", "douban.com")
        # 将修改后的文件输入
        f.write(d)


if __name__ == '__main__':
    main()
