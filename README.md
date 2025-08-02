# Local Apache Spark Setup for CSV Processing with PySpark

This repo shows how to set up Apache Spark locally and run a Python script using PySpark to read and manipulate CSV data.

---
### 📁 Project Structure

```text
mnmcount/
├── data/                     # the CSV file 
├── mnmcount/                 
│   ├── __init__.py
│   ├── processor.py          # Main logic (data loading, aggregation)
│   └── cli.py                # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_processor.py     # Unit tests for processor functions
├── requirements.txt          # Python dependencies
└── spark_submit_entry.py     # Entry point for spark-submit

```
---
## Prerequisites

- Java (version 8 or 17)
- Python 3.6+
- Apache Spark (local installation)
- PySpark Python package (`pip install pyspark`)

---

## Setup

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

## Usage

1. Go to the reposictory where the project is located and run the python script 
```python
spark-submit mnmcount/cli.py data/dataset.csv
```
2. Run unit tests using
```python
python -m unittest discover tests
```
3. Or use pytest for better output:
```python
pip install pytest
pytest tests/
```


