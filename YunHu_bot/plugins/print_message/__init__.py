from YunHu_bot.YHChatClientSDK.Event import Event
from YunHu_bot.YHChatClientSDK import YHChat_recv
from YunHu_bot.YHChatClientSDK.Message import MessageSegment


@YHChat_recv.on_message
async def _(event: Event):
    # logger.info("plugin_message")
    # logger.info(event.message)
    msg = MessageSegment.text("Hello, World!")
    # await send_message(recv_type=event.chat_type, recv_id=event.chat_id, message=msg)


@YHChat_recv.on_event
async def _(event: Event):
    # logger.info("plugin_event")
    # logger.info(event)
    pass

