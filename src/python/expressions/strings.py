# --8<-- [start:setup]
import pandas as pd
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:setup1]
data1 = {"animal": ["Crab", "cat and dog", "rab$bit", None]}
# --8<-- [end:setup1]

# --8<-- [start:setup2]
data2 = {"a": ["http://vote.com/ballon_dor?candidate=messi&ref=polars",
               "http://vote.com/ballon_dor?candidat=jorginho&ref=polars",
               "http://vote.com/ballon_dor?candidate=ronaldo&ref=polars"]}
# --8<-- [end:setup2]

# --8<-- [start:setup3]
data3 = {"foo": ["123 bla 45 asd", "xyz 678 910t"]}
# --8<-- [end:setup3]

# --8<-- [start:setup4]
data4 = {"id": [1, 2], "text": ["123abc", "abc456"]}
# --8<-- [end:setup4]


# --8<-- [start:df_pl1]
df_pl = pl.DataFrame(data1)
print(df_pl)
# --8<-- [end:df_pl1]

# --8<-- [start:df_pl_check_pattern]
out_pl = (df_pl
          .select(pl.col("animal"),
                  pl.col("animal").str.contains("cat|bit").alias("regex"),
                  pl.col("animal").str.contains(
                  "rab$", literal=True).alias("literal"),
                  pl.col("animal").str.starts_with("rab").alias("starts_with"),
                  pl.col("animal").str.ends_with("dog").alias("ends_with"))
          )
print(out_pl)
# --8<-- [end:df_pl_check_pattern]

# --8<-- [start:df_pd1]
df_pd = pd.DataFrame(data1)
print(df_pd)
# --8<-- [end:df_pd1]

# --8<-- [start:df_pd_check_pattern]
out_pd = (df_pd
          .assign(animal=lambda df_: df_.animal,
                  regex=lambda df_: df_.animal.str.contains("cat|bit"),
                  literal=lambda df_: df_.animal.str.contains(
                      "rab$", regex=False),
                  starts_with=lambda df_: df_.animal.str.startswith("rab"),
                  ends_with=lambda df_: df_.animal.str.endswith("dog"))
          )
print(out_pd)
# --8<-- [end:df_pd_check_pattern]

# --8<-- [start:df_pl2]
df_pl = pl.DataFrame(data2)
print(df_pl)
# --8<-- [end:df_pl2]


# --8<-- [start:df_pl_extract_pattern]
out_pl = (df_pl
          .select(pl.col("a").str.extract(r"candidate=(\w+)", group_index=1))
          )
print(out_pl)
# --8<-- [end:df_pl_extract_pattern]

# --8<-- [start:df_pd2]
df_pd = pd.DataFrame(data2)
print(df_pd)
# --8<-- [end:df_pd2]

# --8<-- [start:df_pd_extract_pattern]
out_pd = (df_pd
          .assign(a=lambda df_: df_.a.str.extract(r"candidate=(\w+)"))
          )
print(out_pd)
# --8<-- [end:df_pd_extract_pattern]


# --8<-- [start:df_pl3]
df_pl = pl.DataFrame(data3)
print(df_pl)
# --8<-- [end:df_pl3]

# --8<-- [start:df_pl_extract_all_pattern]
out_pl = (df_pl
          .select(pl.col("foo").str.extract_all(r"(\d+)").alias("extracted_nrs"))
          )
print(out_pl)
# --8<-- [end:df_pl_extract_all_pattern]


# --8<-- [start:df_pd3]
df_pd = pd.DataFrame(data3)
print(df_pd)
# --8<-- [end:df_pd3]

# --8<-- [start:df_pd_extract_all_pattern]
out_pd = (df_pd
          .foo
          .str.extractall(r"(\d+)")
          .droplevel('match', axis="rows")
          .reset_index()
          .groupby("index")
          .agg(list)
          .rename(columns={0: "extracted_nrs"})
          )
print(out_pd)
# --8<-- [end:df_pd_extract_all_pattern]


# --8<-- [start:df_pl4]
df_pl = pl.DataFrame(data4)
print(df_pl)
# --8<-- [end:df_pl4]

# --8<-- [start:df_pl_replace_pattern]
out_pl = (df_pl
          .with_columns(pl.col("text").str.replace(r"abc\b", "ABC"),
                        pl.col("text").str.replace_all(
                            "a", "-", literal=True).alias("text_replace_all"))
          )
print(out_pl)
# --8<-- [end:df_pl_replace_pattern]


# --8<-- [start:df_pd4]
df_pd = pd.DataFrame(data4)
print(df_pd)
# --8<-- [end:df_pd4]

# --8<-- [start:df_pd_replace_pattern]
out_pd = (df_pd
          .assign(text=lambda df_: df_.text.str.replace(r"abc\b", "ABC", n=1, regex=True),
                  text_replace_all=lambda _: df_pd.text.str.replace("a", "-"))
          )
print(out_pd)
# --8<-- [end:df_pd_replace_pattern]
