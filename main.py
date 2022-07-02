nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, any_list):
        self.any_list = any_list
        self.ind = 0
        self.sub_ind = -1
        self.end = len(self.any_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.sub_end = len(self.any_list[self.ind])
        self.sub_ind += 1
        if self.sub_ind > self.sub_end - 1:
            self.sub_ind = 0
            self.ind += 1
        if self.ind > self.end - 1:
            raise StopIteration

        return self.any_list[self.ind][self.sub_ind]


flat_list = [item for item in FlatIterator(nested_list)]


def flat_generator(my_list):
    my = (item for el in my_list for item in el)
    return my


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print(flat_list)
    for item in flat_generator(nested_list):
        print(item)
