# --8<-- [start:setup]
import pandas as pd
import polars as pl

data = {
    "integers": [1, 2, 3, 4, 5],
    "big_integers": [1, 10000002, 3, 10000004, 10000005],
    "floats": [4.0, 5.0, 6.0, 7.0, 8.0],
    "floats_with_decimal": [4.532, 5.5, 6.5, 7.5, 8.5],
    "floats_as_string": ["4.0", "5.0", "6.0", "7.0", "8.0"],
    "strings_not_float": ["4.0", "not_a_number", "6.0", "7.0", "8.0"],
    "bools": [True, False, True, False, True],
}
# --8<-- [end:setup]

# --8<-- [start:df_pl]
df_pl = pl.DataFrame(data)
print(df_pl)
# --8<-- [end:df_pl]

# --8<-- [start:df_pd]
df_pd = pd.DataFrame(data)
print(df_pd.dtypes, end='\n'*2)
print(df_pd)
# --8<-- [end:df_pd]


# --8<-- [start:pl_numerics]
out_pl = (df_pl
          .select(
              pl.col("integers").cast(pl.Float32).alias("integers_as_floats"),
              pl.col("floats").cast(pl.Int32).alias("floats_as_integers"),
              pl.col("floats_with_decimal")
              .cast(pl.Int32)
              .alias("floats_with_decimal_as_integers"))
          )
print(out_pl)
# --8<-- [end:pl_numerics]


# --8<-- [start:pd_numerics]
out_pd = (df_pd
          .assign(
              integers_as_floats=lambda df_: df_.integers.astype("float32"),
              floats_as_integers=lambda df_: df_.floats.astype("int32"),
              floats_with_decimal_as_integers=lambda df_: df_.floats_with_decimal.astype(
                  "int32"))
          .drop(columns=df_pd.columns)
          )
print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_numerics]


# --8<-- [start:pl_numerics_downcast]
out_pl = (df_pl
          .select(
              pl.col("integers").cast(pl.Int16).alias(
                  "integers_smallfootprint"),
              pl.col("floats").cast(pl.Float32).alias("floats_smallfootprint"))
          )
print(out_pl)
# --8<-- [end:pl_numerics_downcast]


# --8<-- [start:pd_numerics_downcast]
out_pd = (df_pd
          .assign(
              integers_smallfootprint=lambda df_: df_.integers.astype("int16"),
              floats_smallfootprint=lambda df_: df_.floats.astype("float32"))
          .drop(columns=df_pd.columns)
          )
print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_numerics_downcast]


# --8<-- [start:pl_numerics_overflow_strict_true]
try:
    out_pl = df_pl.select(pl.col("big_integers").cast(pl.Int8))
    print(out_pl)
except Exception as e:
    print(e)
# --8<-- [end:pl_numerics_overflow_strict_true]

# --8<-- [start:pl_numerics_overflow_strict_false]
out_pl = df_pl.select(pl.col("big_integers").cast(pl.Int8, strict=False))
print(out_pl)
# --8<-- [end:pl_numerics_overflow_strict_false]

# --8<-- [start:pd_numerics_overflow_astype]
out_pd = (df_pd
          .assign(big_integers=lambda df_: df_.big_integers.astype("int8"))
          .drop(columns=df_pd.columns.drop(["big_integers"]))
          )

print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_numerics_overflow_astype]


# --8<-- [start:pd_numerics_overflow_to_numeric]
out_pd = (df_pd
          .assign(big_integers=lambda df_: pd.to_numeric(df_.big_integers, downcast="integer"))
          .drop(columns=df_pd.columns.drop(["big_integers"]))
          )

print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_numerics_overflow_to_numeric]


# --8<-- [start:pl_strings]
out_pl = (df_pl
          .select(pl.col("integers").cast(pl.Utf8),
                  pl.col("floats").cast(pl.Utf8),
                  pl.col("floats_as_string").cast(pl.Float64))
          )
print(out_pl)
# --8<-- [end:pl_strings]


# --8<-- [start:pd_strings]
out_pd = (df_pd
          .assign(integers=lambda df_: df_.integers.astype(str),
                  floats=lambda df_: df_.floats.astype(str),
                  floats_as_string=lambda df_: df_.floats_as_string.astype("float64"))
          .drop(columns=df_pd.columns.drop(["integers", "floats", "floats_as_string"]))
          )
print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_strings]


# --8<-- [start:pl_strings_strict_true]
try:
    out_pl = df_pl.select(pl.col("strings_not_float").cast(pl.Float64))
    print(out_pl)
except Exception as e:
    print(e)
# --8<-- [end:pl_strings_strict_true]


# --8<-- [start:pl_strings_strict_false]
out_pl = df_pl.select(
    pl.col("strings_not_float").cast(pl.Float64, strict=False))
print(out_pl)
# --8<-- [end:pl_strings_strict_false]


# --8<-- [start:pd_strings_to_numeric_raise]
try:
    out_pd = (df_pd
              .assign(strings_not_float=lambda df_: pd.to_numeric(df_.strings_not_float))
              .drop(columns=df_pd.columns.drop(["strings_not_float"]))
              )
    print(out_pd)
except Exception as e:
    print(e)
# --8<-- [end:pd_strings_to_numeric_raise]


# --8<-- [start:pd_strings_to_coerce]
out_pd = (df_pd
          .assign(strings_not_float=lambda df_: pd.to_numeric(df_.strings_not_float, errors='coerce'))
          .drop(columns=df_pd.columns.drop(["strings_not_float"]))
          )
print(out_pd.dtypes, end='\n'*2)
print(out_pd)
# --8<-- [end:pd_strings_to_coerce]


# --8<-- [start:pl_bools]
out_pl = (df_pl
          .select(pl.col("integers").cast(pl.Boolean),
                  pl.col("floats").cast(pl.Boolean))
          )
print(out_pl)
# --8<-- [end:pl_bools]

# --8<-- [start:pd_bools]
out_pd = (df_pd
          .assign(integers=lambda df_: df_.integers.astype(bool),
                  floats=lambda df_: df_.floats.astype(bool))
          .drop(columns=df_pd.columns.drop(["integers", "floats"]))
          )
print(out_pd)
# --8<-- [end:pd_bools]
