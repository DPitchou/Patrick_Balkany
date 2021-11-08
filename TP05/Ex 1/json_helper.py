import json


class JsonHelper:

    def save(self, data, json_file):
        with open(json_file, "w") as file:
            json.dump(data, file, sort_keys=True, indent=4)


    def load(self, json_file):
        with open(json_file) as file:
            jsonfile = json.load(file)
        return jsonfile
