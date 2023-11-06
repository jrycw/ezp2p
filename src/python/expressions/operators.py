# --8<-- [start:setup]
import numpy as np
import pandas as pd
import polars as pl

np.random.seed(42)
data = {
    "nrs": [1, 2, 3, 4, 5],
    "names": ["foo", "ham", "spam", "egg", "baz"],
    "random": np.random.rand(5),
    "groups": ["A", "A", "B", "C", "B"],
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


# --8<-- [start:pl_numerical]
out_pl = df_pl.select(
    (pl.col("nrs") + 5).alias("nrs + 5"),
    (pl.col("nrs") - 5).alias("nrs - 5"),
    (pl.col("nrs") * pl.col("random")).alias("nrs * random"),
    (pl.col("nrs") / pl.col("random")).alias("nrs / random"),
)
print(out_pl)
# --8<-- [end:pl_numerical]


# --8<-- [start:pd_numerical]
out_pd = df_pd.assign(
    **{
        "nrs + 5": lambda df_: df_.nrs + 5,
        "nrs - 5": lambda df_: df_.nrs - 5,
        "nrs * random": lambda df_: df_.nrs * df_.random,
        "nrs / random": lambda df_: df_.nrs / df_.random,
    }
).drop(columns=df_pd.columns)
print(out_pd)
# --8<-- [end:pd_numerical]


# --8<-- [start:pl_logical]
out_pl = df_pl.select(
    (pl.col("nrs") > 1).alias("nrs > 1"),
    (pl.col("random") <= 0.5).alias("random <= .5"),
    (pl.col("nrs") != 1).alias("nrs != 1"),
    (pl.col("nrs") == 1).alias("nrs == 1"),
    ((pl.col("random") <= 0.5) & (pl.col("nrs") > 1)).alias("and_expr"),
    ((pl.col("random") <= 0.5) | (pl.col("nrs") > 1)).alias("or_expr"),
)
print(out_pl)
# --8<-- [end:pl_logical]


# --8<-- [start:pd_logical]
out_pd = df_pd.assign(
    **{
        "nrs > 1": lambda df_: df_.nrs > 1,
        "random <= .5": lambda df_: df_.random <= 0.5,
        "nrs != 1": lambda df_: df_.nrs != 1,
        "nrs == 1": lambda df_: df_.nrs == 1,
        "and_expr": lambda df_: (df_.random <= 0.5) & (df_.nrs > 1),
        "or_expr": lambda df_: (df_.random <= 0.5) | (df_.nrs > 1),
    }
).drop(columns=df_pd.columns)
print(out_pd)
# --8<-- [end:pd_logical]
