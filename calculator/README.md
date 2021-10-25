## Calculator

We're in serious need of a calculator to do some math on our data. As a prototype we build a simple
calculator that takes inputs and calculates outputs.
The outputs should include every intermediate calculation as well.

Example:

```
Input: [1, '+', 2]
Output: 3

Input: [1, '+', 2, '*', 3] # N.B. No operator precedence
Output: 3 9

Input: [1, '+', [2, '*', 3]]
Output: 3 7
```

The calculator has to work in a data pipeline and therefore has to be able to take it's inputs one at a time, something like:

```python
>>> calculate(1)('+')(2)
```

(This is for inspiration only ;) )

As a Proof of concept, create a small program that takes input from the user and calculates results on the fly.
Can this be done with little modification? Which parts of the code contain side effects, and which are pure?
