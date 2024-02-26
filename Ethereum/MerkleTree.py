from typing import List
import hashlib

class Node:
    def __init__(self, left, right, value: str, content) -> None:
        self.left = left
        self.right = right
        self.value = value
        self.content = content

    @staticmethod
    def hash(val: str) -> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def __str__(self):
        return str(self.value)

class MerkleTree:
    def __init__(self, values: List[str]) -> None:
        self.__buildTree(values)

    def __buildTree(self, values: List[str]) -> None:
        leaves = [Node(None, None, Node.hash(e), e) for e in values]
        while len(leaves) % 2 == 1:
            leaves.append(leaves[-1])  # Duplicate last element if odd number of elements
        self.root = self.__buildTreeRec(leaves)

    def __buildTreeRec(self, nodes: List[Node]) -> Node:
        if len(nodes) == 1:
            return nodes[0]
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1]
            value = Node.hash(left.value + right.value)
            content = left.content + "+" + right.content
            new_level.append(Node(left, right, value, content))
        return self.__buildTreeRec(new_level)

    def printTree(self) -> None:
        self.__printTreeRec(self.root)

    def __printTreeRec(self, node) -> None:
        if node is not None:
            if node.left is not None:
                print("Left: " + str(node.left))
                print("Right: " + str(node.right))
            else:
                print("Input")
            print("Value: " + str(node.value))
            print("Content: " + str(node.content))
            print("")
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)

    def getRootHash(self) -> str:
        return self.root.value

def mixmerkletree() -> None:
    elems = ["x", "y", "z", "f", "s", "e", "r", "n"]
    print("Inputs: ")
    print(*elems, sep=" | ")
    print("")
    mtree = MerkleTree(elems)
    print("Root Hash: " + mtree.getRootHash() + "\n")
    mtree.printTree()

mixmerkletree()
