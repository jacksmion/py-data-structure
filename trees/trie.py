# -*- coding:utf-8 -*-
import sys
import cStringIO

class TrieNode(object):
    __slots__ = ["pass_count", "end_count", "childs", "isEnd", "value"]
    def __init__(self):
        self.pass_count = 0
        self.end_count = 0
        self.childs = {}
        self.value = ""
        self.isEnd = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, c):
        if c < 58:
            return c - 48
        elif c < 91:
            return c - 65 + 11
        else:
            return c - 97 + 26 + 11

    def insert(self, word):
        cur_node = self.root
        for w in word:
            i = self.get_index(ord(w))
            node = cur_node.childs.get(i)
            if not node:
                node = TrieNode()
                cur_node.childs[i] = node
                node.value = w
                node.pass_count = 1
            else:
                node = cur_node.childs[i]
                node.pass_count += 1
            cur_node = node
        cur_node.isEnd = True
        cur_node.end_count += 1
        return True

    def remove(self, word):
        pass

    def preorder(self, root, prefix):
        result = {}
        def imp(root, prefix):
            if root.isEnd:
                result[prefix] = root.end_count

            for _, n in root.childs.items():
                if n:
                    tmp_str = prefix + n.value
                    imp(n, tmp_str)
        imp(root, prefix)
        return result

    def word_is_exist(self, word):
        cur_node = self.root
        for w in word:
            i = self.get_index(ord(w))
            node = cur_node.childs.get(i)
            if not node:
                return False
        return cur_node.isEnd

    def count_word(self, word):
        cur_node = self.root
        for w in word:
            i = self.get_index(ord(w))
            node = cur_node.childs.get(i)
            if not node:
                return 0
            else:
                cur_node = cur_node.childs[i]
        return cur_node.end_count

    def count_prefix(self, word):
        cur_node = self.root
        for w in word:
            i = self.get_index(ord(w))
            node = cur_node.childs.get(i)
            if not node:
                return 0
            else:
                cur_node = cur_node.childs[i]
        return cur_node.pass_count

    def get_all_word_by_prefix(self, word):
        cur_node = self.root
        for w in word:
            i = self.get_index(ord(w))
            node = cur_node.childs.get(i)
            if not node:
                return None
            cur_node = cur_node.childs[i]
        return self.preorder(cur_node, word)

def read_data(file_name, line_num):
    count = 0
    with open(file_name, "r+") as fp:
        for w in fp:
            yield w
            if count >line_num:
                break
            count += 1

def main():
    trie = Trie()
    # datas = read_data(r"F:\jacksmion\python-code-lib\data-structure\user.txt", 100000)
    datas = read_data(r"phone.txt", 1000)
    text_buf = cStringIO.StringIO()
    for d in datas:
        trie.insert(d)

    while True:
        text = raw_input(">")
        if text == "":
            break
        result = trie.get_all_word_by_prefix(text)
        if result:
            for w, _ in result.items():
                text_buf.write(w)
            print text_buf.getvalue()
            text_buf.truncate(0)
            print u"本次一共查询到%s个单词." % len(result.keys())
        else:
            print u"未查询到."
    text_buf.close()



main()
