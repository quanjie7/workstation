from __future__ import print_function,division
import numpy as np
import tensorflow as tf

#create a Variable
w = tf.Variable(initial_value=[[0,0],[3,4]],dtype=tf.float32)
x = tf.Variable(initial_value=[[1,1],[1,1]],dtype=tf.float32)
y = tf.matmul(w,x)
z = tf.sigmoid(y)
print(z)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    print(session.run(y))
    z = session.run(z)
    print(z)
    print(x.read_value())


print("----------------------------------------------------------------------------------------")
print("#fetch example")
a = tf.constant([1,2,3.0],name="a")
b = tf.constant([4.,5.,6.],name = "b")
c = tf.constant([1.,4.,2.],name = "c")

add = a+b
mul = add*c

with tf.Session() as session :
    result = session.run([a,b,c,add,mul])
    print("after run:\n",result)

print("\n\n")

#feed example

print("feed example")
input1 = tf.placeholder(tf.float16)