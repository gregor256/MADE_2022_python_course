import json


def my_keyword_callback(word):
    print(word)


def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    json_dict = json.loads(json_str)
    for required_field in required_fields:
        if required_field in json_dict:
            for word in json_dict[required_field].split():
                if word in keywords:
                    keyword_callback(word)


task_json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
task_required_fields = ["key1"]
task_keywords = ["word2"]

parse_json(task_json_str, task_required_fields, task_keywords, my_keyword_callback)

