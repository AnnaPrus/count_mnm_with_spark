import sys
import time
from pyspark.sql import SparkSession
from mnmcount.processor import load_data, aggregate_counts, filter_by_state

def main():
    if len(sys.argv) != 2:
        print("Usage: spark-submit cli.py <file_path>", file=sys.stderr)
        sys.exit(-1)

    file_path = sys.argv[1]

    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()

    df = load_data(spark, file_path)
    df.show(5, truncate=False)

    total_counts = aggregate_counts(df)
    total_counts.show(60, truncate=False)
    print("Total Rows = %d" % total_counts.count())

    ca_counts = filter_by_state(df, "CA")
    ca_counts.show(10, truncate=False)

    print("Sleeping to keep Spark UI alive...")
    time.sleep(600)

if __name__ == "__main__":
    main()
