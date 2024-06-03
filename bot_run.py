from YunHu_bot.YHChatClientSDK import YHChat_run
from YunHu_bot.tools import logger
logger.debug("bot正在启动")

# 导入插件
logger.debug("加载插件")
from YunHu_bot.plugins import print_message

# 启动
YHChat_run.run()

logger.info("bot启动完成")
