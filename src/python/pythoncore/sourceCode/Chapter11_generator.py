# coding:utf-8

def simpleGen():
    yield  1
    yield '2-->punch'

myG = simpleGen()
print myG.next()
print myG.next()

for eachItem in simpleGen():
    print eachItem

def counter(start_at=0):
    count = start_at

    while True:
        val = (yield  count)

        if val is not None:
            count = val

        else:
            count += 1

count = counter(5)
print count.next(), count.next()

count.send(9)

print count.next()
count.close()


