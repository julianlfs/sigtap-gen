from layout import Layout
from os import listdir
import glob
from layout import Layout, FieldLayout

l = Layout('tb_proc.txt', "co_pro", 10, 1, 5, 'varchar2')

# l.print_obj()

# print(listdir('C:\\dev\\tests-siagen\\exportado'))
# print(glob.glob('C:\\dev\\tests-siagen\\exportado\\*_layout.txt'))
la = Layout[]

field = FieldLayout('', 1, 10, 20, 'varchar2')

la.append(field)

print(la)





