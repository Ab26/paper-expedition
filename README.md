# Learning Expedition

A unified, free study hub for faculty/postdoc preparation and continuing research practice.

## Topic-first preparation

Topics is the default landing view. Browse 56 topics across ML, DL, NLP, CV, DSA, DBMS, CN and advanced research without selecting a date. Every topic has fast/deep tasks, multiple primary-resource links, coding practice, three spoken prompts, notes and editable core-gap/fragile flags. Original deep and fast sessions remain browsable separately.

Start a new review to clear its attempt checkboxes. After attempting every prompt aloud, rate Shaky or Solid. Successful due reviews use gaps of 1/3/7/21 days (normal) or 1/2/5/14/30 days (fragile), repeating the final interval. Shaky resets to tomorrow. Early successful practice does not advance the stage or defer the due date. Review dates are advisory local calendar days; breaks do not block access. No audio recording or automatic reasoning assessment is performed.

Topic progress is stored within the existing complete-hub backup, with validation and backward compatibility for backups without topic records. The paper catalog and its storage keys are unchanged. External course-index links include section guidance; they are not all direct lesson links.

## Included

- 86 dated preparation sessions, 22 September 2026–15 January 2027.
- Six study hours: three deep (including 15 minutes by hand and 30 minutes coding), one fast-track, two paper study. Optional 30-minute revision.
- Sundays, 6–15 November and 15–21 December excluded.
- 98 papers, two reading sessions each, with final-paper target 24 May 2027 under the full routine.
- 24 original hand-worked exercise types, numerical variants, worked solutions and a timer. No paid AI-by-hand material is reproduced.
- Architecture investigation templates, 28 interview prompts, research notebooks and monthly review guidance.
- Lighter continuing routines for after joining a role.
- Browser-local notes and progress, with complete JSON backup/restore.

These are study prompts and selected reference links, not a complete textbook or an automatic AI tutoring service. Hand-exercise checks evaluate numerical answers, not reasoning. Frontier papers should be refreshed when reached. Interview dates are blank until explicitly entered.

## Hosting status

[Open Learning Expedition](https://ab26.github.io/paper-expedition/)

The repository is public with the owner's approval. GitHub Pages is enabled from `main` → `/docs`.

`docs/` contains the complete prebuilt static application for GitHub Pages. No server, database, model API or ChatGPT hosting is required for this build.

The older ChatGPT-hosted app remains a separate deployment. Its saved notes are not automatically migrated. This repository update does not redeploy it.

## Local development

Use Node.js 24 and the pnpm version specified in `package.json`.

```sh
pnpm install --frozen-lockfile
pnpm run dev:pages
pnpm run build:pages
node --test github-pages/tests/*.test.mjs
```

The Pages build uses `github-pages/vite.config.ts` and relative asset URLs. `npm run build` is the legacy Sites build, not the Pages build.

Run `node github-pages/package-standalone.mjs` after building to produce a self-contained HTML copy in `work/`. Download/open that copy in a browser. For local HTML files, storage behavior depends on the browser and file location; export backups regularly. A hosted origin is preferable for stable browser storage.

## Source map

- `hub/Hub.tsx`: unified interface.
- `hub/Topics.tsx`, `hub/topics.json`, `hub/create-topics.py`: topic browser and original curriculum prompts.
- `hub/review.ts`: validated review records and deterministic scheduling.
- `hub/content.json`: daily objectives, coding tasks and interview prompts.
- `hub/create-content.py`: source generator for the curriculum.
- `hub/calendar.ts`: exclusions, preparation dates and paper-session dates.
- `hub/exercises.ts`: original numerical worksheets and worked solutions.
- `app/expedition.tsx`: paper catalog, study panels, concept guides and calendar export.
- `lib/papers.json`: catalog and original source-paper URLs.
- `lib/browser-progress.ts`: validated browser paper progress and backups.
- `github-pages/`: static entry point, styling, build configuration and tests.

User-entered notes, database contents, credentials, dependencies and runtime state are not committed. Browser data does not automatically sync across devices. Anyone using the same browser profile/origin can potentially access its local data; a label or local storage is not authentication.

## Validation

Build and type checking, calendar exclusions and counts, paper completion date, storage/backup round trips, malformed-data rejection and quota failures are checked. The published GitHub Pages site was visually checked: the daily dashboard and 98-paper catalog render, a note persists after reload, and the dot-product exercise correctly checks an answer and reveals its worked solution.
