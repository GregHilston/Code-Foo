import unittest
from solution import HashTable

class HashTableTests(unittest.TestCase):
    def setUp(self):
        self.sut = HashTable()

    def test_hashtable_returns_none_when_getting_something_that_was_not_added(self):
        # Given
        key = 1

        # When
        returned_value = self.sut[key]

        # Then
        self.assertIsNone(returned_value, """The returned_value should be None, 
        as we never initially stored key""")
    
    def test_hashtable_returns_none_when_putting_something_that_was_not_added(self):
        # Given
        key = 1
        value = "potato"

        # When
        returned_put_status = self.sut[key] = value

        # Then
        self.assertIsNone(returned_put_status, """The returned_put_status should 
        be None, as we successfully stored key and value""")

    def test_hashtable_returns_none_when_putting_something_that_collides(self):
        # Given
        key_one = 1
        value_one = "potato"

        key_two = 43
        value_two = "fish"

        # When
        returned_put_status_one = self.sut[key_one] = value_one
        returned_put_status_two = self.sut[key_two] = value_two

        # Then
        self.assertIsNone(returned_put_status_one, """The returned_put_status_one 
        should be None, as we successfully stored key and value""")
        self.assertIsNone(returned_put_status_two, """The returned_put_status_two 
        should be None, as we successfully stored key and value""")

    def test_hashtable_returns_value_when_getting_something_that_collides(self):
        # Given
        key_one = 1
        value_one = "potato"

        key_two = 43
        value_two = "fish"

        # When
        returned_put_status_one = self.sut[key_one] = value_one
        returned_put_status_two = self.sut[key_two] = value_two

        returned_value_three = self.sut[key_two]

        # Then
        self.assertIsNone(returned_put_status_one, """The returned_put_status_one 
        should be None, as we successfully stored key and value""")
        self.assertIsNone(returned_put_status_two, """The returned_put_status_two 
        should be None, as we successfully stored key and value""")
        self.assertEqual(value_two, returned_value_three, """The returned_value_three 
        should be equal to value_two, as we set it previously""")

if __name__ == '__main__':
    unittest.main()