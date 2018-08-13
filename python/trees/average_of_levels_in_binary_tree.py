# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        '''
        need to record extra values
        solve this with traversal => could use dfs or bfs
        when doing traversal => use global lists to store results
        '''
        # global lists
        sumList = list()
        cntList = list()
        def dfs(root, levelNum):
            # root
            if root is not None:
                # new level
                # ! could remove all (0,0) in final zip to solve this
                if len(sumList) <= levelNum:
                    sumList.append(0)
                    cntList.append(0)

                sumList[levelNum] += root.val
                cntList[levelNum] += 1
                dfs(root.left, levelNum+1)
                dfs(root.right, levelNum+1)
        dfs(root, 0)
        # if use [[sum,cnt],[sum,cnt]], easy to compute the final results
        return [float(s)/n for s,n in zip(sumList,cntList)]

