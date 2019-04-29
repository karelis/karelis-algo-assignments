from collections import deque

class BKTree:
    def __init__(self, distfn, words):
        """
        Create a new BK-tree from the given distance function and
        words.
        
        Arguments:
        distfn: a binary function that returns the distance between
        two words.  Return value is a non-negative integer.  the
        distance function must be a metric space.
        
        words: an iterable.  produces values that can be passed to
        distfn
        
        """
        self.distfn = distfn

        it = iter(words)
        root = it.next()
        self.tree = (root, {})

        for i in it:
            self._add_word(self.tree, i)

    def BKTreeInsert(self, parent, word):
        pword, children = parent
        d = self.distfn(word, pword)
        if d in children:
            self._add_word(children[d], word)
        else:
            children[d] = (word, {})

    def query(self, word, n):
        """
        Return all words in the tree that are within a distance of `n'
        from `word`.  
        Arguments:
        
        word: a word to query on
        n: a non-negative integer that specifies the allowed distance
        from the query word.  
        
        Return value is a list of tuples (distance, word), sorted in
        ascending order of distance.
        
        """
    def rec(parent):
        pword, children = parent
        d = self.distfn(word, pword)
        results = []
        if d <= n:
            results.append( (d, pword) )
            
        for i in range(d-n, d+n+1):
            child = children.get(i)
            if child is not None:
                results.extend(rec(child))
        return results
        # sort by distance
        return sorted(rec(self.tree))

    



