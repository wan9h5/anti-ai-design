# Initial evaluation record

Latest evaluation: all 12 scenarios were executed on 2026-10-09: 4 pass, 8 partial; 33 jsdom checks pass. Artifact browser/visual/native-input checks remain unperformed. [Full record](runs/2026-10-09/report.md).

Date: 2026-10-09. Scope: the initial publication candidate, not a usability or cross-model benchmark.

## Method and candidate

Two agent contexts used the skill on synthetic tasks. They were instructed to read SKILL.md and selected resources, and not inspect the repository examples or scenario rubrics; both reported honoring that boundary. The maintainer reviewed their artifacts, browser checks, and findings afterward. The exact model build was not recorded, and the contexts shared an execution environment.

The evaluation led to two instruction clarifications: distinguish a written screenshot description from an inspected image; explicitly assert the active focus target after dynamic list changes. AP018's wording was also refined to connect visual sameness to task/brand reasoning while retaining familiar-style exceptions. These editorial changes were checked for package integrity; the full 12-scenario suite was not rerun or completed.

## Results

| Task | Evidence and result | Limits |
| --- | --- | --- |
| Create an incident triage interface with synthetic records and real local filters/claims | A concrete [HTML artifact](artifacts/incident-console.html), inspected source/screenshots, and [26 final browser checks](artifacts/incident-console-checks.json). Filter, claim, undo, release, reload persistence, selected-detail coherence, keyboard operations and focus recovery passed after repair. | One synthetic task, one desktop browser engine. Narrow smoke check at 320 CSS px; no full zoom, screen-reader, storage-failure or operator study. |
| Review a written description of a three-panel synthetic workbench | Preserved fixed-demo/no-LLM disclosures, deterministic exact results, tables/downloads/provenance, and a plausible three-stage task. Raised a provisional wording concern with a contextual exception and a concrete validation; did not invent behavior, geometry, contrast, performance or clinical evidence. | A description review, not inspection of the original image or runnable product. |
| Assess blanket icon-target and zero-axis rules | Correctly distinguished icon artwork from hit targets, AA 24 CSS px with exceptions from enhanced AAA 44 CSS px, and bar magnitude from suitable non-zero line/dot ranges. Rechecked W3C/WAI and Government Analysis Function guidance. | No actual target geometry or chart product was supplied; no product conformance verdict. |
| Refactor a stale-result demo | Reproduced the original configuration mismatch and an empty-value-as-zero defect. Delivered a [working refactor](artifacts/quality-gate.html) with applied configuration, stale/current/history labels, retained provenance, explicit in-page history limits and input recovery. [15 final browser checks](artifacts/quality-gate-checks.json) passed; the first implementation passed 14 checks before one additional Enter/focus check. | One synthetic task. A requested desktop window of 1280 × 900 was not treated as measured inner viewport; 360 CSS px smoke check does not establish WCAG reflow. No complete Tab or assistive-technology evaluation. |

## Failure history: creation

The first keyboard-drilldown failure came from a test harness Enter sequence that did not activate the native button. A later focus-style test used programmatic focus after pointer input, which did not establish keyboard modality. Corrected native key sequences resolved those harness defects.

An interim passing claim test asserted ownership/row changes but omitted the actual focus object. Tightening it reproduced a real implementation defect: a detail-pane claim under the Unclaimed filter removed the selected record and left focus on the page body. The prototype was repaired to focus the next visible heading or the empty-state recovery button. Direct active-element assertions then covered claim, final-item removal, keyboard undo, and release. The final 26-check result is a corrected rerun, not a first-pass claim. The skill had already required keyboard/focus checks.

## Environment and repeatability

The behavior checks used an installed Chrome 154.0.8037.97 headless browser with browser-native pointer/keyboard input through its debugging protocol and DOM/storage assertions. No new browser or library was installed. Creation used 1440 × 1050 CSS px with device scale factor 1 and a 320 × 960 narrow check.

Published HTML files are self-contained and fully synthetic. Open them locally to inspect or repeat their tasks. Published source copies use LF line endings and a single final newline; this formatting does not change the executed program logic. The compact result files identify those published copies with hashes and named checks; local browser profiles, internal tooling paths, private screenshots and raw conversations are excluded. The environment-specific automation harness and diagnostic captures are not bundled. Manual repetition or a new harness is required to independently reproduce browser checks.

The offline package provides a GitHub Actions workflow for package/regression checks. Automated CI is not enabled in the initial public branch: available publishing credentials cannot write workflow files, so that definition is excluded from the public branch. The package/regression checks were run locally; browser scenarios are separate. The [12 scenario rubrics](scenarios.json) provide further tasks, including cases not executed here.

## What this establishes

This limited forward use demonstrated concrete creation and refactoring, bounded review reasoning, valid exceptions, and a verification loop that caught a real implementation defect. It does not demonstrate prevalence in AI-generated UI, broad model reliability, measured usability improvement, whole-product WCAG conformance, clinical validity, or absence of every possible security/privacy issue.
