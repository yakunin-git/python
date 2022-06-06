# Certificate date tracking

## History

Small telegram bot, I used to use it for zabbix before the latter started supporting it natively. But also, I often use it as a library for other projects.

In order to start using the bot, you need to register your bot with the father of bots in telegram. You will get your bot id and use it in the script.

## Getting started

You can read about how to register your bot here: https://core.telegram.org/bots

After registering a bot, you need to create a chat and add the bot to the chat. Next, you need to write any message in the chat and go to the link: https://api.telegram.org/bot<YourBOTToken>/getUpdates
```
Out:

{"update_id":8393,"message":{"message_id":3,"from":{"id":7474,"first_name":"AAA"},
"chat":{"id":<group_ID>,"title":""},
"date":25497,"new_chat_participant":{"id":71,"first_name":"NAME","username":"YOUR_BOT_NAME"}}}
```

Now that you have the bot id, chat id, and token, you can put them into the script and try it out.

```
Out:

# tg.py "Test message"
```
