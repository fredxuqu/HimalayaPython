
import json

python2json = {}

listData = [1,2,3]
python2json["listData"] = listData
python2json["strData"] = "test python obj 2 json"


json_str = json.dumps(python2json)
print (json_str)

class bookvo:
    id = 0
    name= ''
    def __init__(self, id, name):
        self.id = id
        self.name = name

booklist = {}
book = bookvo(1, "java")
print (book)