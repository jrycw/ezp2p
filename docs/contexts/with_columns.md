# df.with_columns()
`df.with_columns([..])` allows you to create new columns in parallel. Unlike `df.select([..])`, it adds the newly created columns to the original dataframe instead of dropping them.

## Setup
```python 
--8<-- "../src/python/contexts/with_columns.py:setup"
```

```python exec="on" session="contexts/with_columns"
--8<-- "../src/python/contexts/with_columns.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/contexts/with_columns.py:df_pl"
    ```

    ```python exec="on" result="text" session="contexts/with_columns"
    --8<-- "../src/python/contexts/with_columns.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/contexts/with_columns.py:df_pd"
    ```

    ```python exec="on" result="text" session="contexts/with_columns"
    --8<-- "../src/python/contexts/with_columns.py:df_pd"
    ```

## Example
The behavior of `df.with_columns([..])` can be treated as `df.assign(..)` in `Pandas`.

=== "Polars"
    ```python 
    --8<-- "../src/python/contexts/with_columns.py:pl_example"
    ```

    ```python exec="on" result="text" session="contexts/with_columns"
    --8<-- "../src/python/contexts/with_columns.py:pl_example"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/contexts/with_columns.py:pd_example"
    ```

    ```python exec="on" result="text" session="contexts/with_columns"
    --8<-- "../src/python/contexts/with_columns.py:pd_example"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/concepts/contexts/#select).
