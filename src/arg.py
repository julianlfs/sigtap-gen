import argparse
import zipfile
import os
from os import path
import glob
from layout import FieldLayout, Layout

import const

def gerar_json(layout):
    print('tamanho do layout: ' + str(len(layout)))



def main():
    parser = argparse.ArgumentParser(prog='sia-gen', description='SIA zip file to descompress')
    parser.add_argument('filename', help=const.HELP_ARGS_FILENAME)
    parser.add_argument('folder', help=const.HELP_ARGS_FOLDER)

    args = parser.parse_args()
    
    if not (zipfile.is_zipfile(args.filename)):
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

    fields_layout = []
    layout = Layout(filterFile, fields_layout)
    for lay in listaLayout:
        print('>: ' + lay)
        layout_file = open(lay, "r", encoding="utf-8")
        content_file = layout_file.readlines()

        for i in range(1, len(content_file)):
            list_fields = content_file[i].split(',')
            field = FieldLayout(list_fields[0], list_fields[1], list_fields[2], list_fields[3], list_fields[4])
            fields_layout.append(field)
            #print(list(a))

        gerar_json(fields_layout)
    

if __name__ == '__main__':
    main()

