```bash
module use /user-environment/modules/
```

```bash
module load <MODULES>
```

```bash
export mimalloc_DIR=/user-environment/linux-sles15-zen2/gcc-11.3.0/mimalloc-2.0.6-lwwsm5p4zylbivujkje54stwmo23ysbs/lib64/cmake/mimalloc-2.0/
export fmt_DIR=/user-environment/linux-sles15-zen2/gcc-11.3.0/fmt-9.1.0-owzorixom52khkdzkevjinanb6mduxyq/lib64/cmake/fmt/
export camp_DIR=/user-environment/linux-sles15-zen2/gcc-11.3.0/camp-0.1.0-yom2owh45mnbbvyodbhydirx4jwn5mk5/lib/cmake/camp/
```

```bash
bash /user-environment/linux-sles15-zen2/gcc-11.3.0/intel-mkl-2020.4.304-rjqmhxljsvwv2oat32oxli2ginffxben/mkl/bin/mklvars.sh intel64
```

```bash
cmake -DDLAF_WITH_MKL=on ..
```
