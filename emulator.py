#############
# Bread CPU #
#############

# https://docs.google.com/document/d/1ElCRIVdjZPaOfBtRwQR4t3v-fzibioF6beGbO_hnlzw/edit?usp=sharing


class CPU:
	def __init__(self):
		self.memory = [0 for i in range(2**20)] # 1MB of memory
		self.stack = [] # Stack
		# General Purpose Registers
		self.GP0 = 0
		self.GP1 = 0
		self.GP2 = 0
		self.GP3 = 0
		self.IO = 0 # IO Interface
		# Instruction Registers (Internal)
		self.IR0 = 0
		self.IR1 = 0
		self.IR2 = 0
		# Flags
		self.halt = False
		self.zeroF = False
		# Program Counter
		self.PC = 1
	def runInstruction(self):
		if self.IR0 == 0x0: # HLT
			# Syntax: HLT
			self.halt = True
		
		elif self.IR0 == 0x1: # MOV
			# Syntax: MOV REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source)
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x2: # MOV
			# Syntax: MOV REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2)
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x3: # MOV
			# Syntax: MOV REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source)
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x4: # MOV
			# Syntax MOV [ADDR], REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				self.memory[self.IR1] = source
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x5: # MOV
			# Syntax MOV [ADDR], INT
			try:
				self.memory[self.IR1] = self.IR2
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x6: # MOV
			# Syntax MOV [ADDR], INT
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				self.memory[self.IR1] = source
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		
		elif self.IR0 == 0x7: # ADD
			# Syntax ADD REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source+getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x8: # ADD
			# Syntax ADD REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2+getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x9: # ADD
			# Syntax ADD REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source+getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0xA: # ADD
			# Syntax ADD [ADDR], INT
			try:
				self.memory[self.IR1] += self.IR2
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		
		elif self.IR0 == 0xB: # SUB
			# Syntax SUB REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source-getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0xC: # SUB
			# Syntax SUB REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2-getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0xD: # SUB
			# Syntax SUB REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source-getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0xE: # SUB
			# Syntax SUB [ADDR], INT
			try:
				self.memory[self.IR1] -= self.IR2
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		
		elif self.IR0 == 0xF: # MUL
			# Syntax MUL REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source*getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x10: # MUL
			# Syntax MUL REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2*getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x11: # MUL
			# Syntax MUL REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source*getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x12: # MUL
			# Syntax MUL [ADDR], INT
			try:
				self.memory[self.IR1] *= self.IR2
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		
		elif self.IR0 == 0x13: # DIV
			# Syntax DIV REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source/getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x14: # DIV
			# Syntax DIV REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2/getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x15: # DIV
			# Syntax DIV REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source/getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x16: # DIV
			# Syntax DIV [ADDR], INT
			try:
				self.memory[self.IR1] /= self.IR2
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		
		elif self.IR0 == 0x17: # MOD
			# Syntax MOD REG, REG
			try:
				source = getattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR2])
			except IndexError:
				print(f"Register #{self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source%getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x18: # MOD
			# Syntax MOD REG, INT
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.IR2%getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x19: # MOD
			# Syntax MOD REG, [ADDR]
			try:
				source = self.memory[self.IR2]
			except IndexError:
				print(f"Memory address {self.IR2} does not exist (See documentation)"); exit()
			try:
				setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], source%getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])))
			except IndexError:
				print(f"Register #{self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1
		elif self.IR0 == 0x1A: # MOD
			# Syntax MOD [ADDR], INT
			try:
				self.memory[self.IR1] %= self.IR2
			except IndexError:
				print(f"Memory address {self.IR1} does not exist (See documentation)"); exit()
			self.PC += 1

		elif self.IR0 == 0x1B: # JMP
			# Syntax JMP INT
			self.PC = self.IR1
		elif self.IR0 == 0x1C: # JMP
			# Syntax JMP REG
			self.PC = getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1]))
		elif self.IR0 == 0x1D: # JMP
			# Syntax JMP [ADDR]
			self.PC = self.memory[self.IR1]

		elif self.IR0 == 0x1E: # JPZ
			# Syntax JPZ INT
			if self.zeroF:self.PC = self.IR1
			else: self.PC += 1
		elif self.IR0 == 0x1F: # JPZ
			# Syntax JPZ REG
			if self.zeroF:self.PC = getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1]))
			else: self.PC += 1
		elif self.IR0 == 0x20: # JPZ
			# Syntax JPZ [ADDR]
			if self.zeroF:self.PC = self.memory[self.IR1]
			else: self.PC += 1

		elif self.IR0 == 0x21: # JNZ
			# Syntax JNZ INT
			if not self.zeroF:self.PC = self.IR1
			else: self.PC += 1
		elif self.IR0 == 0x22: # JNZ
			# Syntax JNZ REG
			if not self.zeroF:self.PC = getattr((self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1]))
			else: self.PC += 1
		elif self.IR0 == 0x23: # JNZ
			# Syntax JNZ [ADDR]
			if not self.zeroF:self.PC = self.memory[self.IR1]
			else: self.PC += 1

		elif self.IR0 == 0x24: # POP
			setattr(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1], self.stack.pop(0))
		elif self.IR0 == 0x22: # POP
			self.memory[self.IR0] = self.stack.pop(0)

		elif self.IR0 == 0x25: # PUSH
			self.stack.append(self, ["GP0", "GP1", "GP2", "GP3", "IO"][self.IR1])
		elif self.IR0 == 0x26: # PUSH
			self.stack.append(self.memory[self.IR0])
	def runCurrentInstruction(self):
		if not self.halt:
			self.IR0 = self.memory[self.PC*3-3]
			self.IR1 = self.memory[self.PC*3-2]
			self.IR2 = self.memory[self.PC*3-1]
			self.runInstruction()

breadCPU = CPU()
breadCPU.runCurrentInstruction()
print(breadCPU.halt) # Should always be True with it running HLT
