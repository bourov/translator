morphemes = float(input())

if morphemes < 2:
    print('Analytic')
elif morphemes <= 3.:
    print('Synthetic ')
else:
    print('Polysynthetic')
