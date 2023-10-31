d = {'Adele': 
{'All I Ask': {'said', 'scared', 'say', 'wrong', 'since', 'way', 'door', 'like', 'last', 'need', 'left', 'coming', 'honesty', 'love', 'memory', 'hold', 'tell', 'use', 'lovers', 'lesson', 'get', 'hand', 'eyes', 'pretend', 'bridge', 'tomorrow', 'cruel', 'forgiveness', 'asking', 'one', 'give', 'next', 'play', 'ask', 'night', 'knows', 'wanna', 'run', 'speak', 'friend', 'ends', 'chorus', 'let', 'word', 'vicious', 'know', 'remember', 'leave', 'matters', 'cause', 'verse', 'heart', 'take', 'sure', 'look'}, 
"Can't Let Go": {'said', 'thought', 'wrong', 'platter', 'die', 'baby', 'like', 'hope', 'hard', 'thinking', 'thrill', 'coat', 'lied', 'loved', 'yet', 'tell', 'love', 'go', 'cold', 'wanted', 'bridge', 'throat', 'gave', 'much', 'feel', 'write', 'faked', 'arms', 'find', 'wrote', 'outro', 'kill', 'note', 'truth', 'lump', 'round', 'told', 'hid', 'time', 'chorus', 'let', 'sometimes', 'even', 'know', 'dark', 'heaven', 'verse', 'oooh', 'save', 'slow', 'everything', 'went', 'life', 'seam'}}, 
'Bob Dylan': {'4Th Time Around': {'make', 'hummed', 'last', 'picture', 'better', 'brought', 'go', 'get', 'eyes', 'forced', 'buttoned', 'mine', 'sense', 'took', 'boot', 'piece', 'threw', 'must', 'waited', 'felt', 'shirt', 'back', 'gum', 'hands', 'pockets', 'clear', 'hallway', 'cried', 'crutch', 'drawer', 'give', 'ask', 'covered', 'tapped', 'walked', 'till', 'time', 'forget', 'shoe', 'look', 'drum', 'got', 'lies', 'forgotten', 'thumbs', 'said', 'thought', 'finding', 'filled', 'worked', 'left', 'something', 'outside', 'leaned', 'handed', 'knocked', 'cute', 'breaking', 'stood', 'much', 'else', 'waste', 'floor', 'red', 'wheelchair', 'gallantly', 'leave', 'rum', 'asked', 'screamed', 'went', 'suit', 'words', 'fell', 'come', 'deaf', 'loved', 'everybody', 'straightened', 'jamaican', 'dear', 'tried', 'dirt', 'wasted', 'face', 'spit'}, 
'A Satisfied Mind': {'say', 'way', 'little', 'fame', 'hard', 'satisfied', 'times', 'man', 'loved', 'friends', 'wading', 'heard', 'dreamed', 'lifes', 'fortune', 'get', 'richer', 'ones', 'world', 'money', 'one', 'happened', 'lost', 'hmm', 'find', 'suddenly', 'comes', 'run', 'someone', 'time', 'far', 'game', 'know', 'many', 'leave', 'start', 'ten', 'doubt', 'old', 'things', 'certain', 'dime', 'everything', 'mind', 'life'}}}
d2 = {}

for singer in d:
    if singer not in d2:
        d2[singer] = {}
    for song in d[singer]:
        if song not in d2[singer]:
            d2[singer].update({song:set(d[singer][song])})
            

songs = [('Adele', "Can't Let Go"), ('Bob Dylan', 'A Satisfied Mind')]

print(len(songs[0]))