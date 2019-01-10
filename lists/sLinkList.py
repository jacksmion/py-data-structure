# coding:utf-8
# 单链表



class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SLinkList(object):
    """
        单链表方法:
            反转
            添加
            删除
            插入
            查找
            输出
    """
    def __init__(self, head=None):
        self.head = head

    def insert_to_front(self, data):
        """
            从链表头插入数据
        """
        if data is None:
            return None
        node = ListNode(data, self.head)
        self.head = node
        return node

    def append(self, data):
        """
            追加数据
        """
        if data is None:
            return None
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return None
        cur_node = self.head
        # 获取最后一个节点
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
            return True
        prev_node = self.head
        cur_node = self.head.next
        while cur_node is not None:
            if cur_node.data == data:
                prev_node.next = cur_node.next
                return cur_node
            prev_node = cur_node
            cur_node = cur_node.next

    def delete_tail(self):
        """
            删除最后一个节点
        """
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        cur_node = self.head
        next_node = cur_node.next
        while next_node.next is not None:
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = None

    def print_all_data(self):
        cur_node = self.head
        while cur_node is not None:
            print cur_node.data,
            cur_node = cur_node.next

    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node is not None:
            tmp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = tmp
        self.head = prev


class LruManage(object):
    def __init__(self, max_size=10):
        self._data_list = SLinkList()
        self.capacity = max_size
        self.count = 0

    def put(self, data):
        if self.count < self.capacity:
            self.count += 1
            self._data_list.insert_to_front(data)
        else:
            self._data_list.delete_tail()
            self._data_list.insert_to_front(data)

    def get(self, data):
        result = self._data_list.find(data)
        if result:
            self._data_list.delete(result.data)
            self._data_list.insert_to_front(result.data)
            return result
        return -1

    def get_cache_data(self):
        self._data_list.print_all_data()


if __name__ == "__main__":
    lru = LruManage()
    lru.put('xomas')
    lru.put('jacksmion')
    lru.put('qq')
    lru.get_cache_data()
    lru.get('jacksmion')
    print ""
    lru.get_cache_data()
    # link_list = SLinkList()
    # link_list.append(2)
    # link_list.append(3)
    # link_list.append(4)
    # link_list.append(5)
    # link_list.delete_tail()
    # link_list.print_all_data()
    # link_list.delete(2)
    # link_list.print_all_data()
    # link_list.append(1)
    # link_list.append(2)
    # link_list.append(3)
    # link_list.insert_to_front(4)
    # link_list.print_all_data()
    # print ""
    # link_list.reverse()
    # link_list.print_all_data()
    # print ""
