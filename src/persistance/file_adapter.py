# file_adapter is a simple utility for persisting objects (such as personalities or game states)

import pickle
from pathlib import Path

from persistance.persistable import Persistable

class FileAdapter():
    # Root directory under which to save/read the files
    BASE_DIRECTORY = ""

    def __init__(self, base_dir):
        self.BASE_DIRECTORY = base_dir
        return
    
    def save_to_file(self, obj: Persistable):
        filepath = obj.get_filepath()

        # Create data directories if they do not exist
        file = Path(filepath)
        file.parent.mkdir(parents=True, exist_ok=True)

        with open("/".join([self.BASE_DIRECTORY, filepath]), "wb") as outf:
            pickle.dump(obj, outf, pickle.HIGHEST_PROTOCOL)
            return
        
    def load_from_file(self, filepath: str) -> Persistable:
        with open("/".join([self.BASE_DIRECTORY, filepath]), "rb") as file:
            return pickle.load(file)