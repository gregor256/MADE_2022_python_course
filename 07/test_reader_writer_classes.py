import unittest
from reader_writer_classes import read_data, dump_data, \
    JsonReader, JsonWriter, TxtWriter, TxtReader, \
    CSVWriter, CSVReader


class TestReaderWriter(unittest.TestCase):
    def test_reading_writing(self):
        data_to_dump = {"x": "1"}
        current_fileobject = 'write_json.json'
        dump_data(data_to_dump, current_fileobject,
                  writer=JsonWriter)

        data_to_dump = 'Python'
        current_fileobject = 'write_txt.txt'
        dump_data(data_to_dump, current_fileobject, TxtWriter)

        data_to_dump = [['one', 'two', 'three'], [1, 2, 3], [4, 5, 6]]
        current_fileobject = 'write_csv.csv'
        dump_data(data_to_dump, current_fileobject, CSVWriter)

        some_txt = read_data('write_txt.txt', reader=TxtReader)
        self.assertEqual('Python\n', some_txt)

        some_csv = read_data('write_csv.csv', reader=CSVReader)
        self.assertListEqual([['one', 'two', 'three'],
                              ['1', '2', '3'], ['4', '5', '6']],
                             some_csv)

        some_json = read_data('write_json.json', reader=JsonReader)
        self.assertDictEqual(some_json, {"x": "1"})

    def test_errors(self):
        with self.assertRaises(TypeError) as error:
            read_data('write_json.json', reader=int)
        self.assertEqual(str(error.exception), 'Invalid reader')
        self.assertRaises(TypeError, read_data,
                          'write_json.json', reader=int)

        with self.assertRaises(FileNotFoundError) as error:
            read_data('write_', reader=JsonReader)
        self.assertEqual(
            str(error.exception), 'No such file or directory: write_')
        self.assertRaises(FileNotFoundError,
                          read_data, 'write_', reader=JsonReader)


if __name__ == '__main__':
    unittest.main()
