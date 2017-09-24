text = u"我今天很快乐。我今天很愤怒。"
from snownlp import SnowNLP
s = SnowNLP(text)
print(s.words)
for sentence in s.sentences:
    print(sentence)
    print(SnowNLP(sentence).sentiments)
    print(SnowNLP("我今天很快乐。我今天很愤怒").sentiments)