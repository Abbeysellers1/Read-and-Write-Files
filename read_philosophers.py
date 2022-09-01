# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    line1= infile.readline().rstrip('\n')
    line2= infile.readline().rstrip('\n')
    line3= infile.readline().rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

main()