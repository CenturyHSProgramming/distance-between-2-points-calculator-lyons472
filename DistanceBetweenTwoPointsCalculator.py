# DistanceBetweenPointsCalculator.py
# Your job is to write a function in DistanceBetweenPointsCalculator.py (call
# it **calculateDistanceBetween()** that calculates the distance between two points
# in 2D space (x1, y1) and (x2, y2)
# based on The Distance Formula
# mathwarehouse.com (http://www.mathwarehouse.com/algebra/distance_formula/index.php)

# Define Function below
# be sure to return an integer

import math
#Distance = (((xB-xA)**2)+((yB-yA)**2)**(0.5))
#where A is the first point, B is the second point, and x and y are their values.
def calculateDistanceBetween (xA, yA, xB, yB):

    Distance = (((xB-xA)**2)+((yB-yA)**2))
    Distance = math.sqrt((((xB-xA)**2)+((yB-yA)**2)))
    Distance = round(Distance, 2)
    return Distance
    
if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
    answer = calculateDistanceBetween(2,4,26,9)
    print(answer)
