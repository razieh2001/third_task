from SocialMedia import SocialMedia
postList =[]
class Instagram(SocialMedia):
    def __init__(self) :
        super(SocialMedia,self).__init__()


    def publishNewPost(body):
        postCaption=str(input("write your post caption :\n"))
        lenOfPost = int(len(postCaption))

        if lenOfPost < 2200 :
            postList.append(postCaption)
            print("the post added to post list succussfully")

        else:
            print("the length of characters is unacceptable")

    def getPost(self):
      return postList
#print(postList)