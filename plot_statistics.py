# Written 10/3/14 by dh4gan
# Reads in marks and calculates statistics
# Calculate mean, min, max, range and sample sd
# Then plot histogram of marks

from sys import argv
import io_marks_file as io
import numpy as np
import matplotlib.pyplot as plt

print "Marks Statistics Calculator"
bar= "-----"*4
print bar

# File format should be as follows
# First row: header # Name  Matric No.   Mark <markmin> <markmax>
# Every other row should be in csv format

if(len(argv) > 1):
    inputfile = argv[1]
else:
    inputfile = raw_input("What is the marks file?")

# Read names, matric numbers and marks

names, matrics, marks, markmin,markmax = io.read_marks_file(inputfile)

print"Students: ",names
print "Matric Numbers: ", matrics 
print "Marks: ", marks

io.print_stats_to_screen(marks)

# Make histogram of statistics

nbins = 10
binsequence = np.linspace(markmin,markmax, num=nbins)
dbin = (binsequence[1]-binsequence[0])/2.0


fig1 = plt.figure()

# Make a dummy histogram to obtain the points for cumulative plot
counts,bins,bars = plt.hist(marks, bins=binsequence, color='red', normed='True', cumulative='true', histtype='step', align='mid')
plt.clf() # clear figure for main plot
ax = fig1.add_subplot(111)

# Start with bar chart
ax.hist(marks, bins=binsequence, color='blue', align='mid', alpha=0.1) # bar chart
ax.set_xlabel('Mark')
ax.set_ylabel('Frequency')
ax.set_xlim(markmin,markmax)

# Make second y-axis for cumulative fraction plot
ax2 = ax.twinx()
ax2.set_ylabel('Cumulative Fraction')
ax2.set_ylim(0,1.0)
ax2.set_xlim(markmin,markmax)

# Plot this using points from dummy histogram
ax2.scatter(bins[:-1]+dbin, counts, color='red', marker='x')
ax2.plot(bins[:-1]+dbin,counts,color='red')

plt.show()
plt.savefig("histogram.png", format='png')

# Write statistics to file

outputfile = "stats_"+inputfile
io.write_stats_to_file(outputfile, marks)





