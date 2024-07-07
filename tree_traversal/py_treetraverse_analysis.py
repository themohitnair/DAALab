import matplotlib.pyplot as plt
import time
import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root: Node, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    result = []
    if root:
        result = inorder(root.left)
        result.append(root.val)
        result += inorder(root.right)
    return result

def preorder(root):
    result = []
    if root:
        result.append(root.val)
        result += preorder(root.left)
        result += preorder(root.right)
    return result

def postorder(root):
    result = []
    if root:
        result = postorder(root.left)
        result += postorder(root.right)
        result.append(root.val)
    return result

def populate_bst(n: int):
    root = Node(random.randint(0,100))
    for _ in range(n):
        insert(root, random.randint(0,100))
    return root

def mean_time(traversal_function, iterations: int):
    total_time = 0.0
    for i in range(iterations):
        root = populate_bst(iterations)
        start_time = time.perf_counter()
        traversal_function(root)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time/iterations

def plot_comparison(x_axis: list, data_algo1: tuple[str, list], data_algo2: tuple[str, list], data_algo3: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12,8))

    ax.plot(x_axis, data_algo1[1], marker='o', color='red', label=data_algo1[0])

    ax.plot(x_axis, data_algo2[1], marker='o', color='blue', label=data_algo2[0])

    ax.plot(x_axis, data_algo3[1], marker='o', color='orange', label=data_algo3[0])

    ax.set_facecolor('lightgreen')
    ax.set_title(f'{data_algo1[0]} vs {data_algo2[0]} vs {data_algo3[0]}', fontsize=24)
    ax.set_xlabel('Input Size (n)', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)  
    ax.tick_params(axis='y', labelsize=12)

    ax.legend()
    plt.savefig(filename)

    plt.show()
    
def main():
    postorder_time = []
    inorder_time = []
    preorder_time = []
    
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        index = 100
        postorder_time.append(mean_time(postorder, index))
        preorder_time.append(mean_time(preorder, index))
        inorder_time.append(mean_time(inorder, index))

    plot_comparison(n_vals, ('Inorder', inorder_time), ('Preorder', preorder_time), ('Postorder', postorder_time), 'traversal_analysis.png')    


if __name__ == "__main__":
    main()