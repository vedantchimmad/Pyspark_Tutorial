# 💥 `explode` in PySpark

---

## 📝 Overview
The `explode` function transforms each element of an **array** or each key-value pair of a **map** into a separate row.  
It is often used to **flatten** nested data structures.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
explode(column)
```

| Parameter | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| `column`  | **Required**. Column containing an array or map to expand into multiple rows. |

**Return Type:**

* If array → element type of array
* If map → struct with `key` and `value` columns

---

## 🎯 Example 1: Exploding an Array

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ExplodeExample").getOrCreate()

# Sample Data
data = [("A", ["x", "y", "z"]),
        ("B", ["p", "q"])]

df = spark.createDataFrame(data, ["id", "letters"])

# Explode array
result = df.withColumn("letter", F.explode("letters"))

result.show()
```

**Output:**

```
+---+---------+------+
|id |letters  |letter|
+---+---------+------+
|A  |[x, y, z]|x     |
|A  |[x, y, z]|y     |
|A  |[x, y, z]|z     |
|B  |[p, q]   |p     |
|B  |[p, q]   |q     |
+---+---------+------+
```

---

## 🎯 Example 2: Exploding a Map

```python
data = [("A", {"x": 1, "y": 2}),
        ("B", {"p": 3})]

df = spark.createDataFrame(data, ["id", "map_col"])

result = df.withColumn("kv", F.explode("map_col"))

result.select("id", "kv.key", "kv.value").show()
```

**Output:**

```
+---+---+-----+
|id |key|value|
+---+---+-----+
|A  |x  |1    |
|A  |y  |2    |
|B  |p  |3    |
+---+---+-----+
```

---

## 🎯 Example 3: Flattening Nested Arrays

```python
nested_data = [("A", [["x", "y"], ["z"]])]

df = spark.createDataFrame(nested_data, ["id", "nested_arr"])

flattened = df.withColumn("inner_arr", F.explode("nested_arr")) \
              .withColumn("element", F.explode("inner_arr"))

flattened.show()
```

**Output:**

```
+---+----------+---------+-------+
|id |nested_arr|inner_arr|element|
+---+----------+---------+-------+
|A  |[[x, y], [z]]|[x, y]|x      |
|A  |[[x, y], [z]]|[x, y]|y      |
|A  |[[x, y], [z]]|[z]   |z      |
+---+----------+---------+-------+
```

---

## 🖼 Visual Representation

**Before:**

```
Row 1 → id=A, letters=[x, y, z]
Row 2 → id=B, letters=[p, q]
```

**After explode:**

```
Row 1 → id=A, letter=x
Row 2 → id=A, letter=y
Row 3 → id=A, letter=z
Row 4 → id=B, letter=p
Row 5 → id=B, letter=q
```

---

## 🔍 Key Points

* Use **`explode_outer`** if you want to keep rows with null or empty arrays (otherwise they are removed).
* When applied to a map, output is a struct with `key` and `value`.
* Can be chained to flatten multiple levels of nesting.

