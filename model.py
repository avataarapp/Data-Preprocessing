from DataPreprocessor import preprocess
#s="Quite what the producers of this appalling adaptation were trying 5 to do is impossible to fathom.<br /><br />A group of top quality actors, in the main well cast (with a couple of notable exceptions), who give pretty good performances. Penelope Keith is perfect as Aunt Louise and equally good is Joanna Lumley as Diana. All do well with the scripts they were given.<br /><br />So much for the good. The average would include the sets. Nancherrow is nothing like the house described in the book, although bizarrely the house they use for the Dower House looks remarkably like it. It is clear then that the Dower House is far too big. In the later parts, the writers decided to bring the entire story back to the UK, presumably to save money, although with a little imagination I have no doubt they could have recreated Ceylon.<br /><br />Now to the bad. The screenplay. This is such an appallingly bad adaptation is hard to find words to condemn it. Edward does not die in the battle of Britain but survives, blinded. He makes a brief appearance then commits suicide - why?? Loveday has changed from the young woman totally in love with Gus to a sensible farmer's wife who can give up the love her life with barely a tear (less emotional than Brief Encounter). Gus, a man besotted and passionately in love, is prepared to give up his love without complaint. Walter (Mudge in the book) turns from a shallow unfaithful husband to a devoted family man. Jess is made into a psychologically disturbed young woman who won't speak. Aunt Biddy still has a drink problem but now without any justification. The Dower House is occupied by the army for no obvious reason other than a very short scene with Jess who has a fear of armed soldiers. Whilst Miss Mortimer's breasts are utterly delightful, I could not see how their display on several occasions moved the plot forward. The delightfully named Nettlebed becomes the mundane Dobson. The word limit prevents me from continuing the list.<br /><br />There is a sequel (which I lost all interest in watching after this nonsense) and I wonder if the changes were made to create the follow on story. It is difficult to image that Rosamunde Pilcher would have approved this grotesque perversion of her book; presumably she lost her control when the rights were purchased"
#s="My name is N. Udaysimha. I like people who are motivated."
#df = open('D:\Avataar AI\DataSet\Authors\Sample.txt', "r")
#lines = df.readlines()
#df.close()

file1 = open("D:\Avataar AI\DataSet\Authors\Sample.txt","r") 
lines = file1.read()
file1.close()
print(preprocess(lines))
