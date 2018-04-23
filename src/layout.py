class FieldLayout:
    
    def __init__(self, field, size, start, end, field_type):
        self.field = field
        self.size = size
        self.start = start
        self.end = end
        self.field_type = field_type

    def print_obj(self):
        print('field: ' + self.field)
        print('size: ' + str(self.size))
        print('start: ' + str(self.start))
        print('end: ' + str(self.end))
        print('field_type: ' + self.field_type)

class Layout:
    """ Layout class """
    def __init__(self, filename, listFieldLayout):
        self.filename = filename
        self.listFieldLayout = listFieldLayout
         
    def print_obj(self)
        print('filename: ' + self.filename)
        print('lista fields: ' + self.listfield) 
    
