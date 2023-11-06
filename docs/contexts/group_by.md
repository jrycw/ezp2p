# df.group_by().agg()
`df.group_by(..).agg([..])` groups specific columns and performs parallel aggregations.

## Setup
```python 
--8<-- "../src//python/contexts/group_by.py:setup"
```

```python exec="on" session="contexts/group_by"
--8<-- "../src//python/contexts/group_by.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src//python/contexts/group_by.py:df_pl"
    ```

    ```python exec="on" result="text" session="contexts/group_by"
    --8<-- "../src//python/contexts/group_by.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src//python/contexts/group_by.py:df_pd"
    ```

    ```python exec="on" result="text" session="contexts/group_by"
    --8<-- "../src//python/contexts/group_by.py:df_pd"
    ```

## Example
`df.group_by(..).agg(..)` behaves similarly to `df.groupby(..).agg(..)` in `Pandas`. In `Polars`, aggregation is primarily achieved through `expressions`, whereas `Pandas` relies on the provided methods of the grouper object.

=== "Polars"
    ```python 
    --8<-- "../src//python/contexts/group_by.py:pl_example"
    ```

    ```python exec="on" result="text" session="contexts/group_by"
    --8<-- "../src//python/contexts/group_by.py:pl_example"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src//python/contexts/group_by.py:pd_example"
    ```

    ```python exec="on" result="text" session="contexts/group_by"
    --8<-- "../src//python/contexts/group_by.py:pd_example"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/concepts/contexts/#group-by-aggregation).