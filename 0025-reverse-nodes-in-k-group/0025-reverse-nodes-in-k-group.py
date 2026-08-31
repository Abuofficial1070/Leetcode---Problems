class Solution:
    def reverseKGroup(self, head, k):

        temp = head

        for i in range(k):
            if temp is None:
                return head
            temp = temp.next

        prev = None
        curr = head

        for i in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        head.next = self.reverseKGroup(curr, k)

        return prev