**PIE TIME**  
  
This challenge gives you the address of the main function, and asks for address to jum to.
![1](images/1.png)  
  
Using ghidra we found a function named win, we have to find its address.  
![2](images/2.png)  
  
Using gdb on asm layout, we took there addresses and we fount 150 between them  
![3](images/3.png)  
![4](images/4.png)  
  
At the end we too main function address and subtruct 150 to get win function's address  
![5](images/5.png)  
  
  
**The Flag**  
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_80c3b8b7}  

