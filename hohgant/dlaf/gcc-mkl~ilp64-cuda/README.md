```bash
squashfs-run dlaf-gcc-mkl~ilp64-cuda.squashfs bash

module use /user-environment/modules/
module load <MODULES>

cmake -DDLAF_WITH_MKL=on -DDLAF_WITH_CUDA=on ..
```
