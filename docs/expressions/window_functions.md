# Window functions

## Setup
```python 
--8<-- "../src/python/expressions/window_functions.py:setup"
```

```python exec="on" session="expressions/window_functions"
--8<-- "../src/python/expressions/window_functions.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:df_pd"
    ```

## Group by aggregations in selection

To ensure comparable results between `Polars` and `Pandas` in `Type 2`, it's necessary to handle `NaN` values. We can achieve this by filling the `NaN` values with a specified `placeholder` in `Pandas`.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pl_group_by_aggs_in_selection"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pl_group_by_aggs_in_selection"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pd_group_by_aggs_in_selection"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pd_group_by_aggs_in_selection"
    ```

## Operations per group

To achieve consistent results between `Polars` and `Pandas`, a trick is employed: duplicate a dummy column from `Type 1` to use as the `by` parameter in the `groupby(by=..)` operation in `Pandas`.

This version maintains clarity while shortening the sentence slightly.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pl_op_per_group"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pl_op_per_group"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pd_op_per_group"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pd_op_per_group"
    ```



## One more Example

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pl_example"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pl_example"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/window_functions.py:pd_example"
    ```

    ```python exec="on" result="text" session="expressions/window_functions"
    --8<-- "../src/python/expressions/window_functions.py:pd_example"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/window/).