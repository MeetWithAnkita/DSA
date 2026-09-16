🟢 DAY 08 — String Foundation + Basic Operations
Part 1 — Fundamentals
What is a String?
Character vs String
String creation
Indexing
Positive indexing
Negative indexing
len()
Traversal using:
for
range()
enumerate()

Part 2 — Basic Operations
Concatenation
Repetition
Membership: in, not in
Comparison
Slicing
Reverse slicing
String immutability


Part 3 — Important Methods
.lower()
.upper()
.capitalize()
.title()
.swapcase()
.isalpha()
.isdigit()
.isalnum()
.isspace()
.islower()
.isupper()
Practice

Basic problems such as:

Print each character
Count characters
Reverse a string
Count vowels
Count digits
Count spaces
Convert lowercase → uppercase
Remove spaces
Check whether a character exists
🎯 Day 08 Goal

You should become completely comfortable with:

String
 ↓
Index
 ↓
Traverse
 ↓
Process each character




NOTE 
1. Strings are immutable.

That means once a String is created, its individual characters cannot be changed directly.

2. | Method          | Checks / Does                             |
| --------------- | ----------------------------------------- |
| `.lower()`      | Converts to lowercase                     |
| `.upper()`      | Converts to uppercase                     |
| `.capitalize()` | First character uppercase, rest lowercase |
| `.title()`      | First character of each word uppercase    |
| `.swapcase()`   | Upper ↔ Lower                             |
| `.isalpha()`    | Only alphabets?                           |
| `.isdigit()`    | Only digits?                              |
| `.isalnum()`    | Only alphabets/digits?                    |
| `.isspace()`    | Only whitespace?                          |
| `.islower()`    | Lowercase?                                |
| `.isupper()`    | Uppercase?                                |


3.                  STRING
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
   Indexing       Operations       Methods
       │              │              │
       ↓              ↓              ↓
   s[i]          +    *          lower()
   s[-1]         in   not in      upper()
                 ==   !=          capitalize()
                 <    >           title()
                 [:]              swapcase()
                 [::-1]           isalpha()
                                  isdigit()
                                  isalnum()
                                  isspace()
                                  islower()
                                  isupper()


