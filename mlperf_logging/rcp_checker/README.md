# MLPerf RCP checker

MLPerf reference convergence point (RCP) checker

## Description

Run Reference Convergence Point checks for a submission directory.
This consists of testing whether a submission does not converge
statistically faster than the reference.

RCPs are loaded from directory mlperf_logging/rcp_checker/*.json

The RCP checker supports only the 1.0.0 version.

## Usage

From the base directory of the repo:

```sh
python3 -m mlperf_logging.rcp_checker FOLDER
```

FOLDER is a results directory, i.e. it contains the correct number
of result log files for a benchmark.

## Requirements

You need numpy and scipy
python3 -m pip install numpy scipy

## Tested software versions

python v3.9.2
