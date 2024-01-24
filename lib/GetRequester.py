import requests
import json

class GetRequester:

    def __init__(self, url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Using a list so that the data can be read as a list.
        load_list = []

        programs = json.loads(self.get_response_body())
        for program in programs:
            load_list.append(program)

        return load_list

program = GetRequester().load_json()
print(program)
