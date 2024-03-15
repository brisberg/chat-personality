# file_read_writer is a simple utility for persisting objects (such as personalities or game states)

import pickle
from pathlib import Path

def save_to_file(obj):
    filepath = obj.get_filepath()

    # Create data directories if they do not exist
    file = Path(filepath)
    file.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "wb") as outf:
        pickle.dump(obj, outf, pickle.HIGHEST_PROTOCOL)
        return
    
def load_from_file(filepath: str):
    with open(filepath, "rb") as file:
        return pickle.load(file)