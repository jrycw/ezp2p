# --8<-- [start:df_pl]
from datetime import date

import polars as pl


def to_describe(col, prefix=""):
    prefix = prefix or f"{col}_"
    return [
        pl.col(col).count().alias(f"{prefix}count"),
        pl.col(col).is_null().sum().alias(f"{prefix}null_count"),
        pl.col(col).mean().alias(f"{prefix}mean"),
        pl.col(col).std().alias(f"{prefix}std"),
        pl.col(col).min().alias(f"{prefix}min"),
        pl.col(col).quantile(0.25).alias(f"{prefix}25%"),
        pl.col(col).quantile(0.5).alias(f"{prefix}50%"),
        pl.col(col).quantile(0.75).alias(f"{prefix}75%"),
        pl.col(col).max().alias(f"{prefix}max"),
    ]


df = pl.DataFrame(
    {
        "date": [
            date(2023, 9, 5),
            date(2023, 9, 25),
            date(2023, 10, 5),
            date(2023, 10, 25),
            date(2023, 11, 5),
            date(2023, 11, 25),
        ],
        "a": [1, 3, 2, 15, 10, None],
        "b": [None, 11, 13, 12, 115, 110],
    }
)
out = (
    df.group_by(pl.col("date").dt.month().alias("month"))
    .agg(*to_describe("a"), *to_describe("b"))
    .sort("month")
)

print(out)
# # --8<-- [end:df_pl]
