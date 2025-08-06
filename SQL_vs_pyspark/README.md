#  SQL VS Pyspark

| SQL      | Pyspark     | module                                      | Return                       | SQL ex                                                         | Pyspark ex                                                 |
|----------|-------------|---------------------------------------------|------------------------------|----------------------------------------------------------------|------------------------------------------------------------|
| SELECT   | select()    | NA                                          | Row                          | SELECT first_name FROM patients                                | df.select(df.first_name).show()                            |
| WHERE    | filter()    | NA                                          | filtered row                 | SELECT first_name FROM patients WHERE first_name="Vedant"      | df.filter(df.first_name=="Vedant").show                    |
| BETWEEN  | between()   | NA                                          | rows between                 | SELECT * FROM Products WHERE Price BETWEEN 10 AND 20           | df.filter(df.Price.between(10,20).show()                   |
| CONCAT() | concat()    | from pyspark.sql.functions import concat    | combine rows without space   | SELECT CONCAT(first_name,last_name) FROM  patients             | df.select(concat(df.first_name,df.last_name).show()        |
| CONCAT() | concat_ws() | from pyspark.sql.functions import concat_ws | Combine rows with charecter  | SELECT CONCAT(first_name,"_",last_name) FROM  patients         | df.select("_",concat_ws(df.first_name,df.last_name).show() |
| MAX()    | max()       | from pyspark.sql.functions import max       | Return max value             | SELECT first_name,last_name,max(height) FROM patients          | df.select(max(df.height).alias("max_height").show()        |
| IN       | isin()      | NA                                          | Return values present in it  | SELECT * FROM patients where patient_id in (1,45,534,879,1000) | df.filter(df.patient_id.isin(1,45,534,879,1000)            |
