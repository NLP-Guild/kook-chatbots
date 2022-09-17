from khl import  Message

def print_msg_info(msg:Message):
    print(msg)
    print(msg.author)
    print(msg.author.id)
    print(f'''
        gate: {msg.author.gate}
        nickname: {msg.author.nickname}
        username: {msg.author.username}
        status: {msg.author.status}
        channel: {msg.ctx.channel}
        ''')
    # await msg.author.send('nihao')
    roles = await msg.ctx.guild.fetch_roles()

    print(roles)
    for role in roles:
        print(f'''
            id: {role.id}
            name: {role.name}
            color: {role.color}
            position: {role.position}
            ''')
