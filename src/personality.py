# personality.py defines the virtual physical and social attributes of a chat bot.
# This class can be persisted to disk as a text file and is used to structure the prompts send
# to ChatGPT.

import pickle

DEFAULT_DIRECTORY = "data/personalities"

class Personality:
    directory = ""
    name = ""
    physical_attributes = []
    clothing = []
    vocal_attributes = []

    def get_filepath(self):
        return "".join([DEFAULT_DIRECTORY, "/", self.directory, "/personality.pkl"])