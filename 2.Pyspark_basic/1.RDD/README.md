# 🔹 RDD (Resilient Distributed Dataset) in PySpark

---
### 📘 What is an RDD?

RDD stands for **Resilient Distributed Dataset**, the **core data structure** of Apache Spark.  
It is an immutable, distributed collection of objects that can be processed in parallel.

---

### 💡 Key Properties

| Property       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Resilient**  | Fault-tolerant and can recover from node failures using lineage information |
| **Distributed**| Data is split across multiple nodes in the cluster                          |
| **Immutable**  | Once created, it cannot be modified                                          |
| **Lazy Eval**  | Transformations are lazy — computed only when an action is called           |

## 🔧 How to Create RDDs

### ✅ 1. From a Python Collection

```python
from pyspark import SparkContext

sc = SparkContext.getOrCreate()

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
```
### ✅ 2. From External File
```python
rdd = sc.textFile("data.txt")
```
### 🔄 RDD Transformations (Lazy)
| Transformation  | Description                                              | Example                            |
| --------------- | -------------------------------------------------------- | ---------------------------------- |
| `map(func)`     | Returns a new RDD by applying a function to each element | `rdd.map(lambda x: x * 2)`         |
| `filter(func)`  | Filters elements matching the condition                  | `rdd.filter(lambda x: x > 3)`      |
| `flatMap(func)` | Similar to `map`, but flattens results                   | `rdd.flatMap(lambda x: x.split())` |
| `distinct()`    | Removes duplicates                                       | `rdd.distinct()`                   |
| `union(other)`  | Combines two RDDs                                        | `rdd1.union(rdd2)`                 |

### ⚡ RDD Actions (Trigger Execution)
| Action         | Description                        | Example                          |
| -------------- | ---------------------------------- | -------------------------------- |
| `collect()`    | Returns all elements to driver     | `rdd.collect()`                  |
| `count()`      | Returns number of elements         | `rdd.count()`                    |
| `first()`      | Returns first element              | `rdd.first()`                    |
| `take(n)`      | Returns first `n` elements         | `rdd.take(3)`                    |
| `reduce(func)` | Aggregates elements using function | `rdd.reduce(lambda x, y: x + y)` |

### 🔍 Example: Transformation & Action
```python
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Transformation
mapped_rdd = rdd.map(lambda x: x * x)

# Action
result = mapped_rdd.collect()
print(result)  # Output: [1, 4, 9, 16, 25]
```
### 🧠 When to Use RDD?
| Use Case                                 | Why RDD?                             |
| ---------------------------------------- | ------------------------------------ |
| Low-level transformations/control needed | Gives full control over computation  |
| Unstructured/complex data processing     | More flexible than DataFrames        |
| Custom partitioning                      | RDDs allow user-defined partitioning |
| Functional-style programming preference  | Supports map/filter/reduce natively  |

### 🔄 Convert Between RDD and DataFrame
```python
# RDD to DataFrame
rdd = sc.parallelize([(1, "Alice"), (2, "Bob")])
df = rdd.toDF(["id", "name"])

# DataFrame to RDD
rdd2 = df.rdd
```