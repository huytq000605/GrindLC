# Backtracking (Mental Checklist)

**Idea:** When building a solution one position at a time, frame each step as two questions about the *current index*: which number to place here, and whether that number has already been tried here. These prompts catch the common pitfalls in subset, combination, and permutation problems.

## Questions to Ask at Each Step

- **Which number do we use for this index?**
- **Have we used this number for this index before?** (avoid revisiting the same choice / duplicates)

## Quick Rules

- If we care about the **sequence/order** of things in `current`, then sort `nums` first.
- If we are finding a **permutation**, swap the number within `nums`.
