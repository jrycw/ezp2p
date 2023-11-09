# Time series

## Setup
It is worth noting that:

* The datapoint for `2023-11-05` is intentionally excluded in both `df_pl` and `df_pd`.
* Some datapoints are deliberately set as `null` in `Polars` and as `NaN` in `Pandas`.
* The results of quantiles are not consistent between `Polars` and `Pandas`. This discrepancy arises from the default interpolation method for quantiles, which is `nearest` in `Polars` and `linear` in `Pandas`.


```python 
--8<-- "../src/python/topics/time_series.py:setup"
```

```python exec="on" session="topics/time_series"
--8<-- "../src/python/topics/time_series.py:setup"
```

=== "Polars_df"
    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pl"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pl"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pd"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pd"
    ```

=== "Polars_describe"
    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pl_describe"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pl_describe"
    ```

=== "Pandas_describe"

    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pd_describe"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pd_describe"
    ```

## Slice time series
`Polars` relies on `expressions` to slice time series data, while `Pandas` can utilize the `DatetimeIndex`.

=== "Polars"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_slice_ts"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_slice_ts"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pd_slice_ts"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pd_slice_ts"
    ```

## Resampling data by day
`Polars` employs `df.group_by_dynamic` for time series resampling, while `Pandas` provides the `df.resample` method. If you need continuous datetime datapoints, similar to `Pandas`, you may find `df.upsample` in `Polars` to be useful.

=== "Polars"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_day"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_day"
    ```

=== "Polars_upsample"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_day_with_upsample"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_day_with_upsample"
    ```


=== "Pandas"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_day"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_day"
    ```

## Resampling data by custom time interval
At the time of writing, a complex combination for datetime, like `3d12h4m25s` will fail. In addition, to achieve the similar behavior like `Pandas`, you might need to tweak the `offset` or `start_by` parameters of `df.group_by_dynamic` in `Polars`.

=== "Polars_upsample_offset"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_time_interval_with_upsample_offset"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_time_interval_with_upsample_offset"
    ```

=== "Polars_upsample_start_by"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_time_interval_with_upsample_start_by"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_time_interval_with_upsample_start_by"
    ```


=== "Pandas"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_custom_time_interval"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_custom_time_interval"
    ```

## Resampling data by custom ending
We created new dataframes with more data points for `Polars` and `Pandas`, respectively, to provide a clearer illustration.

=== "Polars_df"
    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pl2"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pl2"
    ```

=== "Pandas_df"
    ```python 
    --8<-- "../src/python/topics/time_series.py:df_pd2"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:df_pd2"
    ```
    
Achieving this can be done using `anchored offset aliases` in `Pandas`. To replicate this behavior in `Polars`, you might need to make some adjustments.

=== "Polars"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_ending_with_upsample"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pl_resampling_by_custom_ending_with_upsample"
    ```

=== "Pandas"
    ```python 
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_custom_ending"
    ```

    ```python exec="on" result="text" session="topics/time_series"
    --8<-- "../src/python/topics/time_series.py:pd_resampling_by_custom_ending"
    ```


