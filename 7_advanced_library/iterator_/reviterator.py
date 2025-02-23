class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    ia = ReverseIterator(a)

    for i in ia:
        print(i)
