import unittest


def find_second_max(arr: list):
    array = list(set(arr))
    try:
        max1, max2 = (
            (array[0], array[1]) if array[1] < array[0] else (array[1], array[0])
        )
    except IndexError:
        return None
    for i in array[2:]:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max2


def funk(array: list):
    result = []
    for elem in array:
        if elem not in result and array.count(elem) == 1 and elem > 5:
            result.append(elem)
    return result


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_second_max([1, 2, 4, 6, 8, 9]), 8)

    def test_2(self):
        self.assertEqual(find_second_max([100, 100, 99]), 99)

    def test_3(self):
        self.assertEqual(find_second_max([24, -45, 33, 100]), 33)

    def test_4(self):
        self.assertEqual(find_second_max([11, 22, -10, 0, 14]), 14)

    def test_5(self):
        self.assertEqual(find_second_max([22, 1, 0, 12, 33, 45, 96]), 45)

    def test_6(self):
        self.assertEqual(
            funk([1, 2, 3, 4, 4, 4, 4, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8]), [6]
        )

    def test_7(self):
        self.assertEqual(funk([1, 2, 3, 4, 4, 4, 4]), [])

    def test_8(self):
        self.assertEqual(
            funk([3, 4, 3, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 88, 8, 9, 9]), [88]
        )


if __name__ == "__main__":
    unittest.main()
