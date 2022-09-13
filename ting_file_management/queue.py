class Queue:
    def __init__(self):
        self._stack = list()

    def __len__(self):
        return len(self._stack)

    def enqueue(self, value):
        self._stack.append(value)

    def dequeue(self):
        value = self._stack[0]
        del self._stack[0]
        return value

    def search(self, index):
        try:
            if 0 > index < len(self._stack):
                raise IndexError
            value = self._stack[index]
            return value
        except IndexError:
            raise IndexError
