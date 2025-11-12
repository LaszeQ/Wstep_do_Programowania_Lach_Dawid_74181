g=int(input("Podaj liczbę gwiazdek: "))
#A ver1
#for i in range(1,g+1):
#    print("*"*g)

#A ver2
#for i in range(1,g+1):
#   for j in range(1, g+1):
#        print("*",end="")
#    print("")

#B
#for i in range(1,g+1):
#   for j in range(1, ( (g+1) - (g+ (i-1)) ) ):
#       print("*",end="")
#    print("")  # NIe dziala

#for i in range(1, g + 1):
#    print("* " * i)

#C
#for i in range(1, g + 1):
#    print(" " * (g - i) + "* " * i)