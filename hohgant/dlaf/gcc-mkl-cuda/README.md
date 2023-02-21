# DLA-Future 

## Compilation

```bash
squasfs-run dlaf-gcc-mkl-cuda.squashfs bash

module use /user-environment/modules/
module load <MODULES>

cmake -DDLAF_WITH_MKL=on -DDLAF_WITH_CUDA=on ..
```

## Issues

For this Spack stack, the following test fail:

```text
test 3
    Start 3: test_blas_tile

3: Test command: /scratch/e1000/rmeli/git/DLA-Future/build-cpu/test/unit/test_blas_tile
3: Test timeout computed to be: 1500
3: Running main() from gtest_pika_main.cpp
3: [==========] Running 28 tests from 4 test suites.
3: [----------] Global test environment set-up.
3: [----------] 7 tests from TileOperationsTestMC/0, where TypeParam = float
3: [ RUN      ] TileOperationsTestMC/0.Gemm
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 3, n = 11, k = 0, lda = 3, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 3, n = 11, k = 0, lda = 3, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 17, n = 12, k = 16, lda = 18, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 17, n = 12, k = 16, lda = 18, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 11, n = 23, k = 8, lda = 11, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 11, n = 23, k = 8, lda = 11, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 6, n = 9, k = 12, lda = 7, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 6, n = 9, k = 12, lda = 7, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 3, n = 11, k = 0, lda = 3, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 3, n = 11, k = 0, lda = 3, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 17, n = 12, k = 16, lda = 18, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 17, n = 12, k = 16, lda = 18, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 11, n = 23, k = 8, lda = 11, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 11, n = 23, k = 8, lda = 11, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 6, n = 9, k = 12, lda = 7, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 6, n = 9, k = 12, lda = 7, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 3, n = 11, k = 0, lda = 3, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 3, n = 11, k = 0, lda = 3, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 17, n = 12, k = 16, lda = 18, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 17, n = 12, k = 16, lda = 18, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 11, n = 23, k = 8, lda = 11, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 11, n = 23, k = 8, lda = 11, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 6, n = 9, k = 12, lda = 7, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 6, n = 9, k = 12, lda = 7, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: NoTrans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: Trans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 2, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 1, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 19, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 11, ldc = 15
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 10 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 13, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, NoTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, Trans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (1, 0): expected 1.32 == 1.2 (Relative diff: 0.0909091 > 4.76837e-07, Absolute diff: 0.12 > 4.76837e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 3, n = 11, k = 0, lda = 1, ldb = 12, ldc = 3
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 1, n = 1, k = 1, lda = 1, ldb = 4, ldc = 1
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -0.432 == 0 (Relative diff: 1 > 9.53674e-07, Absolute diff: 0.432 > 9.53674e-07)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 1, n = 12, k = 1, lda = 2, ldb = 12, ldc = 8
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -6.912 == 0 (Relative diff: 1 > 8.10623e-06, Absolute diff: 6.912 > 8.10623e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 17, n = 12, k = 16, lda = 17, ldb = 15, ldc = 17
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -3.456 == 0 (Relative diff: 1 > 4.29153e-06, Absolute diff: 3.456 > 4.29153e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 11, n = 23, k = 8, lda = 8, ldb = 26, ldc = 15
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 8 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -5.184 == 0 (Relative diff: 1 > 6.19888e-06, Absolute diff: 5.184 > 6.19888e-06)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 6, n = 9, k = 12, lda = 13, ldb = 10, ldc = 7
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 32, ldb = 32, ldc = 32
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -13.824 == 0 (Relative diff: 1 > 1.57356e-05, Absolute diff: 13.824 > 1.57356e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 32, n = 32, k = 32, lda = 36, ldb = 37, ldc = 39
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3:
3: Intel MKL ERROR: Parameter 13 was incorrect on entry to SGEMM .
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:92: Failure
3: Failed
3: Error at index (0, 0): expected -55.296 == 0 (Relative diff: 1 > 6.1512e-05, Absolute diff: 55.296 > 6.1512e-05)
3:
3: Google Test trace:
3: /scratch/e1000/rmeli/git/DLA-Future/test/unit/test_blas_tile/test_gemm.h:89: GEMM: ConjTrans, ConjTrans, m = 128, n = 128, k = 128, lda = 128, ldb = 128, ldc = 128
3: [  FAILED  ] TileOperationsTestMC/0.Gemm, where TypeParam = float (1012 ms)
3: [ RUN      ] TileOperationsTestMC/0.Hemm
1/2 Test #3: test_blas_tile ...................***Exception: SegFault  2.45 sec
test 4
    Start 4: test_lapack_tile

4: Test command: /scratch/e1000/rmeli/git/DLA-Future/build-cpu/test/unit/test_lapack_tile
4: Test timeout computed to be: 1500
4: Running main() from gtest_pika_main.cpp
4: [==========] Running 38 tests from 6 test suites.
4: [----------] Global test environment set-up.
4: [----------] 9 tests from TileOperationsTestMC/0, where TypeParam = float
4: [ RUN      ] TileOperationsTestMC/0.Hegst
4:
4: Intel MKL ERROR: Parameter 7 was incorrect on entry to SSYGST.
4: unknown file: Failure
4: C++ exception with description "" thrown in the test body.
4: [  FAILED  ] TileOperationsTestMC/0.Hegst, where TypeParam = float (5 ms)
4: [ RUN      ] TileOperationsTestMC/0.lange
2/2 Test #4: test_lapack_tile .................***Exception: SegFault  2.16 sec

0% tests passed, 2 tests failed out of 2
```
