import os
import sys
import unittest

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from src.main import main as src_main

def main():

    return 0