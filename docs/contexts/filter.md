# pl.filter()
`pl.filter([..])` selects rows based on the given conditions.

## Setup
```python 
--8<-- "../src//python/contexts/filter.py:setup"
```

```python exec="on" session="contexts/filter"
--8<-- "../src//python/contexts/filter.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src//python/contexts/filter.py:df_pl"
    ```

    ```python exec="on" result="text" session="contexts/filter"
    --8<-- "../src//python/contexts/filter.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src//python/contexts/filter.py:df_pd"
    ```

    ```python exec="on" result="text" session="contexts/filter"
    --8<-- "../src//python/contexts/filter.py:df_pd"
    ```

## Example
The behavior of `pl.filter([..])` can be treated as `df.query(..)` in `Pandas`.

=== "Polars"
    ```python 
    --8<-- "../src//python/contexts/filter.py:pl_example"
    ```

    ```python exec="on" result="text" session="contexts/filter"
    --8<-- "../src//python/contexts/filter.py:pl_example"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src//python/contexts/filter.py:pd_example"
    ```

    ```python exec="on" result="text" session="contexts/filter"
    --8<-- "../src//python/contexts/filter.py:pd_example"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/concepts/contexts/#filter).