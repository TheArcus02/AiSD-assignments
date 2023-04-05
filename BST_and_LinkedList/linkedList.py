
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_sorted(self, node: Node):
        if self.head is None:
            self.head = node
            return

        if node.data < self.head.data:
            self.add_first(node)
            return

        for current_node in self:
            if current_node.next is None:
                current_node.next = node
                return

            if current_node.next.data > node.data:
                node.next = current_node.next
                current_node.next = node
                return

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def delete_list(self):
        current = self.head
        while current:
            temp = current.next
            del current.data
            current = temp

    def find_element(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.head

        for node in self:
            if node.data == target_node_data:
                return node

        raise Exception("Node with data '%s' not found" % target_node_data)
