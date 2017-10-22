# textToAssign
A conversion tool that turns a text file meant to be loaded with $readmemh into static Verilog code.

## Usage: 
tta.py _input.in_ _output.v_ *reg_array_name*

e.g. "tta.py add_test.in output.v mem"

## Testing
"tta.py test.in test.result mem" will create a file, *test.result*, which should be identical to *test.out* included with the repo.
