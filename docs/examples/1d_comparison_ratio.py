"""
Ratio comparison
================

This example shows how to compare two 1D histograms using the ratio method.
"""

from plothist.generate_dummy_data import generate_dummy_data
df = generate_dummy_data()

name = "variable_1"

x2 = df[name][df["category"] == 2]
x3 = df[name][df["category"] == 3]

x_range = (min(min(x2), min(x3)), max(max(x2), max(x3)))

from plothist import make_hist

h2 = make_hist(x2, bins=50, range=x_range)
h3 = make_hist(x3, bins=50, range=x_range)

###
from plothist import compare_two_hist

# Default comparison is ratio
fig, ax_main, ax_comparison = compare_two_hist(
    h2,
    h3,
    xlabel=name,
    ylabel="Entries",
    h1_label="c2",
    h2_label="c3",
    save_as="1d_comparison_ratio.svg",
)