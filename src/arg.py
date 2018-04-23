import argparse
import zipfile
import os
from os import path
import glob

import const

def main():
    parser = argparse.ArgumentParser(prog='sia-gen', description='SIA zip file to descompress')
    parser.add_argument('filename', help=const.HELP_ARGS_FILENAME)
    parser.add_argument('folder', help=const.HELP_ARGS_FOLDER)

    args = parser.parse_args()
    
    if  not (zipfile.is_zipfile(args.filename)):
        print(const.INVALID_FILENAME % args.filename)
        return False

    if not path.isdir(args.folder):
        os.mkdir(args.folder)
        print('Pasta criada.') 

    with zipfile.ZipFile(args.filename, 'r') as myZip:
        myZip.extractall(args.folder)

    print('extraido, sem erros')

    filterFile = args.folder + '*_layout.txt'
    print(filterFile)
    listaLayout = glob.iglob(filterFile)
    for lay in listaLayout:
        print('>: ' + lay)
        f = open(lay, "r", encoding="utf-8")
        print(f.readline())
    


if __name__ == '__main__':
    main()
# print(args.filename)