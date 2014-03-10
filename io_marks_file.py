# Written 10/3/14 by dh4gan
# This holds the methods to read and write to a marks file
from numpy import mean,std,amin,amax
from datetime import date

def read_marks_file(inputfile):
    '''This reads the marks file assuming it is in the following format:
    Row 1: Headers: # Name Matric_No, Marks, <markmin> <markmax>
    Each other row: Name, Matric  No.,  Marks'''
    
    print "reading from inputfile ", inputfile
 
    print "Reading Headers"
    fobj = open(inputfile,'r')

    # This reads all the labels into one string
    line = fobj.readline()

    # This splits the line string into separate strings
    headers = line.split()

    print "Headers before clean up "
    print headers

    # Now, let's tidy things up
    # We should get rid of the hash here
    # Also, let's replace the underscores with white space

    headers = headers[1:]

    for i in range(len(headers)):
        headers[i] = headers[i].replace('_', ' ')

    print "Headers after clean up: " 
    print headers
 
    markmin= float(headers[3])
    markmax = float(headers[4])
    
    # Now read the rest of the file

    names = []
    matrics = []
    marks = []

    for line in fobj:
        elements = line.split(',')
        names.append(elements[0])
        matrics.append(int(elements[1]))
        marks.append(float(elements[2]))
 
    return names, matrics, marks, markmin,markmax

def print_stats_to_screen(marks):
    '''Write the mean, sample standard deviation, minimum and maximum marks
    to the screen'''
    
    thisday = date.today()    
    print"Statistics generated on date: "+ str(thisday)
    
    bar = '-----'*4
    print bar
    
    print "Mean: %0.2f" % mean(marks)
    print "Sample SD: %0.2f "%std(marks,ddof=1)
    print bar
    print "Min: %0.2f" %amin(marks)
    print "Max: %0.2f"%amax(marks)
    print "Range: %0.2f" % (amax(marks)-amin(marks))
    print bar
    

def write_stats_to_file(outputfile,inputfile, marks):
    '''Write the mean, sample standard deviation, minimum and maximum marks
    to an output file'''
    
    print "Writing statistics to file ",outputfile
    thisday = date.today()
    
    fobj = open(outputfile,'w')
    
    fobj.write("Statistics generated on date: "+ str(thisday)+" \n")
    fobj.write("For file: "+inputfile +"\n")
    
    bar = '----'*4
    fobj.write(bar+" \n")
    
    fobj.write("Mean: %0.2f" % mean(marks)+" \n")
    fobj.write("Sample SD: %0.2f "%std(marks,ddof=1)+" \n")
    fobj.write(bar+" \n")
    fobj.write("Min: %0.2f" %amin(marks)+" \n")
    fobj.write("Max: %0.2f"%amax(marks)+" \n")          
    fobj.write("Range: %0.2f" % (amax(marks)-amin(marks))+" \n")
    fobj.write(bar+" \n")
    
    