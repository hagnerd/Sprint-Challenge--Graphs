class Stack:
    def __init__(self):
        self.storage = []

    def __str__(self):
        output_str = ""
        for item in self.storage:
            output_str = f"({item})" if output_str == "" else f"({item}) <- {output_str}"

        return output_str


    def length(self):
        return len(self.storage)

    def push(self, value):
        """
        
        """
        self.storage.append(value)
        return self.storage

    def pop(self):
        """
        Removes an element from the front of the list (we are storing in reverse
        order for efficiency reasons)
        """
        if self.length() > 0:
            return self.storage.pop()

        return None
