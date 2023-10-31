from proj06 import update_dictionary

singer = "Lennon & McCartney"
song = "Her Majesty"
words = {'bellyful',
 'changes',
 'day',
 'get',
 'girl',
 'going',
 'gotta',
 'lot',
 'love',
 'make',
 'mine',
 'nice',
 'pretty',
 'say',
 'someday',
 'tell',
 'want',
 'wine',
 'yeah'}

data_dict = {'Adele': {'All I Ask': {'use', 'honesty', 'scared', 'hand', 'tell', 'door', 'pretend', 'last', 'sure', 'lovers', 'leave', 'forgiveness', 'say', 'ask', 'night', 'vicious', 'ends', 'love', 'coming', 'left', 'knows', 'asking', 'lesson', 'memory', 'wanna', 'heart', 'eyes', 'let', 'take', 'matters', 'give', 'way', 'play', 'cruel', 'friend', 'run', 'since', 'get', 'cause', 'hold', 'one', 'said', 'next', 'wrong', 'like', 'remember', 'tomorrow', 'need', 'speak', 'know', 'word'}, "Can't Let Go": {'lied', 'write', 'lump', 'truth', 'even', 'baby', 'tell', 'gave', 'die', 'save', 'dark', 'heaven', 'thinking', 'round', 'platter', 'go', 'went', 'feel', 'everything', 'hid', 'seam', 'loved', 'let', 'sometimes', 'throat', 'hope', 'yet', 'thought', 'wanted', 'oooh', 'time', 'kill', 'find', 'note', 'told', 'coat', 'slow', 'said', 'much', 'faked', 'life', 'like', 'hard', 'arms', 'know'}}, 'Bob Dylan': {'4Th Time Around': {'threw', 'else', 'filled', 'dirt', 'forgotten', 'waste', 'wasted', 'last', 'must', 'leave', 'words', 'worked', 'breaking', 'handed', 'ask', 'back', 'pockets', 'gallantly', 'go', 'went', 'picture', 'crutch', 'jamaican', 'loved', 'stood', 'better', 'screamed', 'till', 'tapped', 'waited', 'give', 'got', 'straightened', 'sense', 'brought', 'cried', 'covered', 'thought', 'forced', 'took', 'get', 'rum', 'finding', 'something', 'spit', 'make', 'buttoned', 'tried', 'look', 'face', 'wheelchair', 'hands', 'drum', 'felt', 'shoe', 'fell', 'piece', 'everybody', 'leaned', 'asked'}, 'A Satisfied Mind': {'fame', 'ones', 'money', 'start', 'old', 'certain', 'dreamed', 'leave', 'say', 'game', 'things', 'someone', 'suddenly', 'man', 'world', 'lifes', 'comes', 'everything', 'dime', 'loved', 'richer', 'ten', 'little', 'way', 'run', 'lost', 'fortune', 'get', 'time', 'one', 'far', 'times', 'satisfied', 'find', 'wading', 'life', 'doubt', 'hard', 'friends', 'heard', 'happened', 'know', 'many'}}}

update_dictionary(data_dict, singer, song, words)

instructor_data = {'Adele': {'All I Ask': {'honesty', 'knows', 'forgiveness', 'say', 'asking', 'since', 'take', 'play', 'tell', 'word', 'eyes', 'door', 'pretend', 'way', 'get', 'cruel', 'ends', 'love', 'next', 'tomorrow', 'wanna', 'night', 'coming', 'hold', 'one', 'lovers', 'heart', 'use', 'lesson', 'wrong', 'need', 'leave', 'remember', 'know', 'ask', 'friend', 'run', 'like', 'hand', 'let', 'give', 'speak', 'said', 'cause', 'matters', 'scared', 'memory', 'last', 'vicious', 'sure', 'left'}, "Can't Let Go": {'thinking', 'loved', 'gave', 'life', 'throat', 'platter', 'feel', 'tell', 'wanted', 'coat', 'baby', 'find', 'lump', 'told', 'faked', 'write', 'went', 'even', 'everything', 'hid', 'hard', 'seam', 'oooh', 'know', 'much', 'arms', 'sometimes', 'thought', 'lied', 'die', 'go', 'time', 'hope', 'like', 'heaven', 'let', 'truth', 'yet', 'said', 'kill', 'round', 'slow', 'note', 'save', 'dark'}}, 'Bob Dylan': {'4Th Time Around': {'loved', 'rum', 'face', 'better', 'pockets', 'crutch', 'till', 'back', 'gallantly', 'shoe', 'get', 'got', 'buttoned', 'spit', 'filled', 'piece', 'worked', 'screamed', 'dirt', 'went', 'sense', 'waited', 'finding', 'make', 'drum', 'leaned', 'jamaican', 'tapped', 'covered', 'leave', 'must', 'cried', 'something', 'ask', 'hands', 'look', 'forced', 'thought', 'threw', 'picture', 'go', 'forgotten', 'felt', 'wasted', 'else', 'breaking', 'give', 'asked', 'tried', 'everybody', 'stood', 'fell', 'waste', 'last', 'wheelchair', 'words', 'brought', 'straightened', 'handed', 'took'}, 'A Satisfied Mind': {'loved', 'times', 'say', 'life', 'start', 'ones', 'way', 'little', 'find', 'get', 'friends', 'suddenly', 'money', 'wading', 'man', 'everything', 'one', 'things', 'hard', 'know', 'someone', 'leave', 'far', 'fortune', 'run', 'world', 'game', 'certain', 'doubt', 'dime', 'lost', 'time', 'happened', 'comes', 'many', 'dreamed', 'ten', 'richer', 'lifes', 'fame', 'heard', 'satisfied', 'old'}}, 'Lennon & McCartney': {'Her Majesty': {'gotta', 'someday', 'say', 'lot', 'yeah', 'mine', 'girl', 'pretty', 'tell', 'make', 'changes', 'day', 'bellyful', 'get', 'love', 'want', 'wine', 'going', 'nice'}}}

print("student_data:\n",data_dict)
print("instructor data:\n",instructor_data)
assert data_dict == instructor_data
