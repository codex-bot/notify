# Notify plugin for CodeX Bot platform

Allows you to send messages to telegram

## Getting started

Add @codex_bot in telegram. You can use link

```
https://t.me/codex_bot
```

Press button start

Type /apps to see a list of available applications

Choose /notify command. This will help you to send messages to chat via POST request

Type /notify_start to get a link for chat

Here it is! You'll get something similar to

```
https://notify.bot.ifmo.su/u/your_token_here
```
## See it works

Run the following command in terminal
```
curl -X POST https://notify.bot.ifmo.su/u/your_token_here -d "message=text"
```

You'll get message "text" in telegram chat

Good luck!
## CodeX Team

https://ifmo.su

team@ifmo.su
