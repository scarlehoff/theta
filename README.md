![alt text](https://github.com/RiemannAI/theta/blob/master/docs/theta.png)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1120325.svg)](https://doi.org/10.5281/zenodo.1120325)

## Welcome to theta!

Theta is a machine learning (ML) framework implementing the Riemann-Theta Boltzmann Machine (RTBM), written in Python and Cython. It offers a high-level interface to build and train RTBM based ML architectures for probability density estimation, data regression and classification.

The code implements the RTBM as described in the theoretical paper [arXiv:1712.07581](https://arxiv.org/abs/1712.07581).

### Note

Theta is in a proof-of-concept / research phase. You may observe that
model training requires some fine tune to get proper results.


## User documentation

The complete documentation including:
- installation
- code layout and documentation
- examples 

is available at https://riemannai.github.io/theta.

## Quick install

This package uses [RiemannAI/openRT](https://github.com/RiemannAI/openRT) as submodule.

Before installing the theta package please install the following dependencies:
```bash
python >= 2.7 or python >= 3.6
cython >= 0.26
numpy >= 1.13
cma >= 2.3.1
matplotlib >= 2.0.0
```

Then you can proceed and install theta from the Github source. First, clone the theta repository using `git`:
```bash
git clone --recursive https://github.com/RiemannAI/theta.git
```

Then, `cd` to the theta folder and run the install command:

```bash
cd theta
sudo python setup.py install
```


## License and citation policy

The theta package is an open-source package under AGPLv3. If you use the theta package please cite the following article:
```
Daniel Krefl, Stefano Carrazza, Babak Haghighat, Jens Kahlen, Riemann-Theta Boltzmann Machine. arXiv:1712.07581.
```
