import json

sample_json = """{"key1" : "value1", "key2" : "value2"}"""
json_sample =json.loads(sample_json)
print(json_sample ["key2"])