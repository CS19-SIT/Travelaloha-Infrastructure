solutions = ['ADRIEL', 'ADVENTURE', 'BABIES', 'BROTHERS', 'BUSY', 'CALEB', 'CEDRIC', 'CHERISH', 'CHRISTIAN', 'CUTE', 'DAD', 'DAMON', 'DORAN', 'ETHAN', 'ELEVEN', 'FAMILY', 'FUN',
             'GREATWHITE', 'GROCERIES', 'HOMESCHOOLED', 'JADON', 'LAUNDRY', 'LOVE', 'MARTIN', 'MOM', 'NOISY', 'ONEGIRL', 'PROJECTS', 'SISTER', 'TWINS', 'WETBEDDING', 'WISCONSIN', 'WORK']
puzzle = '''A D E R T Y W I O P A P R O J E C T S Z X C V G R M 
I U O W I S C O N S I N N X C V L M Q W A D T R I O 
G S I S T E R V R P B O M A W R O C N E V E L E D F 
X N V C I R D E C K M N E T I C V D Y R D N U A L Z 
S G J L S M C W E A T Y A R P T E D F G U H K T Z M 
G R A N O I S Y D L R T H R U L S A B D S R Z W S M 
N Y E U H J E R V E F C M D O T S I W I I O H H T C 
I L K H D A D V T I M M B O A D N G R N K K C I I H 
D I V I T D E H E R I E H N M Z Q E J H N V R T J B 
D M H S D O A U P D L C X E K Z H T V B C I D E W S 
E A R P A N R F R A S U K G Z C H F B D N M T L M U 
B F Y G U T F B C E I T S I Y H Q A W E A T Y R S P 
T K H F D C V B M M Q E T R P S I E R E C O R G A U 
E D F S H J J O D X C A B L B O U Q A R W S H E Q M 
W J N U J M H K O L I D L O L I I B A B I E S B T G 
'''
wordgrid = puzzle.replace(' ', '')
length = wordgrid.index('\n')+1
characters = [(letter, divmod(index, length))
              for index, letter in enumerate(wordgrid)]
wordlines = {}
directions = {'going downwards': 0, 'going downwards and left diagonally': -
              1, 'going downwards and right diagonally': 1}

for word_direction, directions in directions.items():
    wordlines[word_direction] = []
    for x in range(length):
        for i in range(x, len(characters), length + directions):
            wordlines[word_direction].append(characters[i])
        wordlines[word_direction].append('\n')
wordlines['going right'] = characters
wordlines['going left'] = [i for i in reversed(characters)]
wordlines['going upwards'] = [
    i for i in reversed(wordlines['going downwards'])]
wordlines['going upwards and left diagonally'] = [
    i for i in reversed(wordlines['going downwards and right diagonally'])]
wordlines['going upwards and right diagonally'] = [
    i for i in reversed(wordlines['going downwards and left diagonally'])]


def printitout(direction, tuple, lines):
    print "Keep in mind, rows are horizontal and columns are vertical.\n"
    for direction, tuple in lines.items():
        string = ''.join([i[0] for i in tuple])
        for word in solutions:
            if word in string:
                coordinates = tuple[string.index(word)][1]
                print word, 'is at row', coordinates[0]+1, 'and column', coordinates[1]+1, direction + "."


printitout(word_direction, tuple, wordlines)
