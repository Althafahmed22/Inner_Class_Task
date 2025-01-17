class Ec2:
    def __init__(self, instance_Type, Ami, Key_Pair):
        self.instance_Type = instance_Type  # Instance type
        self.obj2 = self.Sensitive_data(Ami, Key_Pair)  # Sensitive data object

    def get_sensitive_data(self):
        return self.obj2.get_sensitive_info()  #Access sensitive info

    class Sensitive_data:#inner class contains Sensitive Data
        def __init__(self, Ami, Key_Pair):
            self.__Ami = Ami  # Private variable
            self.__key_Pair = Key_Pair  # Private variable

        def get_sensitive_info(self):
            return f"Ami: {self.__Ami}, Key_Pair: {self.__key_Pair}"  #Return sensitive data
obj = Ec2("t2.micro", "ami-0c55b159cbfafe1f0", "my-key-pair")
print(obj.get_sensitive_data())



