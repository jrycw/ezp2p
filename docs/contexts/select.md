# pl.select()
`pl.select([..])` is a powerful selection tool that allows you to select one or more columns and perform operations on them in parallel. This includes the ability to create new columns as part of your selection process.

## Setup
```python 
--8<-- "../src//python/contexts/select.py:setup"
```

```python exec="on" session="contexts/select"
--8<-- "../src//python/contexts/select.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src//python/contexts/select.py:df_pl"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src//python/contexts/select.py:df_pd"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:df_pd"
    ```

## Basic form
If selecting at least one column from the original dataframe, the behavior of `pl.select([..])` can be treated as `df.loc(:, [..]).assign(..)` in `Pandas`.


=== "Polars"
    ```python 
    --8<-- "../src//python/contexts/select.py:pl_at_least_one_col"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pl_at_least_one_col"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src//python/contexts/select.py:pd_at_least_one_col"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pd_at_least_one_col"
    ```

## Generalized form
It's worth noting that `pl.select([..])` can also be used to create columns. Therefore, the behavior of `pl.select([..])` is akin to `df.assign(..).drop(columns=..)` in `Pandas`."

=== "Polars"
    ```python 
    --8<-- "../src//python/contexts/select.py:pl_no_cols"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pl_no_cols"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src//python/contexts/select.py:pd_no_cols"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pd_no_cols"
    ```

## Example
While this example appears straightforward in `Polars`, there are some nuances in `Pandas`. Let's explore them.

=== "Polars"
    ```python 
    --8<-- "../src//python/contexts/select.py:pl_example"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pl_example"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src//python/contexts/select.py:pd_example"
    ```

    ```python exec="on" result="text" session="contexts/select"
    --8<-- "../src//python/contexts/select.py:pd_example"
    ```

It's noted that, since one of the column names contains a space ('first name'), we need to use a dictionary to store each column name as the key and the corresponding operation as the value. Then, we can unpack this dictionary in `pd.assign(..)`.

Here's a breakdown of the operations:

* "nrs": This operation calculates the sum of the "nrs" column and broadcasts it to all rows.
* "names": This operation sorts the values in the "names" column. To realign the index, we use `df.reset_index(drop=True)`.
* "first name": This operation selects the first row value of the "names" column and broadcasts it to all rows. It's important to note that since we reassigned "names" in the previous line, we need to use the original `df_pd` to retrieve the "names" column.
* "10xnrs": This operation calculates the mean of the "nrs" column and broadcasts it to all rows. Similarly, since we reassigned "nrs" at the beginning, we need to use the original `df_pd` to retrieve the "nrs" column.

Additionally, we use `.drop(columns=df_pd.columns.drop(["nrs", "names"]))` to drop the columns that haven't been reassigned.

## Tips
* Whenever you wish you could use `df.loc(..)`, `df.iloc(..)` or `df[..]` in `Polars`, you're likely looking for `pl.select([..])`. 
* Notably, `pl.select([..])` not only lets you select columns but also enables you to create new columns simultaneously.

## Reference
The examples in this section have been adapted from the [`Polars` user guide](https://pola-rs.github.io/polars/user-guide/concepts/contexts/#select).