# --8<-- [start:setup]
import pandas as pd
import polars as pl

data = {"nrs": [4, 3, 1, 5, 2], "names": ["foo", "ham", "spam", "egg", "baz"]}
df_pl = pl.DataFrame(data)
df_pd = pd.DataFrame(data)
# --8<-- [end:setup]

# --8<-- [start:pl_no_index]
out_pl = df_pl.select(nrs=pl.col("nrs").sort(), names=pl.col("names").reverse())
print(out_pl)
# --8<-- [end:pl_no_index]

# --8<-- [start:pd_no_index]
out_pd = df_pd.assign(
    nrs=lambda df_: df_.nrs.sort_values().reset_index(drop=True),
    names=lambda df_: df_.names[::-1].reset_index(drop=True),
)
print(out_pd)
# --8<-- [end:pd_no_index]

# --8<-- [start:pl_select]
out_pl = df_pl.with_columns(add1=pl.col("nrs") + 1).with_columns(
    add2=pl.col("add1") + 1
)
print(out_pl)
# --8<-- [end:pl_select]

# --8<-- [start:pd_assign]
out_pd = df_pd.assign(add1=lambda df_: df_.nrs + 1, add2=lambda df_: df_.add1 + 1)
print(out_pd)
# --8<-- [end:pd_assign]
