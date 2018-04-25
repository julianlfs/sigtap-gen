from layout import Layout, FieldLayout


listField = []

# l.print_obj()

# print(listdir('C:\\dev\\tests-siagen\\exportado'))
# print(glob.glob('C:\\dev\\tests-siagen\\exportado\\*_layout.txt'))
field = FieldLayout('co_desc', 1, 10, 20, 'varchar2')
field2 = FieldLayout('no_desc', 1, 10, 20, 'varchar2')

listField.append(field)
listField.append(field2)

obj1 = Layout('tb_proc.txt', listField)

obj1.print_obj()





