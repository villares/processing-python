# py5 tips for those comming from Processing Python Mode

**Welcome!**

We hope you enjoy using the Processing graphics vocabulary, now with Python 3.

## The slightly different names

The first thing you might notice is how the Processing function/method names you were used to had the Java community convention of *camelCase* and now use the Python community *snake_case* convention.
-  `mouseX` becomes `mouse_x` , and `noFill()` becomes `no_fill()`
- You might be surprised that the global `mousePressed` variable becomes `is_mouse_pressed` but the event function users can define, `void mousePressed(){ ...`, in Java, is now defined  as `def mouse_pressed(): ...`.
- Also `keyPressed`, `is_key_pressed` for the variable, and `key_pressed` for the event function.
- Processing's `map(value, start, end, target_start, target_end)` is [`remap()`](https://py5coding.org/reference/sketch_remap.htm)  because of Python's [`map(func, iterable)`](https://docs.python.org/3/library/functions.html#map)
- Processing's  `filter()` is `apply_filter()`
-  Processing's `set()` is complicated... You might want to read about [`set_np_pixels()`](http://py5coding.org/reference/sketch_set_np_pixels.html)

- Use `frame_rate()` to [set a target frame rate](https://py5coding.org/reference/sketch_frame_rate.html) and `get_frame_rate()` to find out the current frame rate ([an exponential moving average]

[Please hava a look at the Reference Summary here](https://py5coding.org/reference/summary.html)

## About the libraries 

No more `import processing.pdf.*;` or `add_library('pdf')` needed for PDF or SVG. For other Processing libraries... it could be more complicated. (TODO: write or link to more info about using jars)
On the other hand, you can now import Python libraries with `import`.


#### 2D Arrays


```Python
board = [[0] * grid_w for _ in range(grid_h)]
```



