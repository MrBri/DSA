package main

import (
	"fmt"
	"strings"
)

type Color bool

const (
	red   Color = true
	black Color = false
)

type Node struct {
	value       int
	color       Color
	left, right *Node
}

type RBTree struct {
	root *Node
}

func NewRBTree() *RBTree {
	return &RBTree{}
}

func (t *RBTree) Insert(value int) {
	t.root = insert(t.root, value)
	t.root.color = black
}

func insert(root *Node, value int) *Node {
	if root == nil {
		return &Node{value: value, color: red}
	}

	if value < root.value {
		root.left = insert(root.left, value)
	} else {
		root.right = insert(root.right, value)
	}

	// Fix Red-Black tree properties
	if isRed(root.right) && !isRed(root.left) {
		root = rotateLeft(root)
	}
	if isRed(root.left) && isRed(root.left.left) {
		root = rotateRight(root)
	}
	if isRed(root.left) && isRed(root.right) {
		colorFlip(root)
	}

	return root
}

func isRed(node *Node) bool {
	if node == nil {
		return false
	}
	return node.color == red
}

func rotateLeft(node *Node) *Node {
	newNode := node.right
	node.right = newNode.left
	newNode.left = node
	newNode.color = node.color
	node.color = red
	return newNode
}

func rotateRight(node *Node) *Node {
	newNode := node.left
	node.left = newNode.right
	newNode.right = node
	newNode.color = node.color
	node.color = red
	return newNode
}

func colorFlip(node *Node) {
	node.color = !node.color
	node.left.color = !node.left.color
	node.right.color = !node.right.color
}

func (t *RBTree) InOrderTraversal() {
	inOrderTraversal(t.root)
}

func inOrderTraversal(root *Node) {
	if root != nil {
		inOrderTraversal(root.left)
		fmt.Println(root.value)
		inOrderTraversal(root.right)
	}
}

func (t *RBTree) Print() {
	printTree(t.root, 0)
}

func printTree(root *Node, depth int) {
	if root == nil {
		return
	}

	// Recursively print the right sub-tree
	printTree(root.right, depth+1)

	// Print the current node
	fmt.Printf("%s%s\n", strings.Repeat("  ", depth), nodeColorString(root.color, root.value))

	// Recursively print the left sub-tree
	printTree(root.left, depth+1)
}

func nodeColorString(color Color, value int) string {
	colorCode := "\033[0m"
	if color == red {
		colorCode = "\033[31m"
	}
	return fmt.Sprintf("%s%d%s", colorCode, value, "\033[0m")
}

func main() {
	tree := NewRBTree()
	tree.Insert(10)
	tree.Insert(20)
	tree.Insert(30)
	tree.Insert(15)
	tree.Insert(18)
	tree.Insert(5)

	fmt.Println("In-order traversal:")
	tree.InOrderTraversal()

	fmt.Println("\nTree visualization:")
	tree.Print()
}
