## UPDATE
* being re-written in c++ too big and compicated for my python skills :)

## Table of contents
* [General info](#general-info)
* [Hints](#hints)
* [Future](#future)
* [Issues](#issues)
* [Packages](#packages)
* [Setup](#setup)
* [help-me](#help-me)

## General info
- An LP brute-forcing tool for decrypting cipher-text with user defined keys and functions 
of two runes:   
`Function(plaintext_rune,key_rune) = cipher_rune`     
including automated Gematria rotations, interrupters, key-dragging and plaintext ranking.    
- Very much in early access.
- Much more information, benchmarking, features and manual to follow.   
- Good Luck    

## Hints
- In principle, **anything this app can encrypt it should be able to decrypt** 
(with the right settings and bugfixes).   
- Try setting up test decryptions using your own encryption functions, plaintext, key and encoding and see if they are 
successfully decrypted. 
- If test decryption fails, perhaps settings in the "options" tab are wrong?   
- The app can be used for LP decrypting as is, however, it is still under development.  


## Future
Planned features not yet implemented:
* Load save general set-up 
* Batch-mode support for use without GUI. Once the app is well benchmarked by the community long scans with large key 
lists (etc.) would probably be better run without the gui. This can be accomplished now, but there are no examples and
the expectation is that data-structures etc. will change during this initial-release phase.   
* Moar encryption methods. Hopefully, this will provide a framework in which a wider variety of encryption methods can be
implemented and shared between solvers. 



## Issues
- Be aware: i'm an entirely self-taught coder, this is done out of love not competence :)
- There are bugs, errors and hopefully suggestions. Please share them through the github issues, and irc / discord.  
- Particularly welcome are bugs, code improvements, speed-up suggestions and expanding (or re-writing) the mutl-theading framework 


## packages
1. created with:  
[Python 3.6](https://www.python.org)    
[tabulate](https://pypi.org/project/tabulate/)     
[pyqt5](https://pypi.org/project/PyQt5/)     


	
## setup
1. install python3     
2. you may need to install  
`pip3 install pyqt5`  
`pip3 install tabulate`  
2. To run:  
`python3 main.py  `    
run the text decryption with defaults on start-up 
`python3 main.py -test  `    


## help-me
cicadsolvers irc / discord 