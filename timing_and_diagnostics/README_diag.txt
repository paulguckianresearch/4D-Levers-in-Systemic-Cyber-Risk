Paper 4D mechanism-validation package v0.1 (2 November 2026)

Extract into the SAME folder as the timing pilot v0.2 (it needs engine_4c_v027.py,
timing_engine.py and selection.json from that package; copies are included here
with identical digests, see manifest.json). Python 3.10+ and numpy only.

  python check_diag.py                      exact self-checks, about 7 s; must print PASS
  python run_diag.py --benchmark            runtime estimate for your machine
  python run_diag.py --out diag_v01 --workers 8

Hosted measurement: 94 tasks, 33 s on 2 workers (0.35 s per 600-tick run). On 8
workers expect well under a minute. run_diag.py refuses to start if check_diag.json
is missing or stale.

Read PROTOCOL_diag.md first: section 5 is the first result from the hosted run,
section 6 the rulings it needs from you. diag_v01/ holds that run's report and data.

Files
  diag_engine.py    DiagEngine: run_ticks, snapshot, state rows, burst, capacity, forced capture
  diag_common.py    builder reproducing run_timing.simulate exactly, with dial overrides
  check_diag.py     six exact checks (loop fidelity, checkpoint, branch isolation, cadence, capture, burst)
  run_diag.py       the three audits, the report, the manifest
  PROTOCOL_diag.md  definitions, placeholders, first result, rulings needed
  diag_v01/         diag_report.md, diag_results.jsonl.gz, manifest.json from the hosted run
