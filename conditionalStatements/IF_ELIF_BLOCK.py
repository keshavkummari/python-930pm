#!/usr/bin/python
perl=50
python=80

if (perl>python):               # False
    print ("Perl Course fee is more than python fee")
elif (perl==python):            # False
    print (perl, "course fee is equal to", python ,"fee")
elif (perl<python):              # True
    print (perl, "Less than", python ,"fee")
elif (perl!=python):
    print ("Perl course fee is not less than python fee")
else:
    print ("None of the above are matched")
    
print ("We are out of the if..elif block")    
    
