from discord import HTTPException, NotFound, Message


async def delete(message: Message, **kwargs):
    try:
        await message.delete(**kwargs)
    except HTTPException:
        pass


async def update(message: Message, new_content: str, **kwargs):
    if new_content == message.content:
        return message
    await message.edit(content=new_content, **kwargs)
