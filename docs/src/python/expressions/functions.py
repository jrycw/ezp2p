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


# --8<-- [start:pl_col_naming]
out_pl = df_pl.select(
    (pl.col("nrs") + 5).alias("nrs + 5"), (pl.col("nrs") - 5).alias("nrs - 5")
)
print(out_pl)
# --8<-- [end:pl_col_naming]

# --8<-- [start:pd_col_naming]
out_pd = df_pd.assign(
    **{"nrs + 5": lambda df_: df_.nrs + 5, "nrs - 5": lambda df_: df_.nrs - 5}
).drop(columns=df_pd.columns)
print(out_pd)
# --8<-- [end:pd_col_naming]

# --8<-- [start:pl_unique_values]
out_pl = df_pl.select(
    pl.col("names").n_unique().alias("unique"),
    pl.approx_n_unique("names").alias("unique_approx"),
)
print(out_pl)
# --8<-- [end:pl_unique_values]

# --8<-- [start:pd_unique_values]
out_pd = df_pd.names.to_frame().agg(unique=("names", lambda s: s.unique().size)).T
print(out_pd)
# --8<-- [end:pd_unique_values]

# --8<-- [start:pl_conditionals]
out_pl = df_pl.select(
    pl.col("nrs"),
    pl.when(pl.col("nrs") > 2)
    .then(pl.lit(True))
    .otherwise(pl.lit(False))
    .alias("conditional"),
)
print(out_pl)
# --8<-- [end:pl_conditionals]

# --8<-- [start:pd_conditionals]
out_pd = df_pd.assign(conditional=lambda df_: np.where(df_.nrs > 2, True, False)).drop(
    columns=df_pd.columns.drop("nrs")
)
print(out_pd)
# --8<-- [end:pd_conditionals]
