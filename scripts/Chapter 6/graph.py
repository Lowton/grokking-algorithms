from collections import deque

graph = {}
graph['you'] = ['anna','max','bob']
graph['anna'] = ['max','tom','pope']
graph['max'] = ['anna','hugo','maria','dude']
graph['bob'] = ['maria','dude','kally','jo']
graph['tom'] = ['jo']
graph['pope'] = []
graph['hugo'] = ['jo','marry']
graph['maria'] = ['marry']
graph['dude'] = ['jo', 'mc hammer']
graph['kally'] = []
graph['jo'] = ['mc hammer']
graph['marry'] = ['maria']
graph['mc hammer'] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if isPersonChosenOne(person):
                print(f'{person} is chosen one')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def isPersonChosenOne(person):
    return ' ' in person

search("you")

