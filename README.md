# naturalAI

natural AI is a Python AI (Artificial Intelligence) framework that uses the [sklearn library](http://scikit-learn.org/stable/) to create natural solutions to work with recommenders, classifiers, clusters, etc. among other interesting functions like PCA (Principal Component Analysis), MDS (Multidimensional Scaling), Genetic Algorithms, etc. The library provides examples and wrappers for easy usage  of it.

[![Downloads](https://img.shields.io/badge/downloads-0-blue.svg)]() [![Stable Release](https://img.shields.io/badge/version-1.0-blue.svg)]() [![License](https://img.shields.io/badge/license-GPL-blue.svg)]() [![Python version](https://img.shields.io/badge/python-3.4.2-red.svg)]()

List of libraries required:
---------------------------
- numpy
- matplotlib
- sklearn
- random
- intertools
- math
- functools
- unittest

# Example of usage
```python
from naturalAI_standardisation import *
from naturalAI_PCA import *

standardization = Standardizer("testing.data")
values, valuesNoLastColums = standardization.getValues()

print ("Standardisation:")
for l in values:
    print (l)
pcaObject = PCA(valuesNoLastColums)
pcaObject.printAcumvar()

Output:
mypca.explained_variance_ratio_ [ 0.50 0.25 0.10 0.10 0.05 0.05]
mypca.explained_variance_ratio_.sum() 1.0 
[(0, 0), (1, 0.50), (2, 0.75), (3, 0.80), (4, 0.90), (5, 0.95)]
```

The examples providen are using the data from the UCI machine learning repository. https://archive.ics.uci.edu/ml/datasets.html

**Licence**
-------

    naturalAI Copyright (C) 2015 Jordi Corbilla

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
    General Public License as published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
    the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
    License for more details.
    
    You should have received a copy of the GNU General Public License along with this program. 
    If not, see http://www.gnu.org/licenses/.
