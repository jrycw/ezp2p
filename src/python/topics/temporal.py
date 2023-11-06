# --8<-- [start:setup]
from datetime import date, datetime

import pandas as pd
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:df_pl]
data_pl = {
    "date": pl.date_range(date(2022, 1, 1), date(2022, 1, 5), eager=True),
    "datetime": pl.datetime_range(
        datetime(2022, 1, 1), datetime(2022, 1, 5), eager=True
    ),
    "date_str": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"],
}
df_pl = pl.DataFrame(data_pl)
print(df_pl)
# --8<-- [end:df_pl]

# --8<-- [start:df_pd]
data_pd = {
    "date": pd.date_range("2022-01-01", "2022-01-05"),
    "datetime": pd.date_range("2022-01-01", "2022-01-05"),
    "date_str": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"],
}
df_pd = pd.DataFrame(data_pd)
print(df_pd)
# --8<-- [end:df_pd]
