import sys

# usage: on main class: sys.stdout = Logger(<configFolderPath>)
class Logger(object):
    def __init__(self, configFolderPath):
        self.terminal = sys.stdout
        self.log = open(f'{configFolderPath}/log.txt', 'w')  # option W will rewrite log every time we run, and thats what we want

    def write(self, message):
        self.terminal.write(message)
        self.terminal.flush()
        self.log.write(message)
        self.log.flush()

    def flush(self):
        pass
