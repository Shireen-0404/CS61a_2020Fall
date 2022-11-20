def height(t):
    if is_leaf(t):
        return 0
    return 1+max([height(b) for b in branches(t)])
    
def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    else:
        return label(t)+max([max_path_sum(b) for b in branches(t)])

def square_tree(t):
    return tree(label(t)**2,[square_tree(b) for b in branches(t)])

def find_path(tree,x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b,x)
        if path:
            return [label(tree)] + path

def prune_binary(t,nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [i[1:] for i in nums if i[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b,next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t),new_branches)


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):#if the tree has no branch, the for loop won't execute
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False

