import json
import csv


class BaseReader:
    def __init__(self, file_name=''):
        self.file_name = file_name

    def read(self):
        pass

    @staticmethod
    def function_for_pylint():
        return 'pylint'


class TxtReader(BaseReader):
    def read(self):
        with open(self.file_name, 'r') as cur_file:
            return cur_file.read()


class CSVReader(BaseReader):
    def read(self):
        result = []
        with open(self.file_name, newline='') as cur_file:
            cur_reader = csv.reader(cur_file, delimiter=',', quotechar='|')
            for row in cur_reader:
                result.append(row)
        return result


class JsonReader(BaseReader):
    def read(self):
        with open(self.file_name, 'r') as cur_file:
            return json.load(cur_file)


class BaseWriter:
    def __init__(self, data='', file_name=''):
        self.data = data
        self.file_name = file_name

    def write(self):
        pass

    @staticmethod
    def function_for_pylint():
        return 'pylint'


class TxtWriter(BaseWriter):
    def dump(self):
        with open(self.file_name, 'w') as cur_file:
            print(self.data, file=cur_file)


class JsonWriter(BaseWriter):
    def dump(self):
        with open(self.file_name, 'w') as cur_file:
            json.dump(self.data, cur_file)


class CSVWriter(BaseWriter):

    def dump(self):
        with open(self.file_name, 'w', newline='') as cur_file:
            writer = csv.writer(cur_file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in self.data:
                writer.writerow(row)


def read_data(fileobject, reader):
    try:
        if not isinstance(reader(), BaseReader):
            raise TypeError('Invalid reader')
        current_reader = reader(fileobject)
        return current_reader.read()
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f'No such file or directory: {fileobject}') from error


def dump_data(data, fileobject, writer=None):
    default_writer = {
        str: TxtWriter,
        dict: JsonWriter,
        list: CSVWriter,
    }
    if not writer:
        current_writer = \
            default_writer[type(data)](data, fileobject)
    else:
        current_writer = writer(data, fileobject)
    current_writer.dump()
