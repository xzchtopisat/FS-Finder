# FS-Finder
Basic python file system finder. Can be used to search file systems from EEPROM, Flash ICs.


Can find file systems such as:

EXT (superblock), UBI, CPIO (initramfs), ROMFS, CRAMFS, SquashFS.


Can find compressions such as:

gzip, lzma, xz, lzo



# How does it work?


1: Checks .bin file signatures


2: It returns signature search results


3: (Optional) You can try unpacking the file system using HxD, etc.



# How to start (Windows)


1: Open CMD (Win + R, type in: cmd) 


2: Type in CMD: cd (your disk)/(folder)/FS-Finder/ ; python fs_finder.py firmware.bin

OR
You can just double click the .py file


