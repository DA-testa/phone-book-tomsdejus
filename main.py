# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split(' ', 2)) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for request in queries:
        if request.type == 'add':
            contacts[request.number] = request.name
        elif request.type == 'del':
            if request.number in contacts:
                del contacts[request.number]
        elif request.type == 'find':
            response = contacts.get(request.number, "not found")
            result.append(response)
        else:
            response = "not found"
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))