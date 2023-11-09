# Missing data

In `Polars`, missing data is consistently represented as a `null` value. Additionally, `Polars` permits the use of `Not a Number` or `NaN` values for float columns. It's important to avoid conflating these two concepts.

## Setup
```python 
--8<-- "../src/python/expressions/missing_data.py:setup"
```

```python exec="on" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pl"
    ```

=== "Pandas_df"
    Please note that `col2` is of data type `float64` due to the presence of a `NaN` value.

    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pd"
    ```

## Missing data metadata

### Is a missing value

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_isnull"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_isnull"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_isna"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_isna"
    ```

### Count the missing values
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_null_count"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_null_count"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_na_count"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_na_count"
    ```

## Filling missing data

### Fill with specified literal value
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_literal"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_literal"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_literal"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_literal"
    ```

### Fill with a strategy
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_strategy"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_strategy"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_strategy"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_strategy"
    ```


### Fill with an expression
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_median"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_median"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_median"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_median"
    ```

### Fill with interpolation
=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_interpolation"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_fill_interpolation"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_interpolation"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pd_fill_interpolation"
    ```

## NaN values
Similar to the `null` value, `Polars` has `is_nan` and `fill_nan` to work with the `NaN` value. However, it should be noted that there is no `nan_count` in `Polars`.

These `NaN` values can be created from Numpy's `np.nan` or the native python `float('nan')`.

```python 
--8<-- "../src/python/expressions/missing_data.py:pl_nan_setup"
```

```python exec="on" result="text" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:pl_nan_setup"
```


### Is a `NaN` value
```python 
--8<-- "../src/python/expressions/missing_data.py:pl_isna"
```

```python exec="on" result="text" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:pl_isna"
```

### Count the `NaN` values
```python 
--8<-- "../src/python/expressions/missing_data.py:pl_nan_count"
```

```python exec="on" result="text" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:pl_nan_count"
```

### Filling NaN
```python 
--8<-- "../src/python/expressions/missing_data.py:pl_nan_fill_literal"
```

```python exec="on" result="text" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:pl_nan_fill_literal"
```

### Calculating the mean and median values
When calculating the mean or median of a column with `NaN` values, the result will be `NaN`. To change this behavior, replace `NaN` values with `null` values. With this change, `null` values will be excluded when calculating the mean or median of a column.

=== "Default behaviour"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_nan_mean"
    ```

    One trick to change this behaviour is to replace the `NaN` values with `null` values

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_nan_mean"
    ```

=== "Replace `NaN` values with `null` values"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:pl_nan_mean_fill_null"
    ```


    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:pl_nan_mean_fill_null"
    ```

## pd.NaT
It's worth noting that `Pandas` has a special [`pd.NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT), which serves as the time equivalent of `NaN`.

```python 
--8<-- "../src/python/expressions/missing_data.py:pd_nat"
```

```python exec="on" result="text" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:pd_nat"
```

## More about filling with interpolation
While `Polars` provides `linear` and `nearest` interpolation strategies, `Pandas` offers a broader range.

```python 
--8<-- "../src/python/expressions/missing_data.py:setup2"
```

```python exec="on" session="expressions/missing_data"
--8<-- "../src/python/expressions/missing_data.py:setup2"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pl2"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pl2"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pd2"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pd2"
    ```

Several interpolation methods in `df.interpolation` of `Pandas` are adopted from the `SciPy` package.

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pl_more_interp"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pl_more_interp"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/missing_data.py:df_pd_more_interp"
    ```

    ```python exec="on" result="text" session="expressions/missing_data"
    --8<-- "../src/python/expressions/missing_data.py:df_pd_more_interp"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/null/).