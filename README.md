### What is a Vigenere Cipher?

Originally created by Giovan Battista Bellasto in 1553, the vigenere cipher was
created in order to paliate to the weakness of earlier encryption methods. 
The most popular one, the Ceasar Cipher,  was easily decryptable even without 
the key because one could perform a frequency analysis. By counting the
frequency of each letter, one could guess the real character of each letter
based on the actual letter frequency in the english language.

Bellasto developped a rotating cipher in which not all encrypted letter is
transcribed with the same homologue letter. Instead of only adding an arbitrary
number during the transcription, vigenere cipher uses a key to which add to the
letter, ensuring that the same letter won't be encoded similarly twice.

```
WORD: banana
KEY: key

B: B + K =  2 + 11 = 13 = M
A: A + E =  1 +  5 =  6 = F
N: N + Y = 14 + 25 = 39 = M (39-26) 
A: A + K =  1 + 11 = 12 = L
N: N + E = 14 +  5 = 19 = S
A: A + Y =  1 + 25 = 26 = Z

ENCRYPTED: mslsz
```


