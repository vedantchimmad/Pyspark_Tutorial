# Date and Timestamp

---
* Most of all these functions accept input as, Date type, Timestamp type, or String. If a String used, it should be in a default format that can be cast to date.
* DateType default format is yyyy-MM-dd
* TimestampType default format is yyyy-MM-dd HH:mm:ss.SSSS
* Returns null if the input is a string that can not be cast to Date or Timestamp.
## PySpark SQL Date Functions
* The default format of the PySpark Date is yyyy-MM-dd.

 | PYSPARK DATE FUNCTION                           | 	DATE FUNCTION DESCRIPTION                                                                                                                                                                                                                                                                                                                                 |
  |-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | current_date()	                                 | Returns the current date as a date column.                                                                                                                                                                                                                                                                                                                 |
  | date_format(dateExpr,format)                    | 	Converts a date/timestamp/string to a value of string in the format specified by the date format given by the second argument.                                                                                                                                                                                                                            |
  | to_date()	                                      | Converts the column into `DateType` by casting rules to `DateType`.                                                                                                                                                                                                                                                                                        |
 | to_date(column, fmt)	                           | Converts the column into a `DateType` with a specified format                                                                                                                                                                                                                                                                                              |
  | add_months(Column, numMonths)                   | 	Returns the date that is `numMonths` after `startDate`.                                                                                                                                                                                                                                                                                                   |
  | date_add(column, days),date_sub(column, days)   | 	Returns the date that is `days` days after `start`                                                                                                                                                                                                                                                                                                        |
  | datediff(end, start)                            | 	Returns the number of days from `start` to `end`.                                                                                                                                                                                                                                                                                                         |
  | months_between(end, start)                      | 	Returns number of months between dates `start` and `end`. A whole number is returned if both inputs have the same day of month or both are the last day of their respective months. Otherwise, the difference is calculated assuming 31 days per month.                                                                                                   |
 | months_between(end, start, roundOff)	           | Returns number of months between dates `end` and `start`. If `roundOff` is set to true, the result is rounded off to 8 digits; it is not rounded otherwise.                                                                                                                                                                                                |
  | next_day(column, dayOfWeek)	                    | Returns the first date which is later than the value of the `date` column that is on the specified day of the week.For example, `next_day(‘2015-07-27’, “Sunday”)` returns 2015-08-02 because that is the first Sunday after 2015-07-27.                                                                                                                   |
  | trunc(column, format)	                          | Returns date truncated to the unit specified by the format.For example, `trunc(“2018-11-19 12:01:19”, “year”)` returns 2018-01-01 format: ‘year’, ‘yyyy’, ‘yy’ to truncate by year,‘month’, ‘mon’, ‘mm’ to truncate by month                                                                                                                               |
  | date_trunc(format, timestamp)                   | 	Returns timestamp truncated to the unit specified by the format.For example, `date_trunc(“year”, “2018-11-19 12:01:19”)` returns 2018-01-01 00:00:00 format: ‘year’, ‘yyyy’, ‘yy’ to truncate by year,‘month’, ‘mon’, ‘mm’ to truncate by month,‘day’, ‘dd’ to truncate by day, Other options are: ‘second’, ‘minute’, ‘hour’, ‘week’, ‘month’, ‘quarter’ |
  | year(column)	                                   | Extracts the year as an integer from a given date/timestamp/string                                                                                                                                                                                                                                                                                         |
  | quarter(column)                                 | 	Extracts the quarter as an integer from a given date/timestamp/string.                                                                                                                                                                                                                                                                                    |
  | month(column)	                                  | Extracts the month as an integer from a given date/timestamp/string                                                                                                                                                                                                                                                                                        |
 | dayofweek(column)	                              | Extracts the day of the week as an integer from a given date/timestamp/string. Ranges from 1 for a Sunday through to 7 for a Saturday                                                                                                                                                                                                                      |
  | dayofmonth(column)	                             | Extracts the day of the month as an integer from a given date/timestamp/string.                                                                                                                                                                                                                                                                            |
  | dayofyear(column)	                              | Extracts the day of the year as an integer from a given date/timestamp/string.                                                                                                                                                                                                                                                                             |
 | weekofyear(column)                              | 	Extracts the week number as an integer from a given date/timestamp/string. A week is considered to start on a Monday and week 1 is the first week with more than 3 days, as defined by ISO 8601                                                                                                                                                           |
 | last_day(column)	                               | Returns the last day of the month which the given date belongs to. For example, input “2015-07-27” returns “2015-07-31” since July 31 is the last day of the month in July 2015.                                                                                                                                                                           |
 | from_unixtime(column)	                          | Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp of that moment in the current system time zone in the yyyy-MM-dd HH:mm:ss format.                                                                                                                                                          |
| from_unixtime(column, f)                        | 	Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp of that moment in the current system time zone in the given format.                                                                                                                                                                       |
 | unix_timestamp()                                | 	Returns the current Unix timestamp (in seconds) as a long                                                                                                                                                                                                                                                                                                 |
 | unix_timestamp(column)                          | 	Converts time string in format yyyy-MM-dd HH:mm:ss to Unix timestamp (in seconds), using the default timezone and the default locale.                                                                                                                                                                                                                     |
 | unix_timestamp(column, p)                       | 	Converts time string with given pattern to Unix timestamp (in seconds).                                                                                                                                                                                                                                                                                   |
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create SparkSession
spark = SparkSession.builder \
            .appName('SparkByExamples.com') \
            .getOrCreate()
data=[["1","2020-02-01"],["2","2019-03-01"],["3","2021-03-01"]]
df=spark.createDataFrame(data,["id","input"])
df.show()
```
#### current_date()
* Use current_date() to get the current system date. 
* By default, the data will be returned in yyyy-dd-mm format.
```python
#current_date()
df.select(current_date().alias("current_date")
  ).show(1)
```
#### date_format()
* The below example uses date_format() to parses the date and converts from yyyy-dd-mm to MM-dd-yyyy format.
```python
#date_format()
df.select(col("input"), 
    date_format(col("input"), "MM-dd-yyyy").alias("date_format") 
  ).show()
```
#### to_date()
* Below example converts string in date format yyyy-MM-dd to a DateType yyyy-MM-dd using to_date().
```python
#to_date()
df.select(col("input"), 
    to_date(col("input"), "yyy-MM-dd").alias("to_date") 
  ).show()
```
#### datediff()
* The below example returns the difference between two dates using datediff().
```python
#datediff()
df.select(col("input"), 
    datediff(current_date(),col("input")).alias("datediff")  
  ).show()
```
#### months_between()
The below example returns the months between two dates using months_between().
```python
#months_between()
df.select(col("input"), 
    months_between(current_date(),col("input")).alias("months_between")  
  ).show()
```
#### trunc()
The below example truncates the date at a specified unit using trunc().
```python
#trunc()
df.select(col("input"), 
    trunc(col("input"),"Month").alias("Month_Trunc"), 
    trunc(col("input"),"Year").alias("Month_Year"), 
    trunc(col("input"),"Month").alias("Month_Trunc")
   ).show()
```
#### add_months() , date_add(), date_sub()
```python
#add_months() , date_add(), date_sub()
df.select(col("input"), 
    add_months(col("input"),3).alias("add_months"), 
    add_months(col("input"),-3).alias("sub_months"), 
    date_add(col("input"),4).alias("date_add"), 
    date_sub(col("input"),4).alias("date_sub") 
  ).show()
```
#### year(), month(), month(),next_day(), weekofyear()
```python
df.select(col("input"), 
     year(col("input")).alias("year"), 
     month(col("input")).alias("month"), 
     next_day(col("input"),"Sunday").alias("next_day"), 
     weekofyear(col("input")).alias("weekofyear") 
  ).show()
```
#### dayofweek(), dayofmonth(), dayofyear()
```python
df.select(col("input"),  
     dayofweek(col("input")).alias("dayofweek"), 
     dayofmonth(col("input")).alias("dayofmonth"), 
     dayofyear(col("input")).alias("dayofyear"), 
  ).show()
```
## Timestamp Functions

| PYSPARK TIMESTAMP FUNCTION SIGNATURE	 | TIMESTAMP FUNCTION DESCRIPTION                                          |
|---------------------------------------|-------------------------------------------------------------------------|
| current_timestamp ()	                 | Returns the current timestamp as a timestamp column                     |
| hour(column)	                         | Extracts the hours as an integer from a given date/timestamp/string.    |
| minute(column)                        | 	Extracts the minutes as an integer from a given date/timestamp/string. |
| second(column)                        | 	Extracts the seconds as an integer from a given date/timestamp/string. |
| to_timestamp(column)                  | 	Converts to a timestamp by casting rules to `TimestampType`.           |
| to_timestamp(column, fmt)             | 	Converts time string with the given pattern to timestamp               |
#### current_timestamp()
```python
data=[["1","02-01-2020 11 01 19 06"],["2","03-01-2019 12 01 19 406"],["3","03-01-2021 12 01 19 406"]]
df2=spark.createDataFrame(data,["id","input"])
df2.show(truncate=False)
```
```python
#current_timestamp()
df2.select(current_timestamp().alias("current_timestamp")
  ).show(1,truncate=False)
```
#### to_timestamp()
* Converts string timestamp to Timestamp type format.
```python
#to_timestamp()
df2.select(col("input"), 
    to_timestamp(col("input"), "MM-dd-yyyy HH mm ss SSS").alias("to_timestamp") 
  ).show(truncate=False)
```
#### hour(), Minute() and second()
```python
#hour, minute,second
data=[["1","2020-02-01 11:01:19.06"],["2","2019-03-01 12:01:19.406"],["3","2021-03-01 12:01:19.406"]]
df3=spark.createDataFrame(data,["id","input"])

df3.select(col("input"), 
    hour(col("input")).alias("hour"), 
    minute(col("input")).alias("minute"),
    second(col("input")).alias("second") 
  ).show(truncate=False)
```
