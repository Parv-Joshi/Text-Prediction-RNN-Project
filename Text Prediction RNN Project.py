str = ""
print("Input sample text in one sentence at a time\nDo NOT use any puntuation\nLeave the field blank to stop entering sample text")
while True:
    inp = input("Enter a sentence here: ")
    if inp == "":
        break
    else:
        str += inp

if str == "":
    s = ""
else:
    s = str.split()
    
print("Now let us try out our text predictor\nRemember NOT use any puntuation\nLeave the field blank to stop predicting")
while True:
    print("Input one word at a time to see predictions:")
    inp_ = input("Enter a word here: ")
    if inp_ == "":
        break
    else:
        s.append(inp_)
        if inp_ in s:
            i = -1
            print("\nPrediction words:\n")
            for word in s:
                i+=1
                if inp_.lower() == word.lower():
                    try:
                        print(s[i+1],"\n")
                    except:
                        pass
        else:
            print("-No Predictions-")
                
                
                
                
                
