# DEVELOPER_HANDBOOK.md

## A practical guide to learning Python, Git, GitHub, and building a portfolio

**For:** A 14-year-old learner in England who knows Python basics and
wants to explore programming fields while building real skills.\
**Suggested pace:** Around 4--5 hours per week, adjustable around school
and other activities.\
**Guiding principle:** Build things you understand. Consistency,
curiosity, and reflection matter more than rushing.

------------------------------------------------------------------------

## Contents

1.  [Learning approach](#1-learning-approach)
2.  [12-week roadmap](#2-12-week-roadmap)
3.  [Git and GitHub explained](#3-git-and-github-explained)
4.  [A beginner-friendly Git
    workflow](#4-a-beginner-friendly-git-workflow)
5.  [Repository structure and
    hygiene](#5-repository-structure-and-hygiene)
6.  [Writing a useful README](#6-writing-a-useful-readme)
7.  [Responsible AI use](#7-responsible-ai-use)
8.  [Portfolio and CV advice](#8-portfolio-and-cv-advice)
9.  [Exploring different programming
    fields](#9-exploring-different-programming-fields)
10. [Free learning resources](#10-free-learning-resources)
11. [Weekly reflection template](#11-weekly-reflection-template)

------------------------------------------------------------------------

## 1. Learning approach

You already have a useful foundation: loops, lists, dictionaries,
functions, classes, and basic file operations. The next step is to
combine those concepts in a program that solves a clear problem.

### A good learning loop

1.  Understand the problem and the expected behaviour.
2.  Break it into small parts and make a plan.
3.  Try implementing one small part.
4.  Run it and observe what happens.
5.  Debug unexpected behaviour.
6.  Test normal cases and edge cases.
7.  Record what you learned and commit a working checkpoint.

You do not need to understand every advanced topic before starting.
Learn what you need for the next small step, then return to broader
topics as they become relevant.

### A reasonable weekly rhythm

For a 4--5 hour week, you might spend: - 2--3 hours building or
improving a project. - About 1 hour learning a concept or reading
documentation. - About 30--60 minutes testing, documenting, reviewing,
or using Git.

Treat this as a flexible guide, not a rule. A smaller amount of steady
work is better than burning out.

------------------------------------------------------------------------

## 2. 12-week roadmap

This is a suggested route, not a deadline. Spend longer on a stage if it
is useful. The goal is to finish projects you can explain, not to tick
every box quickly.

### Month 1 --- Build the Personal Task Manager

**Week 1: Understand and plan** - Read `PROJECT_BRIEF.md`. - Identify
the core features and edge cases. - Decide what the user experience
should look like. - Start a `PROGRESS.md` file with goals and
questions. - Set up a local project folder and, if ready, a Git
repository.

**Week 2: Core interactions** - Work on the menu and basic task
operations. - Focus on one feature at a time. - Try invalid input
deliberately. - Make small commits when a meaningful part works.

**Week 3: Data and persistence** - Work with the task fields and stable
IDs. - Save and load data using JSON. - Test the program across
restarts. - Consider missing files and malformed data.

**Week 4: Quality and presentation** - Add priority, optional due dates,
and filters if not already complete. - Test edge cases and add automated
tests with `pytest` when ready. - Write a clear README. - Review the
code and list limitations or future improvements.

**Month 1 outcome:** A usable command-line task manager with documented
behaviour and a sensible testing effort.

### Month 2 --- Algorithms and a data project

**Week 5: Algorithms and data structures** - Practise searching,
sorting, counting, and choosing appropriate data structures. - Learn the
basic idea of time complexity: how work grows as input gets bigger. -
Use beginner exercises rather than memorising solutions.

**Week 6: Plan a CSV data explorer** - Choose a small, public,
non-sensitive dataset. - Decide what questions the program should
answer. - For example: How many rows are there? What are the minimum,
maximum, average, or most common values?

**Week 7: Explore and analyse** - Read a CSV file. - Validate missing or
unexpected values. - Calculate useful summaries. - Consider charts with
`matplotlib` after the basic analysis works. `pandas` is optional; first
understand the data.

**Week 8: Finish and document** - Test empty files, missing columns, and
invalid values. - Add example output and setup instructions. - Explain
the source of the data and any limitations. - Publish a clean
repository.

**Month 2 outcome:** A second project showing data handling, analysis,
and communication.

### Month 3 --- Explore a programming specialism

Choose **one** path that genuinely interests you. You do not need to try
all of them at once.

**Week 9: Explore and choose** - Try a short tutorial or tiny experiment
in one field. - Write down what you enjoyed and what confused you. -
Pick a small project with a clear finish line.

**Week 10: Build a small prototype** - Focus on one useful feature. -
Keep the scope small enough to finish. - Read official documentation as
needed.

**Week 11: Test and improve** - Fix bugs. - Improve the user
experience. - Add tests or a repeatable way to check behaviour. - Ask
someone to try it and note where they get confused.

**Week 12: Polish and reflect** - Write a README. - Make sure the
project runs from a clean setup. - Add screenshots or a short demo only
if they help explain the project. - Review your three months: what can
you now do independently, and what do you want to learn next?

**Month 3 outcome:** A small exploratory project and a better idea of
which area you want to study further.

### What counts as success after 12 weeks?

A good result might be: - One finished task manager. - One finished data
explorer. - One small exploratory project or prototype. - Three readable
repositories or a clear plan for polishing them. - A record of what you
learned and what you would improve.

It is completely fine to have two strong projects instead of three.
Quality, understanding, and honest documentation matter more than
quantity.

------------------------------------------------------------------------

## 3. Git and GitHub explained

These tools are related, but they are not the same thing.

-   **Git** is a version-control tool. It records changes to files so
    you can inspect history and return to earlier versions.
-   **GitHub** is an online service that hosts Git repositories and adds
    collaboration, issues, pull requests, and project pages.
-   **Repository (repo)** is the project folder and its tracked history.
-   **Commit** is a named snapshot of changes. A commit message should
    describe what changed.
-   **Branch** is a separate line of work. You can learn branches later;
    they are not necessary for your first project.
-   **Push** sends local commits to a remote repository such as GitHub.
-   **Pull** brings remote changes into your local repository.
-   **Clone** makes a local copy of a remote repository.
-   **README** explains the project to a person visiting the repository.
-   **`.gitignore`** tells Git which files it should normally leave
    untracked, such as cache files or local configuration.

Git is useful even if you are working alone. It gives you a history of
your work and encourages small, understandable checkpoints.

------------------------------------------------------------------------

## 4. A beginner-friendly Git workflow

You can use the Source Control panel in VS Code or Git commands in its
terminal. Learn what each action means rather than clicking through
without checking.

### One-time setup

1.  Install Git from the official site if it is not already installed.
2.  Configure your Git name and email locally as described in the
    official setup documentation. Consider what email address you want
    visible in public commits.
3.  Open your project folder in VS Code.
4.  Initialise a Git repository or create a GitHub repository and clone
    it.
5.  Add a `.gitignore` and README.
6.  Check which files Git intends to track before making your first
    commit.

### The everyday cycle

1.  **Make a small change.** Pick one feature, fix, or documentation
    improvement.
2.  **Run the program.** Check that it behaves as expected.
3.  **Review the changes.** Look at the diff in VS Code or with Git.
    Make sure you are not including secrets, personal data, temporary
    files, or unrelated edits.
4.  **Stage the intended files.** Staging means selecting what will go
    into the next commit.
5.  **Commit with a meaningful message.** For example, "Validate task
    descriptions" is more informative than "stuff".
6.  **Push to GitHub** when you want the remote copy updated.
7.  **Check the repository online** to confirm that the expected files
    and README are present.

A useful commit represents a coherent change. It does not have to be
large. Avoid making dozens of meaningless commits just to make the
history look busy.

### Common beginner questions

**Do I need GitHub before I start coding?**\
No. You can begin locally and add Git once you are comfortable, or set
it up early to learn gradually.

**Is GitHub the same as a backup?**\
Not completely. A remote repository helps, but it is not a substitute
for understanding what is tracked and keeping important work safe.

**Should I commit every line?**\
No. Commit when you have a meaningful checkpoint, such as a feature that
works or a bug fix.

**What if I make a mistake?**\
Git's history can help you inspect changes and recover work. Before
using commands that discard changes or rewrite history, understand what
they do. If unsure, make a copy of important work and ask for an
explanation before running a destructive command.

**Should my repository be public?**\
A public repository can help you share a portfolio, but only publish
work and information you are comfortable making public. Ask a parent or
guardian if you are unsure about account privacy or online safety.

------------------------------------------------------------------------

## 5. Repository structure and hygiene

Start with a structure that matches the size of your project. Do not
create lots of folders just to make it look professional.

A simple task-manager repository might contain:

-   `main.py` --- the program entry point, if that fits your design.
-   `tests/` --- automated tests as you add them.
-   `README.md` --- purpose, setup, use, testing, and limitations.
-   `PROJECT_BRIEF.md` --- the project requirements, if you want the
    specification in the repository.
-   `PROGRESS.md` --- short notes on progress, questions, and decisions.
-   `.gitignore` --- files Git should not normally track.
-   `requirements.txt` --- only if your project uses external Python
    packages and you need to document them.

If the program grows, you can separate its responsibilities into modules
or a package. Make that change when it helps readability, not just
because a template says you should.

### Typical items to ignore

Depending on your setup, `.gitignore` may exclude: - Python cache
folders such as `__pycache__/`. - Virtual environments such as
`.venv/`. - Local editor or operating-system clutter. - Temporary test
outputs. - A local JSON file containing real personal tasks, if you do
not want that data public.

Do not commit API keys, passwords, tokens, private data, or anything you
would not want public. If you accidentally publish a secret, removing it
from the latest file may not remove it from the repository's history;
revoke or rotate the secret and seek help cleaning up the history.

### Keep a genuine history

Use Git to record real work. Do not fabricate dates, commits,
collaborators, or project claims. A small honest repository is more
valuable than a polished-looking repository that misrepresents your
work.

------------------------------------------------------------------------

## 6. Writing a useful README

The README is the first explanation many people will see. It should let
a new person understand the project and try it without guessing.

Use this checklist:

-   [ ] **Title:** What is the project called?
-   [ ] **Purpose:** What problem does it address?
-   [ ] **Features:** What does the current version actually do?
-   [ ] **Requirements:** Which Python version or packages are needed?
-   [ ] **Setup:** How does someone get a local copy ready?
-   [ ] **Run instructions:** What command or action starts it?
-   [ ] **Usage:** Show example inputs and outputs where helpful.
-   [ ] **Testing:** Explain how tests are run and what they cover.
-   [ ] **Design notes:** Mention important choices you made and why.
-   [ ] **Limitations:** State what is not supported yet.
-   [ ] **Future improvements:** List realistic next steps.
-   [ ] **Credits and assistance:** Acknowledge datasets, tutorials,
    libraries, or substantial help where appropriate.

Keep it accurate. If a feature is planned but not implemented, label it
as a future idea rather than listing it as completed. A short, accurate
README is better than a long, exaggerated one.

------------------------------------------------------------------------

## 7. Responsible AI use

AI can be useful while learning, but the goal is to build your own
understanding.

### Good uses of AI

-   Ask for an explanation of a Python concept in simpler language.
-   Ask for hints rather than a full solution.
-   Share an error message and ask what it means.
-   Ask for possible edge cases you may have missed.
-   Ask for a review of code you wrote and an explanation of trade-offs.
-   Ask for a few test scenarios without asking for the implementation.
-   Ask for feedback on your README or project plan.

### A practical help ladder

When stuck, try these steps in order:

1.  Read the error message carefully.
2.  Identify the smallest part that behaves unexpectedly.
3.  Try a tiny experiment and print or inspect relevant values.
4.  Search official documentation or a trusted tutorial.
5.  Ask for a hint or explanation.
6.  If you look at a suggested solution, close it and try to explain or
    recreate the idea yourself.
7.  Test the result with normal and unusual inputs.

You do not have to follow this exact order every time. The point is to
avoid turning every obstacle into copied code.

### Questions to ask before using AI-generated code

-   Can I explain what each part does?
-   Do I understand why this approach was chosen?
-   Have I run it and tested it myself?
-   Have I checked for incorrect assumptions or unnecessary complexity?
-   Does it fit the project requirements?
-   Did I avoid sharing private information, credentials, or sensitive
    files?

If you cannot explain a piece of code, ask for a smaller explanation or
rewrite that part yourself. Do not include code simply because it runs.

### Be honest about assistance

Follow the rules of any course, competition, school assignment, or
application. If AI or another person made a substantial contribution,
describe that honestly when appropriate. You should be able to
distinguish your own decisions and understanding from outside
suggestions.

Never paste passwords, API keys, private messages, or sensitive personal
data into an AI tool. Check code suggestions carefully, especially
anything involving file deletion, network access, security, or
installing packages.

------------------------------------------------------------------------

## 8. Portfolio and CV advice

At 14, you have plenty of time to explore. A portfolio is a way to show
what you have learned; it is not a contest to collect the largest number
of projects.

### What makes a good beginner portfolio?

-   A few projects that actually run.
-   Clear READMEs and setup instructions.
-   Evidence that you tested normal behaviour and edge cases.
-   A genuine Git history showing development.
-   Honest notes about what you built, what you learned, and what
    remains limited.
-   Projects you can explain without relying on a script or someone
    else's explanation.

Two well-understood projects can be stronger than many unfinished
projects.

### Example CV entry

Adapt this only after the features are genuinely implemented:

**Personal Task Manager --- Python, JSON, Git, pytest**\
- Developed a command-line application to create, prioritise, and track
tasks. - Implemented task persistence using JSON and validation for user
input. - Added tests for key behaviours and common error cases. -
Documented setup, usage, design decisions, and limitations in a README.

Remove or change any claim that is not true of your actual project. Do
not claim professional experience, advanced expertise, or features you
have not built.

### What to record as you work

Keep notes about: - A bug you found and how you diagnosed it. - A design
choice and why you made it. - An edge case you added a test for. -
Something you initially misunderstood. - A feature you chose not to add
and why. - What you would do differently in a second version.

These notes help you explain your work in a README, interview,
application, or conversation with a teacher.

### University and future work

Projects can complement academic study, but they do not replace course
requirements or schoolwork. For computer science, maths is useful, so
keep developing your maths alongside programming. Check the specific
entry requirements for courses you may consider later; requirements vary
and can change.

------------------------------------------------------------------------

## 9. Exploring different programming fields

After your first project or two, choose a small experiment based on
curiosity.

### Games

Try **Pygame** to learn about game loops, input, collision, and
graphics. Start with something tiny, such as moving a shape around the
screen or a simple reaction game.

### Web development and APIs

Try making requests to a public API or building a small API with
**FastAPI**. Learn what HTTP requests and JSON responses are. Keep keys
private and follow the API's rules.

### Data analysis

Use a small public dataset, Python's CSV tools, and eventually
**matplotlib** for charts. **pandas** can help with larger tabular data,
but it is worth learning the underlying data operations too.

### AI and machine learning

Start with the idea of training and evaluating a model using
**scikit-learn** and a small, appropriate dataset. Understand the data
and limitations; do not assume a model is accurate just because it
produces an answer.

### Cybersecurity

Use legal, deliberately designed learning environments such as
**picoCTF**. Practise only on systems you own or have explicit
permission to test. Never probe real websites or networks without
permission.

You do not have to pick a permanent specialism now. Trying small
projects is a sensible way to discover what you enjoy.

------------------------------------------------------------------------

## 10. Free learning resources

These links were selected as starting points. Some platforms offer
optional paid features, but the linked learning material or beginner
access is free. Check current terms and age/account requirements where
relevant.

### Python and development tools

-   [Official Python Tutorial](https://docs.python.org/3/tutorial/) ---
    reference for core Python concepts.
-   [VS Code: Getting Started with
    Python](https://code.visualstudio.com/docs/python/python-tutorial)
    --- setting up and running Python in VS Code.
-   [pytest documentation: Get
    Started](https://docs.pytest.org/en/stable/getting-started.html) ---
    writing and running automated tests.
-   [Git official documentation](https://git-scm.com/doc) --- Git
    reference and guides.
-   [GitHub Skills](https://skills.github.com/) --- guided interactive
    GitHub exercises.
-   [GitHub Hello
    World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
    --- repositories, branches, commits, and pull requests.

### Structured courses and practice

-   [CS50x](https://cs50.harvard.edu/x/) --- a free introductory
    computer science course; it is broader and more challenging than a
    Python-only course.
-   [Exercism: Python track](https://exercism.org/tracks/python) ---
    practice exercises with explanations and mentoring features subject
    to current availability.
-   [Project Euler](https://projecteuler.net/) --- mathematical and
    programming problems; some become challenging, so start wherever
    appropriate.
-   [Python Tutor](https://pythontutor.com/) --- visualises how code
    executes, useful for understanding variables, lists, and function
    calls.

### Libraries and project paths

-   [Matplotlib
    tutorials](https://matplotlib.org/stable/tutorials/index.html) ---
    plotting and charts.
-   [pandas getting
    started](https://pandas.pydata.org/docs/getting_started/index.html)
    --- tabular data analysis.
-   [Pygame documentation](https://www.pygame.org/docs/) --- game
    programming.
-   [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) ---
    building APIs.
-   [scikit-learn getting
    started](https://scikit-learn.org/stable/getting_started.html) ---
    machine learning basics.
-   [picoCTF](https://picoctf.org/) --- cybersecurity learning
    challenges designed for practice in a safe environment.

You do not need to follow every link. Choose one resource that helps
with your current task, then return to building.

------------------------------------------------------------------------

## 11. Weekly reflection template

Copy this section into `PROGRESS.md` each week and fill it in briefly.

### Week of: YYYY-MM-DD

## **What I planned to do**

## **What I actually completed**

## **What I learned**

## **A bug or problem I solved**

## **What I tested**

## **What I still do not understand**

## **A decision I made and why**

## **My next small goal**

## **Git checkpoint or commit worth noting**

The purpose is not to produce impressive notes. It is to notice
progress, identify gaps, and make the next session easier to start.
