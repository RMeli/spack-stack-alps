```bash
squashfs-run dlaf-gcc-mkl+ilp64-cpu.squashfs bash

module use /user-environment/modules/
module load <MODULES>

cmake -DDLAF_WITH_MKL=on ..
```
