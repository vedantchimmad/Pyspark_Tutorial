# Sample

---
* RDD.sample(), and RDD.takeSample() methods to get the random sampling subset from the large dataset,
>Syntax
> 
>sample(withReplacement, fraction, seed=None)

#### Fraction
* By using fraction between 0 to 1, it returns the approximate number of the fraction of the dataset. 
* For example, 0.1 returns 10% of the rows.
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

df=spark.range(100)
print(df.sample(0.06).collect())
```
#### Seed
* Every time you run a sample() function it returns a different set of sampling records, 
* however sometimes during the development and testing phase you may need to regenerate the same sample every time as you need to compare the results from your previous run.
```python
print(df.sample(0.1,123).collect())

print(df.sample(0.1,123).collect())

print(df.sample(0.1,456).collect())
```
* first 2 examples I have used seed value 123 hence the sampling results are the same and for the last example, 
* I have used 456 as a seed value generate different sampling records.

#### withReplacement
* some times you may need to get a random sample with repeated values. By using the value true, results in repeated values.
```python
print(df.sample(True,0.3,123).collect()) //with Duplicates

print(df.sample(0.3,123).collect()) // No duplicates
```


