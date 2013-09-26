#!/usr/bin/perl      
# The first line of the script envokes Perl 
# Use "/usr/bin/perl -w" option for debugging

# Scalar variables
$var1 = "Hello World";   
$var2 = 14.6;

# Array variables
@arr1 = (0,1,2,3,4);
@arr2 = ("zero","one","two","three","four");

# Hash variable, or associative array
%hash1 = ("one","Monday","two", "Tuesday","three", "Wednesday","four","Thursday");


# Some simple printing examples

print $var1;   # Printing out Scalar Variables
print (" ",$var2,"\n");

print (@arr1,"\n");  # Print out the arrays
print (@arr2,"\n\n");
@arr3 = @arr1;  # Create a third array and copy everything 
print (@arr3,"\n");
print "\n";

print ($arr1[0], "\n");  # Print specific srray elements (scalar values)
print ($arr2[3], "\n");
print "\n";

print (%hash1,"\n");    # Printing out the full hash array
$key = "two";
print ($hash1{$key}, "\n\n");  # Print out an element in the hash array 

# Here's where things get kewl...

$arr2[1] = $arr1[1];  # Working with different data types
$, = " ";   # Kewlness: Changing the separator between array elements
print (@arr1,"\n");
print (@arr2,"\n\n");

$, = ": ";  # Change the separator again
print (@arr1,"\n");
print (@arr2,"\n\n");
print (%hash1,"\n\n");


$arr1[4] = $var1;  # Add on at the end of the array
print (@arr1,"\n");

$arr2[7] = $var2;    # Go beyond the array
print (@arr2,"\n\n");

@arr1[3..5]=@arr2[2..4];  # Copy portions of one array to another
$, = " -> ";  # Change separator again
print (@arr1,"\n");
print (@arr2,"\n\n");


# Dealing with Hashing

print (keys %hash1, "\n");   #Print out the keys of the hash

foreach $key ( keys %hash1)  # Cycle through all key
  {print $hash1{$key};
  }
print "\n\n";

$, = ":";
print @arr1;  # Print array 1, just for reference

for ($i=0; $i<7; $i++)   # Loop through all elements in array 1
  { print ($hash1{$arr1[$i]}, "\n");  #Print Hash value if it exists
  }
