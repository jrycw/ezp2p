# --8<-- [start:setup]
from datetime import date

import pandas as pd
import polars as pl

pl.enable_string_cache()
pd.set_option("display.max_seq_items", 3)
url = "https://theunitedstates.io/congress-legislators/legislators-historical.csv"
# --8<-- [end:setup]

# --8<-- [start:df_pl]
dtypes = {
    "first_name": pl.Categorical,
    "gender": pl.Categorical,
    "type": pl.Categorical,
    "state": pl.Categorical,
    "party": pl.Categorical,
}


df_pl = pl.read_csv(url, dtypes=dtypes).with_columns(
    pl.col("birthday").str.to_date(strict=False)
)
print(df_pl)
# # --8<-- [end:df_pl]

# --8<-- [start:df_pd]
dtype = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}
df_pd = pd.read_csv(url, dtype=dtype).assign(
    birthday=lambda df_: pd.to_datetime(df_.birthday, errors="coerce")
)
print(df_pd)
# --8<-- [end:df_pd]


# --8<-- [start:pl_basic_agg]
out_pl = (
    df_pl.lazy()
    .group_by("first_name")
    .agg(pl.count(), pl.col("gender"), pl.first("last_name"))
    .sort("count", descending=True)
    .limit(5)
    .collect()
)
print(out_pl)
# --8<-- [end:pl_basic_agg]

# --8<-- [start:pd_basic_agg]
out_pd = (
    df_pd.assign(count=0)
    .groupby("first_name", observed=True)
    .agg(
        count=("first_name", "size"),
        gender=("gender", list),
        last_name=("last_name", "first"),
    )
    .sort_values("count", ascending=False)
    .reset_index()
    .head(5)
)
print(out_pd)
# --8<-- [end:pd_basic_agg]


# --8<-- [start:pl_cond_type1]
out_pl = (
    df_pl.lazy()
    .group_by("state")
    .agg(
        (pl.col("party") == "Anti-Administration").sum().alias("anti"),
        (pl.col("party") == "Pro-Administration").sum().alias("pro"),
    )
    .sort("pro", descending=True)
    .limit(5)
    .collect()
)
print(out_pl)
# --8<-- [end:pl_cond_type1]

# --8<-- [start:pd_cond_type1]
out_pd = (
    df_pd.groupby("state", observed=True)
    .agg(
        anti=("party", lambda s_: (s_ == "Anti-Administration").sum()),
        pro=("party", lambda s_: (s_ == "Pro-Administration").sum()),
    )
    .sort_values("pro", ascending=False)
    .reset_index()
    .head(5)
)
print(out_pd)
# --8<-- [end:pd_cond_type1]


# --8<-- [start:pl_cond_type2]
out_pl = (
    df_pl.lazy()
    .group_by("state", "party")
    .agg(pl.count("party").alias("count"))
    .filter(
        (pl.col("party") == "Anti-Administration")
        | (pl.col("party") == "Pro-Administration")
    )
    .sort("count", descending=True)
    .limit(5)
    .collect()
)
print(out_pl)
# --8<-- [end:pl_cond_type2]

# --8<-- [start:pd_cond_type2]
out_pd = (
    df_pd.groupby(["state", "party"], observed=True)
    .agg(count=("party", "size"))
    .query("party == 'Anti-Administration' | party == 'Pro-Administration' ")
    .reset_index()
    .sort_values("count", ascending=False)
    .reset_index(drop=True)
    .head(5)
)
print(out_pd)
# --8<-- [end:pd_cond_type2]


# --8<-- [start:pl_filter]
def compute_age() -> pl.Expr:
    return date(2021, 1, 1).year - pl.col("birthday").dt.year()


def avg_birthday(gender: str) -> pl.Expr:
    return (
        compute_age()
        .filter(pl.col("gender") == gender)
        .mean()
        .alias(f"avg {gender} birthday")
    )


out_pl = (
    df_pl.lazy()
    .group_by("state")
    .agg(
        avg_birthday("M"),
        avg_birthday("F"),
        (pl.col("gender") == "M").sum().alias("# male"),
        (pl.col("gender") == "F").sum().alias("# female"),
    )
    .sort(pl.col("state").cat.set_ordering("lexical"))
    .head(5)
    .collect()
)
print(out_pl)
# --8<-- [end:pl_filter]

# --8<-- [start:pd_filter]


def _rename_and_reorder_cols(df_):
    df_.columns = ["avg F birthday", "avg M birthday", "# female", "# male"]
    return df_.loc[:, ["avg M birthday", "avg F birthday", "# male", "# female"]]


out_pd = (
    df_pd.groupby(["state", "gender"], observed=True)
    .agg(
        birthday=("birthday", lambda s_: (date(2021, 1, 1).year - s_.dt.year).mean()),
        count=("gender", "size"),
    )
    .unstack(level="gender")
    .pipe(_rename_and_reorder_cols)
    .fillna({"# female": 0, "# male": 0})
    .sort_index()
    .reset_index()
    .head(5)
)
print(out_pd)
# --8<-- [end:pd_filter]


# --8<-- [start:pl_sort]
def get_person() -> pl.Expr:
    return pl.col("first_name") + pl.lit(" ") + pl.col("last_name")


out_pl = (
    df_pl.lazy()
    .with_columns(pl.col("first_name").cat.set_ordering("lexical"))
    .sort("birthday", descending=True)
    .group_by("state")
    .agg(
        get_person().first().alias("youngest"),
        get_person().last().alias("oldest"),
        get_person().sort().first().alias("alphabetical_first"),
        pl.col("gender").sort_by("first_name").first().alias("gender"),
    )
    .sort(pl.col("state").cat.set_ordering("lexical"))
    .limit(5)
    .collect()
)
print(out_pl)
# --8<-- [end:pl_sort]

# --8<-- [start:pd_sort]


def get_alpha_info(s_):
    sorted_s = s_.sort_values()
    return "___".join([sorted_s.iloc[0], str(sorted_s.index[0])])


def _create_alpha_cols(df_):
    return (
        df_.alpha_info.str.split("___", expand=True)
        .rename(columns={0: "alphabetical_first", 1: "alpha_index"})
        .assign(alpha_index=lambda df2_: df2_.alpha_index.astype("int64"))
    )


def process_alpha_gender(df_):
    return (
        pd.concat([df_, _create_alpha_cols(df_)], axis="columns")
        .assign(
            gender=lambda df_: df_pd.loc[df_.alpha_index.tolist(), ["gender", "state"]]
            .set_index("state")
            .gender
        )
        .drop(columns=["alpha_info", "alpha_index"])
    )


out_pd = (
    df_pd.assign(
        shown_name=lambda df_: df_.first_name.astype(str)
        + " "
        + df_.last_name.astype(str)
    )
    .sort_values("birthday", ascending=False)
    .groupby("state", observed=True)
    .agg(
        youngest=("shown_name", "first"),
        oldest=("shown_name", "last"),
        alpha_info=("shown_name", get_alpha_info),
    )
    .pipe(process_alpha_gender)
    .sort_index()
    .reset_index()
    .head()
)
print(out_pd)
# --8<-- [end:pd_sort]
