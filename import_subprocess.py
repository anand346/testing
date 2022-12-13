from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="Give your repo url")
parser.add_option("-b", "--branch",dest="branch",
                  help="give your branch name here")

(options, args) = parser.parse_args()

print("source is : ",options.source)
print("branch is : ",options.branch)