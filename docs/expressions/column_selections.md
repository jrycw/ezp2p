# Column selections

## Setup
```python 
--8<-- "../src/python/expressions/column_selections.py:setup"
```

```python exec="on" session="expressions/column_selections"
--8<-- "../src/python/expressions/column_selections.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:df_pd"
    ```
## Expression expansion

### Select all

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_select_all"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_select_all"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_select_all"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_select_all"
    ```

### Exclude

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_exclude"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_exclude"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_exclude"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_exclude"
    ```

### By multiple strings

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_multi_strings"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_multi_strings"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_multi_strings"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_multi_strings"
    ```

    If there are dozens of columns that need manipulation, I will use the following approach instead.

    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_multi_strings2"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_multi_strings2"
    ```

### By regular expressions

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_regex"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_regex"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_regex"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_regex"
    ```
### By data type

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_data_type"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_data_type"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_data_type"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_data_type"
    ```

## Using selectors
`selectors` is a unique feature of `Polars`. It behaves similarly to a combination of `df.select_dtypes()` and `df.filter()` in `Pandas`. 

### By dtype

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_dtype"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_dtype"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_dtype"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_dtype"
    ```

### Applying set operations

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_set_op"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_set_op"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_set_op"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_set_op"
    ```

### By patterns and substrings

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pl_patterns_substrs"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pl_patterns_substrs"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/column_selections.py:pd_patterns_substrs"
    ```

    ```python exec="on" result="text" session="expressions/column_selections"
    --8<-- "../src/python/expressions/column_selections.py:pd_patterns_substrs"
    ```
    
## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/column-selections/).