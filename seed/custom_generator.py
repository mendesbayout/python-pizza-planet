from datetime import datetime

from faker.generator import random


class DateTimeGenerator:
    def __init__(self, start=datetime(1970, 1, 1), end=datetime.now()):
        self.start = start
        self.end = end

    def generate(self):
        return datetime.utcfromtimestamp(random.uniform(self.start.timestamp(), self.end.timestamp()))
