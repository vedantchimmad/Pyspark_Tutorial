# Show

---
* PySpark DataFrame `show()` is used to display the contents of the DataFrame in a Table Row and Column Format.
* By default, it shows only 20 Rows, and the column values are truncated at 20 characters.

```python
# Default - displays 20 rows and
# 20 charactes from column value
df.show()

#Display full column contents
df.show(truncate=False)

# Display 2 rows and full column contents
df.show(2,truncate=False)

# Display 2 rows & column values 25 characters
df.show(2,truncate=25)

# Display DataFrame rows & columns vertically
df.show(n=3,truncate=25,vertical=True)
```
