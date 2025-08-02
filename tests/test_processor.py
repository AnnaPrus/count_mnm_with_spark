import unittest
from pyspark.sql import SparkSession
from mnmcount.processor import aggregate_counts, filter_by_state

class ProcessorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()
        cls.sample_data = cls.spark.createDataFrame([
            ("CA", "Red", 10),
            ("CA", "Blue", 20),
            ("NV", "Red", 15),
            ("NV", "Blue", 5),
            ("CA", "Red", 5),
        ], ["State", "Color", "Count"])

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_aggregate_counts(self):
        result = aggregate_counts(self.sample_data).collect()
        expected = {("CA", "Blue", 20), ("CA", "Red", 15), ("NV", "Red", 15), ("NV", "Blue", 5)}
        actual = set((r['State'], r['Color'], r['TotalCount']) for r in result)
        self.assertEqual(actual, expected)

    def test_filter_by_state(self):
        result = filter_by_state(self.sample_data, "CA").collect()
        expected = {("CA", "Blue", 20), ("CA", "Red", 15)}
        actual = set((r['State'], r['Color'], r['TotalCount']) for r in result)
        self.assertEqual(actual, expected)
