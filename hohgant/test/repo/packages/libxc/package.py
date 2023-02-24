# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libxc(AutotoolsPackage, CudaPackage):
    """Libxc is a library of exchange-correlation functionals for
    density-functional theory."""

    homepage = "https://tddft.org/programs/libxc/"
    url = "https://gitlab.com/libxc/libxc/-/archive/6.1.0/libxc-6.1.0.tar.gz"

    # Get checksum from latest release package at https://tddft.org/programs/libxc/download/
    version("6.1.0", sha256="f593745fa47ebfb9ddc467aaafdc2fa1275f0d7250c692ce9761389a90dd8eaf")

    variant("shared", default=True, description="Build shared libraries")

    conflicts("+shared +cuda", msg="Only ~shared supported with +cuda")
    conflicts("+cuda", when="@:4", msg="CUDA support only in libxc 5.0.0 and above")

    depends_on("perl", type="build")

    @property
    def libs(self):
        """Libxc can be queried for the following parameters:

        - "static": returns the static library version of libxc
            (by default the shared version is returned)

        :return: list of matching libraries
        """
        query_parameters = self.spec.last_query.extra_parameters

        libraries = ["libxc"]

        # Libxc installs both shared and static libraries.
        # If a client ask for static explicitly then return
        # the static libraries
        shared = self.spec.variants["shared"].value and "static" not in query_parameters

        # Libxc has a fortran90 interface: give clients the
        # possibility to query for it
        if "fortran" in query_parameters:
            if self.version < Version("4.0.0"):
                libraries = ["libxcf90"] + libraries
            else:  # starting from version 4 there is also a stable f03 iface
                libraries = ["libxcf90", "libxcf03"] + libraries

        return find_libraries(libraries, root=self.prefix, shared=shared, recursive=True)

    def setup_build_environment(self, env):
        # microarchitecture-specific optimization flags should be controlled
        # by Spack, otherwise we may end up with contradictory or invalid flags
        # see https://github.com/spack/spack/issues/17794

        # https://gitlab.com/libxc/libxc/-/issues/430 (configure script does not ensure C99)
        # TODO: Switch to cmake since this is better supported
        env.append_flags("CFLAGS", self.compiler.c99_flag)
        if "%intel" in self.spec:
            if which("xiar"):
                env.set("AR", "xiar")

        if "%aocc" in self.spec:
            env.append_flags("FCFLAGS", "-fPIC")

        if "+cuda" in self.spec:
            nvcc = self.spec["cuda"].prefix.bin.nvcc
            env.set("CCLD", "{0} -ccbin {1}".format(nvcc, spack_cc))
            env.set("CC", "{0} -x cu -ccbin {1}".format(nvcc, spack_cc))

            cuda_arch = self.spec.variants["cuda_arch"].value[0]

            if cuda_arch != "none":
                env.append_flags("CFLAGS", "-arch=sm_{0}".format(cuda_arch))

    def configure_args(self):
        args = []
        args += self.enable_or_disable("shared")
        args += self.enable_or_disable("cuda")
        return args

    @run_after("configure")
    def patch_libtool(self):
        """AOCC support for LIBXC"""
        if "%aocc" in self.spec:
            filter_file(
                r"\$wl-soname \$wl\$soname",
                r"-fuse-ld=ld -Wl,-soname,\$soname",
                "libtool",
                string=True,
            )

    def check(self):
        # libxc provides a testsuite, but many tests fail
        # http://www.tddft.org/pipermail/libxc/2013-February/000032.html
        pass
