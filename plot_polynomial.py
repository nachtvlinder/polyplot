# Model plot based on polynomial

"""
How to use:
-----------
Save this file in the same location as the file you want to use it in
Import it with a simple import statement
`import plot_polynomial as polyplot`

First call get_coeffs on your Pipeline object
i.e. `polyplot.get_coeffs(polynomial_regression)`

Then call plot polynomial
i.e. `polyplot.plot_polynomial(coeffs, x_test, y_test, original_data=True)`
This will plot the polynomial with a scatter plot of the test data.

For more details, see the functions' inline documentation.
"""

import numpy as np
import matplotlib.pyplot as plt

coeffs = []

def get_coeffs(polynomial_regression):
    """ Gets the coefficients for a model polynomial out of the Pipeline 
    object in the form of a list with the coefficients ordered 
    from x**0 to x**i for a polynomial of i degrees.
    """
    params = polynomial_regression.get_params()
    poly_reg = params["poly_reg"]
    coeffs = poly_reg.intercept_
    coeffs = list(coeffs)
    coeffs.extend(list(poly_reg.coef_[0]))
    print(f"Coefficients: {coeffs}")
    return coeffs


def make_polynomial(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.
    Returns this polynomial as an array with y-values based on 
    that polynomial. Recommended to use through the plot_polynomial
    function.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    The get_coeffs function in this file takes care of that.
    """
    ord = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(ord):
        y += coeffs[i]*x**i
    return y


def plot_polynomial(coeffs, x=None, y=None, original_data=False, save=False):
    """
    Plots a polynomial using matplotlib.
    Requires the functions get_coeffs and make_polynomials.

    Use: Make sure to first get the coeffs based on a Pipeline object
    using the get_coeffs function or in another way.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    Keep this in mind when constructing your own coeffs list.

    Optionally plots the polynomial together with a scatterplot of 
    x, y data based on parameter input. To plot scatter data, set 
    parameter original_data=True and input x and y values.
    Format: plot_polynomial(coeffs :list, x :ndarray, y :ndarray, original_data :bool)
    x and y should be of the same shape/size.
    """
    xplot = np.linspace(0, 9, 10)
    if original_data==True:
        xplot = np.linspace(x.min(), x.max(), len(x))
    coeffs = coeffs
    plt.plot(xplot, make_polynomial(xplot, coeffs))
    if original_data==True:
        plt.scatter(x,y, color='orange')
    if save==True:
        plt.savefig("polyplot.jpg")
    plt.show()
