def inorderTraversal(root):
    res = []

    def inorder(root):
        if root:
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

    inorder(root)
    return res


if __name__ == '__main__':
    root = [1, null, 2, 3]

    print(inorderTraversal(root))
    # [1,3,2]
