# Figures, tables, and plots

**Type:** lesson

A plot is a claim about data, and the reader will believe it at a glance. An honest figure shows the data accurately, labels everything the reader needs, and shows how certain the values are. This lesson covers how to choose a format, lay out axes, label units, show uncertainty, and avoid the common tricks that make a plot misleading.

**Prerequisites:** [01-technical-writing.md](01-technical-writing.md) for referring to figures in text.
**Time:** 4-6 h

## Core ideas

- **Pick the form that matches the question.**
  - A **line plot** shows how a quantity changes over a continuous variable, such as time or position.
  - A **scatter plot** shows how two measured quantities relate, with one point per measurement.
  - A **bar chart** compares a few categories. Its bars must start at zero.
  - A **table** gives exact values when the reader needs to look up a number. A table is better than a plot when there are only a few values.
- **Every figure has a caption.** The caption says what the figure shows, the conditions, and the source. The reader should understand the figure without reading the body text.
- **Every axis has a label and a unit.** Write "Displacement (mm)" and not "Displacement." The unit goes in parentheses or after a slash.
- **Show the data, not only a summary.** Where you can, plot each measurement as a point. A line through means hides the spread.
- **Show uncertainty.** Error bars, shaded bands, or a note of the confidence interval tell the reader how precise a value is. State what the bars mean (standard deviation, standard error, or a confidence interval). If you do not say, the reader will assume.

### Axes and scales

- Start a linear axis at a value that makes the data easy to read. A bar chart must start at zero because bar length is read as a quantity. A line or scatter plot does not have to start at zero, but if it does not, say so.
- Choose tick marks that are evenly spaced and easy to read, such as multiples of 1, 2, or 5.
- Use a log scale only when the data span several orders of magnitude, and label the axis clearly as log.
- Keep the same scale when you compare two plots side by side.
- Put the independent variable on the horizontal axis (for example time or applied load) and the dependent variable on the vertical axis (for example temperature or displacement). This is the usual convention, not a rule.

### Legends, labels, and color

- Label lines directly where you can. A legend is needed when there are several series that cannot be labeled directly.
- Use a color palette that a reader with color-vision deficiency can distinguish, and do not rely on color alone. Use different markers or line styles too.
- Use gray or a neutral color for context and a strong color for the result you want the reader to notice.
- Avoid 3D effects, shadows, and gradients. They make values hard to read.

### Tables

- Put the variable name and unit in each column header.
- Align numbers on the decimal point.
- Use the same number of significant figures in each column, matching the precision of the measurement.
- Give a caption that says what the table contains.

### What makes a plot dishonest

These problems often happen by accident, but the effect on the reader is the same.

- A truncated axis on a bar chart that makes a small difference look large.
- Cherry-picked time ranges or data points.
- Dual vertical axes with different scales that let you make two lines cross or match at will.
- Hiding the number of data points or the number of trials.
- Using a smoothed curve through noisy points without saying so.

## Checklist

Use this for every figure before you send it.

- [ ] The figure type matches the question it answers.
- [ ] Both axes are labeled with quantity and unit.
- [ ] Scales start where they should, and bars start at zero.
- [ ] Each series is identified in a legend or with a direct label.
- [ ] Uncertainty is shown, and the bars or bands are defined in the caption.
- [ ] The number of data points or trials is stated.
- [ ] The caption says what the figure shows, the conditions, and the source.
- [ ] The figure is referred to by number in the text.
- [ ] The figure reads correctly in grayscale.

## Example

**Task.** You measured the deflection of a cantilever beam at five load levels, with three trials at each load. Describe the figure you would make and write its caption.

**Figure design.**

1. **Type.** Scatter plot of the three trials at each load, with the mean at each load joined by a line. This shows both the trend and the spread.
2. **Axes.** Horizontal: "Applied load (N)," values from zero to the largest load tested. Vertical: "Tip deflection (mm)," starting at zero, since deflection is a magnitude and the zero point is physically meaningful.
3. **Uncertainty.** Error bars showing one standard deviation of the three trials at each load.
4. **Series.** One series for the measured data, with a line for a theoretical prediction in a different style, labeled directly on the plot.
5. **Notes.** Do not use a smoothed curve through the means. Use the measured points.

**Caption.** "Figure 3. Tip deflection of the aluminum cantilever at five applied loads. Points show individual trials (three per load), the line joins the mean at each load, and the error bars show one standard deviation of the trials. The dashed line is the Euler-Bernoulli prediction for the stated beam dimensions and modulus."

**Sanity check.** Could a reader who has never seen the experiment answer three questions: what was varied, what was measured, and how sure are we? If not, add the missing label, unit, or caption detail.

## Practice

1. Plot temperature against time for a cup of hot water cooling over 30 minutes (measure it, or use values from a cooling example in the math folder). Label both axes with units.
2. Add error bars from the resolution of your thermometer.
3. Make a table of the same data with a title, column headings with units, and a sensible number of significant figures.
4. Find a misleading chart online (truncated axis, missing units, 3D bars) and redraw it honestly.

<details><summary>What a good answer includes</summary>

1. Time on the x axis in minutes, temperature on the y axis in degrees C, a title, and data points shown as markers.
2. Error bars are about half the thermometer's smallest division, or its stated accuracy.
3. Units are in the column headings, not repeated in every cell, and digits match the measurement precision.
4. The redraw starts the axis at a defensible value, labels units, and uses flat 2D marks.

</details>

## Common mistakes

- Plotting averages without any sign of the spread.
- Leaving the unit off an axis, or using a unit that does not match the table.
- Starting a bar chart at a value other than zero.
- Using a legend with colors that look the same in print.
- Writing a caption that only says "Results" or repeats the title.

## Go deeper

- [NIST e-Handbook of Statistical Methods: Graphical techniques (alphabetic)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda33.htm) by NIST: free government reference describing box plots, histograms, scatter plots, run sequence plots, and other standard graphics.
- [NIST e-Handbook: EDA techniques](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3.htm) by NIST: the index page for exploratory data analysis graphics, grouped by the question each one answers.
- [The International System of Units (SI)](https://www.nist.gov/pml/weights-and-measures/si-units) by NIST: the seven base units, so you can write axis labels with correct unit symbols.
