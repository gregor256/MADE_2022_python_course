"""parse_json"""
import json


def my_keyword_callback(word):
    """my_keyword_callback"""
    return word


def parse_json(json_str: str, required_fields=None, keywords=None,
               keyword_callback=None):
    """parse_json"""
    json_dict = json.loads(json_str)
    parsing_result =[]
    for required_field in required_fields:
        if required_field in json_dict:
            for word in json_dict[required_field].split():
                if word in keywords:
                    parsing_result.append(keyword_callback(word))
    return parsing_result
