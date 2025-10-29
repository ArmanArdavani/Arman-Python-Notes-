from abc import ABC, abstractclassmethod

class InvalidOperationsError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False 
    
    def open(self):
        if self.opened:
            raise InvalidOperationsError("Stream is already open")
        self.opened = True 

    def close(self):
        if not self.opened:
            raise InvalidOperationsError("Stream is already closed")
        self.closed = False 

    @abstractclassmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

stream = MemoryStream()
stream.read

