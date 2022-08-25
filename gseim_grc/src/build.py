from pathlib import Path

import cmake_build_extension

ext_modules = [
    cmake_build_extension.CMakeExtension(
        name="gseim_solver",
        install_prefix="gseim_solver",
        expose_binaries=["bin/gseim_solver"],
        cmake_depends_on=["pybind11"],
    ),
]

def build(setup_kwargs):
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmdclass": dict(build_ext=cmake_build_extension.BuildExtension),
        "zip_safe": False,
    })
