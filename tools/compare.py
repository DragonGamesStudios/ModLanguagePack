import configparser
import sys

parser1 = configparser.ConfigParser()
parser2 = configparser.ConfigParser()

parser1.read(sys.argv[1])
parser2.read(sys.argv[2])

extra1 = {}
extra2 = {}

sections1 = parser1.sections()
sections2 = []

for section in parser2.sections():
    extra2[section] = []
    if parser1.has_section(section):
        extra1[section] = []
        options1 = set(parser1.options(section))

        for option in parser2.options(section):
            if option in options1:
                parser1.remove_option(section, option)
            else:
                extra2[section].append(option)
            
        for option in parser1.options(section):
            extra1[section].append(option)

        parser1.remove_section(section)
    else:
        extra2[section] = parser2.options(section)

for section in parser1.sections():
    extra1[section] = parser1.options(section)

print("Entries in " + sys.argv[1] + " that are not present in " + sys.argv[2] + ":")

for k, v in extra1.items():
    if len(v):
        print("\t" + k + ":")
        for opt in v:
            print("\t\t" + opt)

print()

print("Entries in " + sys.argv[2] + " that are not present in " + sys.argv[1] + ":")

for k, v in extra2.items():
    if len(v):
        print("\t" + k + ":")
        for opt in v:
            print("\t\t" + opt)


