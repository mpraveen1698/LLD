# file_manager_srp.py

from pathlib import Path
from zipfile import ZipFile

#this class has two responsibilities  file management(read and write) and file compression(compress and decompress)
# class FileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)

#     def read(self, encoding="utf-8"):
#         return self.path.read_text(encoding)

#     def write(self, data, encoding="utf-8"):
#         self.path.write_text(data, encoding)

#     def compress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
#             archive.write(self.path)

#     def decompress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
#             archive.extractall()



#now the above class is dervied into two class according to the responsibility 
#Note : The concept of responsibility in this context may be pretty subjective. Having a single responsibility doesn’t necessarily mean having a single method. Responsibility isn’t directly tied to the number of methods but to the core task that your class is responsible for, depending on your idea of what the class represents in your code. However, that subjectivity shouldn’t stop you from striving to use the SRP.

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()