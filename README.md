# Webhooks plugin for [@codex_bot](https://ifmo.su/bot) platform

Allows you to send custom messages to Slack or Telegram chat.

## Getting started

Add [@codex_bot](https://t.me/codex_bot) to your chat.

Enter a command `/notify_start` to get a link for current chat.

## Usage

Send a `POST` request to the given url with `message` param.

Set a parse mode if you need to show bold, italic, fixed-width text or inline URLs in the message.

| Field        | Type   | Description                     |
|--------------|--------|---------------------------------|
| `message`    | String | Message text                    |
| `parse_mode` | String | (optional) `HTML` or `Markdown` |

## Example

To see how it works, run the following command in terminal.
```
curl -X POST https://notify.bot.ifmo.su/u/ABCD1234 -d "message=Hello world"
```

You'll get message "Hello world" in telegram chat.

![demo](https://user-images.githubusercontent.com/15448200/29435981-1c1e223e-83b2-11e7-8ee0-a3568b40ed7b.gif "You'll get message Hello world in telegram chat")

Good luck!

## Links

Report a bug on the [create issue page](https://github.com/codex-bot/Webhooks/issues/new).

CodeX Team https://ifmo.su

## License

MIT

Copyright (c) 2017 CodeX Team team@ifmo.su

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
