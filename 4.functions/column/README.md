# Column function

---
Create Dataframe
```python
data=[("James","Bond","100",None),
      ("Ann","Varsa","200",'F'),
      ("Tom Cruise","XXX","400",''),
      ("Tom Brand",None,"400",'M')] 
columns=["fname","lname","id","gender"]
df=spark.createDataFrame(data,columns)
```
1. **alias()** :`alias()` is a function of the Column to give alternate name.
   ```python
   from pyspark.sql.functions import expr
   
   df.select(df.fname.alias("first_name"), \
   df.lname.alias("last_name")
   ).show()```
2. **asc() and dsc()** : asc, desc to sort ascending and descending order repsectively.
```python
df.sort(df.fname.asc()).show()
df.sort(df.fname.desc()).show()
```
3.	**cast()** : Used to convert the data Type.
```python
df.select(df.fname,df.id.cast("int")).printSchema()
```
4.	**between()** : Check values between
```python
df.filter(df.id.between(100,300)).show()
```
5.	**contains()** :  DataFrame column value contains a string value specified in this function.
```python
df.filter(df.fname.contains("Cruise")).show()
```
6.	**startswith() & endswith()** : startsWith() filters rows where a specified substring exists at the beginning while endsWith() filter rows where the specified substring presents at the end.
```python
df.filter(df.fname.startswith("T")).show()
df.filter(df.fname.endswith("Cruise")).show()
```
7.	**isNull() and isNotNull()** : Checks if the DataFrame column has NULL or non NULL values.
```python
df.filter(df.lname.isNull()).show()
df.filter(df.lname.isNotNull()).show()
```
8.	**like()** : Similar to SQL LIKE expression
```python
df.select(df.fname,df.lname,df.id) \
.filter(df.fname.like("%om"))
```
9.	**substr()** : Returns a Column after getting sub string from the Column
```python
 df.select(df.fname.substr(1,2).alias("substr")).show()
```
10.	**when() & otherwise()** : It is similar to SQL Case When, executes sequence of expressions until it matches the condition and returns a value when match.
```python
 from pyspark.sql.functions import when
       df.select(df.fname,df.lname,when(df.gender=="M","Male") \
       .when(df.gender=="F","Female") \
       .when(df.gender==None ,"") \
       .otherwise(df.gender).alias("new_gender") \
       ).show()
```
11.	**isin()** : Check if the value is present in list
```python
li=["100","200"]
df.select(df.fname,df.lname,df.id) \
.filter(df.id.isin(li)) \
.show()
```


