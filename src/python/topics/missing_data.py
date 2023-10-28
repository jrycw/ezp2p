# --8<-- [start:setup]
import numpy as np
import pandas as pd
import polars as pl

data = {
    "col1": [1, 2, 3],
    "col2": [1, None, 9]
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


# --8<-- [start:pl_isnull]
is_null_df_pl = df_pl.select(pl.all().is_null())
print(is_null_df_pl)
# --8<-- [end:pl_isnull]

# --8<-- [start:pd_isna]
is_nan_df_pd = df_pd.isna()
print(is_nan_df_pd)
# --8<-- [end:pd_isna]


# --8<-- [start:pl_null_count]
null_count_df_pl = df_pl.null_count()
print(null_count_df_pl)
# --8<-- [end:pl_null_count]

# --8<-- [start:pd_na_count]
nan_count_df_pd = df_pd.isna().sum().to_frame().T
print(nan_count_df_pd)
# --8<-- [end:pd_na_count]


# --8<-- [start:pl_fill_literal]
fill_literal_df_pl = (df_pl
                      .with_columns(pl.col("col2").fill_null(pl.lit(2)))
                      )
print(fill_literal_df_pl)
# --8<-- [end:pl_fill_literal]

# --8<-- [start:pd_fill_literal]
fill_literal_df_pd = (df_pd
                      .assign(col2=lambda df_: df_.col2.fillna(2))
                      )
print(fill_literal_df_pd)
# --8<-- [end:pd_fill_literal]


# --8<-- [start:pl_fill_strategy]
fill_forward_df_pl = (df_pl
                      .with_columns(pl.col("col2").fill_null(strategy="forward"))
                      )
print(fill_forward_df_pl)
# --8<-- [end:pl_fill_strategy]

# --8<-- [start:pd_fill_strategy]
fill_forward_df_pd = (df_pd
                      .assign(col2=lambda df_: df_.col2.ffill())
                      )
print(fill_forward_df_pd)
# --8<-- [end:pd_fill_strategy]


# --8<-- [start:pl_fill_median]
fill_median_df_pl = (df_pl
                     .with_columns(pl.col("col2").fill_null(pl.median("col2")))
                     )
print(fill_median_df_pl)
# --8<-- [end:pl_fill_median]

# --8<-- [start:pd_fill_median]
fill_median_df_pd = (df_pd
                     .assign(col2=lambda df_: df_.col2.fillna(df_.col2.median()))
                     )
print(fill_median_df_pd)
# --8<-- [end:pd_fill_median]


# --8<-- [start:pl_fill_interpolation]
fill_interpolation_df_pl = (df_pl
                            .with_columns(pl.col("col2").interpolate())
                            )
print(fill_interpolation_df_pl)
# --8<-- [end:pl_fill_interpolation]

# --8<-- [start:pd_fill_interpolation]
fill_interpolation_df_pd = (df_pd
                            .assign(col2=lambda df_: df_.col2.interpolate())
                            )
print(fill_interpolation_df_pd)
# --8<-- [end:pd_fill_interpolation]


# --8<-- [start:pl_nan_setup]
nan_df_pl = pl.DataFrame({"value": [1.0, np.NaN, float("nan"), 3.0]})
print(nan_df_pl)
# --8<-- [end:pl_nan_setup]

# --8<-- [start:pl_isna]
is_nan_df_pl = nan_df_pl.select(pl.all().is_nan())
print(is_nan_df_pl)
# --8<-- [end:pl_isna]


# --8<-- [start:pl_nan_count]
nan_count_df_pl = nan_df_pl.select(pl.all().is_nan()).sum()
print(nan_count_df_pl)
# --8<-- [end:pl_nan_count]


# --8<-- [start:pl_nan_count]
nan_count_df_pl = nan_df_pl.select(pl.all().is_nan()).sum()
print(nan_count_df_pl)
# --8<-- [end:pl_nan_count]

# --8<-- [start:pl_nan_fill_literal]
fill_literal_nan_df_pl = (nan_df_pl
                          .with_columns(pl.col("value").fill_nan(pl.lit(2)))
                          )
print(fill_literal_nan_df_pl)
# --8<-- [end:pl_nan_fill_literal]


# --8<-- [start:pl_nan_mean]
mean_nan_fill_null_df_pl = nan_df_pl.with_columns(pl.col("value")).mean()
print(mean_nan_fill_null_df_pl)
# --8<-- [end:pl_nan_mean]


# --8<-- [start:pl_nan_mean_fill_null]
mean_nan_fill_null_df_pl = (nan_df_pl
                            .with_columns(pl.col("value").fill_nan(None))
                            .mean()
                            )
print(mean_nan_fill_null_df_pl)
# --8<-- [end:pl_nan_mean_fill_null]


# --8<-- [start:pd_nat]
df_pd_nat = pd.DataFrame([pd.Timestamp("2023"), np.nan], columns=["col"])
print(df_pd_nat.dtypes, end='\n'*2)
print(df_pd_nat)
# --8<-- [end:pd_nat]
