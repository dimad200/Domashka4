import sys
sys.stderr.write("Это будет восприниматься как ошибка")
sys.stdout.write("Hello, world!")
sys.stderr.write("Это будет восприниматься как ошибка")
a=sys.stdin.read()
print(a)
