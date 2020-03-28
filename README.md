Easily Parse TFLite Models with Python
======================================

![Continuous Integration](https://github.com/jackwish/tflite/workflows/Continuous%20Integration/badge.svg)

This [`tflite` package](https://pypi.org/project/tflite/) parses TensorFlow Lite (TFLite) models (`*.tflite`), which are built by [TFLite converter](https://www.tensorflow.org/lite/convert) with the help of [FlatBuffers](https://google.github.io/flatbuffers/). For background, please refer to [Introducing TFLite Parser Python Package](https://jackwish.net/2020/introducing-tflite-parser-package.html).


## Installation

Simply install via [pip](https://pypi.org/project/tflite/). This package requires `flatbuffers` and `numpy` which should be installed automatically.

```sh
pip install tensorflow==1.14.0
pip install tflite==1.14.0.post1
```

It would be better if you use a correct version, where the mapping is as below.

| TensorFlow package version   | tflite package version |
|------------------------------|------------------------|
|      1.14.0                  |      1.14.0.post1      |
|      1.15.0                  |      1.15.0.post1      |
|      1.15.2                  |      1.15.2            |
|      2.0.0                   |      2.0.0.post2       |
|      2.0.1                   |      2.0.1             |
|      2.1.0                   |      2.1.0             |


## Usage

The package can be imported with *easy import* or *original import*, where the difference is how many `import` you write - no functionality divergence. For supported interfaces, please refer to [document page](https://jackwish.net/tflite/docs/).

### Easy Import (Recommanded)

*Easy import* enables developers using parsing functionality wich one single `import tflite`. This is achieved by importing classes and functions of one submodules into top module [directly](tflite/__init__.py).

[MobileNet parsing example](https://github.com/jackwish/tflite/blob/master/tests/test_mobilenet.py) shows how to parse model with `import tflite` **ONLY ONCE**.

### Original Import

You can use this package just like the newly FlatBuffers generated one ([example](tests/test_original_import.py)) to avoid any break of your legacy code.

```python
from tflite.Model import Model
# use Model
```

The original generated package needs to import every classes by hand ([see this](https://github.com/apache/incubator-tvm/blob/v0.6.0/python/tvm/relay/frontend/tflite.py#L843-L849)) which is pretty annoying.


## Upgrade

> Steps to upgrade this package corresponding to new TensorFlow release. Package users can safely ignore this part.

Install additional depdendency via `pip install -r requirements.txt`, and:

1. [Download](tools/1-update-schema.sh) `schema.fbs` for a new version.
2. [Update](tools/2-update-importing.py) the classes and functions import of submodules.
3. Update the versioning in [setup.py](setup.py).
4. [Build](tools/4-build.sh) and [Test](tests) around. Don't forget to re-install the newly built `tflite` package before testing it.
5. [Upload](tools/5-upload.sh) the package to PyPI.

Features could be added to make the parsing easy in the future.


## Resources

* [PyPI page](https://pypi.org/project/tflite/).
* [GitHub page](https://github.com/jackwish/tflite).
* [Module list](https://jackwish.net/tflite/docs).
* [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert).


## License

Apache License Version 2.0 as TensorFlow's.


## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly. Maintainer of this package had tried to [contact](assets/disclaimer.eml) TensorFlow maintainers for licensing issues, but received no reply. Ownership or maintainship is open to transfer or close if there were any issue.
