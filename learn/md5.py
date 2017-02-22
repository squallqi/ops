import hashlib
a = raw_input('please tell me your passwd: ')
hash = hashlib.md5()
hash.update(a)
#hash.update('admin')
print hash.hexdigest()