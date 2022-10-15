"""gen_file_rows"""


def gen_file_rows(file_object):
    """gen_file_rows"""
    with open(file_object, encoding='utf-8') as file:
        for line in file:
            yield line
