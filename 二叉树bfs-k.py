def BinTree_BFS_K(root,k):
    if root is None:
        return []
    ret=[]
    queue=[root]
    count=0
    while queue and count<k:
        new_queue=[]
        for node in queue:
            ret.append(node.val)
            if node.left is not None:
                new_queue.append(node.left)
            if node.right is not None:
                new_queue.append(node.right)
        count+=1
        queue=new_queue
    return ret
        
         
    