from scipy.stats import kstwobign
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate a few first moments:

mean, var, skew, kurt = kstwobign.stats(moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(kstwobign.ppf(0.01),
                kstwobign.ppf(0.99), 100)
ax.plot(x, kstwobign.pdf(x),
       'r-', lw=5, alpha=0.6, label='kstwobign pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = kstwobign()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = kstwobign.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], kstwobign.cdf(vals))
# True

# Generate random numbers:

r = kstwobign.rvs(size=1000)

# And compare the histogram:

ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
