text = "X-DSPAM-Confidence:    0.8475";
#text.find("0")
text = float(text[text.find("0"):len(text)])
print text