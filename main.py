# This is a simple service chatbot program

print("Greetings!, I am Zoe. Your virtual assistant!")
print("I am here to assist you with all your enquiries, to begin, may I start by knowing your name please?")

# This line request the name input from the user
name = input()

# This line allows the user to input their name
print("Hi", name, ', Nice to meet you!')

# This line checks how the user is doing
print("How are you doing today?:", name)
reason = input()
print("Everything happens for reason but don't forget to smile and stay positive!", name)

#Service Conversation
print("So, how may I help you today?", name)
need = input()
print("Ahh okay, Have you looked around on our website?")
question = "What sorts of material and colour would you fancy?"
howoften = input(question)
print("Okay, thank you for the information")

#Offer Conversation
products = input("We have a large range of products to suit your needs, look through our list of products, see if you like anything")
if products == "No":
    print("No product to offer")
    exit()
    products = ["Socks, Blazers, Glasses, Shoes, Jackets, Bags, Hats, Scarfs, Blouzers, Vests, Lingeries"]
    print("I have a list of products to offer")
    print(products)
    offer = input("What would you like ")
print("Let's start with your sizes")
topsize = input("What size do you wear on top?")
bottomsize = input("What size do you wear on the bottom?")

# End of conversation
print("Is there anything else I can help you with?")
reply = input()
print("It has been a pleasure serving you", name)
print("Have a good day and do not hesitate to come back again if you need anything")
print("Take care and look after yourself!", name)





