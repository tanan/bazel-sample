# BAZEL-SAMPLE

## requirements

Even if you register a hermetic Python toolchain for runtime execution, a system-installed interpreter is still used to 'bootstrap' Python targets.
I use python `3.8.10`.

## usage

### When adding external libraries

When you import external libraries in your source code, you need to write the dependencies of that libraries in py/requirements.txt.
After revising `requirements.txt`, execute the following command to output `requirements_lock.txt` automatically.

```
$ bazel run //py:py_default.update
```
