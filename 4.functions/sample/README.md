# 📌 PySpark Sampling

---

## 🔹 Overview
In PySpark, **sampling** is used to extract a random subset of data from a larger dataset without processing the entire dataset.

There are two main methods:
1. **`RDD.sample()`** → Returns a sampled subset as an RDD.
2. **`RDD.takeSample()`** → Returns a fixed-size random sample as a Python list.

---

## 🔹 Syntax

### 1️⃣ `sample()`  
```python
RDD.sample(withReplacement, fraction, seed=None)
````

| Parameter           | Description                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| **withReplacement** | `True` → Sampling with replacement (same element can appear multiple times), `False` → Without replacement. |
| **fraction**        | Fraction of the dataset to sample (e.g., `0.1` → 10%).                                                      |
| **seed**            | Optional integer for reproducible results.                                                                  |

---

### 2️⃣ `takeSample()`

```python
RDD.takeSample(withReplacement, num, seed=None)
```

| Parameter           | Description                                |
| ------------------- | ------------------------------------------ |
| **withReplacement** | Same as above.                             |
| **num**             | Number of elements to return.              |
| **seed**            | Optional integer for reproducible results. |

---

## 🔹 Example: `sample()`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SampleExample").getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 21))

# 30% sample without replacement
sample_rdd = rdd.sample(False, 0.3, seed=42)
print("Sample Data (RDD):", sample_rdd.collect())
```

---

## 🔹 Example: `takeSample()`

```python
# Take 5 random elements without replacement
sample_list = rdd.takeSample(False, 5, seed=42)
print("Sample Data (List):", sample_list)
```

---

## 🔹 Output (Sample)

```
Sample Data (RDD): [1, 6, 8, 14, 17, 19]
Sample Data (List): [1, 6, 8, 14, 17]
```

---

✅ **Summary**

* **`sample()`** → returns an **RDD** with a given fraction of data.
* **`takeSample()`** → returns a **list** with a fixed number of elements.
* **`seed`** makes results deterministic for reproducibility.

