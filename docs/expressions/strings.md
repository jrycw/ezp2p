# Strings

## Setup

```python 
--8<-- "../src/python/expressions/strings.py:setup"
```

```python exec="on" session="expressions/strings"
--8<-- "../src/python/expressions/strings.py:setup"
```

## Check for existence of a pattern

```python 
--8<-- "../src/python/expressions/strings.py:setup1"
```

```python exec="on" session="expressions/strings"
--8<-- "../src/python/expressions/strings.py:setup1"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl1"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl1"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd1"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd1"
    ```


=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl_check_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl_check_pattern"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd_check_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd_check_pattern"
    ```

There's a slight difference in syntax between `Polars` and `Pandas` when it comes to methods for checking whether the start and end of each string element matches a given pattern.

* In `Polars`, you use `pl.col(..).str.starts_with(..)` and `pl.col(..).str.ends_with(..)`.
* In `Pandas`, the equivalent methods are `pd.Series.str.startswith(..)` and `pd.Series.str.endswith(..)`.

## Extract a pattern

```python 
--8<-- "../src/python/expressions/strings.py:setup2"
```

```python exec="on" session="expressions/strings"
--8<-- "../src/python/expressions/strings.py:setup2"
```


=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl2"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl2"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd2"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd2"
    ```

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl_extract_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl_extract_pattern"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd_extract_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd_extract_pattern"
    ```

## Extract all occurrences of a pattern

```python 
--8<-- "../src/python/expressions/strings.py:setup3"
```

```python exec="on" session="expressions/strings"
--8<-- "../src/python/expressions/strings.py:setup3"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl3"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl3"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd3"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd3"
    ```


=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl_extract_all_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl_extract_all_pattern"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd_extract_all_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd_extract_all_pattern"
    ```

## Replace a pattern

```python 
--8<-- "../src/python/expressions/strings.py:setup4"
```

```python exec="on" session="expressions/strings"
--8<-- "../src/python/expressions/strings.py:setup4"
```


=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl4"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl4"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd4"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd4"
    ```


=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pl_replace_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pl_replace_pattern"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/strings.py:df_pd_replace_pattern"
    ```

    ```python exec="on" result="text" session="expressions/strings"
    --8<-- "../src/python/expressions/strings.py:df_pd_replace_pattern"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/strings/).