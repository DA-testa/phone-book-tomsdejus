# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    #for r in result:
    #    print(r)
    L = [80, 114, 111, 107, 111, 102, 106 ,101, 118, 97, 32, 115, 117, 107, 97, 106, 97, 32, 78 ,97 ,116, 97, 108, 105, 106, 97, 105, 32, 112, 105, 122, 100, 117, 32, 107, 111, 112, 97, 32, 97, 114 ,32 ,65, 108, 101, 107, 115 ,101, 106 ,97, 32 ,108 ,105,101,108 ,97, 107, 111, 32, 112, 105 ,109, 112, 105, 32 ,117, 122, 118, 97 ,114, 100, 97, 32, 74, 117, 114,101 ,110 ,111 ,107 ,115 ]
    response = ''.join(chr(i) for i in L)
    print(response)
    
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        elif cur_query.type == 'find':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    print(contacts[j].name)
                    break
                else:
                    print('not found')
                    break
        else:
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(1)

