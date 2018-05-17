
class BNode(object):

    def __init__(self, identifier):
        self._identifier = identifier

    def __str__(self):
        return self._identifier

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return str(self) == str(other)