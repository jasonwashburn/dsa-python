from dsa.linked_list import LinkedList, Node


def test_node_builds() -> None:
    # Test that a Node can be instantiated
    node = Node(value=4)
    assert node.value == 4
    assert node.next is None


def test_linked_list_builds() -> None:
    # Test that a LinkedList can be instantiated
    victim = LinkedList(value=4)
    assert isinstance(victim.head, Node)
    assert isinstance(victim.tail, Node)
    assert victim.head is victim.tail
    assert victim.head.value == 4
    assert victim.tail.value == 4
