# Caltech Pedestrian Detection Benchmark Extractor Python

Martin Kersner, m.kersner@gmail.com

[Caltech Pedestrian Detection Benchmark](https://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/) is stored in two exotic formats. Images are stored in *seq* format and labels are in *vbb*. In order to be able to work with such formats one has to be able access original data. There is support for Matlab with [Piotr's Computer Vision Matlab Toolbox](https://pdollar.github.io/toolbox/index.html), however there is no full support for both formats in Python.

This repository consist of two scripts, one (*extract_annotations.py*) for extracting information from *seq* format and one (*extract_images.py*) for *vbb* format. 

*extract_annotations.py* was taken from [mitmul's](https://github.com/mitmul/caltech-pedestrian-dataset-converter) repository and slightly modified.

*extract_images.py* was inspired by [jainanshul's](https://github.com/jainanshul/caltech-pedestrian-dataset-extractor) repository and Piotr's Computer Vision Matlab Toolbox.
