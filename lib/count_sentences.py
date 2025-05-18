#!/usr/bin/env python3

class MyString:
  def __init__(self,value=''):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string." )

  def is_sentence(self):
    has_fullstop = False
    sentence_container=[]
    for word in self.value.split(" "):
      sentence_container.append(word)
    if('.' in sentence_container[-1]):has_fullstop = True
    print(sentence_container, has_fullstop)
    return has_fullstop
  
  def is_question(self):
      has_question_mark = False
      sentence_container=[]
      for word in self.value.split(" "):
        sentence_container.append(word)
      if('?' in sentence_container[-1]):has_question_mark = True
      print(sentence_container, has_question_mark)
      return has_question_mark

  def is_exclamation(self):
      has_exclamation = False
      sentence_container=[]
      for word in self.value.split(" "):
        sentence_container.append(word)
      if('!' in sentence_container[-1]):has_exclamation = True
      print(sentence_container, has_exclamation)
      return has_exclamation

  def count_sentences(self):
    sentences_container =[]
    cleaned_sentence = self.value.replace("!",".").replace("?",".")
    for sentence in cleaned_sentence.split("."):
      if sentence.strip():
        sentences_container.append(sentence)
    
    return len(sentences_container)

"""
sentence = "My name is Rym Mattar. I am a software engineer. I love coding!"
is_fullstop = False
sentence_container=[]
for word in sentence.split(" "):
  sentence_container.append(word)
if('.' in sentence_container[-1]):is_fullstop = True
print(sentence_container, is_fullstop)
"""

how_are_you = MyString("This is a string! It has three sentences. Right?")

print(how_are_you.count_sentences())