expr = input()
minus_exprs = expr.split('-')

eval_result = 0
for minus_expr in minus_exprs[:1]:
    terms = minus_expr.split('+')
    eval_term = 0
    for term in terms:
        eval_term += int(term)
    eval_result += eval_term

for minus_expr in minus_exprs[1:]:
    terms = minus_expr.split('+')
    eval_term = 0
    for term in terms:
        eval_term += int(term)
    eval_result -= eval_term

print(eval_result)
