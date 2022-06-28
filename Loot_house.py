class CLL:
    def __init__(self,val):
        self.val = val
        self.next = head

    def insert_node(self,head,val):
        temp = CLL(val)
        t = head
        if t.next == None:
            t.next = temp
        else:
            while t.next != head:
                t = t.next
            t.next = temp

    def print_nodes(self,head):
        t = head
        while True:
            print(t.val, end=' ')
            t = t.next
            if t == head:
                break

    def find(self,head):
        house_with_max_mny, house_no, max_amt, money_looted = {}, 101, 0, 0
        t = head
        money_looted += t.val
        while t.next != head:
            if t.val > max_amt:
                house_with_max_mny.clear()
                max_amt = t.val
                house_with_max_mny[house_no] = max_amt
            t = t.next
            house_no += 1
        money_looted += t.val
        print('Total money looted',str(money_looted))
        print('House  with max money',str(house_with_max_mny))

L = [95000,142300,410000,34000,74000]
head = None
C = CLL(L[0])
head = C
for val in L[1:]:
    C.insert_node(head,val)
#C.print_nodes((head))
C.find(head)