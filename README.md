# txt-cube
Importable turnable cube with random state LSE scrambles and stuff. Currently without scrambles.

### Why?
For robots :)

## Functions
- Use `lse_scr()` to get a random state lse scrambled cube.
- Use `M, M2, Mp, U, U2, Up` to solve the cube, or mix it up further!
- Check against `SOLVED_CUBE` to see what it should look like when solved.

## Example of usage

```python
>>> from txt_cube import *
>>> cube = lse_scr()
>>> cube
['Y', 'O', 'Y', 'Y', 'W', 'Y', 'Y', 'R', 'Y',
 'G', 'W', 'O', 'B', 'B', 'B', 'B', 'B', 'B', 
 'B', 'W', 'B', 'R', 'O', 'R', 'R', 'Y', 'R',
 
 'R', 'Y', 'R', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'Y', 'G', 'O', 'R', 'O', 'O', 'O', 'O', 'W', 'G', 'W', 'W', 'Y', 'W', 'W', 'W', 'W']
>>> cube = 
```
