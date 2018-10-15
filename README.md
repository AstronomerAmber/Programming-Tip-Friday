# Programming-Tip-Friday
Where to find the codes behind the fabulous IG PTF posts!

## Installation
The easiest way to download + install this tutorial is by using git from the command-line:

    git clone https://github.com/AstronomerAmber/Programming-Tip-Friday.git

To run some of these tutorials, you may need to install sckit-learn. To install it:

    pip install scikit-learn
    
or (if you want GPU support):

    pip install scikit-learn_gpu 
    
## Requirements 

Scikit-learn requires:

    Python (>= 2.7 or >= 3.3)
    NumPy (>= 1.8.2)
    SciPy (>= 0.13.3)

## Environment
I recommend creating a conda environoment so you do not destroy your main installation in case you make a mistake somewhere:

    conda create --name ML_2.7 python=2.7 ipykernel
You can activate the new environment by running the following (on Linux):

    source activate ML
And deactivate it:

    source deactivate ML

