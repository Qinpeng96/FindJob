import SelfList
print('this is a test of SelfList')
head = SelfList.createList()
SelfList.printListInfo(head)
SelfList.addNode(head,1)
SelfList.addNode(head,2)
SelfList.addNode(head,3)
SelfList.printListInfo(head)
print(SelfList.getNthElement(head,2))
print(SelfList.getListLength(head))
print(SelfList.isEmpty(head))
SelfList.printListInfo(head)
SelfList.addNthNode(head,5,2)
SelfList.printListInfo(head)
SelfList.removeNthNode(head,3)
SelfList.printListInfo(head)
SelfList.addNthNode(head,5,5)
SelfList.printListInfo(head)
head = SelfList.removeNthNode(head,1)
SelfList.printListInfo(head)
head = SelfList.addNthNode(head,7,1)
SelfList.printListInfo(head)
SelfList.removeNode(head)
SelfList.printListInfo(head)