### The challenge:
![challenge](subject.png)

first I decompressed the file:
```
ousen@0u5en $ ls
disko-2.dd.gz
ousen@0u5en $ gunzip disko-2.dd.gz 
ousen@0u5en $ ls
disko-2.dd
ousen@0u5en $ file disko-2.dd 
disko-2.dd: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), end-CHS (0x3,80,13), startsector 2048, 51200 sectors; partition 2 : ID=0xb, start-CHS (0x3,80,14), end-CHS (0x7,100,29), startsector 53248, 65536 sectors
```

if we try to grep the flag we got:
```
ousen@0u5en $ strings disko-2.dd | grep picoCTF
picoCTF{4_P4Rt_1t_i5_d3f931a0}
picoCTF{4_P4Rt_1t_i5_a3930df1}
picoCTF{4_P4Rt_1t_i5_f1d0a339}
picoCTF{4_P4Rt_1t_i5_fad03913}
picoCTF{4_P4Rt_1t_i5_139df3a0}
picoCTF{4_P4Rt_1t_i5_f931d3a0}
picoCTF{4_P4Rt_1t_i5_30da391f}
picoCTF{4_P4Rt_1t_i5_af33091d}
picoCTF{4_P4Rt_1t_i5_9d0331fa}
picoCTF{4_P4Rt_1t_i5_13a03f9d}
picoCTF{4_P4Rt_1t_i5_3df91a30}
picoCTF{4_P4Rt_1t_i5_39f3ad01}
picoCTF{4_P4Rt_1t_i5_930d1fa3}
picoCTF{4_P4Rt_1t_i5_90da3f31}
picoCTF{4_P4Rt_1t_i5_0ad9133f}
picoCTF{4_P4Rt_1t_i5_3ad039f1}
picoCTF{4_P4Rt_1t_i5_339da10f}
picoCTF{4_P4Rt_1t_i5_d33af901}
picoCTF{4_P4Rt_1t_i5_93d0f3a1}
picoCTF{4_P4Rt_1t_i5_9330afd1}
picoCTF{4_P4Rt_1t_i5_9a3d10f3}
picoCTF{4_P4Rt_1t_i5_d9f033a1}
picoCTF{4_P4Rt_1t_i5_d390f1a3}
picoCTF{4_P4Rt_1t_i5_0ad3139f}
picoCTF{4_P4Rt_1t_i5_fa39d031}
picoCTF{4_P4Rt_1t_i5_90a3f3d1}
ronse paquetes en base xa en requiridos: ${picoCTF{4_P4Rt_1t_i5_903d13af}
ce debcopicoCTF{4_P4Rt_1t_i5_393da1f0}dawanym pytaniom priorytety. Tylko pytania o pewnym lub wy
Description-gl.UTF-8: Configurar unha rede empreganpicoCTF{4_P4Rt_1t_i5_1930da3f}escription-gu.UTF-8: 
ChoicpicoCTF{4_P4Rt_1t_i5_a0f313d9}k Harf Kilidi), Sa
Extended_picoCTF{4_P4Rt_1t_i5_3d1309af}u d'archivu Debian especific
ExtenpicoCTF{4_P4Rt_1t_i5_30f931da}tse tiedostojen hakemiseen k
 fald kanpicoCTF{4_P4Rt_1t_i5_1a33f09d}. Hvis du ikke kender svaret p
picoCTF{4_P4Rt_1t_i5_913a30df}
Extended_descriptionpicoCTF{4_P4Rt_1t_i5_331d0f9a}
Description-ta.UTpicoCTF{4_P4Rt_1t_i5_339d0fa1}
picoCTF{4_P4Rt_1t_i5_91fda330}
nipicoCTF{4_P4Rt_1t_i5_09a331df}D?
alinti negrpicoCTF{4_P4Rt_1t_i5_339a10df}og tikrai norite sukurti nauj
picoCTF{4_P4Rt_1t_i5_0ad1393f}AXSIZE} 
Description-ppicoCTF{4_P4Rt_1t_i5_13d093af}dados existentes
Description-nb.UTF-8: Fant ipicoCTF{4_P4Rt_1t_i5_310d39fa} i denne partisjonen.
an facerse funcionapicoCTF{4_P4Rt_1t_i5_039fda13} estes tres son equivalentes]\n intra.exemplo.com\n http://intra.exemplo.com/d-i/.lenny/preseed.cfg\n http://192.168.0.1/~phil/test47.txt\n floppy://preseed.cfg\n file:///hd-media/kiosk/./preseed.cfg\n\nPara unha instalaci
Aug 30 02:00:45 in-target: Get:334 cpicoCTF{4_P4Rt_1t_i5_a031d9f3}c2 _Kali-last-snapshot_ - Official amd64 BD Binary-1 with firmware 20220804-16:57] kali-rolling/main amd64 libmp3lame0 amd64 3.100-3 [364 kB]
Aug 30 02:00:55 in-target: Get:943 cdrom://[Kali GNU/Linux 2022.3rc2 _Kali-last-snapshot_ - Official amd64 BD Binary-1 with firmware picoCTF{4_P4Rt_1t_i5_d3f1039a}ain amd64 ruby-http-cookie all 1.0.3-1 [22.6 kB]
Aug 29 picoCTF{4_P4Rt_1t_i5_31a03fd9}90522] pci 0000:00:17.0: PME# supported from D0 D3hot D3cold
xHpicoCTF{4_P4Rt_1t_i5_a9d0f313}
picoCTF{4_P4Rt_1t_i5_1f03d3a9}
picoCTF{4_P4Rt_1t_i5_9a013f3d}
picoCTF{4_P4Rt_1t_i5_f33d091a}
picoCTF{4_P4Rt_1t_i5_1d9fa303}
picoCTF{4_P4Rt_1t_i5_a3f9103d}
picoCTF{4_P4Rt_1t_i5_f19a03d3}
picoCTF{4_P4Rt_1t_i5_93fda130}
picoCTF{4_P4Rt_1t_i5_30df3a91}
picoCTF{4_P4Rt_1t_i5_09ad13f3}
picoCTF{4_P4Rt_1t_i5_a0913df3}
MESSAGE=vmware: picoCTF{4_P4Rt_1t_i5_913d03af} hypervisor : 66000000 Hz
picoCTF{4_P4Rt_1t_i5_f19d3a03}STAMP=294323
picoCTF{4_P4Rt_1t_i5_f3019a3d}
picoCTF{4_P4Rt_1t_i5_309dfa13}
picoCTF{4_P4Rt_1t_i5_0a193f3d}
picoCTF{4_P4Rt_1t_i5_f9033d1a}
_SOURCE_MONOTONIC_TIMESTAMP=3024picoCTF{4_P4Rt_1t_i5_f3013da9}
picoCTF{4_P4Rt_1t_i5_33f0da91}
picoCTF{4_P4Rt_1t_i5_a1f033d9}e
picoCTF{4_P4Rt_1t_i5_f3d0139a}
picoCTF{4_P4Rt_1t_i5_af91303d}
picoCTF{4_P4Rt_1t_i5_af9d0133}
picoCTF{4_P4Rt_1t_i5_f9331ad0}
picoCTF{4_P4Rt_1t_i5_39fa01d3}
picoCTF{4_P4Rt_1t_i5_a1df3903}
picoCTF{4_P4Rt_1t_i5_1daf9033}
picoCTF{4_P4Rt_1t_i5_931afd03}
picoCTF{4_P4Rt_1t_i5_0d93a13f}
picoCTF{4_P4Rt_1t_i5_903a13fd}
picoCTF{4_P4Rt_1t_i5_ad1933f0}
picoCTF{4_P4Rt_1t_i5_90d31a3f}
picoCTF{4_P4Rt_1t_i5_39afd013}
picoCTF{4_P4Rt_1t_i5_1fa09d33}
picoCTF{4_P4Rt_1t_i5_01d93f3a}
picoCTF{4_P4Rt_1t_i5_f30a193d}
picoCTF{4_P4Rt_1t_i5_39afd301}
picoCTF{4_P4Rt_1t_i5_9fda3103}
picoCTF{4_P4Rt_1t_i5_af13d930}
picoCTF{4_P4Rt_1t_i5_9130fa3d}
picoCTF{4_P4Rt_1t_i5_d10f933a}
picoCTF{4_P4Rt_1t_i5_df03931a}
picoCTF{4_P4Rt_1t_i5_301d3fa9}
picoCTF{4_P4Rt_1t_i5_d033fa91}
picoCTF{4_P4Rt_1t_i5_0af31d39}
picoCTF{4_P4Rt_1t_i5_af3093d1}
picoCTF{4_P4Rt_1t_i5_0d913af3}
picoCTF{4_P4Rt_1t_i5_01a3d93f}
picoCTF{4_P4Rt_1t_i5_a3d3901f}
picoCTF{4_P4Rt_1t_i5_d03f391a}
picoCTF{4_P4Rt_1t_i5_f3d9013a}
picoCTF{4_P4Rt_1t_i5_3f1a0d93}
picoCTF{4_P4Rt_1t_i5_3d0913fa}
picoCTF{4_P4Rt_1t_i5_01933adf}
picoCTF{4_P4Rt_1t_i5_109da3f3}
picoCTF{4_P4Rt_1t_i5_f093d13a}
picoCTF{4_P4Rt_1t_i5_a0f1393d}
picoCTF{4_P4Rt_1t_i5_df0139a3}
picoCTF{4_P4Rt_1t_i5_03fa913d}
picoCTF{4_P4Rt_1t_i5_13f90ad3}
picoCTF{4_P4Rt_1t_i5_d39f1a03}
picoCTF{4_P4Rt_1t_i5_303d9fa1}
picoCTF{4_P4Rt_1t_i5_393d10af}
picoCTF{4_P4Rt_1t_i5_01d3f9a3}
picoCTF{4_P4Rt_1t_i5_d093a31f}
picoCTF{4_P4Rt_1t_i5_fa330d19}
picoCTF{4_P4Rt_1t_i5_df13309a}
picoCTF{4_P4Rt_1t_i5_3031a9df}
picoCTF{4_P4Rt_1t_i5_df19a330}
picoCTF{4_P4Rt_1t_i5_01df3a93}
picoCTF{4_P4Rt_1t_i5_13afd390}
picoCTF{4_P4Rt_1t_i5_3fda3910}
picoCTF{4_P4Rt_1t_i5_af93d310}
picoCTF{4_P4Rt_1t_i5_03319adf}
picoCTF{4_P4Rt_1t_i5_339a01df}
picoCTF{4_P4Rt_1t_i5_3ad9f301}
picoCTF{4_P4Rt_1t_i5_f31a903d}
picoCTF{4_P4Rt_1t_i5_d930f31a}
picoCTF{4_P4Rt_1t_i5_93daf130}
picoCTF{4_P4Rt_1t_i5_9a30f13d}
```

to solve this we have to find each partition begins and end:
```
ousen@0u5en $ fdisk -l disko-2.dd 
Disk disko-2.dd: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8ef8eaee

Device      Boot Start    End Sectors Size Id Type
disko-2.dd1       2048  53247   51200  25M 83 Linux
disko-2.dd2      53248 118783   65536  32M  b W95 FAT32
```

now we know the start sector and size we can extract it using dd;
```
ousen@0u5en $ dd if=disko-2.dd of=partition1.dd bs=512 skip=2048 count=51200
51200+0 records in
51200+0 records out
26214400 bytes (26 MB, 25 MiB) copied, 0.3203 s, 81.8 MB/s
```

we can now grep the flag from extracted sector:
```
ousen@0u5en $ strings partition1.dd | grep picoCTF
picoCTF{4_P4Rt_1t_i5_90a3f3d1}
```
