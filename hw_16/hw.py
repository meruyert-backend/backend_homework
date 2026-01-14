class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [0] * capacity

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def get(self, index: int) -> int:
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds")
        return self.data[index]



class DynamicArray:
    def __init__(self):
        self.data = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, value)

    def delete(self, index: int) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        self.data.pop(index)

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]



class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current = self.head
        index = 0

        while current is not None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Index out of bounds")

        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def delete(self, value: int) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

    def find(self, value: int) -> Node:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def reverse(self) -> None:
        prev = None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def insert(self, position: int, value: int) -> None:
        new_node = DoubleNode(value)

        if position <= 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self._size += 1
            return

        if position >= self._size:
            self.append(value)
            return

        current = self.head
        index = 0
        while index < position:
            current = current.next
            index += 1

        prev_node = current.prev
        new_node.prev = prev_node
        new_node.next = current
        prev_node.next = new_node
        current.prev = new_node

        self._size += 1

    def delete(self, value: int) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self._size -= 1
            return

        current = self.head.next
        while current is not None:
            if current.value == value:
                if current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self._size -= 1
                return
            current = current.next

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def reverse(self) -> None:
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        return self.tail




class Queue:
    def __init__(self):
        self.data = [] # Мы создаём пустой список,в котором будет храниться очередь.

    def enqueue(self, value: int) -> None:
        self.data.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            return None
        return self.data.pop(0) #удаляет элемент по индексу & возвращает этот элемент

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0



class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ---------- INSERT ----------
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right
            else:
                return  # duplicate values not inserted

    # ---------- SEARCH ----------
    def search(self, value: int) -> TreeNode:
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None


    def delete(self, value: int) -> None:
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: TreeNode, value: int) -> TreeNode:
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # case 1 & 2: zero or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # case 3: two children
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node


    def minimum(self) -> TreeNode:
        if self.root is None:
            return None
        return self._min_node(self.root)

    def _min_node(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def maximum(self) -> TreeNode:
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current


    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)

    def level_order_traversal(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


    def size(self) -> int:
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def height(self) -> int:
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(
            self._height_recursive(node.left),
            self._height_recursive(node.right)
        )


    def is_valid_bst(self) -> bool:
        return self._is_valid(self.root, float("-inf"), float("inf"))

    def _is_valid(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (
            self._is_valid(node.left, min_val, node.value) and
            self._is_valid(node.right, node.value, max_val)
        )


    def is_empty(self) -> bool:
        return self.root is None





from typing import List


def insertion_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def selection_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def shell_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()

    pivot = lst[len(lst) // 2]
    less = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
