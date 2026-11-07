# Depositing through GitHub (Zenodo's GitHub integration)

The DOI is minted by Zenodo when a GitHub release is published, so the order matters.

1. Create a new public GitHub repository, for example `levers-systemic-cyber-risk` (no internal paper tags
   in the name or description). Description: "Analysis code, timing revision and mechanism-validation
   package for 'Levers in Systemic Cyber Risk: Which Matter, and When'".
2. Fill `outputs/` from the run folders as `outputs/README.md` lists, run `python make_manifest.py`
   from this folder, then upload the whole folder's contents to the repository (web upload of the unzipped
   folder, or `git init`, `git add .`, `git commit -m "v1.1"`, `git push`). `.zenodo.json` at the root
   supplies Zenodo's metadata; `CITATION.cff` makes GitHub show a "Cite this repository" box.
3. On zenodo.org, log in, Account, GitHub, and switch the repository ON. Do this **before** publishing
   the release; Zenodo only archives releases made after the switch.
4. On GitHub, Releases, Draft a new release: tag `v1.1`, title `v1.1`, description "Analysis freeze for the
   manuscript; model digest d3f90805edfee3c7 unchanged." Publish. Within a few minutes the repository's
   Zenodo page shows the record with a version DOI (this release) and a concept DOI (all versions).
5. Put the version DOI into `CITATION.cff` (the `doi:` line) and into the manuscript's title footnote and
   Reproducibility section, replacing `\pending{DOI}`. Commit that change and publish release `v1.1.1`
   ("metadata: DOI recorded"); the concept DOI is unchanged and the manuscript cites the v1.1 version DOI
   as the code that produced the results.
6. On the Zenodo record, check the metadata came through from `.zenodo.json` (title, licence MIT, the two
   related identifiers). Add "Is supplement to" with the manuscript's DOI or preprint once it exists.

If you would rather not use the GitHub route, the same zip uploads directly on zenodo.org (New upload,
Software); `DEPOSIT_CHECKLIST.md` covers that path, including reserving the DOI before publishing.
