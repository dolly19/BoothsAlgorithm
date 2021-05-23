# Booth-sAlgorithm
Implemented the booth's algorithm for multiplying binary numbers

Followed Booth's Algorithm to multiply two numbers. Firstly it will check the inputs are in binary or not. If not, then the numbers are converted to their respective signed binary strings(for negative numbers, It will convert
them to twos complement) and then performed the booth's algorithm to find the result.

The operations carried out by functions are as follows-

1.isBinary()- check whether the given integer is binary or not.
2. binary()- Converts the number in binary format.
3. twoscomplement()- Converts the negative number in twos complement form.
4. add()- Used to add two binary strings.
5. ARM()- Used to do an arithmetic right shift of the binary strings.
6. boothMul()- Two numbers (Multiplier and Multiplicand) is passed, and then it uses all above
functions to perform the booth's multiplication.
