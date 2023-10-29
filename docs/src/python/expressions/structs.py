# --8<-- [start:setup]
import pandas as pd
import polars as pl

data = {
    "Movie": ["Cars", "IT", "ET", "Cars", "Up", "IT", "Cars", "ET", "Up", "ET"],
    "Theatre": ["NE", "ME", "IL", "ND", "NE", "SD", "NE", "IL", "IL", "SD"],
    "Avg_Rating": [4.5, 4.4, 4.6, 4.3, 4.8, 4.7, 4.7, 4.9, 4.7, 4.6],
    "Count": [30, 27, 26, 29, 31, 28, 28, 26, 33, 26],
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

# --8<-- [start:pl_value_counts]
out_pl = df_pl.select(pl.col("Theatre").value_counts(sort=True))
print(out_pl)
# --8<-- [end:pl_value_counts]

# --8<-- [start:pd_value_counts]
out_pd = (df_pd
          .loc[:, ["Theatre"]]
          .value_counts()
          .reset_index()
          .assign(Theatre=lambda df_: df_.values.tolist())
          .drop(columns=["count"])
          )
print(out_pd)
# --8<-- [end:pd_value_counts]


# --8<-- [start:pl_value_counts_unnest]
out_pl = (df_pl
          .select(pl.col("Theatre").value_counts(sort=True))
          .unnest("Theatre")
          )
print(out_pl)
# --8<-- [end:pl_value_counts_unnest]

# --8<-- [start:pd_value_counts_unnest]
out_pd = df_pd.loc[:, ["Theatre"]].value_counts()
print(out_pd)
# --8<-- [end:pd_value_counts_unnest]


# --8<-- [start:pl_ident_dups]
out_pl = df_pl.filter(pl.struct("Movie", "Theatre").is_duplicated())
print(out_pl)
# --8<-- [end:pl_ident_dups]

# --8<-- [start:pd_ident_dups]
out_pd = df_pd[df_pd.duplicated(["Movie", "Theatre"], keep=False)]
print(out_pd)
# --8<-- [end:pd_ident_dups]


# --8<-- [start:pl_multi_col_ranking]
out_pl = (df_pl
          .with_columns(
              pl.struct("Count", "Avg_Rating")
              .rank("dense", descending=True)
              .over("Movie", "Theatre")
              .alias("Rank"))
          .filter(pl.struct("Movie", "Theatre").is_duplicated())
          )
print(out_pl)
# --8<-- [end:pl_multi_col_ranking]

# --8<-- [start:pd_multi_col_ranking]


def _create_rank_col(df_):
    to_be_ranked_cols = ["Count", "Avg_Rating"]
    return (df_
            .assign(rank=lambda df_: df_[to_be_ranked_cols].values.tolist())
            .groupby(["Movie", "Theatre"])
            .rank(ascending=False, method="dense")
            .drop(columns=to_be_ranked_cols)
            )


out_pd = (df_pd
          .assign(rank=_create_rank_col)
          [df_pd.duplicated(["Movie", "Theatre"], keep=False)]
          )
print(out_pd)
# --8<-- [end:pd_multi_col_ranking]
