#!/usr/bin/python3
""" module for testing base class """


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base_creation(unittest.TestCase):
    """ Test for all the base cases """

    def test_empty_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_ids(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_ids(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(15, Base(15).id)

    def test_nb_instances(self):
        b1 = Base()
        b2 = Base(14)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_change_id_main(self):
        b = Base(7)
        b.id = 20
        self.assertEqual(20, b.id)

    def test_id_str(self):
        self.assertEqual("hola", Base("hola").id)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(5).__nb_instances)

    def test_idf(self):
        self.assertEqual(10.5, Base(10.5).id)

    def test_dict_id(self):
        self.assertEqual({"a": 7, "b": 8}, Base({"a": 7, "b": 8}).id)

    def test_bool_id(self):
        self.assertEqual(False, Base(False).id)

    def test_idl(self):
        self.assertEqual([6, 8, 10], Base([6, 8, 10]).id)

    def test_idt(self):
        self.assertEqual((20, 30), Base((20, 30)).id)

    def test_ids(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 4)

    """ Test json exercises """

    def test_to_json_stringrec(self):
        r = Rectangle(5, 2, 4, 7, 10)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_stringrec_len_dict(self):
        r = Rectangle(7, 5, 1, 9, 4)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 52)

    def test_to_json_stringrec_two(self):
        r1 = Rectangle(1, 6, 7, 21, 4)
        r2 = Rectangle(4, 2, 4, 10, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 107)

    def test_to_json_stringsqua(self):
        s = Square(3, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_stringsqua_len_dict(self):
        s = Square(10, 12, 13, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 41)

    def test_to_json_stringsqua_two(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(14, 15, 21, 22)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 81)

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    """ Save to file exceptions """

    @classmethod
    def Delete_Files(self):
        """ Delete created files if exists """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_testone(self):
        r = Rectangle(19, 7, 12, 18, 15)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 56)

    def test_save_to_file_tworecs(self):
        r1 = Rectangle(15, 7, 2, 8, 5)
        r2 = Rectangle(12, 14, 11, 12, 13)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 110)

    def test_save_to_file_squareone(self):
        s = Square(15, 17, 21, 18)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_twosqua(self):
        s1 = Square(10, 5, 6, 4)
        s2 = Square(18, 11, 12, 13)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 81)

    def test_save_to_file_base(self):
        s = Square(11, 17, 12, 18)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_overwrite(self):
        s = Square(19, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 17, 12, 18)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    """ From json_string exercises excepcions """

    def test_from_json_string_type(self):
        list_input = [{"id": 10, "width": 5, "height": 3}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_stringrec(self):
        list_input = [{"id": 109, "width": 10, "height": 14, "x": 17}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_tworec(self):
        list_input = [
            {"id": 120, "width": 100, "height": 40, "x": 2, "y": 4},
            {"id": 77, "width": 50, "height": 20, "x": 10, "y": 1},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_stringsqua(self):
        list_input = [{"id": 189, "size": 100, "height": 40}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_twosqua(self):
        list_input = [
            {"id": 189, "size": 100, "height": 40},
            {"id": 77, "size": 10, "height": 70}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", 1)

    """ Tests for create method """
    def test_create_rectangle(self):
        r1 = Rectangle(30, 50, 4, 2, 17)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (17) 4/2 - 30/50", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(30, 50, 10, 4, 17)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (17) 10/4 - 30/50", str(r2))

    def test_create_rectangle_isnot(self):
        r1 = Rectangle(30, 50, 10, 15, 70)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equal(self):
        r1 = Rectangle(15, 2, 4, 1, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(30, 2, 4, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (12) 2/4 - 30", str(s1))

    def test_create_square_one(self):
        s1 = Square(13, 4, 8, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (12) 4/8 - 13", str(s2))

    def test_create_square_isnot(self):
        s1 = Square(4, 2, 3, 6)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equal(self):
        s1 = Square(4, 2, 3, 6)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    """ Test for load from file exercise """
    @classmethod
    def Delete(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
