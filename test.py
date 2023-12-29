#let's work with literals and identifiers
workers = {"Rensy", "Martin", "Timothy"}
#The example above is workers is an identifiers while the array of names is a literal
my_age = 20

for i in workers:
    if(i == "Martin"):
        print("The name {} has been found", i)
    print(i)

print(workers)