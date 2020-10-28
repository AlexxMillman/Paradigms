line = "густооонаселённое село"
word_1 = line.split(" ")[0]
word_2 = line.split(" ")[1]
used_chars = []
count = 0

for char_index in range(len(word_1)):
   if used_chars.count(word_1[char_index]) == 0 and (word_2.find(word_1[char_index]) != -1):
     count = count + 1
     used_chars.append(word_1[char_index])

if count == len(word_2):
  print("Можна створити з першого слова друге")
else:
  print("Не можна створити з першого слова друге")