# Python-Series-Lec-02

A collection of Python programs and practice exercises focused on covering strings, indexing, slicing, string methods, escape sequences, and conditional statements.

## 📚 Topics Covered
| # | Topic | Status |
|---|-------|--------|
| 1 | Strings & Escape Sequences | ✅ |
| 2 | Indexing (Positive & Negative) | ✅ |
| 3 | Slicing | ✅ |
| 4 | Negative Slicing | ✅ |
| 5 | String Functions & Methods | ✅ |
| 6 | Conditional Statements (if / elif / else) | ✅ |

## 📂 Practice Files
| File | Topics | Questions |
|------|--------|-----------|
| [01_Strings_Basics.py](01_Strings_Basics.py) | Strings, Escape Sequences, Indexing |  08 |
| [02_Slicing_and_Methods.py](02_Slicing_and_Methods.py) | Slicing, Negative Slicing, String Methods | 06 |
| [03_conditionals.py](03_conditionals.py) | if, elif, else, Nested, Ternary |  09 |
|[04_Challenge.py](04_Challenge.py) | ALL Topics Mixed (Boss Level) |  3 |

## 💡 Quick Cheat Sheet (Lecture 2 Highlights)
<details>

<summary><b>Click to expand quick revision notes</b></summary>

### 1. String Indexing & Slicing
H e l l o <br>
0 1 2 3 4 ← Positive Index <br>
-5 -4 -3 -2 -1 ← Negative Index <br>

s[start : stop : step] <br>
s[1:4] → "ell" <br>
s[::-1] → "olleH" (reverse) <br>
s[-3:] → "llo" <br>

### 2. Most Used String Methods
| Method | What it does |
|--------|-------------|
| `.upper()` / `.lower()` | Change case |
| `.strip()` | Remove whitespace |
| `.replace(old, new)` | Replace substring |
| `.split(sep)` | String → List |
| `.join(list)` | List → String |
| `.find(sub)` | Index of substring (-1 if not found) |
| `.count(sub)` | Count occurrences |
| `.startswith()` / `.endswith()` | Check prefix/suffix |

### 3. Escape Sequences
| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

### 4. Conditional Flow
```python
if condition:
    ...
elif condition:
    ...
else:
    ...

 Python uses indentation (4 spaces) — NOT curly braces.
 Ternary: result = "Yes" if condition else "No" 
 ```
 
</details>

## 📅 Series Progress
- [ ] **Lecture 01 — Basics, Data Types & Operators ✅
- [ ] **Lecture 02 — Strings, Slicing & Conditionals 📍(Current)
- [ ] **Lecture 03** — Coming Soon
- [ ] **Lecture 04** — Coming Soon
- [ ] **Lecture 05** — Coming Soon
- [ ] **Lecture 06** — Coming Soon
- [ ] **Lecture 07** — Coming Soon
- [ ] **Lecture 08** — Coming Soon
- [ ] **Lecture 09** — Coming Soon

## 🤝 Connect & Feedback
If you found this helpful or have any questions:

💬 Found a bug / Have a solution? Open an Issue or submit a Pull Request.

