class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Inicializar dos punteros
        left = 0
        right = len(numbers) -1

        # Usar un bucle while para mover los punteros hasta que se encuentren
        while left < right:
            current_sum = numbers[left] + numbers[right]

            # Comprobar si la suma actual es igual al objetivo
            if current_sum == target:
                return [left + 1, right + 1]

            # Si la suma actual es mayor que el objetivo, mover el puntero derecho hacia la izquierda
            elif current_sum > target:
                right -= 1

            # Si la suma actual es menor que el objetivo, mover el puntero izquierdo hacia la derecha
            elif current_sum < target:
                left += 1
                