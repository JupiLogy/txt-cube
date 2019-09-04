# txt-cube
Importable turnable cube with random state LSE scrambles and stuff. Currently without scrambles.

## Why
For robots :)

## Functions
-   Use `lse_scr()` to get a random state lse scrambled cube.
-   Use `M, M2, Mp, U, U2, Up` to solve the cube, or mix it up further!
-   Check against `SOLVED_CUBE` to see what it should look like when solved.

## Example of usage
Solving the cube one or several moves at a time
```python
>>> from txt_cube import *
>>> cube = lse_scr()
>>> cube
['Y', 'O', 'Y', 'Y', 'W', 'Y', 'Y', 'R', 'Y', 'R', 'R', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'G', 'W', 'G', 'R', 'O', 'R', 'R', 'O', 'R', 'O', 'B', 'O', 'G', 'G', 'G', 'G', 'G', 'G', 'B', 'W', 'B', 'O', 'R', 'O', 'O', 'G', 'O', 'W', 'Y', 'W', 'W', 'Y', 'W', 'W', 'Y', 'W']
>>> cube = Mp(Up(M(cube)))
>>> cube = U(cube)
>>> cube
['Y', 'G', 'Y', 'R', 'W', 'R', 'Y', 'W', 'Y', 'R', 'W', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'G', 'O', 'G', 'R', 'O', 'R', 'R', 'O', 'R', 'O', 'Y', 'O', 'G', 'G', 'G', 'G', 'G', 'G', 'B', 'Y', 'B', 'O', 'R', 'O', 'O', 'Y', 'O', 'W', 'Y', 'W', 'W', 'Y', 'W', 'W', 'B', 'W']
>>> cube = M(Up(M(cube)))
>>> cube == SOLVED_CUBE
True
```

Solving the same cube different ways
```python
>>> cube1 = U2(M2(U2(SOLVED_CUBE)))
>>> cube2 = cube1
>>> M2(U2(M2(U2(M2(cube2))))) == U2(M2(U2(cube1)))
True
```
