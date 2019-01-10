#-*- coding:utf-8 -*-

from __future__ import division

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        cur = self.head
        counter = 0
        while cur is not None:
            counter += 1
            cur = cur.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return None
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node
        return node

    def find(self, data):
        if data is None:
            return None
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        return None

    def delete(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        cur_node = self.head.next
        while cur_node is not None:
            if cur_node.data == data:
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print cur_node.data
            cur_node = cur_node.next

    def get_all_data(self):
        data = []
        cur_node = self.head
        while cur_node is not None:
            data.append(cur_node.data)
            cur_node = cur_node.next
        return data


class MyLinkedList(LinkedList):
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        cur_node = self.head
        reversed_list = LinkedList()
        length = 0
        while cur_node is not None:
            reversed_list.insert_to_front(cur_node.data)
            length += 1
            cur_node = cur_node.next

        iterations = length // 2
        cur_node = self.head
        cur_reversed_node = reversed_list.head
        for _ in range(iterations):
            if cur_node.data != cur_reversed_node.data:
                return False
            cur_node = cur_node.next
            cur_reversed_node = cur_reversed_node.next
        return True
