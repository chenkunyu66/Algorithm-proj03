#project 03
#cse 331 
#chen,kunyu
#A54470631

class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        self.root = None
        # added stuff below

    def __len__(self):
        """
        tree nodes count
        """
        return self.mylen(self.root)


    def height(self):
        """
        height
        """

        return self.myheight(self.root)

    def insert(self, item):
        """
        insert tree
        """
        self.dup = 0

        self.root = self.myadd(self.root, item)
        if self.dup == 1:
            return False

        return True

    def remove(self, item):
        """
        remove node from tree, 3 scene
        """
        p = self.root
        f= None

        # locate position
        while p != None and self.comp(p.data, item) != 0:
            f = p
            if self.comp(p.data, item) > 0:
                p = p.left
            else:
                p = p.right

        if p == None: # no found of to remove node
            return False

        if p.left == None:
            if f == None:
                self.root = p.right # delete root node
            elif f.left == p:
                f.left = p.right
            else:
                f.right = p.right
        else:
            q = p
            s = p.left
            while s.right != None: # find next node
                q = s
                s = s.right

            if q == p:
                q.left = s.left
            else:
                q.right = s.left

            p.data = s.data

        return True

    def __contains__(self, item):
        """
        tree traverse compare
        """
        p = self.root
        while p != None:
            if self.comp(p.data, item) == 0: #if item equal data
                return True
            elif self.comp(p.data, item) > 0: #if data greater than item
                p = p.left
            else:
                p = p.right

        return False

    def first(self):
        """
        left-most node
        """
        if self.root == None:
            raise KeyError

        p = self.root
        while p.left != None:
            p = p.left

        return p.data

    def last(self):
        """
        right-most node
        """
        if self.root == None:
            raise KeyError

        p = self.root #p is the root
        while p.right != None: #while loop to right bottom
            p = p.right

        return p.data

    def clear(self):
        """
        clear root node
        """
        self.root = None #set tree to empty


    def __iter__(self):
        """
        in-order tree
        """
        return iter(self.myiter(self.root))

    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    # Helper functions
    # You can add additional functions here

    def mylen(self, tree):
        """
        left + right + 1
        """
        if tree == None:
            return 0
        return self.mylen(tree.left) + self.mylen(tree.right) + 1

    def myheight(self, tree):
        """
        left height or right height
        """
        if tree == None:
            return -1
        return max(self.myheight(tree.left), self.myheight(tree.right)) + 1

    def myadd(self, tree, item):
        """
        tree insert by recursion
        """
        if tree == None:
            return TreeNode(item)
        if self.comp(tree.data, item) == 0:
            self.dup = 1
        elif self.comp(tree.data, item) > 0:
            tree.left = self.myadd(tree.left, item)
        elif self.comp(tree.data, item) < 0:
            tree.right = self.myadd(tree.right, item)

        return tree

    def myiter(self, tree):
        """
        use stack to in-order traverse
        """
        tree_list = [] #left list 
        p = self.root

        ret_list = []#new list 

        while p != None or len(tree_list) > 0:
            if p != None:
                tree_list.append(p)
                p = p.left
            else:
                p = tree_list.pop()
                ret_list.append(p.data)# right + left 
                p = p.right
        
        return ret_list


class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)


