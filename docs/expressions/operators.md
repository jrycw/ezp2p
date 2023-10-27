# Basic operators

## Setup
```python 
--8<-- "../src/python/expressions/operators.py:setup"
```

```python exec="on" session="expressions/operators"
--8<-- "../src/python/expressions/operators.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/operators.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/operators.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:df_pd"
    ```

## Numerical

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/operators.py:pl_numerical"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:pl_numerical"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/operators.py:pd_numerical"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:pd_numerical"
    ```

## Logical

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/operators.py:pl_logical"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:pl_logical"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/operators.py:pd_logical"
    ```

    ```python exec="on" result="text" session="expressions/operators"
    --8<-- "../src/python/expressions/operators.py:pd_logical"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/operators/).