from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

def load_data(spark: SparkSession, file_path: str):
    return (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(file_path))

def aggregate_counts(df):
    return (df.select("State", "Color", "Count")
              .groupBy("State", "Color")
              .agg(_sum("Count").alias("TotalCount"))
              .orderBy("TotalCount", ascending=False))

def filter_by_state(df, state_code: str):
    return (df.filter(df.State == state_code)
              .groupBy("State", "Color")
              .agg(_sum("Count").alias("TotalCount"))
              .orderBy("TotalCount", ascending=False))
