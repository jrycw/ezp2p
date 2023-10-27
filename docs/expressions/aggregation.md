# Aggregation

## Setup
```python 
--8<-- "../src/python/expressions/aggregation.py:setup"
```

```python exec="on" session="expressions/aggregation"
--8<-- "../src/python/expressions/aggregation.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:df_pd"
    ```

## Basic aggregations

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pl_basic_agg"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pl_basic_agg"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pd_basic_agg"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pd_basic_agg"
    ```

## Conditionals

### Type 1
While the `pro` column is correctly sorted in `Pandas`, the order of the `state` and `anti` columns does not entirely match the result in `Polars`.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pl_cond_type1"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pl_cond_type1"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pd_cond_type1"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pd_cond_type1"
    ```

### Type 2

While the `count` column is correctly sorted in `Pandas`, the order of the `state` and `party` columns does not entirely match the result in `Polars`.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pl_cond_type2"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pl_cond_type2"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pd_cond_type2"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pd_cond_type2"
    ```

## Filtering

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pl_filter"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pl_filter"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pd_filter"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pd_filter"
    ```


## Sorting

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pl_sort"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pl_sort"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/aggregation.py:pd_sort"
    ```

    ```python exec="on" result="text" session="expressions/aggregation"
    --8<-- "../src/python/expressions/aggregation.py:pd_sort"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/aggregation/).