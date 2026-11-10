# Datasheet for EDU-FUSE

Structure follows *Datasheets for Datasets* (Gebru et al., 2021). Items marked **TODO** are not stated in the paper and must be completed by the authors.

## Motivation
- **Purpose:** testbed for conflict-aware multimodal fusion; target behavior is observable intolerant behavior in classroom interaction (Section 2.3.2).
- **Creators / funding:** TODO

## Composition
- **Instances:** 3,847 interaction clips, each with transcript, audio, and video.
- **Labels:** tolerance level ∈ {tolerant, ambiguous, intolerant}; behavior class ∈ {C1 discriminatory utterance, C2 stereotyping remark, C3 ridicule of difference, C4 verbal exclusion, C5 exclusionary gesture, C6 prejudiced expression, C7 inclusive or respectful engagement, C8 no target behavior}; Su-Field problem type ∈ {HF, IF, HS, AF} for an expert-labeled subset.
- **Label distribution per level / class / split:** TODO (not reported in the paper; compute from `annotations.csv`).
- **Number of sessions, volunteers, scenarios:** TODO
- **Missing modalities:** TODO (counts per modality from availability flags)

## Collection process
- Scripted role-play by adult volunteers acting as students and teachers; no minors.
- Recording: audio 16 kHz, video 25 fps, synchronized transcripts; segmented into episodes (mean 8.3 s).
- **Recording period, location, equipment, script authorship:** TODO
- **Consent and ethics approval (body, protocol number):** TODO

## Annotation
- Level and class assigned using the coding framework in Table 4 of the paper (most salient behavior coded when several co-occur).
- **Who annotated levels/classes, how many annotators, agreement statistics:** TODO
- Su-Field problem types: two TRIZ-trained annotators; reliability sample N = 200; Cohen's κ = 0.79.

## Preprocessing
- Encoders: RoBERTa-base (text), wav2vec 2.0 (audio), Video Swin-T (16 frames per clip).
- **Transcription method (manual / ASR):** TODO

## Uses
- Intended: research on multimodal fusion; aggregate post-hoc support for teacher reflection with human oversight.
- Not intended: monitoring or evaluating individuals, disciplinary decisions, live surveillance.
- Known risks: staged intolerance is more explicit than real behavior; dialectal speech may be disproportionately misclassified; report errors disaggregated by language variety and speaker group.

## Distribution
- Annotations, features, splits, rules, seeds, and predictions: this repository / TODO archive DOI.
- Raw clips: by data-use agreement, non-commercial research only. **Contact / request procedure:** TODO

## Maintenance
- **Maintainer and contact:** TODO
- **Versioning and erratum policy:** TODO
