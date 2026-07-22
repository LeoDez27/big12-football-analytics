# Big 12 Football Analytics — Project Roadmap

*A living document — we'll update this as decisions get made in each phase.*

---

## ✅ Phase 1 — Planning (Complete)

**Decisions locked in:**
- **Target variable:** predicted point margin (`home_score − away_score`) — a regression problem, not win/loss classification
- **Success criteria (tiered framework):**
  - Tier 1: beat naive baselines (sanity check)
  - Tier 2: track the gap between our error and Vegas's error (the metric we improve every iteration)
  - Tier 3: beat Vegas closing lines over a full season (long-term stretch goal, not a v1 requirement)
- **Software stack:** Python, SQL, Power BI, Git/GitHub (matches your learning goals)
- **Database engine:** SQLite (simple, local, file-based — can migrate to PostgreSQL later if needed)
- **Folder structure:**
  ```
  big12-football-analytics/
  ├── data/
  │   ├── raw/
  │   └── processed/
  ├── sql/
  ├── src/
  ├── notebooks/
  ├── docs/
  ├── README.md
  └── .gitignore
  ```
- **Repo:** public, no license (visible to anyone, but not legally reusable without permission)
- **Tools installed:** Python 3.14, VS Code, Git, GitHub account, DB Browser for SQLite
- **Workflow habits:** commit small/complete changes, imperative-mood commit messages, `git status` before ending a session

**Adjustments to the original plan:**
- **Thin vertical slice approach:** rather than fully completing every phase before touching code, we'll get one season + one simple model + one accuracy check working early, to avoid stalling in pure planning.
- **Phase 3/4 order:** we'll draft a rough schema in Phase 3, then revisit it lightly after seeing real data in Phase 4 — schemas often need adjusting once you actually look at messy real-world data.

---

## ⏭️ Phase 2 — Data Sources (Next)

Identify reliable sources for:
- Historical game results
- Team statistics & advanced metrics
- Recruiting rankings, transfer portal, returning production
- Coaching history
- Betting lines (for our Tier 2/3 benchmarks)
- Weather, injury reports (where available)

For each source: why it matters, potential bias, data quality concerns, update frequency.

---

## Phase 3 — Database Design *(draft schema; revisit after Phase 4)*

Tables: Teams, Games, Schedules, Players, Team Stats, Game Stats, Power Ratings, Predictions, Vegas Lines, Weather, Injuries.

---

## Phase 4 — Exploratory Data Analysis

Distributions, outliers, missing values, correlations, visualizations — and revisiting the Phase 3 schema with real data in hand.

---

## Phase 5 — Feature Engineering

EPA/play, success rate, efficiency stats, recruiting/transfer signals, home field advantage, rest/travel, strength of schedule, opponent adjustments, recent form — each justified, each tested for whether it actually improves the model.

---

## Phase 6 — Rating Systems

Compare Elo, Massey, Colley, Sagarin, SP+, efficiency ratings — choose one appropriate for this project.

---

## Phase 7 — Prediction Models

In order: Linear Regression → Logistic Regression → Decision Trees → Random Forest → Gradient Boosting → XGBoost → LightGBM.

---

## Phase 8 — Model Evaluation

This is where Tier 2/3 success criteria get formalized numerically: RMSE, MAE, log loss, Brier score, calibration, cross-validation, feature importance, residual analysis.

---

## Phase 9 — Automation

Automatically updating schedules, results, ratings, predictions, and dashboards — as practical given data source availability/licensing.

---

## Phase 10 — Dashboard (Power BI)

Conference standings, power rankings, win probabilities, spread/total predictions, confidence ratings, prediction history, Vegas comparison, model accuracy.

---

*Mentorship approach throughout: teach before solving, explain trade-offs, ask before showing solutions, never skip understanding for speed.*
