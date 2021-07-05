

monthly_challanges = {
    "january": "long live iron man",
    "february": "earth has wizards now",
    "march": "when did you became expert , last night",
    "april": "i am not iron man",
    "may": "stark you will have my respect",
    "june": "i just wanted to be like you mr stark",
    "july": "he is supposed to be the best among us",
    "august": "i wished someone has told you",
    "september": "you can take all my toys and suits but still i am iron man",
    "october": "smart peoples they know how to cover their asses",
    "november": "I want her",
    "december": "i am iron man"
}

month = "january"

try:
    challange_text = monthly_challanges[month]
    print(challange_text)
except:
    print("not valid month")   