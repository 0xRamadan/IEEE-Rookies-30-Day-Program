# IEEE_Rookies_task_30
# name: Mahmoud_Ramadan
# task: Binary Search Tree
# link: https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/submissions/

'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        print('YES')

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)'''


if __name__ == '__main__':

    t = int(input())
    result = []
    for i in range(t):
        n, m = list(map(int, input().split()))
        all_students = [int(x) for x in input().split()]
        currently_students = set(all_students[:n])

        for i in all_students[n:]:
            if i in currently_students:
                result.append("YES")
            else:
                result.append("NO")
                currently_students.add(i)

    print("\n".join(result))


'''
    # solution using binary search tree, not complete
    l = [int(x) for x in input('enter l: ').split()]
    r = Node(0)
    for i in range(t):
        for i in range(n):
            r = insert(r, l[i])
            inorder(r)
        for j in range(m):
            r = insert(r, l[n+j])
            s = search(r, l[n+j])
            if s:
                print("YES")
            else:
                print('NO')
    inorder(r)
    '''

