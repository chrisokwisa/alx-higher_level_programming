#!/usr/bin/python3
""" module for testing rectangle class """

import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class Test_Rectangles(unittest.TestCase):
    """ Tests for all rectangles exercises """
    def test_rectangle_istance(self):
        self.assertIsInstance(Rectangle(5, 12), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(5, 20)
        r2 = Rectangle(21, 9)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(12, 6, 8)
        r2 = Rectangle(25, 30, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(7, 8, 1, 6)
        r2 = Rectangle(11, 12, 15, 14)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(12, Rectangle(9, 1, 6, 3, 12).id)

    def test_more_than_fiveargs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 3, 5, 7, 9)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(14, 15, 3, 2, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 17, 16, 18, 3).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 6, 7, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 6, 7, 1).__y)

    def test_width_setter(self):
        r = Rectangle(1, 1, 2, 3, 5)
        r.width = 14
        self.assertEqual(14, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 3, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(1, 1, 2, 3, 5)
        r.height = 17
        self.assertEqual(17, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 3, 8, 15, 1)
        self.assertEqual(8, r.x)

    def test_x_setter(self):
        r = Rectangle(1, 1, 2, 3, 5)
        r.x = 14
        self.assertEqual(14, r.x)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 17, 14)
        self.assertEqual(17, r.y)

    def test_y_setter(self):
        r = Rectangle(50, 72, 76, 3, 2)
        r.y = 19
        self.assertEqual(19, r.y)

    """ Test width exceptions """
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hola", 1)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(100000.5, 1)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 6, "b": 7}, 1)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 1)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([6, 7, 3], 1)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((8, 9, 3), 1)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 1)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_negativewidth(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 1)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

    """ Test for height cases """
    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "hello")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 100.5)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 100, "b": 20})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [3, 5, 6])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (7, 8, 9))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negativeheight(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -3)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    """ Test for all x cases """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, "Hola", 6)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, 105.5, 6)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, {"a": 2, "b": 3}, 8)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, False, 8)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, [7, 8, 9], 8)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, (7, 8, 9), 8)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, b'Python')

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, float('nan'), 8)

    def test_negativex(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 6, -1, 8)

    """ Test for all y cases """
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, "Hola")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, 100.5)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, {"a": 7, "b": 9})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, [5, 7, 9])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, (5, 7, 9))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, b'Python')

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 8, float('nan'))

    def test_negativey(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 6, 8, -3)

    """ Attribute order tests """
    def test_width_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("no es valido crack", "F")

    def test_width_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("no es valido crack", 3, "F")

    def test_width_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("no es valido crack", 1, 2, "F")

    def test_height_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "no es valido crack", "F")

    def test_height_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "no es valido crack", 6, "F")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "no es valido crack", "F")

    """ Tests for area """
    def test_area_small(self):
        r = Rectangle(20, 4, 0, 0, 0)
        self.assertEqual(80, r.area())

    def test_area_big(self):
        r = Rectangle(100000, 100000, 0, 0, 3)
        self.assertEqual(10000000000, r.area())

    def test_area_attr(self):
        r = Rectangle(20, 30, 3, 3, 3)
        r.width = 14
        r.height = 10
        self.assertEqual(140, r.area())

    def test_area_one_arg(self):
        r = Rectangle(30, 100, 3, 3, 3)
        with self.assertRaises(TypeError):
            r.area(1)

    """ Test for __str__ and display methods """
    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_case0(self):
        r = Rectangle(7, 8)
        capture = self.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 7/8\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_case1(self):
        r = Rectangle(7, 8, 14)
        correct = "[Rectangle] ({}) 14/0 - 7/8".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_case2(self):
        r = Rectangle(7, 8, 14, 12)
        correct = "[Rectangle] ({}) 14/12 - 7/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_case3(self):
        r = Rectangle(7, 8, 14, 12, 13)
        self.assertEqual("[Rectangle] (13) 14/12 - 7/8", str(r))

    def test_str_method_attr(self):
        r = Rectangle(7, 8, 14, 12, [13])
        r.width = 13
        r.height = 11
        r.x = 81
        r.y = 100
        self.assertEqual("[Rectangle] ([13]) 81/100 - 13/11", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 1, 2, 3, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_case0(self):
        r = Rectangle(4, 5, 0, 0, 0)
        capture = self.capture_stdout(r, "display")
        self.assertEqual("####\n####\n####\n####\n####\n", capture.getvalue())

    def test_display_case1(self):
        r = Rectangle(3, 5, 1, 0, 1)
        capture = self.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n ###\n ###\n ###\n", capture.getvalue())

    def test_display_case2(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = self.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_case3(self):
        r = Rectangle(3, 4, 1, 1, 0)
        capture = self.capture_stdout(r, "display")
        display = "\n ###\n ###\n ###\n ###\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 1, 3, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    """ Test for update args and kwargs """
    def test_update_args_case0(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update()
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(r))

    def test_update_args_case1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109)
        self.assertEqual("[Rectangle] (109) 14/14 - 14/14", str(r))

    def test_update_args_case2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1)
        self.assertEqual("[Rectangle] (109) 14/14 - 1/14", str(r))

    def test_update_args_case3(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, 1)
        self.assertEqual("[Rectangle] (109) 14/14 - 1/1", str(r))

    def test_update_args_case4(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, 2, 3)
        self.assertEqual("[Rectangle] (109) 3/14 - 1/2", str(r))

    def test_update_args_case5(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, 2, 3, 4)
        self.assertEqual("[Rectangle] (109) 3/4 - 1/2", str(r))

    def test_update_args_more_sixargs(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (109) 3/4 - 1/2", str(r))

    def test_update_args_emptyid(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(None)
        correct = "[Rectangle] ({}) 14/14 - 14/14".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_attr(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(None, 1, 2, 3)
        correct = "[Rectangle] ({}) 3/14 - 1/2".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, 2, 3, 5, 6)
        r.update(6, 5, 3, 2, 1, 109)
        self.assertEqual("[Rectangle] (6) 2/1 - 5/3", str(r))

    def test_update_args_invalid_width(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(109, "Hola")

    def test_update_args_zero(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(109, 0)

    def test_update_args_negative(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(109, -5)

    def test_update_args_invalid_height(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(109, 1, "hola")

    def test_update_args_zero2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(109, 1, 0)

    def test_update_args_negative2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(109, 1, -5)

    def test_update_args_invalid_x(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(109, 1, 2, "hola")

    def test_update_args_negative3(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(109, 1, 1, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(109, 1, 2, 3, "hola")

    def test_update_args_negative4(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(109, 1, 1, 2, -6)

    def test_update_args_width_case1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(109, "hola", "crack")

    def test_update_args_width_case2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(109, "hola", 1, "crack")

    def test_update_args_width_case3(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(109, "hola", 1, 1, "crack")

    def test_update_args_height_case1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(109, 1, "hola", "crack")

    def test_update_args_height_case2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(109, 1, "hola", 1, "crack")

    def test_update_args_x_case1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(109, 1, 1, "hola", "crack")

    """ Kwargs tests """
    def test_update_kwargs_case1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(id=109)
        self.assertEqual("[Rectangle] (109) 14/14 - 14/14", str(r))

    def test_update_kwargs_case2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(width=1, id=109)
        self.assertEqual("[Rectangle] (109) 14/14 - 1/14", str(r))

    def test_update_kwargs_case3(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(width=1, height=2, id=109)
        self.assertEqual("[Rectangle] (109) 14/14 - 1/2", str(r))

    def test_update_kwargs_case4(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(id=109, x=3, height=2, y=4, width=1)
        self.assertEqual("[Rectangle] (109) 3/4 - 1/2", str(r))

    def test_update_kwargs_case5(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(y=4, x=3, id=109, width=1, height=2)
        self.assertEqual("[Rectangle] (109) 3/4 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(id=None)
        correct = "[Rectangle] ({}) 14/14 - 14/14".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_none_attr(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(id=None, height=2, y=4)
        correct = "[Rectangle] ({}) 14/4 - 14/2".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(id=109, x=1, height=1)
        r.update(y=2, height=15, width=1)
        self.assertEqual("[Rectangle] (109) 1/2 - 1/15", str(r))

    def test_update_kwargs_invalid_width(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="hola")

    def test_update_kwargs_zero(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_negative(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-8)

    def test_update_kwargs_invalid_height(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="hola")

    def test_update_kwargs_zero1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_negative1(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_invalid_x(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="hola")

    def test_update_kwargs_negative2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="hola")

    def test_update_kwargs_negative3(self):
        r = Rectangle(14, 14, 14, 14, 14)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(109, 1, height=3, y=6)
        self.assertEqual("[Rectangle] (109) 14/14 - 1/14", str(r))

    def test_update_kwargs_wrong_keywords(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(a=9, b=17)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(r))

    def test_update_kwargs_wrong_keywords2(self):
        r = Rectangle(14, 14, 14, 14, 14)
        r.update(height=5, id=109, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (109) 19/7 - 14/5", str(r))

    def test_to_dictionary_case2(self):
        r1 = Rectangle(14, 1, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 1, 14)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_case3(self):
        r = Rectangle(14, 1, 3, 1, 1)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
