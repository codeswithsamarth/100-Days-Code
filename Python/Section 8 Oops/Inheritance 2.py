class Processor:
    def __init__(self,name,speed,cores):
        super().__init__()
        self.name = name
        self.speed = speed
        self.cores = cores

class Graphic_Card:
    def __init__(self,model,memory):
        self.model = model
        self.memory = memory
        super().__init__()

class Laptop:
    def __init__(self,name,model,manufacturer,):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        super().__init__()

class Gaming_Laptop(Laptop):
    def __init__(self,Name,Model,Manufacturer,Graphic_Model,Graphic_Memory,Processor_Name,Processor_Speed
                        ,Processor_cores):
        super().__init__(name=Name,model=Model, manufacturer=Manufacturer)

        self.processor = Processor(name=Processor_Name,speed=Processor_Speed,cores=Processor_cores)
        self.graphics = Graphic_Card(model=Graphic_Model,memory=Graphic_Memory)

        print(f"Laptop: {self.name}, Model: {self.model}, Manufacturer: {self.manufacturer}")
        print(f"Processor: {self.processor.name}, Speed: {self.processor.speed}, Cores: {self.processor.cores}")
        print(f"Graphics: {self.graphics.model}, Memory: {self.graphics.memory}")

Laptop = Gaming_Laptop(Name="Victus 15",
                       Model="fx991MS",
                       Manufacturer="Hp",
                       Processor_Name="Intel i5",
                       Processor_Speed=1600,
                       Processor_cores=16,
                       Graphic_Model="RTX3050",
                       Graphic_Memory="4GB")


