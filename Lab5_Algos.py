class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    
    return root


def search(root, target):
    if root is None:
        return False
    
    if target == root.value:
        return True
    elif target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)


def inorder(root, result=None):
    if result is None:
        result = []
    
    if root is not None:
        inorder(root.left, result)
        print(root.value, end=" ")
        result.append(root.value)
        inorder(root.right, result)
    
    return result


def get_sorted_list(root):

    result = []
    inorder(root, result)
    return result


if __name__ == "__main__":
    root = None
    
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print("Вставляем значения:", values)
    
    for val in values:
        root = insert(root, val)
        
    print("\nПоиск значений:")
    test_values = [40, 90, 25, 100]
    for val in test_values:
        found = search(root, val)
        print(f"  Значение {val}: {'найдено' if found else 'не найдено'}")
    
    
    print("\nСимметричный обход (возрастающий порядок):")
    sorted_list = inorder(root)
    
    
    print("\nОтсортированный список всех элементов:")
    sorted_list = get_sorted_list(root)
    print(sorted_list)
    
    
    print("\nПроверка вставки дубликата (60):")
    root = insert(root, 60) 
    sorted_list = get_sorted_list(root)
    print("Список после вставки дубликата:", sorted_list)
    print("Размер списка остался прежним - дубликаты не добавляются")
    
    
    print("\nДругой пример: дерево из значений [5, 3, 7, 1, 4, 6, 8]")
    root2 = None
    for val in [5, 3, 7, 1, 4, 6, 8]:
        root2 = insert(root2, val)
    
    print("Значения в порядке возрастания:")
    inorder(root2)
    print("\nОтсортированный список:", get_sorted_list(root2))
