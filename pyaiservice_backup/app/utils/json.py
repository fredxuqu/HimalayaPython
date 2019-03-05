import json


def to_json(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=False, indent=4))
