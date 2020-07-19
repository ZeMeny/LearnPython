"""reversing the lines"""
with open('text.txt') as f,  open('output.txt', 'w+') as fout:
    fout.writelines(reversed(f.readlines()))

"""reversing the words in each line"""
with open('text.txt') as f,  open('reverse.txt', 'w+') as rev:
    f_content = f.readlines()
    rev.writelines(i[::-1] for i in f_content)



filenames = ['text.txt', 'reverse.txt']

with open('combine_file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())








