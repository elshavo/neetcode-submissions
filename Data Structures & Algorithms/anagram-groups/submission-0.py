class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grupos_anagramas = defaultdict(list) # Inicializamos un diccionario que crea una lista [] por defecto

        # El bucle FOR se ejecuta UNA SOLA VEZ
        for palabra_original in strs:
            # 1. Creamos la clave (las letras de la palabra ordenadas)
            #    Ej: "tops" -> ['p', 's', 't'] -> "post"
            clave_anagrama = "".join(sorted(palabra_original))
            
            # 2. Usamos la clave para encontrar la lista correspondiente en el diccionario
            #    y añadimos la palabra original a esa lista.
            grupos_anagramas[clave_anagrama].append(palabra_original)

        # Convertimos los valores del diccionario (las listas de anagramas) 
        # de nuevo a una lista de listas (listanueva)
        return list(grupos_anagramas.values())



