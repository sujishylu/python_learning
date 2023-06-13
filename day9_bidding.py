# to create a bidding
bidders = {}
conti = 'Y'
while conti == "Y":
    name= input("enter your name = ")
    amnt = input( "enter your amnt =")
    bidders[name]=amnt
    conti = input(" do you want to contY/N?")
print (bidders)
max_bidder = max(bidders, key=bidders.get)
max_bid = bidders[max_bidder]

print("The highest bidder is", max_bidder, "with a bid of", max_bid)
