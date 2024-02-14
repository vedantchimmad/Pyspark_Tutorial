# Aggregate

---
* when we need to make aggregate operations on DataFrame columns. 
* Aggregate functions operate on a group of rows and calculate a single return value for every group.
* PySpark SQL Aggregate functions are grouped as “agg_funcs” in Pyspark. Below is a list of functions defined under this group. 
```python
simpleData = [("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("James", "Sales", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000),
    ("Saif", "Sales", 4100)
  ]
schema = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)
```
#### approx_count_distinct Aggregate Function
* approx_count_distinct() function returns the count of distinct items in a group.
```python
print("approx_count_distinct: " + \
      str(df.select(approx_count_distinct("salary")).collect()[0][0]))
```
#### avg (average) Aggregate Function
* avg() function returns the average of values in the input column.
```python
# avg
print("avg: " + str(df.select(avg("salary")).collect()[0][0]))
```
#### collect_list Aggregate Function
* collect_list() function returns all values from an input column with duplicates.
```python
# collect_list
df.select(collect_list("salary")).show(truncate=False)
```
#### collect_list
* df.select(collect_list("salary")).show(truncate=False)
```python

# collect_set
df.select(collect_set("salary")).show(truncate=False)
```
#### countDistinct Aggregate Function
countDistinct() function returns the number of distinct elements in a columns
```python
# countDistinct
df2 = df.select(countDistinct("department", "salary"))
df2.show(truncate=False)
print("Distinct Count of Department & Salary: "+str(df2.collect()[0][0]))
```
#### count function
count() function returns number of elements in a column.
```python
print("count: "+str(df.select(count("salary")).collect()[0]))
```
#### first function
first() function returns the first element in a column when ignoreNulls is set to true, it returns the first non-null element.
```python
# first
df.select(first("salary")).show(truncate=False)
```
#### last function
last() function returns the last element in a column. when ignoreNulls is set to true, it returns the last non-null element.
```python
# last
df.select(last("salary")).show(truncate=False)
```
#### kurtosis function
kurtosis() function returns the kurtosis of the values in a group.
```python
df.select(kurtosis("salary")).show(truncate=False)
```
#### max function
max() function returns the maximum value in a column.
```python
df.select(max("salary")).show(truncate=False)
```
#### min function
* min() function returns the minimum value in a column.
```python
df.select(min("salary")).show(truncate=False)
```
#### Mean()
*function returns the average of the values in a column. Alias for Avg
```python
df.select(mean("salary")).show(truncate=False)
```
#### Skewness()
* function returns the skewness of the values in a group.
```python
df.select(skewness("salary")).show(truncate=False)
```
#### Stddev(),stddev_samp() & stddev_pop()
* stddev() alias for stddev_samp.
* stddev_samp() function returns the sample standard deviation of values in a column.
* stddev_pop() function returns the population standard deviation of the values in a column.
```python
df.select(stddev("salary"), stddev_samp("salary"), \
stddev_pop("salary")).show(truncate=False)
```
#### sum()
* function Returns the sum of all values in a column.
```python
df.select(sum("salary")).show(truncate=False)
```
#### sumDistinct()
* function returns the sum of all distinct values in a column.
```python
df.select(sumDistinct("salary")).show(truncate=False)
```
