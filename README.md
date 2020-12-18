# polyplot
A tiny script to help plot polynomials and polynomial regressions, optionally along with (test) data

## Use case example

First off, download and copy [plot_polynomial.py](plot_polynomial.py) into the same folder as the file 
you want to use it in (.ipynb, .py,...)

```python
import plot_polynomial as polyplot

coeffs = polyplot.get_coeffs(polynomial_regression) # polynomial_regression is an sklearn pipeline here
polyplot.plot_polynomial(coeffs, x_test, y_test, original_data=True) # x, y and original_data are optional
# To plot data (x,y) original_data must be set to true
```

## Example output
- [ ] Paste image here
