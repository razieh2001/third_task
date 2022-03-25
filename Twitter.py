from SocialMedia import SocialMedia 
twittList=[]

class Twitter(SocialMedia):
    def __init__(self) :
        super(SocialMedia,self).__init__()
    
    def createNewTwitt(body):
        Twitt=str(input("write your twitt :\n"))
        lenOfTwitt = int(len(Twitt))

        if lenOfTwitt < 280 :
            twittList.append(twittList)
            print("the Twitt added to twitt list succussfully")

        else:
            print("the length of characters is unacceptable")

    def getTwitt(self):
        return twittList

        