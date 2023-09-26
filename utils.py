import re
import math

def remove_non_alphanumeric(s):
    alphanumericS = re.sub(r'[^a-zA-Z0-9]', '', s)
    return alphanumericS

def count_points(data):
    point = 0

    # One point for every alphanumeric character in the retailer name.
    point += len(remove_non_alphanumeric(data.get('retailer')))

    # 50 points if the total is a round dollar amount with no cents.
    total = float(data.get('total'))
    if total * 100 % 100 == 0:
        point += 50

    # 25 points if the total is a multiple of 0.25.    
    if total * 4 % 1 == 0:
        point += 25

    # 5 points for every two items on the receipt.
    point += len(data.get('items')) // 2 * 5

    # If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in data.get('items'):
        if len(item.get('shortDescription').strip()) % 3 == 0:
            point += math.ceil(float(item.get('price')) * 0.2)

    # 6 points if the day in the purchase date is odd.
    date = data.get('purchaseDate').split('-')[-1]
    if int(date) % 2 == 1:
        point += 6
    
    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    hour = data.get('purchaseTime').split(':')[0]
    if 14 <= int(hour) < 16:
        point += 10
    
    return point