* `.tobytes()` stores values without any metadata or offset
* `.tobytes()` has `order`, C-contiguous or F-contiguous
* dtype has `byteorder`, which is different from order in tobytes
  * Modern many platforms are based on little-endian

> [!NOTE]
> On macOS
>
> ```py
> > uv run python -c 'import sys; print(sys.byteorder)'
> little
> ```

* :link: https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.tobytes.html
