import os


class FileManager:
    download_location = None

    def __init__(self, download_location):
        self.download_location = download_location

    def rename_m3u8(self, src, dest):
        os.rename(os.path.join(self.download_location, src), os.path.join(self.download_location, dest))
        return os.path.join(self.download_location, dest)

    def delete(self, filename):
        os.remove(filename)
