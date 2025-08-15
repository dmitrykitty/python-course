class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.freq = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        max_mem_slots = max(len(args), self.total_mem_slots)
        self.mem_slots = []
        for i in range(max_mem_slots):
            self.mem_slots.append(args[i])

    def get_config(self):
        return f"Mother board: {self.name}; \nSlots amount: {len(self.mem_slots)}; \nCPU: {self.cpu.name}; \nFrequency: {self.cpu.freq} MHz;"



