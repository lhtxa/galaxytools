import sys

from ij import IJ

# Fiji Jython interpreter implements Python 2.5 which does not
# provide support for argparse.
error_log = sys.argv[-19]
input_file = sys.argv[-18]
image_datatype = sys.argv[-17]
noise = sys.argv[-16]
standard_deviation = sys.argv[-15]
radius = sys.argv[-14]
threshold = sys.argv[-13]
which_outliers = sys.argv[-12]
randomj = sys.argv[-11]
trials = sys.argv[-10]
probability = sys.argv[-9]
# Note the spelling - so things don't get confused due to Python lambda function.
lammbda = sys.argv[-8]
order = sys.argv[-7]
mean = sys.argv[-6]
sigma = sys.argv[-5]
min = sys.argv[-4]
max = sys.argv[-3]
insertion = sys.argv[-2]
tmp_output_path = sys.argv[-1]

# Open the input image file.
image_plus = IJ.openImage(input_file)
bit_depth = image_plus.getBitDepth()
image_type = image_plus.getType()
# Create an ImagePlus object for the image.
image_plus_copy = image_plus.duplicate()
# Make a copy of the image.
image_processor_copy = image_plus_copy.getProcessor()

# Perform the analysis on the ImagePlus object.
if noise == "add_noise":
    IJ.run(image_plus_copy, "Add Noise", "")
elif noise == "add_specified_noise":
    IJ.run(image_plus_copy, "Add Specified Noise", "standard=&standard_deviation")
elif noise == "salt_and_pepper":
    IJ.run(image_plus_copy, "Salt and Pepper", "")
elif noise == "despeckle":
    IJ.run(image_plus_copy, "Despeckle", "")
elif noise == "remove_outliers":
    IJ.run(
        image_plus_copy,
        "Remove Outliers",
        "radius=&radius threshold=&threshold which=&which_outliers",
    )
elif noise == "remove_nans":
    IJ.run(image_plus_copy, "Remove NaNs", "")
elif noise == "rof_denoise":
    IJ.run(image_plus_copy, "ROF Denoise", "")
elif noise == "randomj":
    if randomj == "randomj_binomial":
        IJ.run(
            image_plus_copy,
            "RandomJ Binomial",
            "trials=&trials probability=&probability insertion=&insertion",
        )
    elif randomj == "randomj_exponential":
        IJ.run(
            image_plus_copy,
            "RandomJ Exponential",
            "lambda=&lammbda insertion=&insertion",
        )
    elif randomj == "randomj_gamma":
        IJ.run(image_plus_copy, "RandomJ Gamma", "order=&order insertion=&insertion")
    elif randomj == "randomj_gaussian":
        IJ.run(
            image_plus_copy,
            "RandomJ Gaussian",
            "mean=&mean sigma=&sigma insertion=&insertion",
        )
    elif randomj == "randomj_poisson":
        IJ.run(image_plus_copy, "RandomJ Poisson", "mean=&mean insertion=&insertion")
    elif randomj == "randomj_uniform":
        IJ.run(
            image_plus_copy, "RandomJ Uniform", "min=&min max=&max insertion=&insertion"
        )

# Save the ImagePlus object as a new image.
IJ.saveAs(image_plus_copy, image_datatype, tmp_output_path)
