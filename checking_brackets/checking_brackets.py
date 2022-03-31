with open("checking_brackets/brackets.txt") as brackets:
    for i in brackets:
        line_stripped = i.strip()
        x = 0
        i = 0
        while(i < len(line_stripped)):
            
        
            if line_stripped[i] == "[":
                x += 1
                
            elif line_stripped[i] == "]":
                x -= 1
            if (i != len(line_stripped) and line_stripped[i] == 0): 
                i = len(line_stripped)
            i += 1
        if (x != 0):
            print("False")
        elif(x == 0):
            print("True")