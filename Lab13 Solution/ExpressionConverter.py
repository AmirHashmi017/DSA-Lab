class ExpressionConverter:
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}

    def __init__(self,expression):
        self.Expression=expression
    
    def IsOperand(self,character):
        return character.isalnum()
    
    def IsOperator(self,character):
        if character in ['+','-','*','/','^']:
            return True
        return False
    
    def PrintExpression(self,expression):
        for character in expression:
            print(character,end="")
        print()

    def InfixToPostfix(self,expression):
        stack=[]
        postfix=[]

        for character in expression:
            if(self.IsOperand(character)):
                postfix.append(character)
            elif(character=='(' or character=='{' or character=='['):
                stack.append(character)
            elif(character==')' or character=='}' or character==']'):
                while(stack and stack[-1] not in "({["):
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while(stack and stack[-1] not in "({[" and self.precedence[character]<=self.precedence[stack[-1]]):
                    postfix.append(stack.pop())
                stack.append(character)
        
        while stack:
            postfix.append(stack.pop())
            
        return postfix
    
    def PostfixToInfix(self,expression):
        stack=[]
        for character in expression:
            if(self.IsOperand(character)):
                stack.append(character)
            elif(self.IsOperator(character)):
                operand1=stack.pop()
                operand2=stack.pop()
                stack.append(f"({operand2}{character}{operand1})")

        return stack[-1]
    
    def InfixToPrefix(self,expression):
        reversedexpression=expression[::-1]
        adjustedexpression=reversedexpression.replace('(','temp').replace(')','(').replace('temp',')')
        adjustedexpression=adjustedexpression.replace('{','temp').replace('}','{').replace('temp','}')
        adjustedexpression=adjustedexpression.replace('[','temp').replace(']','[').replace('temp',']')

        reversepostfix=self.InfixToPostfix(adjustedexpression)
        prefix=reversepostfix[::-1]
        return prefix
    
    def PrefixToInfix(self,expression):
        stack=[]
        for character in reversed(expression):
            if(self.IsOperand(character)):
                stack.append(character)
            elif(self.IsOperator(character)):
                operand1=stack.pop()
                operand2=stack.pop()
                stack.append(f"({operand1}{character}{operand2})")
        
        return stack[-1]
    
# Driver Code
expression = "a+[(b*{c+[d-e]})/f]*g"  
# expression = "a+b*c+d"  
converter = ExpressionConverter(expression)

print("Infix Expression:", expression)
postfix = converter.InfixToPostfix(expression)
print("Postfix Expression:",end="")
converter.PrintExpression(postfix)
prefix = converter.InfixToPrefix(expression)
print("Prefix Expression:",end="")
converter.PrintExpression(postfix)
infixfrompostfix=converter.PostfixToInfix(postfix)
print("Converted back to Infix from Postfix:",end="")
converter.PrintExpression(infixfrompostfix)
infixfromprefix=converter.PrefixToInfix(prefix)
print("Converted back to Infix from Prefix:",end="")
converter.PrintExpression(infixfromprefix)
