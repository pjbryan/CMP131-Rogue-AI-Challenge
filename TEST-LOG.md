# Rogue AI Test Log

## Team Information

- Team name: N/A
- Team members: Ang, Ayden, PJ
- Driver: PJ
- Logic Checker: Ang
- Test Engineer:Ayden
- Reporter:N/a

## Required Boundary Predictions

Complete these predictions before running the program.

| Test | Temperature | Battery | Security | Predicted messages | Actual messages | Match? |
|---|---:|---:|---|---|---|---|
| A | 99 | 19 | safe | safe |System temperature is safe   |yes  |
| B | 100 | 20 | danger | danger |LOW Power  | yes |
| C | 101 | 21 | DANGER | DANGER | DANGER |yes  |

## AI-Assisted Tests

Ask the course AI assistant for one test at a time. Predict before running.

| Test | Temperature | Battery | Security | Team prediction | Actual result | What we learned |
|---|---:|---:|---|---|---|---|
| 1 |102|88|DANGER|its going to shut down|shut down required|all bad means shutdown
| 2 | 80|21|Safe|its fine|SAFE| all goodmeans safe
| 3 | 101 |19|danger|short safe| shutdown required| half and half is safe but keep an eye on it 

## Random AI Safety Scenario

- Random temperature: 102- overheatting
- Random battery:80- Power normal
- Random security status: Safe- system secured
- Copilot's simulated program results: Yes
- Did the logic pass this scenario? Yes
- Temperature safety advice: Stay off phone for a bit. 
- Power safety advice: Enter charger plug. 
- Privacy/security advice: Shutdown required 
- Funny scenario message:
- What we learned: How to insert multiple messages with different names to adjust 1 subject. 

## Instructor Mystery Test

- Temperature:100
- Battery:20
- Security: danger
- Our prediction: High temperature warning, insert battery, and shut down
- Actual result: It outputted all comands 
- Did it match? Explain: Yes, it followed the print comands for the specific levels that were needed. 

## Debugging Record

- What did not work or almost caused a problem? Our if else statements gave us a little bit of trouble
- What hint did the instructor or AI assistant provide? It ran all the programs 
- What change did the team make? If anything came out incorrect we checked and fixed
- Why did that change work? It worked because everything was right at the end and there was no error message at the end. 
