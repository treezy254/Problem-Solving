def timeInWords(h, m):
    # Write your code here
    # hour = hour
    # 00 = oclock
    # 01 - 30 = past
    # 31 - 59 = to 
    # 15 = quater past
    # 45 = quater to
    # 30 = half past 
    
    nums = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}
    dope = ""
    
    if m == 00:
        dope = dope + nums[h] + " o' clock"
    elif m == 1:
        dope += "one minute past " + nums[h]
    elif m < 15:
        dope += nums[m] + " minutes past " + nums[h]
    elif m == 15:
        dope += "quarter past " + nums[h]
    elif  m < 21:
        dope += nums[m] + " minutes past " + nums[h]
    elif m < 30:
        dope += "twenty " + nums[m%10] + " minutes past " + nums[h]
    elif m == 30:
        dope += "half past " + nums[h]
    elif m < 40:
        dope += "twenty " + nums[(60-m)%10] + " minutes to " + nums[h+1]
    elif m < 45:
        dope += nums[60-m] + " minutes to " + nums[h+1]
    elif m == 45:
        dope += "quarter to " + nums[h+1]
    elif m > 40 and m < 59:
        dope += nums[60-m] + " minutes to " + nums[h + 1]
    elif m == 59:
        dope += "one minute to" + nums[h+1]
    
    return dope
    