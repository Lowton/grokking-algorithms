from box_rundom_generator import Box

box = [Box()]

print(box[0].getBoxes())

def checkBox(boxes):
    for box in boxes:
        if box.checkKey() == True:
            print(f'Key founded in box {box.id}')
            return box.id
        else:
            print(f"{box.age} aged box {box.id} doesn't have a key, but has {len(box.content)} boxes inside")
            id = checkBox(box.content)
            if id != None:
                return id

id = checkBox(box)
