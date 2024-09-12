# 2024-Xu-scripts

This repository contains scripts used to produce the densMAP embeddings and conformational landscapes from cryoDRGN analysis as shown in our paper [Xu *et al* 2024](https://doi.org/10.1101/2024.06.16.599213)

These scripts require the results files from cryoDRGN landscape analysis. ChimeraX scirpts and Jupyter notebook in this repository should be run in order, with certain paths edited as needed. We include the output files from Jupyter notebooks but omited the ones from ChimeraX scripts due to their large size.

Trained cryoDRGN models will be deposited at a future time.

Create a conda environment as follows to run the jupyter notebooks:

```python
conda create --name RNR_landscape python=3.9
conda activate RNR_landscape
conda install -c conda-forge matplotlib mrcfile numpy=1.26.4 scipy biopython numba umap-learn jupyterlab
pip install connected-components-3d
```

## Reference

D Xu, WC Thomas, AA Burnim, and N Ando. "Conformational landscapes of a class I ribonucleotide reductase complex during turnover reveal intrinsic dynamics and asymmetry." (2024) <i>bioRxiv</i> https://doi.org/10.1101/2024.06.16.599213
