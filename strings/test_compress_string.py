#-*- coding:utf-8 -*-

from compress_string import CompressString
from nose.tools import assert_equal



class TestCompress(object):

    def test_compresss(self, func):
        assert_equal(func(""), "")
        assert_equal(func(None), None)
        assert_equal(func("AABBCC"), "AABBCC")
        assert_equal(func("AAABCCDDDDE"), "A3BC2D4E")
        assert_equal(func("BAAACCDDDD"), "BA3C2D4")
        print "Success: test compress."


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compresss(compress_string.compress)


if __name__ == "__main__":
    main()