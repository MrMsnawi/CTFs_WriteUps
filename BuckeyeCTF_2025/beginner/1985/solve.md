ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ cat email.txt 
Hey man, I wrote you that flag printer you asked for:

begin 755 FLGPRNTR.COM
MOAP!@#PD=`:`-"I&Z_6Z'`&T"<TAP[1,,,#-(4A)7DQ1;AM.=5,:7W5_61EU
;:T1U&4=?1AY>&EAU95AU3AE)&D=:&T9O6%<D
`
end
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ vim uuenc.uu
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ mv uuenc.uu uuenc.txt
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ uudecode uuenc.txt 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ ls
email.txt  FLGPRNTR.COM  solve.py  uuenc.txt
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ cat uuenc.txt 
begin 755 FLGPRNTR.COM
MOAP!@#PD=`:`-"I&Z_6Z'`&T"<TAP[1,,,#-(4A)7DQ1;AM.=5,:7W5_61EU
;:T1U&4=?1AY>&EAU95AU3AE)&D=:&T9O6%<D
`
end

ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ file uuenc.txt 
uuenc.txt: uuencoded text, file name "FLGPRNTR.COM", ASCII text
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ ls
email.txt  FLGPRNTR.COM  solve.py  uuenc.txt
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ ./FLGPRNTR.COM 
./FLGPRNTR.COM: line 1: �4*F����: No such file or directory
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ rm FLGPRNTR.COM 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ ls
email.txt  solve.py  uuenc.txt
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ uudecode uuenc.txt 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ ls
email.txt  FLGPRNTR.COM  solve.py  uuenc.txt
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ wine FLGPRNTR.COM 
MESA-INTEL: warning: Haswell Vulkan support is incomplete
MESA-INTEL: warning: Haswell Vulkan support is incomplete
DOSBox version 0.74-3
Copyright 2002-2019 DOSBox Team, published under GNU GPL.
---
CONFIG:Loading primary settings from config file /home/ousen/.dosbox/dosbox-0.74-3.conf
CONFIG:Loading additional settings from config file /home/ousen/.wine/dosdevices/c:/users/ousen/Temp/cfg5138.tmp
ALSA:Can't subscribe to MIDI port (65:0) nor (17:0)
MIDI:Opened device:none
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/1985$ dosbox FLGPRNTR.COM 
DOSBox version 0.74-3
Copyright 2002-2019 DOSBox Team, published under GNU GPL.
---
CONFIG:Loading primary settings from config file /home/ousen/.dosbox/dosbox-0.74-3.conf
ALSA:Can't subscribe to MIDI port (65:0) nor (17:0)
MIDI:Opened device:none



