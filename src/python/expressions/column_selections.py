# --8<-- [start:setup]
from datetime import date, datetime

import numpy as np
import pandas as pd
import polars as pl
import polars.selectors as cs

# --8<-- [end:setup]

# --8<-- [start:df_pl]
df_pl = pl.DataFrame(
    {
        "id": [9, 4, 2],
        "place": ["Mars", "Earth", "Saturn"],
        "date": pl.date_range(date(2022, 1, 1), date(2022, 1, 3), "1d", eager=True),
        "sales": [33.4, 2142134.1, 44.7],
        "has_people": [False, True, False],
        "logged_at": pl.datetime_range(
            datetime(2022, 12, 1), datetime(2022, 12, 1, 0, 0, 2), "1s", eager=True
        ),
    }
).with_row_count("rn")
print(df_pl)
# --8<-- [end:df_pl]

# --8<-- [start:df_pd]
df_pd = (
    pd.DataFrame(
        {
            "id": [9, 4, 2],
            "place": ["Mars", "Earth", "Saturn"],
            "date": pd.date_range("2022-01-01", "2022-01-03"),
            "sales": [33.4, 2142134.1, 44.7],
            "has_people": [False, True, False],
            "logged_at": pd.date_range("2022-12-01", "2022-12-01 00:00:02", freq="S"),
        }
    )
    .rename_axis("rn")
    .reset_index()
)
print(df_pd)
# --8<-- [end:df_pd]


# --8<-- [start:pl_select_all]
out_pl = df_pl.select(pl.all())  # or df_pl.select(pl.col("*"))
print(out_pl)
# --8<-- [end:pl_select_all]


# --8<-- [start:pd_select_all]
out_pd = df_pd.loc[:, :]  # or df_pd.iloc[:, :]
print(out_pd)
# --8<-- [end:pd_select_all]

# --8<-- [start:pl_exclude]
out_pl = df_pl.select(pl.all().exclude("logged_at", "rn"))
print(out_pl)
# --8<-- [end:pl_exclude]

# --8<-- [start:pd_exclude]
out_pd = df_pd.drop(["logged_at", "rn"], axis="columns")
print(out_pd)
# --8<-- [end:pd_exclude]

# --8<-- [start:pl_multi_strings]
out_pl = df_pl.select(pl.col("date", "logged_at").dt.to_string("%Y-%h-%d"))
print(out_pl)
# --8<-- [end:pl_multi_strings]

# --8<-- [start:pd_multi_strings]
out_pd = df_pd.loc[:, ["date", "logged_at"]].assign(
    date=lambda df_: df_.date.dt.strftime("%Y-%h-%d"),
    logged_at=lambda df_: df_.logged_at.dt.strftime("%Y-%h-%d"),
)
print(out_pd)
# --8<-- [end:pd_multi_strings]

# --8<-- [start:pd_multi_strings2]
columns = df_pd.select_dtypes("datetime").columns
out_pd = df_pd.loc[:, columns].assign(
    **{col: lambda df_: df_[col].dt.strftime("%Y-%h-%d") for col in columns}
)
print(out_pd)
# --8<-- [end:pd_multi_strings2]

# --8<-- [start:pl_regex]
out_pl = df_pl.select(pl.col("^.*(as|sa).*$"))
print(out_pl)
# --8<-- [end:pl_regex]

# --8<-- [start:pd_regex]
out_pd = df_pd.filter(regex="^.*(as|sa).*$")
print(out_pd)
# --8<-- [end:pd_regex]


# --8<-- [start:pl_data_type]
out_pl = df_pl.select(pl.col(pl.Int64, pl.UInt32, pl.Boolean).n_unique())
print(out_pl)
# --8<-- [end:pl_data_type]

# --8<-- [start:pd_data_type]
out_pd = (
    df_pd.select_dtypes(["int64", "bool"]).agg(lambda s_: s_.unique().size).to_frame().T
)
print(out_pd.dtypes, end="\n" * 2)
print(out_pd)
# --8<-- [end:pd_data_type]

# --8<-- [start:pl_dtype]
out_pl = df_pl.select(cs.integer(), cs.string())
print(out_pl)
# --8<-- [end:pl_dtype]

# --8<-- [start:pd_dtype]
out_pd = df_pd.select_dtypes(["int64", "object"])
print(out_pd.dtypes, end="\n" * 2)
print(out_pd)
# --8<-- [end:pd_dtype]

# --8<-- [start:pl_set_op]
out_pl = df_pl.select(cs.numeric() - cs.first())
print(out_pl)
# --8<-- [end:pl_set_op]

# --8<-- [start:pd_set_op]
out_pd = df_pd.select_dtypes(np.number).iloc[:, 1:]
print(out_pd.dtypes, end="\n" * 2)
print(out_pd)
# --8<-- [end:pd_set_op]

# --8<-- [start:pl_patterns_substrs]
out_pl = df_pl.select(cs.contains("rn"), cs.matches(".*_.*"))
print(out_pl)
# --8<-- [end:pl_patterns_substrs]

# --8<-- [start:pd_patterns_substrs]
out_pd = df_pd[
    df_pd.filter(like="rn").columns.append(df_pd.filter(regex=".*_.*").columns)
]
print(out_pd)
# --8<-- [end:pd_patterns_substrs]
