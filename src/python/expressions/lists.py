# --8<-- [start:setup1]
import pandas as pd
import polars as pl

data = {
    "station": ["Station " + str(x) for x in range(1, 6)],
    "temperatures": ["20 5 5 E1 7 13 19 9 6 20",
                     "18 8 16 11 23 E2 8 E2 E2 E2 90 70 40",
                     "19 24 E9 16 6 12 10 22",
                     "E2 E0 15 7 8 10 E1 24 17 13 6",
                     "14 8 E0 16 22 24 E1"]
}
# --8<-- [end:setup1]

# --8<-- [start:df_pl1]
df_pl = pl.DataFrame(data)
print(df_pl)
# --8<-- [end:df_pl1]

# --8<-- [start:df_pd1]
df_pd = pd.DataFrame(data)
print(df_pd)
# --8<-- [end:df_pd1]


# --8<-- [start:pl_create_list_col]
out_pl = df_pl.with_columns(pl.col("temperatures").str.split(" "))
print(out_pl)
# --8<-- [end:pl_create_list_col]

# --8<-- [start:pd_create_list_col]
out_pd = (df_pd
          .assign(temperatures=lambda df_: df_.temperatures.str.split())
          )
print(out_pd)
# --8<-- [end:pd_create_list_col]

# --8<-- [start:pl_col_list]
out_pl = (df_pl
          .with_columns(pl.col("temperatures").str.split(" "))
          .with_columns(pl.col("temperatures").list.head(3).alias("top3"),
                        pl.col("temperatures").list.slice(-3,
                                                          3).alias("bottom_3"),
                        pl.col("temperatures").list.len().alias("obs"))
          )
print(out_pl)
# --8<-- [end:pl_col_list]


# --8<-- [start:pd_col_list]
from operator import itemgetter  # noqa: E402

out_pd = (df_pd
          .assign(
              temperatures=lambda df_: df_.temperatures.str.split(),
              top3=lambda df_: df_.temperatures.apply(
                  itemgetter(slice(None, 3))),
              bottom_3=lambda df_: df_.temperatures.apply(
                  itemgetter(slice(-3, None))),
              obs=lambda df_: df_.temperatures.apply(len))
          )
print(out_pd)
# --8<-- [end:pd_col_list]


# --8<-- [start:pl_col_list_elem]
out_pl = (df_pl
          .with_columns(
              pl.col("temperatures")
              .str.split(" ")
              .list.eval(pl.element().cast(pl.Int64, strict=False).is_null())
              .list.sum()
              .alias("errors"))
          )
print(out_pl)
# --8<-- [end:pl_col_list_elem]

# --8<-- [start:pd_col_list_elem]


def eval_sum(v):
    return pd.to_numeric(pd.Series(v), errors="coerce").isna().sum()


out_pd = (df_pd
          .assign(
              errors=lambda df_: df_.temperatures.str.split().apply(eval_sum))
          )
print(out_pd)
# --8<-- [end:pd_col_list_elem]


# --8<-- [start:setup2]
data2 = {
    "station": ["Station " + str(x) for x in range(1, 11)],
    "day_1": [17, 11, 8, 22, 9, 21, 20, 8, 8, 17],
    "day_2": [15, 11, 10, 8, 7, 14, 18, 21, 15, 13],
    "day_3": [16, 15, 24, 24, 8, 23, 19, 23, 16, 10]
}
# --8<-- [end:setup2]

# --8<-- [start:df_pl2]
df_pl = pl.DataFrame(data2)
print(df_pl)
# --8<-- [end:df_pl2]

# --8<-- [start:df_pd2]
df_pd = pd.DataFrame(data2)
print(df_pd)
# --8<-- [end:df_pd2]


# --8<-- [start:pl_col_list_row]
rank_pct = (pl.element().rank(descending=True) / pl.col("*").count()).round(2)


out_pl = (df_pl
          .with_columns(pl.concat_list(pl.all().exclude("station")).alias("all_temps"))
          .select(pl.all().exclude("all_temps"),
                  pl.col("all_temps").list.eval(rank_pct, parallel=True).alias("temps_rank"))
          )
print(out_pl)
# --8<-- [end:pl_col_list_row]


# --8<-- [start:pd_col_list_row]
def cal_rank_pct(df_):
    n_days = df_.columns.drop(["station"]).size
    return (df_
            .drop(columns=["station"])
            .rank(axis="columns", ascending=False)
            .div(n_days)
            .round(2)
            .agg(list, axis="columns")
            )


out_pd = df_pd.assign(temps_rank=cal_rank_pct)
print(out_pd)
# --8<-- [end:pd_col_list_row]
