# --8<-- [start:setup]
import numpy as np
import pandas as pd
import polars as pl

np.random.seed(42)
data = {"nrs": [1, 2, 3, 4, 5], "random": np.random.rand(5)}
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
out_pl = df_pl.filter((pl.col("nrs") > 2) & (pl.col("random") > 0.5))
print(out_pl)
# --8<-- [end:pl_example]

# --8<-- [start:pd_example]
out_pd = df_pd.query("nrs > 2 & random > 0.5")
print(out_pd)
# --8<-- [end:pd_example]
