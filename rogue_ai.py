# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members: Ang, Ayden, PJ
# ============================================================
print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.

temperature = int(input("Enter AI system Temperature: "))

if temperature >= 100:
    print ("WARNING: System temperature is too high! Initiating emergency shutdown.")
else:  
    print ("System temperature is safe ")

# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.

batteryPercentage = int(input("Enter Battery Percentage: "))

if batteryPercentage >= 21:
  print ("Power Normal")
if batteryPercentage <= 20:
    print ("LOW POWER")
else:
    print ("Your in danger power is low.")


# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.

securityStatus = input("Enter Security Status: ")

if securityStatus == "danger" or securityStatus == "DANGER":
    print ("WARNING: SHUTDOWN REQUIRED.")
else:
    print("System Secure")
    
print ("========================================")
print ("Diagnostic complete.")
print ("========================================")
