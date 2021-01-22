from config import TreeConfig, GlobalConfig
from document import Document
from utils.random import Random

import os
import time
import pickle
from enum import Enum


class Fuzzer:
    def __init__(self, executor, manager):
        super().__init__()
        self.manager = manager
        self.executor = executor
        self.start_time = time.time()

    def generate_one(self):
        document = Document(Random.range(TreeConfig.min_element_count, TreeConfig.max_element_count))
        document.generate_nodes()
        document.generate_attributes()
        document.generate_css_rules()
        document.generate_js_functions()
        return document

    def generate_only(self, num):
        for i in range(num):
            print("Generating testcase #{}".format(i))
            document = self.generate_one()
            self.manager.save_testcase(document)
        print("Total {} testcases have been written to '{}'".format(num, os.path.abspath(self.manager.output_dir)))

