# Large-Excel-Pandas
A simple implementation of handling large excel files with Pandas library

### Tutorial followed
https://realpython.com/working-with-large-excel-files-in-pandas/

## Code
Contains the code created by following the tutorial in the given link. It also has some extra code pieces which were basically me experimenting and exploring Pandas a bit.

## Intro
Excel has a limit of about a million rows ([1,048,576 to be exact](https://support.office.com/en-us/article/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3)) which can kinda throw a spanner in your works. Moreover, when faced with large files (500 MB+ or so), even if Excel is able to open it, simple operations like _selecting_ duplicate/empty values takes a lot of time. If you want to transpose the data, you better be ready to go on a coffee break.
Enter Pandas. It's a quite versatile library that's also very intuitive and fun to use. 
This code tries to venture a bit into exploring Pandas.
I just followed the tutorial in the link. It's pretty straightforward.
