# Data formats

`templates/` contains **empty CSV headers only**. Copy them to `data/`, then fill them with files exported from the real EDU-FUSE annotations and the real model runs. Do not fill them with values reconstructed from the paper or with simulated data.

| File | One row per | Columns |
|---|---|---|
| `annotations.csv` | clip | `clip_id`, `session_id`, `duration_s`, `tolerance_level` ∈ {tolerant, ambiguous, intolerant}, `behavior_class` ∈ {C1…C8}, modality availability flags (0/1) |
| `problem_type_annotations.csv` | clip with expert problem-type labels (incl. the N = 200 reliability sample) | labels ∈ {HF, IF, HS, AF} from each annotator, plus the adjudicated label |
| `splits.csv` | clip | `split` ∈ {train, val, test}; session-wise, no session in more than one split |
| `predictions_edufuse.csv` | clip × method × seed (test split) | predicted level and class, softmax scores for C1–C8, predicted problem type (SuFGMF variants only, else empty) |
| `predictions_benchmark.csv` | sample × method × seed | native label and prediction for CMU-MOSEI, MUStARD, HateMM |

Derived modality features (768-d encoder outputs, e.g. `features/{text,audio,video}/<clip_id>.npy`) are usually too large for GitHub; host them on Zenodo/OSF/Hugging Face and link them here.
Raw video and audio are **not** distributed in this repository. Access is under the data-use agreement described in the paper.
