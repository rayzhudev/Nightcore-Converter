# Nightcore Converter
Nightcore converter is a python script used to convert mp3 files to nightcore.

### Usage
1. Locate the directory containing the songs you wish to convert. e.g. `music/`
2. Create a folder named `nightcored songs/`. This is where the converted songs will go. 
3. Run the command `python3 nightcoreconverter.py music/`. This will convert every mp3 file in this folder to nightcore and then proceed to delete the original mp3 after doing so. If you wish to keep the mp3 file, comment out the line of code indicated in nightcoreconverter.py. 
4. Enjoy!

### Notes
- This script turns songs into nightcore by speeding them up by √2 times (~1.4). You can try other values depending on your preference but I have found that √2 works the best.
- If you choose not to delete the songs, you may leave them in the folder because the script ignores files that have already been converted.
