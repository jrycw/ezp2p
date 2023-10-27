# Functions

## Setup
```python 
--8<-- "../src/python/expressions/functions.py:setup"
```

```python exec="on" session="expressions/functions"
--8<-- "../src/python/expressions/functions.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/functions.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/functions.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:df_pd"
    ```

## Column naming

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pl_col_naming"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pl_col_naming"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pd_col_naming"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pd_col_naming"
    ```

## Count unique values
In `Pandas`, it appears that there is no built-in method for approximating the count of unique values.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pl_unique_values"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pl_unique_values"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pd_unique_values"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pd_unique_values"
    ```

## Conditionals

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pl_conditionals"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pl_conditionals"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/functions.py:pd_conditionals"
    ```

    ```python exec="on" result="text" session="expressions/functions"
    --8<-- "../src/python/expressions/functions.py:pd_conditionals"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/functions/).