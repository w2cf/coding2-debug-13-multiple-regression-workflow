"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "d2267abe1637e0425a12027f918933be"
GRADE_HASH = "25f1d9bb90e26dd646c121cabd1774b454377d6fa2a060c6781836fb8fdcd7ba"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
