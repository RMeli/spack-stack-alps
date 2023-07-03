```bash
module use /user-environment/modules/
```

```bash
module load <modules>
```

```bash
cmake -DDLAF_WITH_MKL=on -DDLAF_WITH_CUDA=on -DCMAKE_INSTALL_PREFIX=$HOME/software/dlaf/
make -j 32
make install
```

```bash
cmake -DCP2K_USE_COSMA=off -DCP2K_USE_ACCEL=CUDA -DCP2K_WITH_GPU=V100 -DCP2K_SCALAPACK_VENDOR=MKL -DCMAKE_INSTALL_PREFIX=$HOME/software/dlaf/ ..
make -j 32
```

# Hack

`dlaf` does not seem to play nicely with `intel-oneapi-mkl` (**to be investigated**), while `intel-mkl` does not tap into the correct MPI provided by `cray-mpich-binary` (see [stackinator#43](https://github.com/eth-cscs/stackinator/issues/43)).

Spack's file `spack/lib/spack/spack/build_systems/intel.py` was manually amended (within the Spack instance of the environment) in order to hit `^cray-mpich-binary` as follows:
```diff
        elif (
            "^mpich@2:" in spec_root
            or "^cray-mpich" in spec_root
+           or "^cray-mpich-binary" in spec_root
            or "^mvapich2" in spec_root
            or "^intel-mpi" in spec_root
            or "^intel-oneapi-mpi" in spec_root
            or "^intel-parallel-studio" in spec_root
        ):
            blacs_lib = "libmkl_blacs_intelmpi"
```

**This is now in the `buildcache` (see `mirror.yaml`) and therefore subsequent builds will work, but the environment is not reproducible!**
