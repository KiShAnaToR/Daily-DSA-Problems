class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = dict(knowledge)
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(current_key)
                result.append(knowledge_dict.get(key, "?"))
                current_key.clear()
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)