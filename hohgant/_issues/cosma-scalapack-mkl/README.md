```text
==> Installing cosma-2.5.1-w77v3baocrcqhbbj4pqkwja6a2cdaa4j
==> No binary for cosma-2.5.1-w77v3baocrcqhbbj4pqkwja6a2cdaa4j found: installing from source
==> Error: InstallError: Cannot find a BLACS library for the given MPI.

/dev/shm/rmeli/issue/spack/lib/spack/spack/build_systems/intel.py:856, in scalapack_libs:
        853            blacs_lib = "libmkl_blacs_intelmpi"
        854        elif "^mpt" in spec_root:
        855            blacs_lib = "libmkl_blacs_sgimpt"
  >>    856        else:
        857            raise_lib_error("Cannot find a BLACS library for the given MPI.")
        858
        859        int_suff = "_" + self.intel64_int_suffix
```
