def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
        
    return secret_codes
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))

######### log_analyzer.py
def log_analyzer(server_logs):
    flagged_activities = []
    
    for log in server_logs:
        # Splitting each log line into individual words
        words = log.split()
        
        # In real-world scenarios, logs follow a specific format:
        # [Date] [Time] [IP_Address] [Status] [Message]
        # We know that IP is at index 2 and Status is at index 3.
        
        if len(words) > 3:
            ip_address = words[2]
            status = words[3]
            
            # If the status is "FAILED", "404", or "CRITICAL", flag it
            if status in ["FAILED", "404", "CRITICAL"]:
                flagged_activities.append(f"Alert: Threat detected from IP {ip_address} | Status: {status}")
                
    return flagged_activities

# Sample real-world server logs
raw_logs = [
    "2026-07-01 10:00:00 192.168.1.50 SUCCESS User_Logged_In",
    "2026-07-01 10:02:15 10.0.0.12 FAILED Password_Incorrect",
    "2026-07-01 10:05:00 192.168.1.99 SUCCESS Page_Loaded",
    "2026-07-01 10:06:45 172.16.254.1 CRITICAL Unauthorized_Access_Attempt"
]

# Running the function
alerts = log_analyzer(raw_logs)

# Printing the results
for alert in alerts:
    print(alert)
        
