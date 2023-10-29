# Structs
While `Struct` is a unique feature in `Polars`, emulating its behavior in `Pandas` might initially feel unfamiliar. Nonetheless, I made an effort to replicate this functionality in `Pandas` to appreciate its elegance.

## Setup

```python 
--8<-- "../src/python/expressions/structs.py:setup"
```

```python exec="on" session="expressions/structs"
--8<-- "../src/python/expressions/structs.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:df_pd"
    ```

## Encountering the `Struct` type

### Nested `Struct`
=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pl_value_counts"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pl_value_counts"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pd_value_counts"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pd_value_counts"
    ```

### Unnested `Struct`
=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pl_value_counts_unnest"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pl_value_counts_unnest"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pd_value_counts_unnest"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pd_value_counts_unnest"
    ```

## Identifying duplicate rows
=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pl_ident_dups"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pl_ident_dups"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pd_ident_dups"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pd_ident_dups"
    ```

## Multi-column ranking
=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pl_multi_col_ranking"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pl_multi_col_ranking"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/structs.py:pd_multi_col_ranking"
    ```

    ```python exec="on" result="text" session="expressions/structs"
    --8<-- "../src/python/expressions/structs.py:pd_multi_col_ranking"
    ```


## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/structs/).