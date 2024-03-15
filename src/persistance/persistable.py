# Persistable is a light weight base class for classes which can be persisted to disk

class Persistable():
    directory = "" # subdirectory under the data directory to be saved
    filename = "" # filename to use for this object on disk (should include extension)

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def get_filepath(self) -> str:
        """Generate the filepath for persisting this object under a personality directory."""
        return "/".join([self.directory, self.filename])