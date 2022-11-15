var1 = 24
var2 = 66
if var1 < var2:
    var1, var2 = var2, var1
PGCD = var2
while var1 % PGCD != 0 or var2 % PGCD != 0:
    PGCD -= 1
print(PGCD)
