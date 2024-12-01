from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        
    for key in graph:
        graph[key].sort(reverse=True)
    
    answer = []
    
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        answer.append(airport)
    
    
    dfs("ICN")
    return answer[::-1]