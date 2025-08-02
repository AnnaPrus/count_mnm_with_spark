# Local Apache Spark Setup for CSV Processing with PySpark

This repo shows how to set up Apache Spark locally and run a Python script using PySpark to read and manipulate CSV data.

---

## Prerequisites

- Java (version 8 or 17)
- Python 3.6+
- Apache Spark (local installation)
- PySpark Python package (`pip install pyspark`)

---

## Setup & Usage

1. **Install Java**  
Make sure Java is installed and available in your terminal:

```bash
java -version
```
2. Download and extract Apache Spark
Download Spark from https://spark.apache.org/downloads.html, extract it (e.g., ~/spark).

3. (Optional) Set environment variables
Add these lines to your shell profile (~/.bashrc or ~/.zshrc):

```bash
export SPARK_HOME=~/spark
export PATH=$SPARK_HOME/bin:$PATH
```
Reload profile with source ~/.zshrc

4. Install PySpark
   
```bash
pip install pyspark
```
5. Go to the reposictory where the project is located and run the python script 
```python
spark-submit mnmcount.py data/dataset.csv
```



<pre> mnmcount/ ├── data/ # Your CSV files (e.g., mnm_data_2025.csv) ├── mnmcount/ │ ├── __init__.py │ ├── processor.py # Main logic (data loading, aggregation) │ └── cli.py # Command-line interface ├── tests/ │ ├── __init__.py │ └── test_processor.py # Unit tests for processor functions ├── requirements.txt # Python dependencies └── spark_submit_entry.py # Optional: Entry point for spark-submit </pre>
