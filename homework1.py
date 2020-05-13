import string

def process_file(filename):
  hist=dict()
  fp=open(filename)
  for line in fp:
    process_line(line,hist)
  return hist

def process_line(line,hist):
  line=line.replace('-','')
  for word in line.split():
    word=word.strip(string.punctuation+string.whitespace)
    word=word.lower()
    hist[word]=hist.get(word,0)+1

process_file('62086-0.txt')

def zhaolin(d1,d2):
  apple=dict()
  for t in d1:
    if t not in d2:
      apple[t]=None
    return t
  print(apple)

banana=process_file('62086-0.txt')
peach=process_file('words.txt')
zhaolin(banana,peach)
   
