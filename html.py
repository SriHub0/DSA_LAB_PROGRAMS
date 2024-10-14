class Stack:
    def __init__(self):
        self.S = []

    def push(self, element):
        self.S.append(element)

    def is_empty(self):
        return len(self.S) == 0

    def pop(self):
        if not self.is_empty():
            return self.S.pop()
        else:
            return "Cannot pop from an empty stack."
    def size(self):
        return len(self.S)
    def top(self):
        if not self.is_empty():
            return self.S[-1]
        else:
            return "Empty stack"
def is_matched_html(raw):
    S = Stack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return s.is_empty()
raw = "<body> <center> <p> the storm tossed the little boat likje a cheap snaeker in an old machine,the three drunken fishermen were used to such treatment ,of couse,but not the trhree salesmanm,who even as a stowaway now felt that he had overpaid for the voyage</p><0l><li>will the salesman die</li><li>what color is the boat?</li><li>and what about naomi</li></ol></body>"
print(is_matched_html(raw))