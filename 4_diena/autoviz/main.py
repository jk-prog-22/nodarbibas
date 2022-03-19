from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()

filename = "titanic_2.xls"
sep = ","
dft = AV.AutoViz(
    filename,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=2,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
)