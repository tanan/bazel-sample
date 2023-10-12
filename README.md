# BAZEL-SAMPLE

## usage

### When adding external libraries

When you import external libraries in your source code, you need to write the dependencies of that libraries in py/requirements.txt.
After revising `requirements.txt`, execute the following command to output `requirements_lock.txt` automatically.

```
$ bazel run //py:py_default.update
```
