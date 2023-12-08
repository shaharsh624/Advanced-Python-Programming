class OSNotFound(Exception):
    def __init__(self, string):
        self.string = string
        print("OS Not Found:", string)