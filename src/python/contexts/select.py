# --8<-- [start:setup]
import numpy as np
import pandas as pd
import polars as pl

np.random.seed(42)
data = {
    "nrs": [1, 2, 3, 4, 5],
    "names": ["foo", "ham", "spam", "egg", "baz"],
    "random": np.random.rand(5),
    "groups": ["A", "A", "B", "C", "B"]
}
# --8<-- [end:setup]


# --8<-- [start:df_pl]
df_pl = pl.DataFrame(data)
print(df_pl)
# --8<-- [end:df_pl]

# --8<-- [start:df_pd]
df_pd = pd.DataFrame(data)
print(df_pd)
# --8<-- [end:df_pd]

# --8<-- [start:pl_at_least_one_col]
out_pl = (df_pl
          .select(pl.col("nrs"),
                  (pl.col("nrs") + 1).alias("add1"),
                  (pl.col("nrs") - 1).alias("sub1"),
                  (pl.col("nrs") * 2).alias("mul2"),
                  (pl.col("nrs") / 3).alias("div3"))
          )
print(out_pl)
# --8<-- [end:pl_at_least_one_col]


# --8<-- [start:pd_at_least_one_col]
out_pd = (df_pd
          .loc[:, ["nrs"]]
          .assign(add1=lambda df_: df_.nrs + 1,
                  sub1=lambda df_: df_.nrs - 1,
                  mul2=lambda df_: df_.nrs * 2,
                  div3=lambda df_: df_.nrs / 3)
          )
print(out_pd)
# --8<-- [end:pd_at_least_one_col]


# --8<-- [start:pl_no_cols]
out_pl = (df_pl
          .select((pl.col("nrs") + 1).alias("add1"),
                  (pl.col("nrs") - 1).alias("sub1"),
                  (pl.col("nrs") * 2).alias("mul2"),
                  (pl.col("nrs") / 3).alias("div3"))
          )
print(out_pl)
# --8<-- [end:pl_no_cols]


# --8<-- [start:pd_no_cols]
out_pd = (df_pd
          .assign(add1=lambda df_: df_.nrs + 1,
                  sub1=lambda df_: df_.nrs - 1,
                  mul2=lambda df_: df_.nrs * 2,
                  div3=lambda df_: df_.nrs / 3)
          .drop(columns=df_pd.columns)
          )
print(out_pd)
# --8<-- [end:pd_no_cols]


# --8<-- [start:pl_example]
out_pl = (df_pl.select(
    pl.col("nrs").sum(),
    pl.col("names").sort(),
    pl.col("names").first().alias("first name"),
    (pl.col("nrs").mean() * 10).alias("10xnrs"))
)
print(out_pl)
# --8<-- [end:pl_example]


# --8<-- [start:pd_example]
out_pd = (df_pd
          .assign(**{
              "nrs": lambda df_: df_.nrs.sum(),
              "names": lambda df_: df_.names.sort_values().reset_index(drop=True),
              "first name": lambda _: df_pd.names.iloc[0],
              "10xnrs": lambda _: df_pd.nrs.mean() * 10})
          .drop(columns=df_pd.columns.drop(["nrs", "names"]))
          )
print(out_pd)
# --8<-- [end:pd_example]
