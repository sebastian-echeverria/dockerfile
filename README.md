[![build status](https://github.com/asottile/dockerfile/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/dockerfile/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/dockerfile/main.svg)](https://results.pre-commit.ci/latest/github/asottile/dockerfile/main)

dockerfile
==========

The goal of this repository is to provide a wrapper around
[docker/docker](https://github.com/docker/docker)'s parser for dockerfiles.


## python library

### Installation

This project uses [setuptools-golang](https://github.com/asottile/setuptools-golang)
when built from source.  To build from source you'll need a go compiler.

If you're using linux and sufficiently new pip (>=8.1) you should be able to
just download prebuilt manylinux1 wheels.

```
pip install dockerfile
```

### Usage

There's three api functions provided by this library:

#### `dockerfile.all_cmds()`

List all of the known dockerfile cmds.

```python
>>> dockerfile.all_cmds()
('add', 'arg', 'cmd', 'copy', 'entrypoint', 'env', 'expose', 'from', 'healthcheck', 'label', 'maintainer', 'onbuild', 'run', 'shell', 'stopsignal', 'user', 'volume', 'workdir')
```

#### `dockerfile.parse_file(filename)`

Parse a Dockerfile by filename.
Returns a `tuple` of `dockerfile.Command` objects representing each layer of
the Dockerfile.
Possible exceptions:
- `dockerfile.GoIOError`: The file could not be opened.
- `dockerfile.GoParseError`: The Dockerfile was not parseable.

```python
>>> pprint.pprint(dockerfile.parse_file('testfiles/Dockerfile.ok'))
(Command(cmd='from', sub_cmd=None, json=False, original='FROM ubuntu:xenial', start_line=1, flags=(), value=('ubuntu:xenial',)),
 Command(cmd='cmd', sub_cmd=None, json=True, original='CMD ["echo", "hi"]', start_line=2, flags=(), value=('echo', 'hi')))
```

#### `dockerfile.parse_string(s)`

Parse a dockerfile using a string.
Returns a `tuple` of `dockerfile.Command` objects representing each layer of
the Dockerfile.
Possible exceptions:
- `dockerfile.GoParseError`: The Dockerfile was not parseable.

```python
>>> dockerfile.parse_string('FROM ubuntu:xenial')
(Command(cmd='from', sub_cmd=None, json=False, original='FROM ubuntu:xenial', start_line=1, flags=(), value=('ubuntu:xenial',)),)
```

## go library

Slightly more convenient than the api provided by docker/docker?  Might not be
terribly useful -- the main point of this repository was a python wrapper.

### Installation

```
go get github.com/asottile/dockerfile
```

### Usage

[godoc](https://godoc.org/github.com/asottile/dockerfile)


## Working from source

### Env setup

1. Prepare environment: `python -m venv .venv`
1. Activate environment: `source .venv/bin/activate`
1. Install python deps: `pip install -r requirements-dev.txt`

### Building and installing

1. Install go
1. Get go dependencies: `go mod tidy`
1. Build with go: `go build`
1. Build Python wheel: `python setup.py bdist_wheel`
1. Install wheel in local env: `pip install dist/dockerfile-3.3.1-cp39-abi3-macosx_14_0_arm64.whl`

You can also test the whole process by calling `tox`.
