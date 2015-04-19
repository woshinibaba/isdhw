for i in range(1,10):
    s=""
    t=""
    if(i==2):t="      "
    elif(i==3):t="            "
    if(i==4):t="                  "
    elif(i==5):t="                        "
    if(i==6):t="                              "
    elif(i==7):t="                                    "
    if(i==8):t="                                          "
    elif(i==9):t="                                                "
    for j in range(i,10):
        s+=str.format("{0:1}*{1:1}={2:<2}",i,j,i*j)
      
    t+=s        
    print(t)
  
   

  

