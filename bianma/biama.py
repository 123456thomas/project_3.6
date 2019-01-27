"""编码问题
"""
__author__ = 'Manstein'

from urllib import request

target_url ="http://www.sina.com.cn"

response = request.urlopen(target_url)

print(dir(response))
print(response.read())

"""['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
"""