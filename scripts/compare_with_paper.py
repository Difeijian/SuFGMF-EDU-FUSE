"""Compare recomputed EDU-FUSE metrics with the values reported in Table 6 / Table 7."""
import pandas as pd

rep = pd.concat([
    pd.read_csv("results/table6_main_results.csv").set_index("method")[["edufuse_3cls_wf1_mean", "edufuse_fine_map_mean"]],
    pd.read_csv("results/table7_ablation.csv").set_index("variant")[["f1_3cls_mean", "map_fine_mean"]]
      .rename(columns={"f1_3cls_mean": "edufuse_3cls_wf1_mean", "map_fine_mean": "edufuse_fine_map_mean"}),
])
rep = rep[~rep.index.duplicated()]
rec = pd.read_csv("results/recomputed/edufuse_summary.csv", header=[0, 1], index_col=0)
for m in rec.index:
    if m not in rep.index:
        print(f"{m}: not in paper tables")
        continue
    for col, rc in [("edufuse_3cls_wf1_mean", ("wf1_3cls", "mean")), ("edufuse_fine_map_mean", ("map_fine", "mean"))]:
        diff = rec.loc[m, rc] - rep.loc[m, col]
        flag = "OK" if abs(diff) <= 0.05 else "MISMATCH"
        print(f"{m:34s} {col:24s} paper={rep.loc[m, col]:5.1f} recomputed={rec.loc[m, rc]:5.1f} {flag}")
