from Builder import Builder

fileName = "story1.txt"

fileNames = ["story1.txt", "story2.txt", "story3.txt"]

builder = Builder()
backing = builder.buildMulti(fileNames, 2)
#backing = builder.build("bible.txt", 3)


builder.read(backing, 300)
