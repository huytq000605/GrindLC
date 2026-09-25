# Stack + Ops (Expression Evaluation Pattern)

Scan left to right, **operands on one stack**, **pending operators on another**. Apply an
operator only when nothing stronger can still arrive on its right.

> Re-read the card below. Everything else is folded — open a section only when that detail is
> the thing you forgot.

---

## Recall card

**Three rules**

1. Operand → push to `stack`. `(` → push a marker to `ops`.
2. Operator → **first fire everything on `ops` that is >= its precedence**, then push it.
3. `)` → fire until the `(` marker, drop the marker. End of input → fire everything.

**A calculation fires in exactly 4 situations** — nothing else:

| Trigger | Meaning |
| --- | --- |
| weaker operator arrives | `2*x` then `+` → the `*` can't grow right |
| equal operator arrives | `3*x` then `*` → left-assoc (`>=`, not `>`) |
| `)` | the group is done, collapses to one stack slot |
| end of input | flush all pending |

**Template**

```python
stack = []   # operands (values)
ops   = []   # pending operators + "(" markers
PREC  = {"+": 1, "-": 1, "*": 2, "/": 2}

def ope():                      # pop one operator, apply to the two top operands
    op = ops.pop()
    r, l = stack.pop(), stack.pop()     # r first!
    stack.append(apply(op, l, r))

for token in scan(s):
    if token is operand:
        stack.append(value(token))
    elif token == "(":
        ops.append("(")
    elif token == ")":
        while ops[-1] != "(":
            ope()
        ops.pop()               # drop the "("
    else:                       # binary operator
        while ops and ops[-1] != "(" and PREC[ops[-1]] >= PREC[token]:
            ope()               # left-assoc: >=   |   right-assoc: >
        ops.append(token)

while ops:
    ope()
answer = stack[-1]
```

**Invariant:** within a bracket level, precedence in `ops` is non-decreasing bottom→top, so the
top is always the operator that must fire first. `"("` is a floor the pop-loop never crosses.

**Only `apply()` changes between problems.** The scanner is written once.

---

<details>
<summary><b>Same scanner, 4 swaps</b> — the plug-in table</summary>

| Plug-in point | Basic Calculator III | Brace Expansion II | Basic Calculator IV |
| --- | --- | --- | --- |
| Value domain `V` | `int` | `set[str]` | polynomial: `dict[tuple[str,...], int]` |
| Operand parser | multi-digit number | single letter → `{ch}` | number / known var → constant; free var → `{(v,): 1}` |
| Operators (high → low) | `* /` then `+ -` | `*` (concat) then `+` (union, written `,`) | `*` then `+ -` |
| `apply(op, l, r)` | `l+r`, `l-r`, `l*r`, trunc div | cross-product concat, set union | poly add/sub, poly multiply |
| Brackets | `( )` | `{ }` | `( )` |

**When to reach for this pattern:** the input is an *expression* — operands, binary operators
with differing precedence, nested brackets; sometimes an operator is implicit (`{a,b}{c,d}`).

Family: 224 Basic Calculator, 227 Basic Calculator II, 772 Basic Calculator III,
770 Basic Calculator IV, 1096 Brace Expansion II, 394 Decode String, 726 Number of Atoms,
1106 Parsing A Boolean Expression, 439 Ternary Expression Parser.

**Why the fire rule is correct:** an operator may be applied only once you know nothing stronger
is coming on its right. A weaker-or-equal operator, a `)`, or end-of-input is exactly that proof.

</details>

<details>
<summary><b>Basic Calculator III</b> — ints, and the table-free pop-loop</summary>

`Stack & Queue/Basic Calculator III/solution.py` writes the same pop condition without a `PREC`
dict:

```python
while ops and \
    not (ops[-1] in "()" or (ops[-1] in "+-" and ch in "*/")):
    ope()
```

*stop at a bracket, or when the pending op is weaker than the incoming one* — otherwise fire.

Trace of `1-(2+3)*2`:

```
   1 | push operand                 | stack=[1]        ops=[]
   - | push (nothing weaker)        | stack=[1]        ops=['-']
   ( | push marker                  | stack=[1]        ops=['-', '(']
   2 | push operand                 | stack=[1, 2]     ops=['-', '(']
   + | push (nothing weaker)        | stack=[1, 2]     ops=['-', '(', '+']
   3 | push operand                 | stack=[1, 2, 3]  ops=['-', '(', '+']
   ) | fire ['+'], drop (           | stack=[1, 5]     ops=['-']
   * | push (nothing weaker)        | stack=[1, 5]     ops=['-', '*']
   2 | push operand                 | stack=[1, 5, 2]  ops=['-', '*']
 END | flush *                      | stack=[1, 10]    ops=['-']
 END | flush -                      | stack=[-9]       ops=[]
```

The `1` sits untouched at the bottom for the whole bracket — the pending `-` below `(` protects it.

</details>

<details>
<summary><b>Brace Expansion II</b> — sets, and implicit operators</summary>

`Stack & Queue/*Brace Expansion II/solution.py` — same scanner over sets, `,` is the weak op,
`{ }` are the brackets:

```python
def ope():
    r, l = stack.pop(), stack.pop()
    result = set()
    op = ops.pop()
    if op == "*":
        for ll in l:
            for rr in r:
                result.add(ll + rr)
    elif op == "+":
        result = l | r
    stack.append(result)
    return result
```

**Implicit operator:** there is no concat symbol, so insert one while scanning — before pushing
an operand (letter or `{`), if the previous character *ended* an operand, push a `*` first.

```python
if i > 0 and (expr[i-1] == '}' or expr[i-1].isalpha()):
    ops.append("*")
```

Rule of thumb: *operand-ender* (`}`, `)`, letter, digit) immediately followed by
*operand-starter* ⇒ inject the operator. Push it **before** the `{` marker so it parks below the
bracket floor and survives until the group closes.

Trace of `{a,b}{c,{d,e}}`:

```
   { | push marker                  | stack=[]                     ops=['{']
   a | push operand                 | stack=[{a}]                  ops=['{']
   , | push +                       | stack=[{a}]                  ops=['{', '+']
   b | push operand                 | stack=[{a}, {b}]             ops=['{', '+']
   } | fire ['+'], drop {           | stack=[{a,b}]                ops=[]
   { | implicit *, push marker      | stack=[{a,b}]                ops=['*', '{']
   c | push operand                 | stack=[{a,b}, {c}]           ops=['*', '{']
   , | push +                       | stack=[{a,b}, {c}]           ops=['*', '{', '+']
   { | push marker                  | stack=[{a,b}, {c}]           ops=['*', '{', '+', '{']
   d | push operand                 | stack=[{a,b}, {c}, {d}]      ops=['*', '{', '+', '{']
   , | push +                       | stack=[{a,b}, {c}, {d}]      ops=['*', '{', '+', '{', '+']
   e | push operand                 | stack=[{a,b}, {c}, {d}, {e}] ops=['*', '{', '+', '{', '+']
   } | fire ['+'], drop {           | stack=[{a,b}, {c}, {d,e}]    ops=['*', '{', '+']
   } | fire ['+'], drop {           | stack=[{a,b}, {c,d,e}]       ops=['*']
 END | flush *                      | stack=[{ac,ad,ae,bc,bd,be}]  ops=[]
```

`ops = ['*', '{', '+', '{', '+']` reads directly as the nesting: pending concat, inside a brace,
pending union, inside a brace, pending union. Each `}` unwinds one level.

</details>

<details>
<summary><b>Basic Calculator IV</b> — polynomials (the richest instantiation)</summary>

A value is a **polynomial**: `dict` from a *sorted* tuple of free variables to its coefficient.

```
3*a*b   ->  {("a","b"): 3}        constant 3 -> {(): 3}        zero -> {}
```

Two properties carry the whole solution: sorting the tuple **canonicalizes** the term (so
`a*b*c` and `b*a*c` are the same key and merge for free), and `len(tuple)` **is** the degree,
which is exactly the output sort key.

```python
def add(l, r, k):                     # k = +1 for "+", -1 for "-"
    res = defaultdict(int, l)
    for key, c in r.items(): res[key] += k * c
    return {key: c for key, c in res.items() if c}          # drop zero terms

def mul(l, r):
    res = defaultdict(int)
    for k1, c1 in l.items():
        for k2, c2 in r.items():
            res[tuple(sorted(k1 + k2))] += c1 * c2          # sorted key = canonical form
    return {key: c for key, c in res.items() if c}
```

Operand parsing: a number, or a variable — substituted to a constant if it is in `evalvars`,
else kept as the degree-1 term `{(v,): 1}`. Substitution happens **at push time**, so an
evaluated variable never enters the polynomial as a variable.

Problem-specific extras (not part of the pattern):
- Tokens are space-separated ⇒ `expression.replace("(", " ( ").replace(")", " ) ").split()` is
  the whole tokenizer. No multi-digit hand-rolling.
- **Prune zero coefficients inside add/mul**, not just at the end — otherwise `7 - 7` emits a term.
- Output: `sorted(poly, key=lambda t: (-len(t), t))` → degree desc, then lexicographic.
- No division, so precedence is just `* > + -`.

<details>
<summary>&nbsp;&nbsp;↳ Inside <code>mul</code> — three things to watch</summary>

```
  op = '*'   l = {e: 1, 1: 8}   r = {e: 1, 1: -8}         # from (e + 8) * (e - 8)
      2 x 2 = 4 pairwise products
        (e:1)  x (e:1)   -> key ('e','e')  coeff 1
        (e:1)  x (1:-8)  -> key ('e',)     coeff -8
        (1:8)  x (e:1)   -> key ('e',)     coeff 0   <-- MERGES, then CANCELS, pruned
        (1:8)  x (1:-8)  -> key ()         coeff -64
      => {e*e: 1, 1: -64}
```

1. **Key = `tuple(sorted(t1 + t2))`** — concat the variable lists, re-sort. `(b:1) x (a:1)` →
   key `('a','b')`. This one `sorted` is why `a*b*c + b*a*c*4` merges to `5*a*b*c` with no extra code.
2. **`+=`, never `=`** — different pairs land on the same key (the two `('e',)` products above).
3. **Prune zeros on the way out** — else you emit a phantom `0*e`.

`0` parses to `{}`, so the double loop runs zero times and multiply-by-zero needs no special case.

`add`/`sub` are one function: `res` starts as a copy of `l`, then `r` folds in with sign `k`.

</details>

<details>
<summary>&nbsp;&nbsp;↳ The 4 fire triggers, with live variable states</summary>

**A — weaker operator arrives** (`2 * x + ...`)

```
before:  stack=[{1:2}, {x:1}]   ops=['*']
  FIRE  trigger='+'   ('*' prec 2 >= '+' prec 1)
        op='*'  l={1: 2}  r={x: 1}   =>  {x: 2}
after:   stack=[{x:2}]          ops=['+']
```

**B — equal operator arrives** (`3 * x * y`, left-assoc)

```
before:  stack=[{x:2}, {1:3}, {x:1}]   ops=['+', '*']
  FIRE  trigger='*'   ('*' prec 2 >= '*' prec 2)
        op='*'  l={1: 3}  r={x: 1}   =>  {x: 3}
after:   stack=[{x:2}, {x:3}]          ops=['+', '*']
```

`>=` is what collapses `3*x` before `y` arrives. `{x:2}` is protected by the `+` beneath the `*`.

**C — `)` closes the group** (`(e + 8) * ...`)

```
before:  stack=[{e:1}, {1:8}]   ops=['(', '+']
  FIRE  trigger=')'
        op='+'  l={e: 1}  r={1: 8}   =>  {e: 1, 1: 8}     then pop the '(' marker
after:   stack=[{e:1, 1:8}]     ops=[]
```

The group is now **one stack slot** — indistinguishable from a plain operand.

**D — end of input, cascade** (`a*b*c + b*a*c*4`)

```
before:  stack=[{a*b*c:1}, {a*b*c:1}, {1:4}]   ops=['+', '*']
  FIRE  op='*'  l={a*b*c: 1}  r={1: 4}        =>  {a*b*c: 4}
  FIRE  op='+'  l={a*b*c: 1}  r={a*b*c: 4}    =>  {a*b*c: 5}
after:   stack=[{a*b*c:5}]                     ops=[]
```

Top-down is correct because `ops` is non-decreasing in precedence. One token can cascade too —
the `-` in `2*x + 3*x*y - x` fires `*` then `+` before being pushed.

</details>

</details>

<details>
<summary><b>Degenerate case</b> — no brackets, two precedence levels (Basic Calculator II)</summary>

With no brackets and only `+ - * /`, `ops` never holds more than one pending operator, so it
collapses into a single `sign` variable: **defer** the low-precedence ops by pushing onto
`stack`, **apply** the high-precedence ones immediately to the top, fold at the end (`sum`,
because `-` is pushed as a negative).

```python
if   sign == "+": stack.append(current)
elif sign == "-": stack.append(-current)
elif sign == "/": stack.append(int(stack.pop() / current))
elif sign == "*": stack.append(stack.pop() * current)
```

Set version: push a set for `,`, `stack.append(cross(stack.pop(), cur))` for concat, fold with
union. Three or more precedence levels ⇒ go back to the full two-stack template.

</details>

<details>
<summary><b>Gotchas checklist</b></summary>

1. **Multi-digit numbers** — `cur = cur*10 + int(c)`, or a
   `while i+1 < n and s[i+1].isdigit()` lookahead.
2. **Spaces** — skip them explicitly.
3. **Unary minus / leading `-`** — a `-` with an empty operand stack (start of string, or right
   after `(`) needs a `0` pushed first, else `ope()` underflows.
4. **Flush at the end** — `while ops: ope()`. Forgetting it drops the last operator.
5. **`r` is popped before `l`** — `r, l = stack.pop(), stack.pop()`. Getting this backwards only
   shows up on non-commutative ops (`-`, `/`, concat).
6. **Truncation toward zero** — Python's `//` floors, so `-7 // 2 == -4`. Use `int(a / b)` or
   `sign * (abs(l) // abs(r))`.
7. **`-(...)` flattening** (optional) — after popping a `)`, if the pending op is `-`, negate the
   sub-result and rewrite it as `+`:

   ```python
   if ops and ops[-1] == "-":
       stack[-1] = -stack[-1]
       ops[-1] = "+"
   ```

   Not needed for correctness (the pop-loop already gets `1-(2+3)*2` right); it just normalizes
   everything to additions.

</details>

<details>
<summary><b>Complexity</b></summary>

- Calculators (I–III): **O(n)** time, **O(n)** space — each character pushed and popped once.
- Brace Expansion II: the scan is linear, but the set ops dominate —
  **O(total expanded size × word length)**.
- Basic Calculator IV: scan is linear in tokens; each `mul` is `O(|l|·|r|)`, so the real bound is
  the size of the expanded polynomial. Same blow-up story as Brace Expansion II.

</details>
