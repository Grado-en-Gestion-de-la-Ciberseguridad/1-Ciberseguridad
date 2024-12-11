---
title: "Advent of Cyber 2024"
source: "https://tryhackme.com/r/room/adventofcyber2024"
tags:
  - "clippings"
---
Once the machine is up and running, we can connect to the Elastic SIEM by visiting [https://10-101-77-13.p.thmlabs.com](https://10-101-77-13.p.thmlabs.com/) in your browser using the following credentials:

![TryHackMe Credentials](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/0cbfa0d0f3a7f16cefa9fddd04b6de8d.png)

| **URL** | https://10-101-77-13.p.thmlabs.com |
| --- | --- |
| **Username** | elastic |
| **Password** | elastic |

Once we log in, we can click the menu in the top-left corner and go to the `Discover` tab to see the events. 

![Instructions to access the Discover console.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730130654839.png)  

According to the alert sent by the Mayor's office, the activity occurred on Dec 1st, 2024, between 0900 and 0930. We can set this as our time window by clicking the timeframe settings in the upper-right corner. Note that we need to click the **Absolute** tab and set the exact timeframe we want to view. Lastly, click the **Update** button to apply the changes.

![Instructions to configure the search timeframe.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730130936812.png)  

After updating the settings, we see 21 events in the mentioned timeframe.

![Initial query results from the given timeframe.](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1728231315005.png)  

In their current form, these events don't look very easily readable. We can use the fields in the left pane to add columns to the results and make them more readable. Hovering on the field name in the left pane will allow adding that field as a column, as shown below.

![Instructions to add fields as table columns.](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1728121458086.png)

Since we are looking for events related to PowerShell, we would like to know the following details about the logs.

- The hostname where the command was run. We can use the `host.hostname` field as a column for that.
- The user who performed the activity. We can add the `user.name` field as a column for this information.
- We will add the `event.category` field to ensure we are looking at the correct event category.
- To know the actual commands run using PowerShell, we can add the `process.command_line` field.
- Finally, to know if the activity succeeded, we will add the `event.outcome` field.

Once we have added these fields as columns, we will see the results in a format like this.

![View after adding the field columns.](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1728231315014.png)  

Interesting! So, it looks like someone ran the same encoded PowerShell command on multiple machines. Another thing to note here is that before each execution of the PowerShell command, we see an authentication event, which was successful.

![Authentication and PowerShell execution pattern.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730132203152.png)  

![It seems like Glitch is involved.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730369342463.png)This activity is observed individually on each machine, and the time difference between the login and PowerShell commands looks very precise. Best practices dictate that named accounts are used for any kind of administrator activity so that there is accountability and attribution for each administrative activity performed. The usage of a generic admin account here also seems suspicious. On asking, the analysts informed us that this account is used by two administrators who were not in the office when this activity occurred. Hmmm, something is definitely not right. Are these some of Glitch's shenanigans? Is Christmas in danger? We need to find out who ran these commands.

Let's also add the `source.ip` field as a column to find out who ran the PowerShell commands.

![Adding source.ip field column to the current view.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730132260949.png)  

Since the `source.ip` field is only available for the authentication events, we can filter out the process events to see if there is a pattern.  To do that, we can hover over the `event.category` field in one of the process events. We will see the option to filter only for this value (+ sign) or filter out the value (- sign), as seen below. Let's filter for authentication events by clicking the plus (+) sign beside it to show only those in the results.

![Filtering using the plus button.](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1728123886843.png)

As a result, you can see that the output only renders the authentication events. Since the result does not give useful insights, let's remove it for now. You can do this by clicking the `x` beside the filter.

![Removing the filter using the x button.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730133793388.png)  

Since the timeframe we previously used was for the PowerShell events, and the authentication events might have been coming from before that, we will need to expand the search to understand the context and the historical events for this user. Let's see if we have any events from the user from the 29th of November to the 1st of December. Updating the time filter for these days, the results look like this.

**Note: Remember to remove the `event.category` filter before this step.**

![Adjusting the timeframe to November 29 to December 1.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730133980599.png)  

Woah, there have been more than 6800 events in these three days, and we see a spike at the end of the logs. However, even though we used the time filter for the day end on the 1st of December, we see no events after successful PowerShell execution. There have also been a lot more authentication events in the previous days than on the 1st of December.

To understand the events further, let's filter for our `user.name` with `service_admin` and `source.ip` with `10.0.11.11` to narrow our search.

![Applied source IP and username filters.](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1728233609356.png)  

Uh-oh! It looks like all these events have been coming from the same user and the same IP address. We definitely need to investigate further. This also does not explain the spike. Let's filter for authentication events first by clicking the plus (+) button beside it.

![Filtering authentication events using the plus button.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730134648151.png)  

Moreover, let's filter out the Source IP here to see if we can find the IP address that caused the spike. This can be done by clicking the minus (-) button beside it.

![Filtering out the source IP using the minus button.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730134648084.png)  

After applying the filters, the expected result will be similar to the image below.

![Updated results based on the new filters.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730134858251.png)  

Scrolling down, we see many events for failed logins. We also see that the IP address for the spike (ending in **.255.1**) differs from the one we saw for the events continuously coming in the previous days (10.0.11.11). The analysts have previously investigated this and found that a script with expired credentials was causing this issue. However, that script was updated with a fresh set of credentials. Anyhow, this might just be another script. Let's find out.

Let's remove the `source IP` filter so we can focus on authentication events close to the spike. After applying the new filter, we see that the failed logins stopped a little while after the successful login from the new IP.

![Authentication patterns close to the spike.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730135308423.png)  

Our suspicions are rising. It seems that someone tried a brute-force attack on December 1st, as shown by the same filters applied above.

![Indicators of brute-forcing attempts.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730135585773.png)  

The results also showed that they succeeded with the brute-force attempt because of the successful authentication attempt and quickly ran some PowerShell commands on the affected machines. Once the PowerShell commands were run, we didn't see any further login attempts. This looks like a TP, and there needs to be an escalation so that McSkidy can help us respond to this incident.

## Christmas in Danger?

The alarms have gone off, and McSkidy has been called to help take this incident further. The analysts have briefed McSkidy about the incident. McSkidy observed that nobody had actually looked at what the PowerShell command contained. Since the command was encoded, it needs to be decoded. McSkidy changed the filters with `event.category: process` to take a deeper look at the PowerShell commands.

![New filter applied to view PowerShell commands.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730135920764.png)  

We can see the PowerShell command in the `process.command_line` field. 

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -EncodedCommand SQBuAHMAdABhAGwAbAAtAFcAaQBuAGQAbwB3AHMAVQBwAGQAYQB0AGUAIAAtAEEAYwBjAGUAcAB0AEEAbABsACAALQBBAHUAdABvAFIAZQBiAG8AbwB0AA==`

McSkidy knows that Encoded PowerShell commands are generally Base64 Encoded and can be decoded using tools such as [CyberChef](https://gchq.github.io/CyberChef/). Since the command might contain some sensitive information and, therefore, must not be submitted on a public portal, McSkidy spins up her own instance of CyberChef hosted locally. McSkidy started by pasting the encoded part of the command in the Input pane in CyberChef. 

![Using CyberChef to decode the PowerShell command.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730131256096.png)  

Since it is a Base64 encoded command, McSkidy used two recipes, named `FromBase64` and `Decode text` from the left pane. Note that McSkidy configured the **Decode text** to **UTF-16LE (1200)** since it is the encoding used by PowerShell for Base64.

![Applying recipes to decode the PowerShell command.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730131884795.png)  

The result provided a sigh of relief to McSkidy, who had feared that the Christmas had been ruined. Someone had come in to help McSkidy and the team secure their defences, but who?

## Villain or Hero?

McSkidy further analysed the secret hero and came to a startling revelation. The credentials for the script in the machines that ran the Windows updates were outdated. Someone brute-forced the systems and fixed the credentials after successfully logging in. This was evident from the fact that each executed PowerShell command was preceded by a successful login from the same Source IP, causing failed logins over the past few days. And what's even more startling? It was Glitch who accessed **ADM-01** and fixed the credentials after McSkidy confirmed who owned the IP address.

![Evidence that Glitch fixed the recurring issue.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/5dbea226085ab6182a2ee0f7-1730136203704.png)  

This meant that the people of Wareville had misunderstood Glitch, who was just trying to help shore up the defences. But if Glitch was the one helping the defences, who was trying to sabotage it? Was it the Mayor who informed the SOC about these 'suspicious' PowerShell commands? Just like alerts aren't always what they seem in a SOC, so was the case here at Wareville with people. As hard as it was to differentiate between a TP and an FP, so was the case with the Mayor and Glitch. However, McSkidy can perhaps use the evidence-based deduction skills learned in a SOC to make this difference easier for the people of Wareville.