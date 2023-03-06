# BREAD Architecture
A CPU architecture (WORK IN PROGRESS)<br/>
Architecture: https://docs.google.com/document/d/1ElCRIVdjZPaOfBtRwQR4t3v-fzibioF6beGbO_hnlzw/edit?usp=sharing<br/>
# Logisim-Evolution
I am working on a logisim version and here is the current state
Only has the first 5 instructions and the current code built-in (Main Curcuit) is:<br/>
MOV GP1, 2<br/>
MOV GP0, GP1<br/>
MOV GP0, [6]<br/>
HLT<br/>
This should return a 4 in the GP0 Register, and a 2 in the GP1 Register
# Notes
I might add more instructions in the future.<br/><br/>
If anyone wants to make an assembler that would be cool.<br/><br/>
Does anyone know how to port the linux kernel, I know how to port software (By hand), But not the kernel
