class main:
    def __init__(self):
        import os

        self.os = os

    def runFile(self, filename: str, starter: str='python'):
        com = starter+' '+filename
        self.os.system(com)
        del com