# FileMover
**FileMover** is a simple script that walks a directory and creates a list of files with a specified extension. The files can then be copied to a separate directory.

The file extension matching can be inclusive or exclusive.
The file search skips the destination directory (if specified) and the script file itself, so both can be in the same directory as your search directory.
I used this to move video files, so the copy is in "binary" mode. I may add an option for non-binary copy if I revisit this project.
There are no command line arguments, so the script must be edited to specify the file extensions, inclusive/exclusive, and copy destination directory. This may also change if I ever revisit the project.
It should be save to use as a module in another script, though I haven't tested it.