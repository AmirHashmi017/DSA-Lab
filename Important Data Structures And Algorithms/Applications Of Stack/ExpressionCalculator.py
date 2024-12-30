class ExpressionCalculator:
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def __init__(self,expression):
        self.Expression=expression
    
    def IsOperand(self,character):
        return character.isnumeric()
    
    def IsOperator(self,character):
        return character in ['+','-','*','/','^']
    
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

        while(stack):
            postfix.append(stack.pop())

        return postfix
    
    def CalculateExpression(self):
        postfixexpression=self.InfixToPostfix(self.Expression)
        stack=[]
        for character in postfixexpression:
            if(self.IsOperand(character)):
                stack.append(int(character))
            elif(self.IsOperator(character)):
                operand1=stack.pop()
                operand2=stack.pop()
                if(character=='+'):
                    stack.append(operand2+operand1)
                elif(character=='-'):
                    stack.append(operand2-operand1)
                elif(character=='*'):
                    stack.append(operand2*operand1)
                elif(character=='/'):
                    stack.append(operand2/operand1)
                elif(character=='^'):
                    stack.append(operand2**operand1)
        
        return stack[-1]
    
# Driver Code
expression="(1+5)*5^2"
calculator=ExpressionCalculator(expression)
print("(1+5)*5^2 = ",calculator.CalculateExpression())
