import types

# b = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]

import types


def flat_generator(list_of_lists):
    cursor = 0
    cursor_in = 0
    #m = list_of_lists[cursor]
    try:
        while cursor_in != len(list_of_lists[cursor]):
            m = list_of_lists[cursor]
            n = m[cursor_in]
            yield list_of_lists[cursor][cursor_in]
            cursor_in += 1
        
            if cursor_in == len(m):
                cursor += 1
                cursor_in = 0
    except:
        StopIteration  
     

# for i in flat_generator(b):
#     print(i)




def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    