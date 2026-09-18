# CMPT 142 — Introduction to Computer Science for Engineers

Starter code for the lecture demonstrations, in-class exercises, and lab
quizzes in CMPT 142.

Each `week_N/` folder holds the files we open together in class. Most of them
are **deliberately incomplete** — comments describe what the code should do,
and we fill in the rest during the lecture. Blank space in a file is not a
mistake; it is where your work goes.

## Getting started

1. Download or clone this repository:

   ```
   git clone https://github.com/ganglix/CMPT_142_code.git
   ```

2. Open the folder for the current week in your editor.
3. Follow along in class and type the code yourself. Typing it out is the
   point — reading finished code feels productive, but writing it is what
   actually teaches you the material.

## What you need

- **Python 3** — everything runs on a standard Python 3 install.
- **matplotlib** and **numpy** — used in a few later demos:

  ```
  pip install matplotlib numpy
  ```

Everything else comes from the Python standard library.

## Week by week

| Folder | Topics |
|--------|--------|
| `week_0` | Warm-up programs: getting Python running, first look at functions and randomness |
| `week_1` | Data types (`int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`); indexing and slicing sequences |
| `week_2` | Arithmetic and math; writing functions (parameters, arguments, `return`, scope); importing modules; branching with `if` |
| `week_3` | Repetition: `while` and `for` loops; lists and tuples in depth |
| `week_4` | The algorithm → pseudocode → code workflow; testing your functions; dictionaries |
| `week_5` | Reading and writing files; number systems and binary |
| `week_6` | Recursion; search algorithms (linear and binary search) |
| `week_7` | Sorting algorithms (merge sort, quick sort) and comparing their running times |

Exact chapter coverage may shift slightly as the term goes on — the course
schedule is the authority, not this table.

## A note on how to use this repo

Work through each exercise before looking anywhere else for an answer. Getting
stuck, then getting unstuck, is how the ideas stick. If you are stuck for more
than a few minutes, ask in class, in the lab, or at office hours — that is what
they are for.

## File naming

| Pattern | Meaning |
|---------|---------|
| `chNN__intro.py` | Lecture introduction to a chapter's ideas |
| `chNN_demoN.py` | Worked demonstration done at the front of the class |
| `chNN_exN.py` | Exercise for you to complete |
| `quiz*.txt`, `*quiz*.txt` | Lab quiz prompts |
