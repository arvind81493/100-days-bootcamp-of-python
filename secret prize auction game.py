logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\'''
                      
print(logo)                      
print("WELCOME TO THE SECRET AUCTION PROGRAM")
bids={}
bidding_finished=False

def highest_bidder(bidder_record):
    highest_bid=0
    winner=""
    for bidder in bidder_record:
        bid_amount=bidder_record[bidder]
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner=bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")

while not bidding_finished:
    name=input("what is your name?: ")
    price=int(input("what is your bid price$ : "))
    bids[name]=price
    should_continue=input("are there any bidders 'type=yes' or 'no':")
    if should_continue=="no":
        bidding_finished=True
        highest_bidder(bids)

    elif should_continue=="yes":
        bidding_finished=False
print(bids)