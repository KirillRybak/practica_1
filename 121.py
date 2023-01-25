from collections import Counter

txt = """
Стоял солнечный день. Небо голубое, птицы поют. За зелёными кустами кто-то прятался, было хорошо слышно шелест сочных зелёных листьев. Там сидел маленький крольчонок и мирно пожёвывал травку, одуванчики, клевер и листочки. Заметив меня, он заторопился и, дожевав последний лист, ринулся в сторону леса. Только и видно было, как он заскочил в дальние кусты, слышно было громкий шелест и чириканье, и как множество маленьких птичек выпорхнуло из-за кустов, и эта небольшая стайка скрылась за высокими деревьями.
"""
word_list = []
for i in txt.split():
    clear_world = ""
    for letter in i:
        if letter.isalpha():
            clear_world += letter.lower()
        word_list.append(clear_world)
print(Counter(word_list))


