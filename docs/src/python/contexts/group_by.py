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

# --8<-- [start:pl_example]
out_pl = (
    df_pl.group_by("groups")
    .agg(
        pl.col("nrs").sum(),
        pl.col("random").count(),
        (
            pl.col("random")
            .filter(pl.col("names").str.contains("m"))
            .sum()
            .suffix("_sum")
        ),
        pl.col("names").reverse().alias("reversed names"),
    )
    .sort(by="groups")
)
print(out_pl)
# --8<-- [end:pl_example]

# --8<-- [start:pd_example]
out_pd = (
    df_pd.assign(random_m=lambda df_: df_.random[df_.names.str.contains("m")])
    .groupby("groups")
    .agg(
        **{
            "nrs": ("nrs", "sum"),
            "random": ("random", "count"),
            "random_sum": ("random_m", "sum"),
            "reverse names": ("names", lambda s_: s_[::-1]),
        }
    )
    .reset_index()
)
print(out_pd)
# --8<-- [end:pd_example]
