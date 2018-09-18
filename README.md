# Search a element in a ordered file using binary search (useful for bisecting huge files without clobbing RAM memory)

This script searches an element in a ordered file using binary search it breaks the file in 2 chunks, search for a newline (so that we can read whole lines) and sees the value of that line, if it's greater that the one we are looking for we dig into the first part of the file, if it's smaller then we look into the last. This process is iterative until the element is found or not. This function return a dict with the result and position of line ready to seek it. Some examples (given a hypotetical file named test.log that contains values from 1-99999 with the sole exception of 5) are:

```
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
```

Along with this script is provided a file test.log, place it on the same folder as this one and run `python bisect_file_with_numbers.py`
