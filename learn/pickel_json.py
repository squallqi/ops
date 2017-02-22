'''import pickle
q = ['qiweiwei','Qzai','squallqi']
print pickle.dumps(q)
dump = pickle.dumps(q)
print dump
print type(dump)
load = pickle.loads(dump)
print load
print type(load)
pickle.dump(q,open('/tmp/1.pk','w'))
loadfile = pickle.load(open('/tmp/1.pk','r'))
print loadfile'''
import json
q = {'wife':'qiweiwei', 'son':'Qzai'}
print json.dumps(q)


