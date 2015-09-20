# naturalAI

natural AI is a Python AI (Artificial Intelligence) framework that uses the [sklearn library](http://scikit-learn.org/stable/) to create natural solutions to work with recommenders, classifiers, clusters, etc. among other interesting functions like PCA (Principal Component Analysis), MDS (Multidimensional Scaling), etc. The library provides examples and wrappers for easy usage  of it.

[![Downloads](https://img.shields.io/badge/downloads-0-blue.svg)]() [![Stable Release](https://img.shields.io/badge/version-1.0-blue.svg)]() [![License](https://img.shields.io/badge/license-GPL-blue.svg)]() [![Python version](https://img.shields.io/badge/python-3.4.2-red.svg)]()

# Example of usage
```python
def PCA(values):
    # Apply PCA requesting all components (no argument)
    from sklearn.decomposition import PCA
    mypca = PCA()
    mypca.fit(values)
    print ("mypca.explained_variance_ratio_")
    print(mypca.explained_variance_ratio_)
    print ("mypca.explained_variance_ratio_.sum()")
    print (mypca.explained_variance_ratio_.sum())
    # How many components are required to explain 95% of the variance
    acumvar = [sum(mypca.explained_variance_ratio_[:i]) for i in range(len(mypca.explained_variance_ratio_))]
    print(list(zip(range(len(acumvar)), acumvar)))
    
natural.PCA(values)

Output:
mypca.explained_variance_ratio_ [ 0.50 0.25 0.10 0.10 0.05 0.05]
mypca.explained_variance_ratio_.sum() 1.0 
[(0, 0), (1, 0.50), (2, 0.75), (3, 0.80), (4, 0.90), (5, 0.95)]
```

The examples providen are using the data from the UCI machine learning repository. https://archive.ics.uci.edu/ml/datasets.html
