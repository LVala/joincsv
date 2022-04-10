import os
import sys
import unittest
import io

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from src.main import main as src_main, gen_header

class HeaderTest(unittest.TestCase):
    def test_header_1(self):
        ex2_left = os.path.join("ex2", "ex2_left.csv")
        ex2_right = os.path.join("ex2", "ex2_right.csv")
        header = gen_header(ex2_left, ex2_right, "id")
        real_header = ["id", "firstname", "lastname", "email", "profession", "country", "city", "countrycode", "birthdate"]
        self.assertEqual(header, real_header)
    
    def test_header_2(self):
        ex3_left = os.path.join("ex3", "ex3_left.csv")
        ex3_right = os.path.join("ex3", "ex3_right.csv")
        header = gen_header(ex3_left, ex3_right, "cityId")
        real_header = ["id", "firstname", "lastname", "cityId", "cityName"]
        self.assertEqual(header, real_header)

class JoinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.real_stdout = sys.stdout

    @classmethod
    def setUp(self):
        sys.stdout = self.my_stdout = io.StringIO()

    @classmethod
    def tearDown(self):
        sys.stdout = JoinTest.real_stdout 
    
    def join_helper(self, file_num, col_name, mode):
        res_file = os.path.join(f"ex{file_num}", f"ex{file_num}_res_{mode}.csv")
        left_file = os.path.join(f"ex{file_num}", f"ex{file_num}_left.csv")
        right_file = os.path.join(f"ex{file_num}", f"ex{file_num}_right.csv")
        sys.argv = ["join", left_file, right_file, col_name, mode]
        src_main()
        with open(res_file, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_inner_join_1(self):
        self.join_helper(1, "id", "inner")

    def test_inner_join_2(self):
        self.join_helper(2, "id", "inner")

    def test_inner_join_3(self):
        self.join_helper(3, "cityId", "inner")

    def test_left_join_1(self):
        self.join_helper(1, "id", "left")

    def test_left_join_2(self):
        self.join_helper(2, "id", "left")

    def test_left_join_3(self):
        self.join_helper(3, "cityId", "left")

    def test_right_join_1(self):
        self.join_helper(1, "id", "right")

    def test_right_join_2(self):
        self.join_helper(2, "id", "right")

    def test_right_join_3(self):
        self.join_helper(3, "cityId", "right")

if __name__ == "__main__":
    unittest.main()