# Zenodo deposit checklist: Levers in Systemic Cyber Risk, code v1.1

## Before uploading
1. Unzip Levers_Code_v1.1.zip. Copy the output files listed in `outputs/README.md` from the run folders
   into `outputs/` (all small text files; no results.jsonl). From the deposit root run
   `python make_manifest.py`, then zip the folder again as `Levers_Code_v1.1.zip`.
2. On Zenodo: New upload, add the zip, and press "Get a DOI now" (reserve) before filling the form.
   Copy the reserved DOI.
3. Put the DOI in three places: `CITATION.cff` (the `doi:` line, replacing XXXXXXXX), and in the
   manuscript at the title footnote and the Reproducibility section (both `\pending{DOI}`). Re-run
   `make_manifest.py`, re-zip, replace the file on Zenodo.

## Zenodo form
- Resource type: Software.
- Title: Levers in Systemic Cyber Risk: analysis code, timing revision and mechanism-validation package.
- Creator: Guckian, Paul; affiliation Independent Researcher, London, United Kingdom; ORCID if you have one.
- Description: the first two paragraphs of README.md, plus the line "Companion to the manuscript
  'Levers in Systemic Cyber Risk: Which Matter, and When' (under review)."
- Version: 1.1. Publication date: the day you publish. Language: English. Licence: MIT.
- Keywords: systemic cyber risk; global sensitivity analysis; Sobol indices; Morris screening;
  response surface validation; Cyber Triangle; simulation.
- Related identifiers: "Is derived from" 10.5281/zenodo.23669511 (the model's source code);
  "References" 10.5281/zenodo.23669054 (its specifications, protocols and run outputs); when the paper
  has a DOI or preprint, add "Is supplement to" it.
- Do not add this record as a new version of the earlier deposits; it is a new concept record.

## After publishing
- The record page shows the version DOI (this upload) and the concept DOI (all versions). The
  manuscript cites the version DOI.
- Update the manuscript's two DOI fields and CITATION.cff if you used a reserved DOI they already match.
- Archive the large results.jsonl files separately (the paper says so); a second Zenodo record of
  compressed outputs is the pattern used before, and can be added later with "Is supplemented by".
