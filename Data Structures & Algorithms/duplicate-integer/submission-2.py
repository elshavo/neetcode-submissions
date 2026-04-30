#Mario Alberto González Méndez
#A00832313
#Neetcode duplicate-integer

#Método Hash Map
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        
#Se crea un hashset que almacena los numeros con el primer for,
#luego va a hace la vuelta con el for, en la que empieza con el
#primer valor de la lista, si ese n esta en el hashset, es true 
#porque se repite, sino, lo añade al hashmap para que si encuentra
#uno similar, pues lo agarre y de false si hay un duplicado.


#Metodo Fuerza bruta
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True        
        return False
'''
'''
Primer for del i para despues comparar con la j
i comienza con el primer valor y j con uno despues, por eso tiene i + 1. 
tiene 2 el j porque el primer parametro es con el que empieza, y el otro 
es con el que termina, si nomas tiene un parametro, es con el que termina.

despues de tener el primer parametro en i y j checa si son iguales, si no, solo cambia la j.
entonces i con el siguiente j y siguiente, y siguiente. ya vio que no, entonces va a cambiar la i.
y la j es una mas de i. entonces hace lo mismo, si encuetra duplicado, regresa true y termina.
si no encuentra despues de todo, da false.
'''

#Método Sort
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
                if nums[i] == nums[i - 1]:
                    return True
        return False
'''
'''
El metodo sort funciona de la manera que basicamente ordenas la lista,
luego haces solo un for, con un espacio adelante para que no te excedas de la lista,
comparas con el anterior, y como está ordenado, debe de salir un repetido o si no hay.
'''



