from khl import Bot, Message,EventTypes, Event
from pprint import pprint
# init bot
# 小新
bot = Bot(token='1/MTA0NjM=/knqsAvLfRTAgxmz7tSYmnA==')






# register command
# invoke this via saying `!hello` in channel
@bot.command(name='hello')
async def roll(msg: Message):
    await msg.reply('world!')
    print(msg)
    print(msg.author)
    print(msg.author.id)
    print(f'''
    roles: {msg.author.roles}
    nickname: {msg.author.nickname}
    username: {msg.author.username}
    status: {msg.author.status}
    channel: {msg.ctx.channel}
    ''')
    # await msg.author.send('nihao')
    await bot.send(msg.ctx.channel,content='This is a text content.')
    roles = await msg.ctx.guild.fetch_roles()

    print(roles)
    for role in roles:
        print(f'''
        id: {role.id}
        name: {role.name}
        color: {role.color}
        position: {role.position}
        ''')



def prn_obj(obj):
  print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]) )


'''
[#128587;] 小学
[#128583;] 中学
[#129489;]‍[#127891;] 大学
[#129489;]‍[#128187;] 社畜
'''


@bot.on_event(EventTypes.ADDED_REACTION)
async def grantRoles(b: Bot, event: Event):
    await b.fetch_me(True)
    MSGS = ['9169a4db-fdc3-4c5d-855b-0db188cd0117','5ff54957-500c-4617-a841-9543c81c41b6']
    msgId = event.extra['body']['msg_id']
    emojiID = event.extra['body']['emoji']['id']
    userID = event.extra['body']['user_id']
    guild = await b.fetch_guild('7578113303774016')

    # 学历身份组
    if msgId == MSGS[0]:
        if emojiID == '''[#128587;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215135')
            print('done')

        if emojiID == '''[#128583;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215159')
            print('done')

        if emojiID == '''[#129489;]‍[#127891;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215166')
            print('done')

        if emojiID == '''[#129489;]‍[#128187;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215173')
            print('done')

    # 学科身份组
    '''
    [#128187;] CS
    [#128200;] math
    [#127777;] science
    [#127490;] language
    '''
    if msgId == MSGS[1]:
        if emojiID == '''[#128187;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215678')
            print('done')

        if emojiID == '''[#128200;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215694')
            print('done')

        if emojiID == '''[#127777;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215701')
            print('done')

        if emojiID == '''[#127490;]''':
            await guild.grant_role(await guild.fetch_user(userID),'1215702')
            print('done')

    else:
        print('Not specified message.')


@bot.on_event(EventTypes.DELETED_REACTION)
async def rovokeRoles(b: Bot, event: Event):
    await b.fetch_me(True)
    MSGS = ['9169a4db-fdc3-4c5d-855b-0db188cd0117','5ff54957-500c-4617-a841-9543c81c41b6']
    msgId = event.extra['body']['msg_id']
    emojiID = event.extra['body']['emoji']['id']
    userID = event.extra['body']['user_id']
    guild = await b.fetch_guild('7578113303774016')

    # 学历身份组
    if msgId == MSGS[0]:
        if emojiID == '''[#128587;]''':
            await guild.revoke_role(await guild.fetch_user(userID), '1215135')
            print('done')

        if emojiID == '''[#128583;]''':
            await guild.revoke_role(await guild.fetch_user(userID), '1215159')
            print('done')

        if emojiID == '''[#129489;]‍[#127891;]''':
            await guild.revoke_role(await guild.fetch_user(userID), '1215166')
            print('done')

        if emojiID == '''[#129489;]‍[#128187;]''':
            await guild.revoke_role(await guild.fetch_user(userID), '1215173')
            print('done')

    # 学科身份组
    '''
        [#128187;] CS
        [#128200;] math
        [#127777;] science
        [#127490;] language
    '''
    if msgId == MSGS[1]:
            if emojiID == '''[#128187;]''':
                await guild.revoke_role(await guild.fetch_user(userID), '1215678')
                print('done')

            if emojiID == '''[#128200;]''':
                await guild.revoke_role(await guild.fetch_user(userID), '1215694')
                print('done')

            if emojiID == '''[#127777;]''':
                await guild.revoke_role(await guild.fetch_user(userID), '1215701')
                print('done')

            if emojiID == '''[#127490;]''':
                await guild.revoke_role(await guild.fetch_user(userID), '1215702')
                print('done')


    else:
        print('Not specified message.')


# everything done, go ahead now!
bot.run()