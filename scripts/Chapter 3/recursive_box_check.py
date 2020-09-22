from box_rundom_generator import Box

box = Box()

print(box.getBoxes())

def checkBox(box):
    if box.checkKey() == True:
        print(f'Key founded in box {box.id}')
        return box.id
    else:
        print(f"{box.age} aged box {box.id} doesn't have a key, but has {len(box.content)} boxes inside")
        for child in box.content:
            id = checkBox(child)
            if not id == None:
                return id

id = checkBox(box)
