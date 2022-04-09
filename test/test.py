import os
import sys
import unittest
import filecmp

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

def cleanUp():
    try:
        os.remove("joined_1.csv")
    except FileNotFoundError as e:
        print(f"Cleanup after test failes: {os.strerror}")
        exit(1)

class HeaderTest(unittest.TestCase):
    def test_header_1(self):
        header = gen_header(ex2_left, ex2_right, "id")
        real_header = ["id", "firstname", "lastname", "email", "profession", "country", "city", "countrycode", "birthdate"]
        self.assertEqual(header, real_header)
    
    def test_header_2(self):
        header = gen_header(ex3_left, ex3_right, "cityId")
        real_header = ["id", "firstname", "lastname", "cityId", "cityName"]
        self.assertEqual(header, real_header)

class InnerJoinTest(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        cleanUp()

    def test_inner_join_1(self):
        ex1_res_inner = os.path.join("ex1", "ex1_res_inner.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "inner"]
        src_main()
        self.assertTrue(filecmp.cmp(ex1_res_inner, "joined_1.csv"))

    def test_inner_join_2(self):
        ex2_res_inner = os.path.join("ex2", "ex2_res_inner.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "inner"]
        src_main()
        self.assertTrue(filecmp.cmp(ex2_res_inner, "joined_1.csv"))

    def test_inner_join_3(self):
        ex3_res_inner = os.path.join("ex3", "ex3_res_inner.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "inner"]
        src_main()
        self.assertTrue(filecmp.cmp(ex3_res_inner, "joined_1.csv"))

class LeftJoinTest(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        cleanUp()

    def test_left_join_1(self):
        ex1_res_left = os.path.join("ex1", "ex1_res_left.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "left"]
        src_main()
        self.assertTrue(filecmp.cmp(ex1_res_left, "joined_1.csv"))

    def test_left_join_2(self):
        ex2_res_left = os.path.join("ex2", "ex2_res_left.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "left"]
        src_main()
        self.assertTrue(filecmp.cmp(ex2_res_left, "joined_1.csv"))

    def test_left_join_3(self):
        ex3_res_left = os.path.join("ex3", "ex3_res_left.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "left"]
        src_main()
        self.assertTrue(filecmp.cmp(ex3_res_left, "joined_1.csv"))

class RightJoinTest(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        cleanUp()

    def test_right_join_1(self):
        ex1_res_right = os.path.join("ex1", "ex1_res_right.csv")
        sys.argv = ["join", ex1_left, ex1_right, "id", "right"]
        src_main()
        self.assertTrue(filecmp.cmp(ex1_res_right, "joined_1.csv"))

    def test_right_join_2(self):
        ex2_res_right = os.path.join("ex2", "ex2_res_right.csv")
        sys.argv = ["join", ex2_left, ex2_right, "id", "right"]
        src_main()
        self.assertTrue(filecmp.cmp(ex2_res_right, "joined_1.csv"))

    def test_right_join_3(self):
        ex3_res_right = os.path.join("ex3", "ex3_res_right.csv")
        sys.argv = ["join", ex3_left, ex3_right, "cityId", "right"]
        src_main()
        self.assertTrue(filecmp.cmp(ex3_res_right, "joined_1.csv"))

if __name__ == "__main__":
    unittest.main()