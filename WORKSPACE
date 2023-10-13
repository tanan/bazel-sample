load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "9d04041ac92a0985e344235f5d946f71ac543f1b1565f2cdbc9a2aaee8adf55b",
    strip_prefix = "rules_python-0.26.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.26.0/rules_python-0.26.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")

py_repositories()

default_python_version = "3.11"

python_register_multi_toolchains(
    name = "python",
    default_version = default_python_version,
    python_versions = [
        "3.10",
        "3.11",
    ],
)

load("@python//:pip.bzl", "multi_pip_parse")
load("@python//3.10:defs.bzl", interpreter_3_10 = "interpreter")
load("@python//3.11:defs.bzl", interpreter_3_11 = "interpreter")


multi_pip_parse(
    name = "my_deps",
    default_version = default_python_version,
    python_interpreter_target = {
    "3.11": interpreter_3_11,
    "3.10": interpreter_3_10,
    },
    requirements_lock = {
        "3.11": "//py:requirements_lock.txt",
        "3.10": "//py:requirements_lock.txt",
    },
)

load("@my_deps//:requirements.bzl", "install_deps")

install_deps()