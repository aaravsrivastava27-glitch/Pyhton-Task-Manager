# PROJECT_BRIEF.md

## Python Portfolio Project: Personal Task Manager

**Audience:** A 14-year-old Python learner who knows the basics of
loops, lists, dictionaries, functions, classes, and simple file
operations.\
**Project type:** Command-line application\
**Suggested tools:** Python 3, a code editor such as VS Code, Git,
GitHub, and later `pytest` for automated tests\
**Primary goal:** Build a useful program independently, practise
problem-solving, and learn how to test, document, and explain your own
work.

------------------------------------------------------------------------

## 1. Project purpose

Create a command-line Personal Task Manager that lets a user keep track
of tasks. It should be simple enough to build with core Python, but
substantial enough to practise organising data, validating input,
handling errors, saving information, and testing edge cases.

This is a learning project, not a race to write the most code. Aim to
understand every feature you implement and be able to explain your
design choices. You do not need to add every optional enhancement for
the project to be worthwhile.

## 2. Scope

The finished program should let a user:

-   Add a task.
-   View saved tasks and their details.
-   Mark a task as complete.
-   Delete a task.
-   Set a priority.
-   Optionally set a due date.
-   Filter tasks to find relevant items.
-   Keep tasks between program runs using a JSON file.
-   Recover gracefully from ordinary mistakes and common file problems.

The program is intended for one user on one computer. A graphical
interface, online accounts, synchronisation, and a database are not
required.

## 3. Functional requirements

### 3.1 Main menu

-   Display a clear menu of available actions.
-   Let the user choose an action.
-   Keep running so the user can perform several actions in one session.
-   Include a clear option to quit.
-   Handle unknown menu choices without crashing.

### 3.2 Add a task

-   Ask for a task description.
-   Reject a description that is empty or contains only whitespace.
-   Ask the user to choose a priority: **Low**, **Medium**, or **High**.
-   Allow a due date to be omitted.
-   If a due date is provided, accept a valid date in `YYYY-MM-DD`
    format.
-   Give each task a unique ID.
-   Confirm when a task has been added.

### 3.3 View tasks

Show the tasks in a readable format. For each task, display:

-   ID
-   Description
-   Priority
-   Due date, or a clear indication that no due date is set
-   Completion status (for example, incomplete or complete)

If there are no tasks, show a helpful message rather than an empty or
confusing display.

### 3.4 Complete a task

-   Ask which task ID the user wants to complete.
-   Mark that task as complete if the ID exists.
-   Explain clearly if the ID is invalid or does not match a task.
-   Avoid silently changing a different task.
-   Decide and document what happens if the user tries to complete a
    task that is already complete.

### 3.5 Delete a task

-   Ask which task ID the user wants to delete.
-   Delete only the task with that ID.
-   Explain clearly if the ID is invalid or does not exist.
-   Confirm successful deletion.
-   Keep the IDs of remaining tasks stable. Deleting one task must not
    accidentally change the identity of another task.

A confirmation prompt before deletion is a sensible optional
improvement.

### 3.6 Priority

Every task must have one of these priority values:

-   Low
-   Medium
-   High

Reject or reprompt for invalid values. Display priority consistently.
You may choose whether the user enters the priority by number or by
name, as long as the behaviour is clear.

### 3.7 Due date

-   A due date is optional.
-   If entered, it must be a real calendar date in `YYYY-MM-DD` format.
-   Reject impossible dates such as `2026-02-30`.
-   Make it clear to the user how to leave the due date blank.
-   Display dates consistently.

You do not need to warn about overdue tasks in the first version; that
can be a future enhancement.

### 3.8 Filters

Provide ways to show:

-   All tasks
-   Incomplete tasks
-   Completed tasks
-   Tasks of a selected priority

Filtering should affect what is displayed, not delete or alter tasks. If
a filter matches no tasks, show a useful message.

### 3.9 Saving and loading

-   Save tasks to a local JSON file so they remain available after the
    program closes.
-   Load previously saved tasks when the program starts.
-   Save changes after operations that alter task data, or otherwise
    ensure that the user can save changes safely before quitting.
-   Use a predictable file location and explain it in the README.
-   Handle the case where the save file does not exist yet. On a first
    run, the program should still start normally.
-   Handle unreadable or malformed JSON without an unexplained crash. Do
    not silently overwrite a damaged file and destroy recoverable data
    without warning.
-   Do not store passwords, private information, or sensitive personal
    data in the task file.

## 4. Task data fields

Each task should contain these fields:

  -----------------------------------------------------------------------
  Field                   Purpose                 Expected value
  ----------------------- ----------------------- -----------------------
  `id`                    Identifies the task     Unique, stable
                                                  identifier

  `description`           Explains what needs     Non-empty text
                          doing                   

  `priority`              Indicates importance    `Low`, `Medium`, or
                                                  `High`

  `due_date`              Optional deadline       Valid `YYYY-MM-DD` date
                                                  or no date

  `completed`             Records whether the     Boolean status: true or
                          task is finished        false
  -----------------------------------------------------------------------

These are field names for the data model, not a required internal
implementation. You may organise the program in a way that makes sense
to you, provided the required behaviour is met.

### ID expectations

IDs must uniquely identify tasks. They should not be based only on a
task's current position in a displayed list if that would cause another
task to receive a different identity after deletion. Decide how new IDs
are assigned and document the choice.

## 5. Expected behaviour and quality

The program should be:

-   **Understandable:** menu labels and messages make sense to a
    first-time user.
-   **Predictable:** an action does what the menu says it will do.
-   **Resilient:** ordinary incorrect input does not crash the program.
-   **Consistent:** priorities, dates, status labels, and IDs are
    displayed consistently.
-   **Persistent:** normal changes are still present after restarting.
-   **Honest:** messages report what actually happened.
-   **Maintainable:** functions and names are clear, and
    responsibilities are not needlessly tangled.

Keep the first version command-line based. Do not feel you need a
graphical interface or advanced features to make it a successful
project.

## 6. Edge cases to consider

Use these as design questions and tests:

### User input

-   The user enters a blank or whitespace-only description.
-   The user enters an unknown menu option.
-   The user enters letters where a numeric menu choice is expected.
-   The user enters an invalid priority.
-   The user enters a task ID that does not exist.
-   The user enters a blank ID when an ID is required.
-   The user tries to complete or delete a task when there are no tasks.
-   The user tries to complete a task that is already complete.
-   The user provides a very long description or a description with
    punctuation.

### Dates

-   The due date is left blank.
-   The date uses the wrong format.
-   The date contains impossible values, such as month 13.
-   The date has the correct format but is not a real date, such as
    2026-02-30.
-   A valid leap-day date is entered.

### Data and files

-   The JSON file does not exist on first launch.
-   The JSON file contains no tasks.
-   The JSON file is malformed or truncated.
-   The file cannot be read or written.
-   The program is restarted after adding, completing, and deleting
    tasks.
-   A task is deleted and another task is added; IDs must remain
    unambiguous.
-   Saved data is unexpectedly missing or has an unexpected structure.

## 7. Testing checklist

Test the program manually as you build it. Later, add automated tests
with `pytest` where useful. Testing should cover both normal use and
mistakes.

### Core features

-   [ ] Add a task with a valid description.
-   [ ] Add tasks with Low, Medium, and High priorities.
-   [ ] Add a task with a due date.
-   [ ] Add a task without a due date.
-   [ ] View all tasks and check every required field appears.
-   [ ] Complete a task and verify its status changes.
-   [ ] Delete a task and verify the correct task disappears.
-   [ ] Filter incomplete tasks.
-   [ ] Filter completed tasks.
-   [ ] Filter by each priority.
-   [ ] Quit and restart; verify data persists.

### Validation and errors

-   [ ] Blank description is rejected.
-   [ ] Invalid priority is rejected or reprompted.
-   [ ] Invalid menu choice is handled.
-   [ ] Unknown task ID is handled.
-   [ ] Actions with an empty task list are handled.
-   [ ] Invalid and impossible dates are rejected.
-   [ ] Already-completed task behaviour is clear.
-   [ ] No matching filter results are handled helpfully.

### File handling and data integrity

-   [ ] Missing JSON file on first run is handled.
-   [ ] Valid JSON loads correctly.
-   [ ] Malformed JSON does not cause an unexplained crash.
-   [ ] File read/write errors produce a useful message.
-   [ ] IDs remain unique after deleting and adding tasks.
-   [ ] Changes survive restart without unintended loss.

### Code quality

-   [ ] Names are descriptive.
-   [ ] Functions have clear responsibilities.
-   [ ] Repeated logic is reduced where sensible.
-   [ ] Important behaviour is tested, not just the happy path.
-   [ ] The README accurately explains the current state of the project.

## 8. Optional extensions

Only consider these after the core requirements work:

-   Search task descriptions.
-   Sort by priority or due date.
-   Warn about overdue tasks.
-   Edit an existing task.
-   Ask for confirmation before deletion.
-   Export a report to CSV.
-   Add a simple graphical interface.
-   Add more automated tests.

Choose extensions because they help you learn something, not just to
make the project bigger.

## 9. Completion criteria

The project is ready to call a solid first version when:

-   [ ] All required menu actions work.
-   [ ] Tasks have the required fields and stable unique IDs.
-   [ ] Input validation covers common mistakes.
-   [ ] Optional dates are validated properly.
-   [ ] Filters work and do not alter task data.
-   [ ] Tasks persist through normal program restarts.
-   [ ] Missing or damaged files are handled sensibly.
-   [ ] The manual testing checklist has been tried and results
    recorded.
-   [ ] Automated tests cover key behaviour, if you have reached that
    stage.
-   [ ] A README explains purpose, features, setup, usage, tests,
    limitations, and future ideas.
-   [ ] The project is committed to Git, with a `.gitignore` that
    excludes generated or private files where appropriate.
-   [ ] You can explain how the project works, what you found difficult,
    what you tested, and what you would improve next.

**Important:** Completion does not mean the program is perfect. A
finished, understandable project with honest documentation and known
limitations is more valuable than a huge unfinished project.

## 10. Working independently

Treat this brief as the specification, not as a recipe. Plan your own
design, try small experiments, and look up documentation when needed. If
you use AI or another person's help, make sure you understand the
resulting code, verify it, and follow the guidance in
`DEVELOPER_HANDBOOK.md`. Keep notes on decisions and problems you
solved; those notes will help you write the README and discuss the
project later.
