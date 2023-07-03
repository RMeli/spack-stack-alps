```bash
module use /user-environment/modules/
```

```bash
module load <modules>
```

```bash
cmake -DDLAF_WITH_MKL=ON -DCMAKE_INSTALL_PREFIX=$HOME/software/dlaf/
make -j 32
make install
```

```bash
cmake -DCP2K_USE_COSMA=OFF -DCP2K_SCALAPACK_VENDOR=MKL -DCMAKE_INSTALL_PREFIX=$HOME/software/dlaf/ ..
make -j 32
```
