def timeConversion(s):
    # This condition checks if the last two characters of the input string s are equal to "PM." 
    if s[-2:] == "PM":  
        # This condition checks if the first two characters of the input string (representing the hours) as an integer are less than 12.
        if int(s[0:2]) < 12:   
            # If the above condition is true, it means the time is in the afternoon or evening. To convert it to 24-hour format, it adds 12 to the hour part to get the new hour, 
            #  and then reconstructs the string with the new hour, minutes, and seconds.
            return str(str(int(s[0:2])+12) + ":" + str(s[3:5]) + ":" + str(s[6:8]))  
        else:
            # If the condition in step 2 is not true, it means the time is already in the late afternoon or evening, and it doesn't need any changes. 
            # So, the original input string is returned without modification.
            return str(str(s[0:2]) + ":" + str(s[3:5]) + ":" + str(s[6:8]))
    # This condition checks if the last two characters of the input string 's' are equal to "AM." 
    if s[-2:] == "AM":
        # This condition checks if the first two characters of the input string (representing the hours) as an integer are greater than or equal to 12. 
        if int(s[0:2]) >= 12:
            # If the above condition is true, it means the time is in the morning. To convert it to 24-hour format, it sets the hour part to "00" (midnight) and 
            # keeps the minutes and seconds the same.
            return str("00" + ":" + str(s[3:5]) + ":" + str(s[6:8]))
        else:
            # If the condition in step 6 is not true, it means the time is already in the morning and doesn't need any changes. So, the original input string is returned without modification.
            return str(str(s[0:2]) + ":" + str(s[3:5]) + ":" + str(s[6:8]))
