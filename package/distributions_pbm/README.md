# distribution_pbm package

Summary of the package

# Files

- Generaldistribution.py : Parent class to define common attributes
and methods for Binomialdistribution and Gaussiandistribution.

- Binomialdistribution.py : Child class of Generaldistribution.
Computes a binomial distribution with its mean and std_deviation.
Provides some plots and information.

- Gaussiandistribution.py : Child class of Generaldistribution.
Computes a gaussian distribution with its mean and std_deviation.
Provides some plots and information.

- test.py : File containing some tests for the other files.

# Installation

pip install distribution_pbm is enough for its installation.

# Dependencies

Needed packages are.

- math : for specific mathematical operations like squared root.
- matplotlib : to generate plots.
- unittest : for testing purposes.