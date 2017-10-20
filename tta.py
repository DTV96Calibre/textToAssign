import sys

def main():
    if len(sys.argv) != 4:
        print("Incorrect argument structure")
        return 1;
    mem_name = str(sys.argv[3])
    in_file = open(str(sys.argv[1]))
    out_file = open(str(sys.argv[2]), 'a')
    
    m_cm = False    //multi-line comment flag
    for line in in_file:
            words = line.split()
            if m_cm == True and '*/' in words:
                m_cm = False
            elif m_cm == True:
                continue
            elif '//' in words or words[0][0] == '' or words[0][0] == '\n':
                continue
            elif '/*' in words:
                m_cm = True
                if '*/' in words:
                    m_cm = False
                continue
            a_high = words[0][1:5]
            a_low = words[0][5:9]
            for word in words[1:]:
                word = word.replace("_", "")
                if a_low == '':
                    return 1
                definition = mem_name + "[32'h" +a_high+a_low+"] = 32'h" + word + ';\n'
                out_file.write(definition)
                a_low = format(int(a_low,16) + 1, '04X')
    in_file.close()
    out_file.close()
    print("Complete")

main()