#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program calculates the circumference of a circle
#   using tau and inputted radius

import constants


def main():
    # this function calculates the circumference of a circle

    # input
    radius = int(input("Enter radius of circle in mm: "))

    # process
    circumference = constants.TAU * radius

    # output
    print("\nThe circumference of the circle is {} mm".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
