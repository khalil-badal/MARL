# MARL — Bus Scheduling Thesis (Group B3)

**Title:** An Evaluation of Multi-Agent Reinforcement Learning for Dynamic Bus
Scheduling Under Non-Ideal Conditions
**Institution:** University of Santo Tomas, ECE 21126
**Status:** Undergraduate thesis proposal, ACCEPTED with major revisions —
currently incorporating RTC panel feedback ahead of the August 8, 2026
resubmission deadline.

This repository holds the LaTeX manuscript **and** a structured workflow for
using an AI coding assistant (Claude Code, or similar) to carry out the
panel's requested revisions accurately, with every change tracked and every
factual claim checkable against its source.

---

## Start here if you're an AI assistant

Read these three files, in order, before touching anything:

1. **[`CLAUDE.md`](CLAUDE.md)** — the full rulebook. No data fabrication, no
   citation fabrication, how the revision queue works, how to log changes,
   what's currently blocked and why. This is the actual instruction set;
   everything below is just a map to help you navigate faster.
2. **[`REVISION_QUEUE.md`](REVISION_QUEUE.md)** — the live task list. Every
   panel comment is a checkbox item with file/section/instruction/constraint.
   Check this for current status before assuming anything is done or pending.
3. **[`RTC_DECISION_LETTER.md`](RTC_DECISION_LETTER.md)** — the verbatim,
   unedited panel feedback email. This is the source of truth if anything
   else (including your own memory of a prior session) seems to disagree
   with what the panel actually asked for.

Then, before claiming a task complete, check **[`TRACKER.md`](TRACKER.md)**
for what's already been logged, and consult **[`RRL/sources.md`](RRL/sources.md)**
before trusting any specific factual claim attributed to a citation — several
have already been found wrong by checking against the actual source PDFs
(see the "Source Verification" entries in `TRACKER.md`).

### The REWRITE workflow (applying the user's own writing-style edits)

Once a revision task has landed and shipped, the user may come back with
their own polished version of that same passage — a REWRITE. Do not treat
this as a fresh revision task or reopen `REVISION_QUEUE.md`; it's a
writing-style pass over text that's already substantively correct. Handle it
like this:

1. **Find the entry.** Locate the audit trail entry (in
   `AUDIT_TRAIL_READABLE.md`) whose **AFTER** text matches what the user is
   rewriting. It must currently be tagged `ACTIVE` — never apply a rewrite on
   top of a `SUPERSEDED` or `REVERTED` entry, since that text isn't live in
   the manuscript anymore. If the entry is `mixed`, apply the rewrite only to
   the specific sub-part the user is targeting.
2. **Create a new entry, dated today.** In both `AUDIT_TRAIL.md` and
   `AUDIT_TRAIL_READABLE.md`, append a new entry (not an edit to the old
   one) with:
   - **BEFORE** = the old entry's **AFTER** text, quoted exactly as it
     appears there
   - **AFTER** = the user's REWRITE text, quoted exactly as supplied
   - a `**Status:** ACTIVE` tag
   - a one-line `**Why:**` noting this is a user-supplied writing-style
     rewrite of the entry it follows (name that entry by its task ID/date)
3. **Update the manuscript.** Apply the REWRITE text to the actual `.tex`
   file, replacing the old AFTER text exactly where it lives.
4. **Leave the original entry alone.** Don't retag the original entry as
   SUPERSEDED — the rewrite is a style pass, not a substantive replacement,
   and the original entry is still the correct historical record of what the
   RTC comment actually required. The new entry's BEFORE/AFTER makes the
   lineage from original → rewrite fully traceable on its own.
5. **BEFORE/AFTER must be real quoted text, never narration.** Don't write
   "the paragraph was reworded to sound more natural" — quote the actual
   sentences, exactly as they read in the .tex file, with the changed part
   bolded in the AFTER block. No `...` truncation either: if a sentence is
   long, quote all of it.

## Start here if you're a human contributor

Same files, different angle: `REVISION_QUEUE.md` tells you what's left to
do and what's blocking it (mostly: waiting on dataset access, or waiting on
someone to pull the missing presentation figures from the defense slides).
`AUDIT_TRAIL_READABLE.md` is the fastest way to see what an AI session
actually changed in plain English, without reading raw LaTeX diffs.

---

## Repository map

**Manuscript source** (what compiles into the actual thesis):
```
main.tex            preamble, \input list — do not restructure
title.tex            title page
introduction.tex     Chapter 1 — Introduction and Literature Review
problem.tex          Chapter 2 — Problem Statement
methods.tex          Chapter 3 — Methods and Research Design
results.tex          Chapter 4 (not yet written — commented out of main.tex)
discussion.tex       Chapter 5 (not yet written — commented out of main.tex)
futurework.tex       (not yet written — commented out of main.tex)
appendix.tex         (not yet written — commented out of main.tex)
ai_declaration.tex   AI-use declaration (currently empty)
thesis_refs.bib      bibliography
```

**Revision workflow** (how the manuscript gets edited, and how that's tracked):
```
CLAUDE.md                  rules and process for an AI revision agent
REVISION_QUEUE.md          live task list, one checkbox per panel comment
TRACKER.md                 per-task change log + conformity-table rows
AUDIT_TRAIL.md             before/after LaTeX diffs, Overleaf-facing
AUDIT_TRAIL_READABLE.md    same diffs, plain English, easier to skim
RTC_DECISION_LETTER.md     verbatim panel feedback (source of truth)
```

**Citation verification** (checking that what the manuscript says a paper
found is actually what that paper found):
```
RRL/                local copies of cited papers, gitignored (copyrighted,
                     not pushed — see RRL/.gitignore rule in the root .gitignore)
RRL/sources.md       maps bib keys to local PDF filenames, tracks which
                     citations have actually been checked against source text
                     vs. only filename-matched
```

**Not tracked by this workflow:** the conformity-of-revisions document itself
(a Word/PDF form signed by the thesis adviser) lives outside this repo's
scope — `TRACKER.md`'s conformity-table rows are meant to be copy-pasted into
that form, not a replacement for it.

---

## Why this workflow exists

Early in this revision process, an AI session drafted a "Dataset Description"
section using placeholder-tagged numbers but confidently-worded qualitative
claims about a dataset the group doesn't actually have access to yet. It was
caught and reverted before commit (see `TRACKER.md`, "Reverted Work"), but it's
the reason `CLAUDE.md` has explicit rules against describing anything the
group hasn't verified firsthand — and the reason `RRL/sources.md` exists:
a separate pass through the same manuscript found citations that misstated
what their source papers actually said (a "freeway" that was really an
arterial road, a comparison to continuous action spaces that doesn't exist
in the cited paper, a clip range attributed to the wrong source paper). Both
kinds of mistakes are easy for an AI to make confidently and hard to catch
without deliberately checking. The queue/tracker/audit-trail/source-index
system exists to make that checking systematic instead of hopeful.

## Deadline

Revised proposal manuscript + signed conformity of revisions due
**August 8, 2026**, per `RTC_DECISION_LETTER.md`.
