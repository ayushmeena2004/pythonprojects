def m_gen():
    for i in range(5):
        yield i

gen=m_gen()
for k in gen:
    print(k)