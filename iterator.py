# a = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#         ]

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.lst = []
        return self

    def __next__(self):
        
           
            if self.cursor == len(self.lst):
                for item in self.list_of_list:
                    for  ii in item:
                        self.lst.append(ii)
                self.cursor  += 1
            
                #return self.lst   # если закоментировать, то проходит первый тест
            raise StopIteration    
            
                


# flat_iterator = FlatIterator(a)

# for i in flat_iterator:
#     print(i)
    
    

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
   

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    