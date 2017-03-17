import os
import shutil
import sys
import re

base_path = r'C:\Users\vanshin\Downloads'
# pdf_path = make_path(base_path,r'pdf')
# pdf_java_path = make_path(base_path,r'pdf/java')
# pdf_python_path = make_path(base_path,r'pdf/python')
# zip_path = make_path(base_path,r'zip')


java = r'.*[Jj]ava.*\.pdf'
python = r'.*[Pp]ython.*\.pdf'
zip = r'.*\.zip'





def zhengli(path):
    for files in os.listdir(path):
        sourceFile = os.path.join(path,files)
        if os.path.isfile(sourceFile) and re.match(python,files):
            move_file(sourceFile,python_pdf_path)
        elif os.path.isfile(sourceFile) and re.match(java,files):
            move_file(sourceFile,java_pdf_path)
        elif os.path.isfile(sourceFile) and re.match(zip,files):
            move_file(sourceFile,zip_path)



def get_rests(path):
    suffix = set()
    pathname = set()
    for files in os.listdir(path):
        sourceFile = os.path.join(path,files)
        if os.path.isfile(sourceFile):
            suffix.add(get_suffix(files))
        else:
            pathname.add(files)
    rest = suffix - (suffix&pathname)
    return rest

def move_file(file,path):
    shutil.move(file,path)

def make_path(path):
    return os.path.join(base_path,path)

def get_suffix(filename):
    return filename.split('.').pop()

def main(path):
    rest = get_rests(path)
    for dir in rest:
        try:
            os.makedirs(make_path(dir))
        finally:
            print('存在文件夹%s' %dir)

    for files in os.listdir(path):
        sourceFile = make_path(files)
        if os.path.isfile(sourceFile):
            filepath = make_path(get_suffix(files))
            move_file(sourceFile,filepath)

if __name__ == '__main__':
    path = r'C:\Users\vanshin\Downloads'
    main(path)
