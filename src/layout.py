class FieldLayout:
    
    def __init__(self, field_name, field_size, field_pos_start, field_pos_end, field_type):
        self.field_name = field_name
        self.field_size = field_size
        self.field_pos_start = field_pos_start
        self.field_pos_end = field_pos_end
        self.field_type = field_type

    def print_obj(self):
        print('field: ' + self.field_name)
        print('size: ' + str(self.field_size))
        print('start: ' + str(self.field_pos_start))
        print('end: ' + str(self.field_pos_end))
        print('field_type: ' + self.field_type)


class Layout:

    list_field = []

    def __init__(self, filename, list_field):
        self.filename = filename
        self.list_field = list_field

    def print_obj(self):
        print('filename: ' + self.filename)
        print('lista fields: ' + str(len(self.list_field)))
