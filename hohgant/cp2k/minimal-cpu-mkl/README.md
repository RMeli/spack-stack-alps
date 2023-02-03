```bash
module load cmake/3.25.2 cray-mpich-gcc fftw/3.3.10 intel-oneapi-mkl/2023.0.0 \
    libxc/6.1.0 pkgconf/1.8.0 spglib/1.16.1 cosma/2.5.1 dbcsr/2.5.0 gcc/11.3.0 \
    libint/2.6.0 libxsmm/1.17 python/3.9.15
```

```bash
cmake .. -DCP2K_USE_COSMA=OFF -DCP2K_SCALAPACK_VENDOR=MKL
```
