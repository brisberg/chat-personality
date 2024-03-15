# personality.py defines the virtual physical and social attributes of a chat bot.
# This class can be persisted to disk as a text file and is used to structure the prompts send
# to ChatGPT.

from persistance.persistable import Persistable

DEFAULT_FILENAME =  "personality.pkl"

class Personality(Persistable):
    directory = ""
    name = ""
    physical_attributes = []
    clothing = []
    vocal_attributes = []

    def __init__(self, directory, name, physical_attributes = [], clothing = [], vocal_attributes = []):
        super().__init__(directory, DEFAULT_FILENAME)
        self.name = name
        self.physical_attributes = physical_attributes
        self.clothing = clothing
        self.vocal_attributes = vocal_attributes

    def get_filepath(self):
        return "/".join([self.directory, DEFAULT_FILENAME])