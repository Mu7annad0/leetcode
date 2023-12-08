def tree2str(root) -> str:
    res = []

    def preorder(root):

        if not root:
            return

        res.append("(")
        res.append(str(root.val))

        if not root.left and root.right:
            res.append("()")

        preorder(root.left)
        preorder(root.right)

        res.append(")")

    preorder(root)

    return "".join(res)[1:-1]


if __name__ == "__main__":
    root = [1, 2, 3, 4]
    print(tree2str(root))
    # "1(2(4))(3)"
