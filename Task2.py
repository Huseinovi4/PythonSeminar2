# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.ц

p, q = map(int, input().split())
x1 = ((-(-p) - ((-p)**2 - 4*q)**0.5) // 2)
x2 = ((-(-p) + ((-p)**2 - 4*q)**0.5) // 2)
print(int(x1), int(x2))
