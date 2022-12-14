import unittest


class SongDescriptor:

    def __init__(self):
        self._song = """
        On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
        
        On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        """


        self._number_of_lines = len(list(filter(lambda x: x.strip(), self._song.splitlines())))
        self._array_of_verses = list(filter(lambda x: x.strip(), self._song.splitlines()))
        pass

    def describe_whole_song(self):
        return self._song

    def describe_single_verse(self, line):
        if not isinstance(line, int):
            raise TypeError
        if line <= 0 or line > self._number_of_lines:
            raise ValueError

        return self._array_of_verses[line - 1].strip()


    def describe_verse_in_range(self, left, right):
        if not isinstance(left, int) or not isinstance(right, int):
            raise TypeError
        if left <= 0 or right > self._number_of_lines or right < left:
            raise ValueError

        if left == right:
            return self.describe_single_verse(left)

        result = ""
        for i in range(left - 1, right):
            result += self._array_of_verses[i].strip()
            if i != (right - 1):
                result += "\n"


        return result



class SongDescriptorTest(unittest.TestCase):

    def test_describe_whole_song(self):
        descriptor = SongDescriptor()
        song = """
        On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
        
        On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        """
        self.assertEqual(descriptor.describe_whole_song(), song)

    def test_describe_single_verse_on_line_0(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_single_verse(0)

    def test_describe_single_verse_on_line_1(self):
        descriptor = SongDescriptor()
        third_verse = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        self.assertEqual(descriptor.describe_single_verse(1), third_verse)

    def test_describe_single_verse_on_line_3(self):
        descriptor = SongDescriptor()
        third_verse = "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(descriptor.describe_single_verse(3), third_verse)

    def test_describe_single_verse_on_line_12(self):
        descriptor = SongDescriptor()
        third_verse = "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(descriptor.describe_single_verse(12), third_verse)

    def test_describe_single_verse_when_out_of_bound(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_single_verse(99)

    def test_describe_single_verse_when_out_of_bound_2(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_single_verse(13)

    def test_describe_single_verse_when_negative_line_number(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_single_verse(-5)

    def test_describe_single_verse_when_right_is_not_a_number(self):
        descriptor = SongDescriptor()
        with self.assertRaises(TypeError):
            descriptor.describe_single_verse("3")

    def test_describe_verse_in_range(self):
        descriptor = SongDescriptor()
        verses = """On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""
        self.assertEqual(descriptor.describe_verse_in_range(2, 5), verses)

    def test_describe_verse_in_range_when_left_is_negative(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(-5, 2)

    def test_describe_verse_in_range_when_left_is_zero(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(0, 2)

    def test_describe_verse_in_range_when_right_is_negative(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(2, -5)

    def test_describe_verse_in_range_when_right_is_smaller(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(4, 1)

    def test_describe_verse_in_range_when_range_is_equal(self):
        descriptor = SongDescriptor()
        third_verse = "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(descriptor.describe_verse_in_range(3, 3), third_verse)

    def test_describe_verse_in_range_when_left_is_not_a_number(self):
        descriptor = SongDescriptor()
        with self.assertRaises(TypeError):
            descriptor.describe_verse_in_range("3", 4)

    def test_describe_verse_in_range_when_right_is_not_a_number(self):
        descriptor = SongDescriptor()
        with self.assertRaises(TypeError):
            descriptor.describe_verse_in_range(3, "4")
