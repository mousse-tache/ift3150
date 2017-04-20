def main():
	with open("bibtest100","w+") as file:
		for x in range(0,100):
			file.write("@BOOK{, author = {Adams}, publisher = {Bookclub}, title = {H2G2"+str(x)+"}, year = {1978}, volume = {1} }\n")


	with open("bibtest1000","w+") as file:
		for x in range(0,1000):
			file.write("@BOOK{, author = {Adams}, publisher = {Bookclub}, title = {H2G2"+str(x)+"}, year = {1978}, volume = {1} }\n")



	with open("bibtest10000","w+") as file:
		for x in range(0,10000):
			file.write("@BOOK{, author = {Adams}, publisher = {Bookclub}, title = {H2G2"+str(x)+"}, year = {1978}, volume = {1} }\n")

	with open("bibtest100000","w+") as file:
		for x in range(0,100000):
			file.write("@BOOK{, author = {Adams}, publisher = {Bookclub}, title = {H2G2"+str(x)+"}, year = {1978}, volume = {1} }\n")


if __name__ == '__main__':
            main()
