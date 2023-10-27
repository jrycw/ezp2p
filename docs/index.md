# Introduction

## Purpose
This repository is designed to help those transitioning from `Pandas` to `Polars` become acquainted with `Polars`' syntax. Most of the code examples are sourced from the excellent [Polars user guide](https://pola-rs.github.io/polars/user-guide/). Each example features both `Polars` and `Pandas` code, encouraging you to practice converting `Polars` to `Pandas` independently. If you encounter challenges with `Polars`, you can refer to my solutions for guidance. I believe that with these hints, you'll develop even better solutions of your own. This approach will enable you to swiftly grasp `Polars` through the familiar lens of `Pandas`.

## Why take this approach?
Converting code from `Polars` to `Pandas` involves a three-step process:

1. Familiarizing with `Polars`: First, you must acquaint yourself with `Polars`' syntax to understand its meaning.
2. Converting to `Pandas`: During the conversion process, you'll need to determine how to accomplish tasks using `Pandas`.
3. Comparing the results: Finally, you'll compare the results and gain insights into the strengths and weaknesses of both libraries.

This approach ensures a comprehensive understanding of both `Polars` and `Pandas`, enabling you to make informed decisions when working with data manipulation libraries.

## Embrace the new mindset

### Contexts
Contexts in `Polars` determine how to perform operations similar to `df.loc[.., ..]`, `df.iloc[.., ..]` and `df[..]`. 

In `Polars`, You'll mainly work with these three contexts to manipulate rows and columns:

* `pl.select([..])`: Select or create columns.
* `pl.with_columns([..])`: Create columns.
* `pl.filter(..)`: Filter rows.

It's worth noting that `pl.group_by(..).agg([..])` serves as a specialized context in `Polars` for aggregation purposes.

### Expressions
Expressions in `Polars` are akin to the operations you wish to perform. They are present throughout the library. You'll find them used for various tasks, such as changing a column's data type, sorting a column, extracting the initial rows, and even computing the mean value for each group after performing a `group by` operation.

### No more index
`Polars` excels at data manipulation through a column-based approach, unburdened by index-based constraints. In contrast, `Pandas` primarily relies on index alignment as the key concept for connecting columns within each row. If you need to break the relationship for a single column in `Pandas`, especially when the original index is multi-indexed, you'll likely find yourself doing a substantial amount of work to figure out how to realign it.

```python 
--8<-- "../src/python/concepts.py:setup"
```

```python exec="on" session="concepts/no_index"
--8<-- "../src/python/concepts.py:setup"
```

=== "Polars"
    ```python 
    --8<-- "../src/python/concepts.py:pl_no_index"
    ```

    ```python exec="on" result="text" session="concepts/no_index"
    --8<-- "../src/python/concepts.py:pl_no_index"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/concepts.py:pd_no_index"
    ```

    ```python exec="on" result="text" session="concepts/no_index"
    --8<-- "../src/python/concepts.py:pd_no_index"
    ```

!!! info "Pseudo Index"
    If you really need the index to help you get used to `Polars`, you can refer to [df.with_row_count()](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.with_row_count.html#polars.DataFrame.with_row_count).

### Parallel
`Polars` is designed to operate in parallel. This means that you can't refer a column name you've assigned within the same context. This behavior may require some adjustment for `Pandas` users who are accustomed to heavily using `pd.assign()`.

```python 
--8<-- "../src/python/concepts.py:setup"
```

```python exec="on" session="concepts/parallel"
--8<-- "../src/python/concepts.py:setup"
```

=== "Polars"
    ```python 
    --8<-- "../src/python/concepts.py:pl_select"
    ```

    ```python exec="on" result="text" session="concepts/parallel"
    --8<-- "../src/python/concepts.py:pl_select"
    ```

    !!! failure "This code snippet will raise `pl.exceptions.ColumnNotFoundError`."
        ```python
        df_pl.with_columns(add1=pl.col("nrs") + 1,
                           add2=pl.col("add1") + 1)
        ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/concepts.py:pd_assign"
    ```

    ```python exec="on" result="text" session="concepts/parallel"
    --8<-- "../src/python/concepts.py:pd_assign"
    ```

### Namespaces
Namespaces in `Polars` are akin to accessors in `Pandas`. However, `Polars` offers more robust namespaces compared to `Pandas`, with features such as the [list namespace](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/list.html), which can be incredibly useful.

### Lazy
Lazy is at the core of `Polars` and offers numerous advantages compared to the eager mode. For a more in-depth understanding, you should refer to the [user guide](https://pola-rs.github.io/polars/user-guide/lazy/using/).

### Missing data
In `Polars`, missing data is consistently represented as a `null` value. Additionally, `Polars` permits the use of `Not a Number` or `NaN` values for float columns. It's important to avoid conflating these two concepts." 