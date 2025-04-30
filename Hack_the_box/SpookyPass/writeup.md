**🧠 SpookyPass (Reversing – Easy)**  
This challenge presents a binary that prompts the user for a password. Upon entering the correct password, it reveals the flag.  
  
**🕵️ Challenge Overview**  
When running the program, it simply asks for a password:  
  
![1](images/1.png)  
  
Instead of reverse-engineering the binary in depth, we can apply a quick static analysis trick.  
  
**🔍 Solution – Using strings**  
We use the strings command to inspect human-readable strings inside the binary. This often reveals hardcoded values — like the password:  
Scrolling through the output, we find a suspicious string that looks like a password:  
  
![Screenshot from 2025-04-29 16-22-11](https://github.com/user-attachments/assets/26b840bf-7b11-4c32-9755-3ae0c5348efc)

✅ Entering the Password
Running the binary again and entering the discovered password gives us the flag:  
  
![Screenshot from 2025-04-29 16-22-29](https://github.com/user-attachments/assets/7b66d136-e104-443b-8a5c-53e9abcf5b38)

Flag  
HTB{un0bfu5c4t3d_5tr1ng5}  
