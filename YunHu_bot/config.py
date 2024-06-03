import os
import toml


config_data = None

# 配置默认设置
default_config = {
    "bot": {
        "yunhu_token": None,
        "host": "0.0.0.0",
        "port": 8080,
        "request_path": "/",
        "cilent_url": "https://chat-go.jwzhd.com/open-apis/v1/bot",
        "log_style": "loguru",
        "log_level": "INFO",
    }
}


def config_(config_group: str = None, config_name: str = None):
    """
    获取配置
    :param config_group: 获取的配置名称
    :param config_name:
    :return: 配置内容
    """
    global config_data
    path = f"{os.path.abspath('.')}/config.toml"

    def save_config():
        global config_data
        with open(path, 'w') as config_file:
            toml.dump(config, config_file)
        config_data = config

    if config_data is None:
        if not os.path.exists(path):
            config = default_config
            save_config()
            print("--未存在配置文件，正在创建--")
        config = config_data = toml.load(path)
    else:
        config = config_data

    # 如果存在设置，则直接回复
    if config_group in list(config) and config_name in list(config[config_group]):
        return config[config_group][config_name]

    # 保存默认设置
    if config_group in list(default_config) and config_name in list(default_config[config_group]):
        if config_group in list(config):
            if config_name not in list(config[config_group]):
                config[config_group][config_name] = default_config[config_group][config_name]
                save_config()
        elif config_group in list(default_config):
            config[config_group] = default_config[config_group]
            save_config()

    # 如果存在设置，则直接回复
    if config_group in list(config) and config_name in list(config[config_group]):
        return config[config_group][config_name]

    return None



