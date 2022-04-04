class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	prevNode, currentNode=None, head
	
	while currentNode != None:
		nextNode=currentNode.next
		currentNode.next=prevNode
		prevNode=currentNode
		currentNode=nextNode
	return prevNode
