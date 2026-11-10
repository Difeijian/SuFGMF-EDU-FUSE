# SuFGMF / EDU-FUSE — release materials

Materials accompanying *A Su-Field Analysis-Guided Multimodal Fusion Framework for Conflicting, Degraded, and Missing Modalities: Application to Classroom Interaction Analysis*.

> **Status:** this repository currently contains the results **as reported in the paper**, the machine-readable rule set, the configuration, and the evaluation code. The per-clip annotations, split indices, derived features, and predictions listed in the paper's data-availability statement still need to be added from the original experiment outputs (see `data/README.md`).

## Contents

```
results/     values reported in the paper (Tables 5–7, Fig. 5, scattered scalars) — summary statistics only
rules/       the 18 author-defined fusion rules (Table 1) in JSON
configs/     hyperparameters (Table 3, Section 5.3); fields not reported in the paper are null
data/        data README and empty CSV templates for the per-clip release
scripts/     evaluate.py (recompute metrics from per-clip files), compare_with_paper.py
DATASHEET.md datasheet for EDU-FUSE (partly filled from the paper; TODO items need the authors)
```

## Reproducing the reported numbers

```bash
pip install -r requirements.txt
cp data/templates/*.csv data/            # then replace with the real exported files
python scripts/evaluate.py --data data --out results/recomputed
python scripts/compare_with_paper.py     # flags any value that differs from Tables 6–7 by > 0.05 pp
```

## About EDU-FUSE

- 3,847 staged classroom interaction clips (scripted role-play by adult volunteers; no minors; not real lessons; not synthetic).
- Mean duration 8.3 s; audio 16 kHz; video 25 fps; synchronized transcripts.
- Labels: 3 tolerance levels (tolerant / ambiguous / intolerant) and 8 behavior classes (C1–C8, see `DATASHEET.md`).
- Session-wise stratified split 70 / 15 / 15.
- Raw recordings contain identifiable video and voice and are available only under a non-commercial data-use agreement.

## Intended use

Research on multimodal fusion, and aggregate, post-hoc support for teacher reflection. **Not** for monitoring, evaluating, or disciplining individual students or teachers, and not for live classroom surveillance. Results on this staged corpus are an upper bound under controlled conditions and do not establish effectiveness in real classrooms.

## Citation

```
TODO: add the final bibliographic entry once published.
```

## License

TODO: choose licenses (e.g., MIT for code, CC BY-NC 4.0 for annotations) and add `LICENSE` files.
