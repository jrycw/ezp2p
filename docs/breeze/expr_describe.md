# Describe  method for expressions
At the moment, `Polars` lacks built-in `expressions` for generating a `describe` summary. Nevertheless, it is possible to create custom expressions to achieve a similar result [manually](https://github.com/pola-rs/polars/issues/8066).


```python 
--8<-- "../src/python/breeze/expr_describe.py:df_pl"
```

```python exec="on" result="text" session="breeze/expr_describe"
--8<-- "../src/python/breeze/expr_describe.py:df_pl"
```