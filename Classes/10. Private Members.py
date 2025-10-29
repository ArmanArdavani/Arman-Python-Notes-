class TagCloud:
    def __init__(self):
        self.__tags = {}  #the double underline makes it harder for someone to access the given attribute of the class
    
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1 
    
    def __getitem__(self, tag):
         return self.tag.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
         return iter(self.__tags)
    
cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags["PYTHON"])