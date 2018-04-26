import argparse
import zipfile
import os
from os import path
import glob
from layout import FieldLayout, Layout

import const


def gerar_json(layout):
    print('tamanho do layout: ' + str(len(layout.list_field)))
    arquivo = layout.filename.replace('_layout', '')
    try:
        arq_lay = open(arquivo, 'r')
        print(arq_lay.name)

        str_json = str('[')

        content_file = arq_lay.readlines()
        for idx, line in enumerate(content_file):
            str_json += '{'.expandtabs(4)
            for i in range(len(layout.list_field)):
                name = layout.list_field[i].field_name.lower()
                start = int(layout.list_field[i].field_pos_start)-1
                end = int(layout.list_field[i].field_pos_end)
                value = '\"' + line[start:end].strip() + '\"'

                str_json += '\"' + name + '\": ' + value

                if i < len(layout.list_field) - 1:
                    str_json += ','

            str_json += '}'
            if idx < len(content_file) - 1:
                str_json += ','
        str_json += ']'

        a = open(arquivo.replace('.txt', '') + '.json', 'w')
        a.write(str_json)
        print(str_json)

    except IOError as err:
        print('File not found: ' + str(err))
        pass
    except BaseException as err:
        print('Error: ' + str(err))


def main():
    parser = argparse.ArgumentParser(prog='sigtap-gen', description='SIGTAP json generator')
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

    filter_file = args.folder + '*_layout.txt'
    print(filter_file)
    lista_layout = glob.iglob(filter_file)

    for lay in lista_layout:
        fields_layout = []
        layout = Layout(None, fields_layout)
        print('> ' + lay)
        layout_file = open(lay, "r", encoding="utf-8")
        layout.filename = layout_file.name
        content_file = layout_file.readlines()

        for i in range(1, len(content_file)):
            list_fields = content_file[i].split(',')
            field = FieldLayout(list_fields[0], list_fields[1], list_fields[2], list_fields[3], list_fields[4])
            fields_layout.append(field)

        gerar_json(layout)
    

if __name__ == '__main__':
    main()

