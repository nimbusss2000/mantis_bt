from sys import maxsize


class Task:

    def __init__(self, name=None, topic=None, description=None, id=None):
        self.user = name
        self.topic = topic
        self.description = description
        self.id = id

    def __repr__(self):
        return f'{self.id}, {self.topic}, {self.description}'

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.topic == other.topic

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
