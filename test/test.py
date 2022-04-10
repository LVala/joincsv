import os
import sys
import unittest
import io

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from src.main import main as src_main, gen_header

# files to test on
ex1_left = os.path.join("ex1", "ex1_left.csv")
ex1_right = os.path.join("ex1", "ex1_right.csv")
ex2_left = os.path.join("ex2", "ex2_left.csv")
ex2_right = os.path.join("ex2", "ex2_right.csv")
ex3_left = os.path.join("ex3", "ex3_left.csv")
ex3_right = os.path.join("ex3", "ex3_right.csv")

class HeaderTest(unittest.TestCase):
    def test_header_1(self):
        header = gen_header(ex2_left, ex2_right, "id")
        real_header = ["id", "firstname", "lastname", "email", "profession", "country", "city", "countrycode", "birthdate"]
        self.assertEqual(header, real_header)
    
    def test_header_2(self):
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

    def test_inner_join_1(self):
        ex1_res_inner = os.path.join("ex1", "ex1_res_inner.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "inner"]
        src_main()
        with open(ex1_res_inner, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_inner_join_2(self):
        ex2_res_inner = os.path.join("ex2", "ex2_res_inner.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "inner"]
        src_main()
        with open(ex2_res_inner, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())
    def test_inner_join_3(self):
        ex3_res_inner = os.path.join("ex3", "ex3_res_inner.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "inner"]
        src_main()
        with open(ex3_res_inner, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_left_join_1(self):
        ex1_res_left = os.path.join("ex1", "ex1_res_left.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "left"]
        src_main()
        with open(ex1_res_left, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_left_join_2(self):
        ex2_res_left = os.path.join("ex2", "ex2_res_left.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "left"]
        src_main()
        with open(ex2_res_left, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_left_join_3(self):
        ex3_res_left = os.path.join("ex3", "ex3_res_left.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "left"]
        src_main()
        with open(ex3_res_left, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_right_join_1(self):
        ex1_res_right = os.path.join("ex1", "ex1_res_right.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "right"]
        src_main()
        with open(ex1_res_right, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_right_join_2(self):
        ex2_res_right = os.path.join("ex2", "ex2_res_right.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "right"]
        src_main()
        with open(ex2_res_right, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

    def test_right_join_3(self):
        ex3_res_right = os.path.join("ex3", "ex3_res_right.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "right"]
        src_main()
        with open(ex3_res_right, "r") as file:
            self.assertEqual(file.read(), self.my_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()