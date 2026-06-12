# Counting Distinct Subsequences

**Idea:** Track the number of distinct subsequences that **end with each character**. When you process a new character, every existing subsequence can be extended by it, so the new count for that character becomes `Sum(all subsequence counts) + 1` (the `+1` accounts for the single-character subsequence consisting of the new character itself). Storing counts per ending character is what automatically deduplicates repeated letters.

## Examples

- **940. Distinct Subsequences II**
- **1987. Number of Unique Good Subsequences**
