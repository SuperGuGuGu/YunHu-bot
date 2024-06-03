from YunHu_bot.config import config_
import loguru
log_style = config_("bot", "log_style")
log_level = config_("bot", "log_level")


if log_style == "loguru":
    from loguru import logger as logger
    import sys
    logger.remove()
    handler_id = logger.add(sys.stderr, level=log_level)

elif log_style == "nonebot":
    from nonebot import logger as logger

    def _log_patcher(record: "loguru.Record"):
        module_name = record["name"]
        record["name"] = module_name and module_name.split(".")[-1]
    logger.configure(extra={"nonebot_log_level": log_level}, patcher=_log_patcher)

else:
    from loguru import logger as logger
    import sys
    logger.remove()
    handler_id = logger.add(sys.stderr, level=log_level)
    logger.warning("配置项：bot/log_style错误，已加载默认配置‘loguru’")


