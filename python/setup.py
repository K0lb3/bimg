from setuptools import setup, Extension, find_packages
import os

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
INCLUDE = [
    os.path.join(ROOT, *x)
    for x in [
        ["include"],
        ["bx", "include"],
        ["bx", "3rdparty"],
        ["3rdparty"],
        ["3rdparty", "astc"],
        ["3rdparty", "astc-codec"],
        ["3rdparty", "astc-codec", "include"],
        ["3rdparty", "edtaa3"],
        ["3rdparty", "etc1"],
        ["3rdparty", "etc2"],
        ["3rdparty", "iqa", "include"],
        ["3rdparty", "libsquish"],
        ["3rdparty", "lodepng"],
        ["3rdparty", "nvtt"],
        ["3rdparty", "pvrtc"],
        ["3rdparty", "stb"],
        ["3rdparty", "tinyexr", "deps", "miniz"],
    ]
]

# TODO: check the compiler and add corresponding compat to INCLUDE
INCLUDE.append(os.path.join(ROOT, "bx", "include", "compat", "msvc"))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bimgPy",
    description="",
    author="K0lb3",
    version="0.0.1",
    keywords=["astc", "atc", "pvrtc", "etc", "crunch"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Multimedia :: Graphics",
    ],
    url="https://github.com/K0lb3/bimg",
    download_url="https://github.com/K0lb3/bimg/tarball/master",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[
        Extension(
            "bimgPy",
            [
                os.path.join(root, f)
                for root, dirs, files in os.walk(ROOT)
                for f in files
                if (
                    f.endswith((".c", ".cc", ".cpp", ".cxx"))
                    and f not in ["amalgamated.cpp", "debug.cpp", "lodepng.cpp"]
                    and not any(x in root for x in ["test", "tool"])
                )
            ],
            language="c++",
            include_dirs=INCLUDE,
            extra_compile_args=[
                "/DBX_CONFIG_DEBUG=0",
                "/DBUILD_TOOLS_CONFIG=release64",
                "/DBUILD_TOOLS_SUFFIX=Release",
            ],
        )
    ],
)
