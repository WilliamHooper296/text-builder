from Builder import Builder

fileName = "story1.txt"

fileNames = ["story1.txt", "Job28.txt"]

builder = Builder()
backing = builder.buildMulti(fileNames, 2)


builder.read(backing, 100)
