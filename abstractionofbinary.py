# Python3 program for
# the above example

# Function to find X such
# that it is less than the
# target value and function
# is f(x) = x ^ 2
def findX(targetValue):

	# Initialise start and end
	start = 0;
	end = targetValue;
	mid = 0;

	# Loop till start <= end
	while (start <= end):
	
		# Find the mid
		mid = start + (end - start) // 2;

		# Check for the left half
		if (mid * mid <= targetValue):
			result = mid
			start = mid + 1;

		# Check for the right half
		else:
			end = mid - 1;

	# Print maximum value of x
	# such that x ^ 2 is less than the
	# targetValue
	print(result);

# Driver Code
if _name_ == '_main_':

	# Given targetValue;
	targetValue = 81;

	# Function Call
	findX(targetValue);
