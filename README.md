You could use it to find a certain peice of text in multiple or single pdf files. Incase there is more than one file then just put all of them in a folder and then enter the folder path in the folder_path variable. If there is text matching what you put in the input, then it will return the file name and the page on which it exists. 

If you want to find text in one file then just put the file path in the folder_path variable and you are good to go. If any matching text is found it will return the file name and the page number

Some notes:
1. You need to have the PyPDF package installed [installer guide](https://pypdf2.readthedocs.io/en/3.0.0/user/installation.html)
2. Type the exact folder path in the folder_path variable (Example: /user/name/desktop/folder)
3. Run the program, and then type the string you want to search. 


In my case i wanted to search for my specific certificate inside a folder that had 450+ other certificates, so I put in the folder address and then typed my name as the string and then it gave me the file name of my certificate, which then I "ctrl + f" and it saved me lots of time 
