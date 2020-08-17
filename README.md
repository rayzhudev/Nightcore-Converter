# Nightcore Converter
Nightcore converter is a python script used to convert mp3 files to nightcore.

### Usage
1. Places your mp3 files in the `input/` folder.  
(Optional step but recommended) Rename each mp3 file such that the name follows the structure `{Artist} - {Song Title}.mp3`. e.g. `Linkin Park - Numb.mp3`. This is so that the mp3 metadata can be recorded so you can sort by artist name and title.  
2. Run the command `python3 nightcoreconverter.py input/` in your terminal. Or alternatively run the `nightcore.command` script<sup>1</sup> by double clicking it [FOR MAC USERS ONLY]. This will convert every mp3 file in the input folder to nightcore and then proceed to delete the original mp3 after doing so. If you wish to keep the mp3 file, comment out the line of code indicated in nightcoreconverter.py.  
1: If you are unable to run the `nightcore.command` script, try running the command `chmod u+x nightcore.command` to gain the sufficient permissions.  
3. Enjoy!

### Notes
- This script turns songs into nightcore by speeding them up by √2 times (~1.4). You can try other values depending on your preference but I have found that √2 works the best.
- If you choose not to delete the songs, you may leave them in the folder because the script ignores files that have already been converted.
