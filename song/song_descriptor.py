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
        pass

    def describe_whole_song(self):
        return self._song

    def describe_single_verse(self, line):
        pass

    def describe_verse_in_range(self, left, right):
        pass


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

    def test_describe_single_verse_on_line_3(self):
        descriptor = SongDescriptor()
        third_verse = "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(descriptor.describe_single_verse(3), third_verse)

    def test_describe_single_verse_when_out_of_bound(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_single_verse(99)

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
        verses = """
        On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        
        On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
        """
        self.assertEqual(descriptor.describe_verse_in_range(2, 5), verses)

    def test_describe_verse_in_range_when_left_is_negative(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(-5, 2)

    def test_describe_verse_in_range_when_right_is_negative(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range(2, -5)

    def test_describe_verse_in_range_when_right_is_smaller(self):
        descriptor = SongDescriptor()
        with self.assertRaises(ValueError):
            descriptor.describe_verse_in_range("4", 1)

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
