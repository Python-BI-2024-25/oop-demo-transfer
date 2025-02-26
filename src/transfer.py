from src.abstracts import AbstractDestination, AbstractSource


class Transfer:
    def __init__(self, src: AbstractSource, dest: AbstractDestination):
        self.source = src
        self.destination = dest

    def run(self):
        with self.source as src, self.destination as dest:
            data = src.read_data()
            dest.write_data(data)
