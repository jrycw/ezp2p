# --8<-- [start:setup]
from datetime import date, datetime, timedelta
from functools import lru_cache

import numpy as np
import pandas as pd
import polars as pl
from zoneinfo import ZoneInfo

np.random.seed(42)
pl.Config.set_fmt_str_lengths(50)
pl.Config.set_tbl_rows(50)
_tzinfo = "Asia/Taipei"
tzinfo = ZoneInfo(_tzinfo)


@lru_cache
def get_nrs(n):
    return np.random.rand(n) * 100


# --8<-- [end:setup]

# --8<-- [start:df_pl]
df_pl = (
    pl.datetime_range(
        date(2023, 11, 1),
        date(2023, 11, 8),
        timedelta(hours=8),
        closed="left",
        time_unit="ms",
        time_zone=_tzinfo,
        eager=True,
    )
    .to_frame()
    .filter(~pl.col("datetime").dt.day().is_in([5]))
    .pipe(
        lambda df_: df_.with_columns(
            nrs=pl.when(~pl.col("datetime").dt.day().is_in([6])).then(
                pl.lit(get_nrs(df_.height))
            )
        )
    )
)

print(df_pl)
# # --8<-- [end:df_pl]

# --8<-- [start:df_pl_describe]
print(df_pl.describe())
# # --8<-- [end:df_pl_describe]

# --8<-- [start:df_pd]
df_pd = (
    pd.DataFrame(
        {
            "datetime": pd.date_range(
                "2023-11-01", "2023-11-08", freq="8h", inclusive="left", tz=_tzinfo
            )
        }
    )
    .query("~datetime.dt.day.isin([5])")
    .assign(
        nrs=lambda df_: np.where(
            ~df_.datetime.dt.day.isin([6]), get_nrs(df_.shape[0]), np.nan
        )
    )
    .set_index("datetime")
)
print(df_pd.shape)
print(df_pd)
# --8<-- [end:df_pd]

# --8<-- [start:df_pd_describe]
print(df_pd.reset_index().describe(include="all"))
# # --8<-- [end:df_pd_describe]


# --8<-- [start:pl_slice_ts]
t_start = datetime(2023, 11, 1, tzinfo=tzinfo)
t_end = datetime(2023, 11, 4, tzinfo=tzinfo)
out_pl = df_pl.filter(pl.col("datetime").is_between(t_start, t_end, closed="left"))
print(out_pl)
# # --8<-- [end:pl_slice_ts]

# --8<-- [start:pd_slice_ts]
out_pd = df_pd.loc["2023-11-01":"2023-11-03", :]
print(out_pd.shape)
print(out_pd)
# # --8<-- [end:pd_slice_ts]

# --8<-- [start:pl_resampling_by_day]
out_pl = df_pl.group_by_dynamic("datetime", every="1d").agg(pl.col("nrs").mean())
print(out_pl)
# --8<-- [end:pl_resampling_by_day]


# --8<-- [start:pl_resampling_by_day_with_upsample]
out_pl = (
    df_pl.group_by_dynamic("datetime", every="1d")
    .agg(pl.col("nrs").mean())
    .upsample("datetime", every="1d")
)
print(out_pl)
# --8<-- [end:pl_resampling_by_day_with_upsample]


# --8<-- [start:pd_resampling_by_day]
out_pd = df_pd.resample("D").mean()
print(out_pd.shape)
print(out_pd)
# --8<-- [end:pd_resampling_by_day]


# --8<-- [start:pl_resampling_by_custom_time_interval_with_upsample_offset]
out_pl = (
    df_pl.group_by_dynamic("datetime", every="16h30m", offset="4h30m")
    .agg(pl.col("nrs").mean())
    .upsample("datetime", every="16h30m")
)
print(out_pl)
# --8<-- [end:pl_resampling_by_custom_time_interval_with_upsample_offset]


# --8<-- [start:pl_resampling_by_custom_time_interval_with_upsample_start_by]
out_pl = (
    df_pl.group_by_dynamic("datetime", every="16h30m", start_by="datapoint")
    .agg(pl.col("nrs").mean())
    .upsample("datetime", every="16h30m")
)
print(out_pl)
# --8<-- [end:pl_resampling_by_custom_time_interval_with_upsample_start_by]


# --8<-- [start:pd_resampling_by_custom_time_interval]
out_pd = df_pd.resample("16H30min").mean()
print(out_pd.shape)
print(out_pd)
# --8<-- [end:pd_resampling_by_custom_time_interval]

# --8<-- [start:df_pl2]
df_pl2 = (
    pl.datetime_range(
        date(2023, 1, 1),
        date(2025, 1, 1),
        timedelta(hours=12),
        closed="left",
        time_unit="ms",
        time_zone=_tzinfo,
        eager=True,
    )
    .to_frame()
    .pipe(lambda df_: df_.with_columns(nrs=pl.lit(get_nrs(df_.height))))
)
with pl.Config(tbl_rows=10):
    print(df_pl2)
# --8<-- [end:df_pl2]

# --8<-- [start:df_pd2]
df_pd2 = (
    pd.DataFrame(
        {
            "datetime": pd.date_range(
                "2023-01-01", "2025-01-01", freq="12h", inclusive="left", tz=_tzinfo
            )
        }
    )
    .assign(nrs=lambda df_: get_nrs(df_.shape[0]))
    .set_index("datetime")
)
print(df_pd2.shape)
print(df_pd2)
# --8<-- [end:df_pd2]


# --8<-- [start:pl_resampling_by_custom_ending_with_upsample]
out_pl = (
    df_pl2.group_by_dynamic("datetime", every="1q", offset="-2mo", label="right")
    .agg(pl.col("nrs").mean())
    .with_columns(pl.col("datetime").dt.offset_by("-1d"))
)
print(out_pl)
# --8<-- [end:pl_resampling_by_custom_ending_with_upsample]

# --8<-- [start:pd_resampling_by_custom_ending]
out_pd = df_pd2.resample("Q-JAN").mean()
print(out_pd.shape)
print(out_pd)
# --8<-- [end:pd_resampling_by_custom_ending]
