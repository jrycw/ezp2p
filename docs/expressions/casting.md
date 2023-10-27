# Casting
`pl.Expr.cast` serves as the primary function for type conversion in Polars. It includes a keyword argument, `strict`,  which, by default, is set to `True` and will raise an exception if a conversion error occurs. Alternatively, you can set `strict=False`. In this case, if a conversion error occurs, the values will be set to `null`.

## Setup
```python 
--8<-- "../src/python/expressions/casting.py:setup"
```

```python exec="on" session="expressions/casting"
--8<-- "../src/python/expressions/casting.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/expressions/casting.py:df_pl"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/expressions/casting.py:df_pd"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:df_pd"
    ```


## Numerics

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_numerics"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_numerics"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_numerics"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_numerics"
    ```

### Downcast

=== "Polars"
    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_numerics_downcast"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_numerics_downcast"
    ```

=== "Pandas"

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_numerics_downcast"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_numerics_downcast"
    ```


### Overflow

=== "Polars"
    
    **strict=True**

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_numerics_overflow_strict_true"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_numerics_overflow_strict_true"
    ```

    **strict=False**

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_numerics_overflow_strict_false"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_numerics_overflow_strict_false"
    ```


=== "Pandas"

    **`pd.Series.astype(..)`**

    This behavior might not be as you expected.

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_numerics_overflow_astype"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_numerics_overflow_astype"
    ```
    
    **`pd.to_numeric(.., downcast=..)`**

    Alternatively, `pd.to_numeric` will do its best to downcast the resulting data to the smallest numerical dtype as specified in the `downcast` parameter.

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_numerics_overflow_to_numeric"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_numerics_overflow_to_numeric"
    ```
    The type of `big_integers` is converted from `int64` to `int32`.

## Strings

### Numeric values

=== "Polars"

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_strings"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_strings"
    ```


=== "Pandas"

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_strings"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_strings"
    ```

### Non-numeric values
* The behavior of `pl.col().cast(.., strict=True)` in `Polars` behaves similarly to `pd.to_numeric(.., errors=raise)` in `Pandas` in this example.

* The behavior of `pl.col().cast(.., strict=False)` in `Polars` behaves similarly to `pd.to_numeric(.., errors=coerce)` in `Pandas` in this example.


=== "Polars"
    
    **strict=True**

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_strings_strict_true"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_strings_strict_true"
    ```

    **strict=False**

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_strings_strict_false"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_strings_strict_false"
    ```

=== "Pandas"

    **erros=raise**
    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_strings_to_numeric_raise"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_strings_to_numeric_raise"
    ```
    
    **erros=coerce**

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_strings_to_coerce"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_strings_to_coerce"
    ```

## Booleans

=== "Polars"

    ```python 
    --8<-- "../src/python/expressions/casting.py:pl_bools"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pl_bools"
    ```

=== "Pandas"

    ```python 
    --8<-- "../src/python/expressions/casting.py:pd_bools"
    ```

    ```python exec="on" result="text" session="expressions/casting"
    --8<-- "../src/python/expressions/casting.py:pd_bools"
    ```

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/expressions/casting/).