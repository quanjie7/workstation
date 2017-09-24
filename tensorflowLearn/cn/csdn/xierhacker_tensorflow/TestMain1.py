#encoding:utf-8
from __future__ import print_function,division

import tensorflow as tf

#build a graph

print("build a graph")
a = tf.constant([[1,2],[3,4]])
b = tf.constant([[1,1],[0,1]])

print("a:",a)
print("b:",b)
print("type of a:",type(a))

c = tf.matmul(a,b)
print("c:",c.consumers())

#construct a 'Session' to execute the graph
with tf.Session() as sess:
    #Execute the graph and store the value that 'c' represents in 'result'.
    print("excuted in Session")
    result_a = sess.run(a)
    result_a2 = a.eval(session=sess)
    print()
    print("type of result_a:",type(result_a))
    print("result_a:\n",result_a)
    print("result_a2:\n",result_a2)

    result_b = sess.run(b)
    print("result_b:\n",result_b)

    result_c = sess.run(c)
    print("result_c:\n",result_c)
    print("type of result_c:" ,type(result_c))


