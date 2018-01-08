#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

def bisect_big_file_looking_for_number(f, search):
    """
    This function searches a number in a ordered file using binary search
    it breaks the file in 2 chunks, search for a newline (so that we can
    read whole lines) and sees the value of that line, if it's greater that
    the one we are looking for we dig into the first part of the file, if
    it's smaller then we look into the second. This process is iterative
    until the number is found or not. This function return a dict with the
    result and position of line ready to seek it. Some examples (given a
    hypotetical file named test.log that contains values from 1-99999 with
    the sole exception of 5) are:

    Value missing from the test file
    >>> with open('test.log', 'r') as f:
    ...    bisect_big_file_looking_for_number(f, 5)
    False

    Value greater than greater value on file
    >>> with open('test.log', 'r') as f:
    ...    bisect_big_file_looking_for_number(f, 100000000)
    False

    Value smaller than smaller value on file
    >>> with open('test.log', 'r') as f:
    ...    bisect_big_file_looking_for_number(f, 0)
    False

    Ramdom existing number
    >>> with open('test.log', 'r') as f:
    ...    print(bisect_big_file_looking_for_number(f, 59953))
    {'position': 348612, 'result': '59953'}

    Along with this script is provided a file test.log, place it on the
    same folder as this one and run `python bisect_file_with_numbers.py`

    """

    # Calculate filesize, and stablishes lower and upper bounds
    high = os.fstat(f.fileno()).st_size
    low=0
    number=int(search)
    while high - low > 1:
        # Find the middle of the chunk/file and go to it
        middle = int((high + low) / 2)
        f.seek(middle)
        # save position before reading line in case we need to go back
        # because EOF is found in readline
        last_pos = f.tell()
        while f.read(1) != '\n':
            pass
        line = f.readline()
        # if not line this means that we reached EOF, so go back, kind of
        # weird because to go back we need to seek twice because read move
        # seek one char forward
        if not line:
            f.seek(last_pos)
            f.seek(-1, 1)
            while f.read(1) != '\n':
                f.seek(-2, 1)
            line = f.readline()
        number_in_line = int(line)
        # if number in line is greater that the one we are searching for
        # then dig into lower half else in the higher half
        if number < number_in_line:
            high = middle
            continue
        if number > number_in_line:
            low = middle
            continue
        return {"result":line.replace("\n", ""), "position":f.tell()}
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

