# SortedList (sortedcontainers Internals)

## Idea

`SortedList` from `sortedcontainers` is **not** a balanced BST or a skip list. Internally it keeps a list of sub-lists (`_lists`) plus a list of each sub-list's maximum (`_maxes`), with a default `load_factor` of `1000`. Each sub-list stays sorted, and `_maxes` lets you binary-search to the right sub-list quickly. When a sub-list grows too large it is split in two, which keeps every sub-list bounded in size and keeps operations fast.

## Add an element

To add a value:

1. Binary-search `_maxes` (`bisect_right`) to find which sub-list the value belongs in.
2. If the value is past the last sub-list's max, append it to the final sub-list and update that max.
3. Otherwise `insort` it into the chosen sub-list (sorted insertion).
4. Call `_expand(pos)` to split the sub-list if it has grown too big.

If the structure is empty, start a fresh sub-list.

```python
 def add(self, value):
        _lists = self._lists
        _maxes = self._maxes

        if _maxes:
            pos = bisect_right(_maxes, value)

            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _maxes[pos] = value
            else:
                insort(_lists[pos], value)

            self._expand(pos)
        else:
            _lists.append([value])
            _maxes.append(value)

        self._len += 1
```

## Split a full sub-list (`_expand`)

When a sub-list grows beyond `2 * load_factor` elements, it is split into two:

- The second half (`_lists_pos[_load:]`) is sliced off into a new sub-list `half`, leaving the first half in place.
- `_maxes` is updated for the original sub-list and a new entry is inserted for `half`.
- The positional `_index` cache is invalidated (`del _index[:]`) since the layout changed.

If no split is needed, the cached `_index` (if present) is incremented up the tree instead of being rebuilt.

```python

    def _expand(self, pos):
        _load = self._load
        _lists = self._lists
        _index = self._index

        if len(_lists[pos]) > (_load << 1):
            _maxes = self._maxes

            _lists_pos = _lists[pos]
            half = _lists_pos[_load:]
            del _lists_pos[_load:]
            _maxes[pos] = _lists_pos[-1]

            _lists.insert(pos + 1, half)
            _maxes.insert(pos + 1, half[-1])

            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1
```
