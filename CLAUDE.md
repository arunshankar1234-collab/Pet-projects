# my-projects: notes for Claude

This repo holds Arun's pet projects, which may be shown in interviews, and the practice for a 16-week DSA + system design plan for product-company interviews (Day 1 = Wed 21 Oct 2026, Day 112 = Tue 9 Feb 2027). Python, NeetCode 150 in pattern order.

## Read first

The full plan, the delivery routine, progress and the user's preferences are in:
`/home/arun-bonito/.claude/projects/-home-arun-bonito-bonito-app/memory/user_dsa_interview_prep.md`

Read it at the start of a session, and keep it updated with progress (last day done, problems marked 🟡/🔴 for re-solve). It is the single source of truth; don't copy the plan into this file.

- Plan page: https://claude.ai/artifact/MPJRS5mJEfrxWcZvaZBYZB
- DSA Daily Plan doc (filled by a 7:00 IST routine): https://claude.ai/artifact/7HcbDZVNYh38krSSPxaERR

## How to help

- Teach, don't hand over solutions. Give hints first, and give a full solution only when asked or after a real attempt. Review pasted code for correctness, Big-O and style.
- "Day N" / "today's plan": work out the day from 21 Oct 2026 and give that day's plan.
- Include one short motivational quote (hope, hard work, optimism) with each day's plan or check-in. Only use quotes whose attribution is solid, and don't repeat ones already given (the memory file lists them).
- Explain in plain language. The user is new to some of this.
- The user is also working toward data science roles. DSA is the main track for now; data science is light (about 3–4 h/week) until week 12.

## Repo layout

- `dsa/weekNN/dN_<problem>.py`: one file per problem; re-solves go in `_r2`, `_r3` files.
- `system-design/`: notes, from week 9.
- Pet projects will go in their own top-level folders, each with its own README, since they may be shown to interviewers.
- Remote `origin` is the user's personal GitHub (arunshankar1234-collab/Pet-projects) over the SSH alias `github-personal`, with a repo-local personal email. Never push with the company account (`arun-bonito`) or to the company repo (Squadro). Branch `main`. Commit when the user asks.
- Machine Python is 3.8.10 (`python3`). An upgrade to 3.11+ was offered and not yet done.
