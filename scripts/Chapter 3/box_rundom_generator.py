from uuid import uuid4
from random import randrange
import json

max_internal_boxes_count = 10
key_putted_to_the_box = False
boxes = 0

class Box:
    def __init__(self, age=0):
        self.increaseBoxesCount()
        self.age = age
        self.id = uuid4()
        self.content = self.addInternalBoxes(age+1);
        self.key = self.addKeyIntoTheBox(self.id);

    def checkKey(self):
        return self.key

    def increaseBoxesCount(self):
        global boxes
        boxes += 1

    def addInternalBoxes(self,age):
        content = []
        if age <= 6 :
            global max_internal_boxes_count
            boxes_count = randrange(max_internal_boxes_count - age)
            for i in range(boxes_count):
                content.append(Box(age))
        return content

    def addKeyIntoTheBox(self,id):
        global key_putted_to_the_box
        if not key_putted_to_the_box:
            if randrange(200) == 0:
                key_putted_to_the_box = True
                print(f'Key put into box with id: {id}')
                return True
        return False

    def toString(self):
        return f'(id: {self.id}; age: {self.age}; key: {self.key}; internal-boxes:{len(self.content)})'

    def getBoxes(self):
        global boxes
        return f'There are {boxes} boxes in total.'
