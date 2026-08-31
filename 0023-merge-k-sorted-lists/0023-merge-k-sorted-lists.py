import heapq

class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(0)
        tail = dummy

        heap = []

        # Put first node of every list into heap
        for i in range(len(lists)):

            if lists[i] is not None:

                heapq.heappush(
                    heap,
                    (lists[i].val, i, lists[i])
                )

        # Merge all lists
        while heap:

            # Get smallest node
            value, i, node = heapq.heappop(heap)

            # Attach node to result
            tail.next = node
            tail = tail.next

            # Add next node from same list
            if node.next is not None:

                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next