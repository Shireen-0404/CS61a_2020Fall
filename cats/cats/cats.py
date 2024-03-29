"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime
from operator import abs


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    true_para = [i for i in paragraphs if select(i) == True]
    if len(true_para) < k+1:
        return ''
    else:
        return true_para[k]

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(para):
        for word in topic:
            if word in split(lower(remove_punctuation(para))):
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if len(typed_words)==0 or len(reference_words)== 0:
        return 0.0
    correct_words = [typed_words[i] for i in range(min(len(typed_words),len(reference_words))) if typed_words[i]==reference_words[i] ]
    return 100*len(correct_words)/len(typed_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    num_words = len(typed)/5
    return 60*num_words/elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words or limit == 0:
        return user_word
    elif min(diff_function(user_word,i,limit) for i in valid_words) > limit:
        return user_word
    def diff(word,compare):
        if diff_function(word,compare,limit) <= limit:
            return diff_function(word,compare,limit)
        else:
            return limit+1
    return min(valid_words,key = lambda i: diff(user_word,i))       
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # 要将计算最简化，需要时刻check临界条件：
    # 1.start和goal的diff_len大于limit，直接return
    # 2.每出现一个不同的字母，diff_len+1，并立刻check是否大于limit
    # BEGIN PROBLEM 6
    diff_len = abs(len(start)-len(goal))
    if diff_len > limit:
        return diff_len
    com_len = min(len(start),len(goal))
    def compare(s,g,l,d): 
        if len(s) == 0:
            return d
        elif s[0] != g[0]:
            d += 1
            if d > l:
                return d
            return compare(s[1:], g[1:], l,d)
        return compare(s[1:], g[1:], l,d)
    return compare(start[:com_len], goal[:com_len], limit,diff_len)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
     #if abs(len(start)-len(goal)) > limit:
     #   return limit+1这段可以不要,这样可以直接从limit里面-1，check limit是否小于0
     # 反正就是整个变量出来记载edit次数，每次更新都check，一旦大于limit就停止recursion
    def edit(s,g,lim,edition=0):
        if edition > lim:
            return edition
        elif len(s) == 0 or len(g) == 0: 
            return max(len(s),len(g)) + edition
        elif s[0] == g[0]:
            return edit(s[1:], g[1:], lim,edition)
        elif s[0] != g[0]:
            add_diff = edit(g[0]+s, g, lim,edition+1)
            remove_diff = edit(s[1:], g, lim,edition+1)
            substitute_diff = edit(g[0]+s[1:], g, lim,edition+1)
        return min(add_diff,remove_diff,substitute_diff)
    return edit(start,goal,limit,edition=0)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    corr = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            corr += 1
        elif typed[i] != prompt[i]:
            message = {'id':user_id,'progress':corr/len(prompt)}
            send(message)
            return corr/len(prompt)
    message = {'id':user_id,'progress':corr/len(prompt)}
    send(message)
    return corr/len(prompt)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    times = []
    for list in times_per_player:
        times = times + [[list[i]-list[i-1] for i in range(1,len(list))]]
    return game(words,times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    fastest = [[] for _ in player_indices]
    for i in word_indices:
        fastest_player = min([p for p in player_indices],key=lambda x:time(game,x,i))
        fastest[fastest_player].append(word_at(game,i))
    return fastest


    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)