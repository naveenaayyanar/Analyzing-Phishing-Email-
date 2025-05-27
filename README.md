🛡️ Phishing Email Analysis - Task 2 Report

🎯 Introduction
This report presents an analysis of three suspicious email samples that exhibit common phishing characteristics. Each email was reviewed for spoofed sender identities, misleading URLs, suspicious attachments, and manipulative language. The objective is to improve phishing detection awareness and analytical skills.

 📧 Email Overview

📌 Email 1: PayPal Account Alert
- **Spoofed Sender**: `support@paypa1.com` (note the number '1' replacing 'l')
- **Fake URL**: `https://paypal.secure-login-help.com`
- **Urgency**: Threat of account suspension in 24 hours
- **Social Engineering**: Attempts to panic user
- **Generic Greeting**: "Dear Customer"

📌 Email 2: Fake Microsoft HR Offer
- **Spoofed Sender**: `careers@microsofft-jobs.com` (typo in "Microsoft")
- **Suspicious Attachment**: `.docm` file (macro-enabled and risky)
- **Social Engineering**: Too-good-to-be-true job offer
- **Requests Sensitive Info**: Asks for personal details

 📌 Email 3: Chase Bank Fraud Alert
- **Spoofed Domain**: `alerts@secure-chaseonline.com`
- **Fake URL**: `https://chase.verify-secure.com/login`
- **Urgency & Threats**: Claims your account will be suspended
- **Generic Greeting**: Not personalized

---

 🚩 Indicators of Phishing Found

| Indicator                 | Email 1 | Email 2 | Email 3 |
|--------------------------|---------|---------|---------|
| Spoofed Email Address    | ✅      | ✅      | ✅      |
| Mismatched/Fake Link     | ✅      | ❌      | ✅      |
| Suspicious Attachment    | ❌      | ✅      | ❌      |
| Urgent Language          | ✅      | ✅      | ✅      |
| Generic Greeting         | ✅      | ✅      | ✅      |
| Social Engineering Tactics | ✅    | ✅      | ✅      |
| Grammar or Typos         | Minor   | Minor   | Minor   |


🧪 Tools Used

- 🔍 **Google Header Analyzer** – https://toolbox.googleapps.com/apps/messageheader/
- 🔗 **Link Hover Preview** – To identify actual vs shown URLs
- ✍️ **Manual Review** – Checked for tone, grammar, branding, and urgency
- 🛑 **Attachment Safety Check** – `.docm` flagged as malicious


 🧠 Conclusion

All three email samples exhibit classic phishing techniques including spoofed domains, urgent language, and manipulative content. Recognizing these traits helps reduce risk and protect users from credential theft or malware infections. Users should always verify suspicious messages and never click unverified links or download unexpected attachments.



 📂 Repository Contents

- `sample_email_1.txt` – PayPal phishing email
- `sample_email_2.txt` – Fake Microsoft HR offer
- `sample_email_3.txt` – Chase bank phishing alert
- `README.md` – Full phishing analysis report

---

## 📤 Submission Instructions

1. Upload all files to a GitHub repo titled: `cybersecurity-task2-phishing-analysis`
2. Paste your repo link into this form:  
   🔗 [Task Submission Form](https://forms.gle/8Gm83s53KbyXs3Ne9)
