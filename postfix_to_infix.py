class A:
    def postfix_to_infix(self, expression):
        a = ['+', '-']
        b = ['*', '/']
        char_a = ''
        char_b = ''
        last = ''
        now = ''

        for i, v in enumerate(expression):

            if v in a:
                now = 'a'
                char_a = char_a + v + char_b
                last = now
                now = ''
            elif v in b:
                now = 'b'
                if last != 'b' and last != '':
                    char_a = '(' + char_a + ')' + v + char_b
                elif last == '':
                    char_a = char_a + v + char_b
                    last = now
                    now = ''
            else:
                if char_a == '':
                    char_a = v
                else:
                    char_b = v
        return char_a

a = A()
print(a.postfix_to_infix('fk*a+b-c-e*'))
