# --8<-- [start:setup]
import numpy as np
import pandas as pd
import polars as pl

np.random.seed(42)
data = {
    "a": [1, 2, 3],
    "b": [10, 20, 30],
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


# --8<-- [start:pl_]
out_pl = df_pl.select(pl.fold(acc=pl.lit(0),
                              function=lambda acc, x: acc + x,
                              exprs=pl.all()).alias("sum")
                      )

print(out_pl)
# --8<-- [end:pl_]

# --8<-- [start:pd_]

# --8<-- [end:pd_]
