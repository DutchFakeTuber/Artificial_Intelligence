question_24 = {
    'I was aware of some': None,
    'Yes, I was aware of all of them': None,
    'No, I only became aware later': None,
}

question_25 ={
    'None did': None,
    'Some did': None,
    'Yes, they all did': None
}

question_27 = {
    "I don't know": None ,
    'Yes, always': None ,
    'Sometimes': None ,
    'No' : None
}

question_28 = {
    'Some of my previous employers': None,
    'No, at none of my previous employers': None,
    'Yes, at all of my previous employers': None,
    'Yes, all of my previous supervisors': None,
    'No, none of my previous supervisors': None,
    'Some of my previous supervisors': None
}

question_29 = {
    'Maybe': None,
    'Yes': None,
    'No': None,
}

question_30 = {
    'Somewhat open': None,
    'Neutral': None,
    'Not applicable to me (I do not have a mental illness)': None,
    'Very open': None,
    'Not open at all': None,
    'Somewhat not open': None,
}

question_32 = {
    'Yes': None,
    'Maybe': None,
    'No': None,
    'Possibly': None
}

question_34 = {
    'Yes': None,
    'No': None
}

question_35 = {
    'Not applicable to me': None,
    'Rarely': None,
    'Sometimes': None,
    'Never': None,
    'Often': None
}

question_39 = {
    'Sometimes, if it comes up': None,
    "No, because it doesn't matter": None,
    'No, because it would impact me negatively': None,
    'Yes, always': None,
}

question_41 = {
    'Yes': None,
    'Not applicable to me': None,
    'No': None,
    'Unsure': None
}

question_42 = {
    '1-25%': None,
    '76-100%': None,
    '26-50%': None,
    '51-75%': None
}

question_43 = {
    'No': None,
    'Maybe/Not sure': None,
    'Yes, I experienced': None,
    'Yes, I observed': None,
    'Ive always been self-employed': None
}

question_44 = {
    'Same level of comfort for each': None,
    'Physical health': None,
    'Mental health': None
}

question_53 = {
    'No change': None,
    "I'm not sure": None,
    'Negatively': None,
    'Positively': None
}

question_94 = {
    "Don't know": None, 
    'No': None,
    'Yes': None
}

question_99 = {
    'Some of them': None,
    'No': None,
    'Yes': None,
}

question_110 = {
    'Some of my previous employers': None,
    'No, at none of my previous employers': None,
    'Yes, at all of my previous employers': None,
}

question_113 = {
    'Maybe': None,
    "No, I don't think it would": None,
    'Yes, I think it would': None,
    'No, it has not': None,
    'Yes, it has': None,
}

question_114 = {
    "No, I don't think they would": None,
    'Maybe': None,
    'Yes, they do': None,
    'Yes, I think they would': None,
    'No, they do not': None,
}

question_118 = {
    'Sometimes': None,
    'Never': None,
    'Always': None,
}

totalValue = str()
for x in range(105):
    value = ('Question %d, ' %x)
    totalValue = totalValue + value

print(totalValue)

#1:  6 - Do you have a family history of mental illness?
#2:  7 - Have you ever sought treatment for a mental health disorder from a mental health professional?
#3:  21 - Do you know local or online resources to seek help for a mental health issue?
#4:  24 - Are you aware of the options for mental health care provided by your current employer?
#5:  25 - Did your employer ever formally discuss mental health (as part of a wellness campaign or other official communication)?
#6:  26 - Did your employer provide resources to learn more about mental health disorders and how to seek help? 
#7:  27 - Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources with your employer?
#8:  32 - Have you had a mental health disorder in the past?
#9:  33 - Do you currently have a mental health disorder?
#10: 57 - Did you ever discuss your mental health with your current employer?
#11: 59 - Did you ever discuss your mental health with a current coworker(s)?
#12: 99 - Did you hear of/or observe negative consequences for co-workers with mental health issues in your current workplace?