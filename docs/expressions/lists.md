# List

## Powerful List manipulation

### Setup
```python 
--8<-- "../src/python/expressions/lists.py:setup1"
```

```python exec="on" session="expressions/lists"
--8<-- "../src/python/expressions/lists.py:setup1"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/lists.py:df_pl1"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:df_pl1"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/lists.py:df_pd1"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:df_pd1"
    ```

### Creating a List column

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pl_create_list_col"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pl_create_list_col"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pd_create_list_col"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pd_create_list_col"
    ```

### Operating on List columns

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pl_col_list"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pl_col_list"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pd_col_list"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pd_col_list"
    ```

### Element-wise computation within Lists

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pl_col_list_elem"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pl_col_list_elem"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pd_col_list_elem"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pd_col_list_elem"
    ```

## Row-wise computations

```python 
--8<-- "../src/python/expressions/lists.py:setup2"
```

```python exec="on" session="expressions/lists"
--8<-- "../src/python/expressions/lists.py:setup2"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/lists.py:df_pl2"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:df_pl2"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/lists.py:df_pd2"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:df_pd2"
    ```
    
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pl_col_list_row"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pl_col_list_row"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/lists.py:pd_col_list_row"
    ```

    ```python exec="on" result="text" session="expressions/lists"
    --8<-- "../src/python/expressions/lists.py:pd_col_list_row"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/lists/).