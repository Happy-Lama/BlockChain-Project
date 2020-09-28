import json
import hashlib
import time

class Chain:
	def __init__(self):
		self.blocks = []

	def push(self, block):
		if len(self.blocks) !=  0:
			if block.info["previous_hash"] == self.blocks[-1].info["hash"]:
				self.blocks.append(block)
				return block.info["hash"]
			else:
				return "CORRUPTED BLOCK"
		else:
			self.blocks.append(block)
			return block.info["hash"]

	def length(self):
		return len(self.blocks)

	def __repr__(self):
		return f"{self.blocks}"

	def __getitem__(self,index):
		return self.blocks[index]

class block:
	def __init__(self, previous_hash=None):
		self.info = {
						"time_initiated": time.time(),
						"previous_hash": previous_hash,
						"events":[],
						"hash": None
					}

	def add_info(self, info):
		self.info['events'].append([time.time(), info])

	def hash(self):
		string = str(len(self.info["events"])).encode("utf-8")
		self.info["hash"] = hashlib.sha224(string).hexdigest()
		return self.info["hash"]

	def __repr__(self):
		return json.dumps(self.info, indent=2)

# chain = Chain()
# chain.push(block())
# # print(chain)
# block1 = block()
# block1.add_info("hello world")
# new_hash = block1.hash()
# chain.push(block1)
# print(block1)
# block2 = block(previous_hash=new_hash)
# block2.add_info("My First Block")
# new_hash = block2.hash()
# chain.push(block2)
# print(chain[-1])