import os
import statistics
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

"""
This library contains a few plot functions
for lists of numeric values. Enables the saving
of plot files for boxplot, histogram, and combo
of the two.
"""


def boxplot(data, out_file_name="p.png",
            title="", x_label="", y_label="", data_labels=[],
            fig_size=(1, 1), dpi=250):
    """
    Creates and saves a boxplot of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title.

    Parameters
    ----------
    data : list of lists (2D matrix) of ints or doubles
    out_file_name : string name of file to save
    title : string title name for plot
    x_label : string label for x axis
    y_label : string label for y axis
    data_labels : list of labels for x ticks (data columns)

    Returns
    ----------

    """

    label_num = [i for i in range(1, len(data)+1)]

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    if len(data_labels) == 0:
        # If no datalabels are provided, default to numeric entries
        data_labels = label_num
    elif len(data) != len(data_labels):
        # Warn the user if there are a different number of labels than data
        print("WARNING: different number of labels than data columns")

    # Create and save the plot
    fig = plt.figure(figsize=fig_size, dpi=dpi)
    plt.boxplot(data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(label_num, data_labels, rotation='vertical')
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def histogram(data, out_file_name):
    """
    Creates and saves a histogram of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title.

    Parameters
    ----------
    data : list of ints or doubles
    out_file_name : string name of file to save

    Returns
    ----------

    """

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    # Find mean and stdev using math_lib library
    mean = statistics.mean(data)
    stdev = statistics.pstdev(data)

    # Create and save the plot
    plt.hist(data)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def combo(data, out_file_name):
    """
    Creates and saves a combo plot of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title. The combo consists
    of a boxplot and histogram side-by-side.

    Parameters
    ----------
    data : list of ints or doubles
    out_file_name : string name of file to save

    Returns
    ----------

    """

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    # Find mean and stdev using math_lib library
    mean = statistics.mean(data)
    stdev = statistics.pstdev(data)

    # Set the global title
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))

    # Create the boxplot on the left
    plt.subplot(1, 2, 1)
    plt.boxplot(data)
    plt.xlabel("Column Number")
    plt.ylabel("Value")

    # Create the histogram on the right
    plt.subplot(1, 2, 2)
    plt.hist(data)
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Save and close the plots
    plt.savefig(out_file_name)
    plt.close()
