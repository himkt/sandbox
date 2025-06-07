* `.tobytes()` stores values without any metadata or offset
* `.tobytes()` has `order`, C-contiguous or F-contiguous
  * It changes the way to flatten array (row-oriented or column oriented)
* dtype has `byteorder`, which is different from order in tobytes
  * Modern many platforms are based on little-endian

> [!NOTE]
```
> uv run main.py
data=array([[6, 0],
       [1, 0]]), order='C'

> cargo run
[6, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 6
[0, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 0
[1, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 1
[0, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 0
```

> [!NOTE]
```
> uv run main.py
data=array([[2, 4],
       [0, 9]]), order='F'

> cargo run
[2, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 2
[0, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 0
[4, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 4
[9, 0, 0, 0, 0, 0, 0, 0]
Parsed value: 9
```

> [!NOTE]
> On macOS
>
> ```py
> > uv run python -c 'import sys; print(sys.byteorder)'
> little
> ```

* :link: https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.tobytes.html
