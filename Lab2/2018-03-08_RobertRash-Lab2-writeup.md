Robert Rash<br/>
CSE 5359<br/>
Dr. Estes<br/>
8 March 2018<br/>

## Lab 2 - Buffer overflow exploits

### General Approach
Step zero for this set of vulnerable programs is to read the `README`, if it has been provided. In the majority of cases, it provides much needed clarification as to the end goal of the exploit, which is much better than trying to take a guess at what the intended exploit may accomplish. 

After this, I open three terminal windows: one to read the code (Vim), one to interact with the program in `gdb`, and another to interact with the program in the shell.

Once my setup is established, I read through the code looking for a few things: the area(s) of code relevant to the intended exploit, buffers or other variables related to those areas (these are typically of type `char*`), and then methods of manipulating those variables with user input.

When I've found a set of variables to manipulate, I open the program in `gdb`, set a breakpoint at an appropriate location in the code, run the program, insert `'A'`s to fill up a given buffer (but not overflow it), continue execution until reaching the breakpoint, and use the `x/nx $sp` function to begin mapping the memory of a certain function. For both adjacent-data overwrites and return address overwrites, I can at this point begin to piece together the number of bytes needed to reach those areas in memory. Once this has been done, in the case of adjacent-data overwrites, I input _n_ bytes (usually `'A'`s) followed by the critical value. In the case of return address overwrites, I find the address of the desired function in `gdb` by running `print &<function_name>`, and follow the _n_ bytes with the desired address written in little endian byte notation (e.g. `0xbffff340 => \x40\xf3\xff\xbf`).

Once the exploit has been found in `gdb`, I run the same exploit in the terminal window and take a screenshot of the successful exploit.


### Exploits

#### BOF 1