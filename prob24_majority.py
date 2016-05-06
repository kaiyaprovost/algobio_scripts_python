def majority(n,k,array):    
    split = array.split()
    mid = n/2.0
    tempDict = {}
    for i in range(n):
        num = split[i]
        #print num,"num"
        tempDict[num] = tempDict.get(num,0) + 1
        #print tempDict[num],"current count"
        if tempDict[num] > mid:
            return num
        elif i == n-1:
            return -1
            
def main():
    #infile = open("C:/Users/Kaiya/Desktop/scratch_rosalind.txt","rU")
    infile = open("C:/Users/Kaiya/Desktop/rosalind_maj.txt","rU")
    
    kn = infile.readline()
    lines = infile.readlines()

    infile.close()

    knList = kn.split()
    k = int(knList[0])
    n = int(knList[1])

    lines = [i.strip() for i in lines]

    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")
    outfile = open("C:/Users/Kaiya/Desktop/rosalind_maj_ans.txt","w")

    for array in lines:
        print >>outfile, majority(n,k,array),

    outfile.close()

if __name__ == "__main__":
    main()
