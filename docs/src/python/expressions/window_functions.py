# --8<-- [start:setup]
import pandas as pd
import polars as pl

url = "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
# --8<-- [end:setup]

# --8<-- [start:df_pl]
df_pl = pl.read_csv(url)
print(df_pl)
# --8<-- [end:df_pl]

# --8<-- [start:df_pd]
df_pd = pd.read_csv(url)
print(df_pd)
# --8<-- [end:df_pd]

# --8<-- [start:pl_group_by_aggs_in_selection]
out_pl = df_pl.select(
    "Type 1",
    "Type 2",
    pl.col("Attack").mean().over("Type 1").alias("avg_attack_by_type"),
    pl.col("Defense")
    .mean()
    .over(["Type 1", "Type 2"])
    .alias("avg_defense_by_type_combination"),
    pl.col("Attack").mean().alias("avg_attack"),
)
print(out_pl)
# --8<-- [end:pl_group_by_aggs_in_selection]

# --8<-- [start:pd_group_by_aggs_in_selection]
out_pd = (
    df_pd.loc[:, ["Type 1", "Type 2", "Attack", "Defense"]]
    .assign(
        avg_attack_by_type=lambda df_: df_[["Type 1", "Attack"]]
        .groupby(["Type 1"])
        .transform("mean"),
        avg_defense_by_type_combination=lambda df_: (
            df_[["Type 1", "Type 2", "Defense"]]
            .fillna({"Type 2": "placeholder"})
            .groupby(["Type 1", "Type 2"])
            .transform("mean")
        ),
        avg_attack=lambda df_: df_.Attack.mean(),
    )
    .drop(columns=["Attack", "Defense"])
)
print(out_pd)
# --8<-- [end:pd_group_by_aggs_in_selection]


# --8<-- [start:pl_op_per_group]
out_pl = (
    df_pl.filter(pl.col("Type 2") == "Psychic")
    .select("Name", "Type 1", "Speed")
    .with_columns(
        pl.col(["Name", "Speed"]).sort_by("Speed", descending=True).over("Type 1")
    )
)
print(out_pl)
# --8<-- [end:pl_op_per_group]

# --8<-- [start:pd_op_per_group]
out_pd = (
    df_pd.query("`Type 2` == 'Psychic'")
    .loc[:, ["Name", "Type 1", "Speed"]]
    .assign(type1_tmp=lambda df_: df_["Type 1"])
    .groupby("type1_tmp")
    .transform(lambda g: sorted(g, reverse=True))
)
print(out_pd)
# --8<-- [end:pd_op_per_group]

# --8<-- [start:pl_example]
out_pl = df_pl.sort("Type 1").select(
    pl.col("Type 1").head(3).over("Type 1", mapping_strategy="explode"),
    pl.col("Name")
    .sort_by(pl.col("Speed"), descending=True)
    .head(3)
    .over("Type 1", mapping_strategy="explode")
    .alias("fastest/group"),
    pl.col("Name")
    .sort_by(pl.col("Attack"), descending=True)
    .head(3)
    .over("Type 1", mapping_strategy="explode")
    .alias("strongest/group"),
    pl.col("Name")
    .sort()
    .head(3)
    .over("Type 1", mapping_strategy="explode")
    .alias("sorted_by_alphabet"),
)
print(out_pl)
# --8<-- [end:pl_example]

# --8<-- [start:pd_example]


def _process_speed(df_):
    return (
        df_.loc[:, ["Type 1", "Speed", "Name"]]
        .sort_values("Speed", ascending=False)
        .groupby("Type 1")
        .agg(list)
        .assign(**{"fastest/group": lambda df_: df_["Name"].str.slice(0, 3)})
        .explode("fastest/group")
        .loc[:, "fastest/group"]
    )


def _process_attack(df_):
    return (
        df_.loc[:, ["Type 1", "Attack", "Name"]]
        .sort_values("Attack", ascending=False)
        .groupby("Type 1")
        .agg(list)
        .assign(**{"strongest/group": lambda df_: df_["Name"].str.slice(0, 3)})
        .explode("strongest/group")
        .loc[:, "strongest/group"]
    )


def _process_name(df_):
    return (
        df_.loc[:, ["Type 1", "Name"]]
        .sort_values("Name")
        .groupby("Type 1")
        .agg(list)
        .assign(**{"sorted_by_alphabet": lambda df_: df_["Name"].str.slice(0, 3)})
        .explode("sorted_by_alphabet")
        .loc[:, "sorted_by_alphabet"]
    )


def window_pipeline(df_):
    s_speed = _process_speed(df_)
    s_attack = _process_attack(df_)
    s_name = _process_name(df_)
    return pd.concat([s_speed, s_attack, s_name], axis="columns")


out_pd = (
    df_pd.loc[:, ["Type 1", "Speed", "Attack", "Name"]]
    .pipe(window_pipeline)
    .reset_index()
)
with pd.option_context("display.max_rows", 15):
    print(out_pd)
# --8<-- [end:pd_example]
