import win32com.client
import os
import datetime

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
dh_folder = inbox.Folders("DH")
save_folder = "C:/Users/zhall3/OneDrive - FEMA/Desktop/DH Dashboard/DH02" 
target_subject = "DH02"

target_email = None
for item in dh_folder.Items:
    if item.Subject.find(target_subject) != -1:
        if target_email is None or item.CreationTime > target_email.CreationTime:
            target_email = item

if target_email is not None:
    for attachment in target_email.Attachments:
        if attachment.FileName.endswith(".xlsx"):
            attachment.SaveAsFile(os.path.join(save_folder, "DH02.xlsx"))
            print("File saved to {0}.".format(save_folder))
else:
    print("No matching email found.")

