#-*- coding:utf-8 -*-

from nose.tools import assert_equal
from linked_list import LinkedList, Node, MyLinkedList



class TestLinkedList(object):

    def test_insert_to_front(self):
        print "Test: insert_to_front on empty list"
        linked_list = LinkedList()
        linked_list.insert_to_front(10)
        assert_equal(linked_list.get_all_data(), [10])

        print "Test: insert_to_front on a None"
        linked_list.insert_to_front(None)
        assert_equal(linked_list.get_all_data(), [10])

        print 'Test: insert_to_front general case'
        linked_list.insert_to_front("a")
        linked_list.insert_to_front("bc")
        assert_equal(linked_list.get_all_data(), ["bc", "a", 10])
        print "Success: test_insert_to_front."

    def test_append(self):
        print "Test: append on an empty list"
        linked_list = LinkedList()
        linked_list.append(10)
        assert_equal(linked_list.get_all_data(), [10])

        print "Test: append a None"
        linked_list.append(None)
        assert_equal(linked_list.get_all_data(), [10])

        print "Test: append general case"
        linked_list.append("a")
        linked_list.append("bc")
        assert_equal(linked_list.get_all_data(), [10, 'a', 'bc'])
        print "Success: test_append"

    def test_find(self):
        print "Test: find on an empty list"
        linked_list = LinkedList()
        node = linked_list.find('a')
        assert_equal(node, None)

        print "Test: find a None"
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        assert_equal(node, None)

        print "Test: find general case with matches"
        linked_list.append('a')
        linked_list.append('bc')
        node = linked_list.find('a')
        assert_equal(str(node), 'a')

        print "Test: find general case with no matches"
        node = linked_list.find('aaa')
        assert_equal(node, None)
        print "Success: test_find"

    def test_delete(self):
        print "Test: delete on an empty list"
        linked_list = LinkedList()
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), [])

        print "Test: delete a None"
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        assert_equal(linked_list.get_all_data(), [10])

        print "Test: delete general case with matches"
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print "Test: delete general case with no matches"
        linked_list.delete('aa')
        assert_equal(linked_list.get_all_data(), ['bc', 10])
        print "Success: test_delete"

    def test_len(self):
        print "Test: len on an empty list"
        linked_list = LinkedList()
        assert_equal(len(linked_list), 0)

        print "Test: len general case"
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.append('a')
        linked_list.append('bc')
        assert_equal(len(linked_list), 3)
        print "Success: test_len"

    def test_palindrome(self):
        print "Test: Empty list"
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print "Test: Single element list"
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print "Test: Two element list, not a palindrome"
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print "Test: General case, not a palindrome"
        linked_list.append(3)
        assert_equal(linked_list.is_palindrome(), False)

        print "Test: General case: Palindrome with even length"
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print "Test: General case: Palindrome with odd length"
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)
        print "Success: test_palindrome"

def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()
    test.test_palindrome()

if __name__ == '__main__':
    main()