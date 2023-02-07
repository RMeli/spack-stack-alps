```bash
module use /user-environment/modules/
```

```bash
module load 
```

```bash
cmake -DCP2K_USE_COSMA=off -DCP2K_USE_ACCEL=CUDA -DCP2K_WITH_GPU=V100 -DCP2K_SCALAPACK_VENDOR=MKL ..
```
