"""Recompute Table 6 / Table 7 / Fig. 5 metrics from per-clip outputs.

Usage:  python scripts/evaluate.py --data data --out results/recomputed
Requires: pandas, numpy, scikit-learn
"""
import argparse
import os

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, cohen_kappa_score, confusion_matrix, f1_score

CLASSES = [f"C{i}" for i in range(1, 9)]
PTYPES = ["HF", "IF", "HS", "AF"]


def edufuse(d):
    ann = pd.read_csv(f"{d}/annotations.csv")
    spl = pd.read_csv(f"{d}/splits.csv")
    pred = pd.read_csv(f"{d}/predictions_edufuse.csv")
    test = ann.merge(spl, on="clip_id").query("split == 'test'")
    df = pred.merge(test, on="clip_id", how="inner")
    rows = []
    for (m, s), g in df.groupby(["method", "seed"]):
        y = np.stack([(g.behavior_class == c).astype(int) for c in CLASSES], 1)
        p = g[[f"p_{c}" for c in CLASSES]].to_numpy()
        aps = [average_precision_score(y[:, k], p[:, k]) for k in range(8) if y[:, k].any()]
        rows.append({"method": m, "seed": s,
                     "wf1_3cls": 100 * f1_score(g.tolerance_level, g.level_pred, average="weighted"),
                     "map_fine": 100 * np.mean(aps)})
    per_seed = pd.DataFrame(rows)
    summary = per_seed.drop(columns="seed").groupby("method").agg(["mean", "std"]).round(1)
    return df, per_seed, summary


def diagnosis(d, df):
    pt = pd.read_csv(f"{d}/problem_type_annotations.csv")
    both = pt.dropna(subset=["annotator_1", "annotator_2"])
    out = {"n_reliability": len(both),
           "kappa_annotators": round(cohen_kappa_score(both.annotator_1, both.annotator_2), 3)}
    x = df.dropna(subset=["problem_type_pred"]).merge(pt[["clip_id", "adjudicated"]], on="clip_id")
    cms = {}
    for m, g in x.groupby("method"):
        out[f"agreement[{m}]"] = round((g.adjudicated == g.problem_type_pred).mean(), 3)
        cm = confusion_matrix(g.adjudicated, g.problem_type_pred, labels=PTYPES)
        cms[m] = pd.DataFrame(100 * cm / cm.sum(1, keepdims=True), index=PTYPES, columns=PTYPES).round(1)
    return out, cms


def benchmarks(d):
    f = f"{d}/predictions_benchmark.csv"
    if not os.path.exists(f):
        return None
    b = pd.read_csv(f)
    r = (b.groupby(["dataset", "method", "seed"])
          .apply(lambda g: 100 * f1_score(g.label_true, g.label_pred, average="weighted"))
          .rename("wf1").reset_index())
    return r.groupby(["dataset", "method"]).wf1.agg(["mean", "std"]).round(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="results/recomputed")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    df, per_seed, summary = edufuse(a.data)
    per_seed.to_csv(f"{a.out}/edufuse_per_seed.csv", index=False)
    summary.to_csv(f"{a.out}/edufuse_summary.csv")
    print(summary)
    stats, cms = diagnosis(a.data, df)
    print(stats)
    for m, cm in cms.items():
        cm.to_csv(f"{a.out}/diagnosis_confusion_{m.replace(' ', '_').replace('/', '')}.csv")
    bm = benchmarks(a.data)
    if bm is not None:
        bm.to_csv(f"{a.out}/benchmarks_summary.csv")
        print(bm)
