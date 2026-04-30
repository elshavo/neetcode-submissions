class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = '' #crear string vacio
        for caracter in s: #recorrer caracter en string
            if caracter.isalnum(): #isalnum es si es caracter a-zaz o un 09
                newstring += caracter.lower() #los hace minuscula
        return newstring == newstring[::-1] #compara normal contra reversa y devuelve true si si
        
        