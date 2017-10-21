import re
import sys
try:
    from StringIO import StringIO
except ImportError:
    import io
    from io import StringIO

# https://stackoverflow.com/questions/241327/python-snippet-to-remove-c-and-c-comments


def removeCCppComment(text):

    # Return a string containing only the newline chars contained in strIn
    def blotOutNonNewlines(strIn):
        return "" + ("\n" * strIn.count('\n'))

    def replacer(match):
        s = match.group(0)
        # Matched string is //...EOL or /*...*/  ==> Blot out all non-newline
        # chars
        if s.startswith('/'):
            return blotOutNonNewlines(s)
        else:                  # Matched string is '...' or "..."  ==> Keep unchanged
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )

    return re.sub(pattern, replacer, text)


def main():
    if len(sys.argv) != 4:
        print("Incorrect argument structure")
        return 1
    mem_name = str(sys.argv[3])
    in_file = open(str(sys.argv[1]))
    out_file = open(str(sys.argv[2]), 'a')
    
    total_file = in_file.read()
    in_file.close()

    no_comments = removeCCppComment(total_file)
    no_comment_file = io.StringIO(no_comments)

    for line in no_comment_file:
        #print("line:{0}".format(line.strip()))
        words = line.split()
        
        if words[0][0] == '/' or words[0][0] == '' or words[0][0] == '\n':
            continue
        a_high = words[0][1:5]
        a_low = words[0][5:9]
        for word in words[1:]:
            word = word.replace("_", "")
            if a_low == '':
                return 1
            definition = mem_name + \
                "[32'h" + a_high + a_low + "] = 32'h" + word + ';\n'
            out_file.write(definition)
            a_low = format(int(a_low, 16) + 1, '04X')
        
    out_file.close()
    print("Complete")

main()
