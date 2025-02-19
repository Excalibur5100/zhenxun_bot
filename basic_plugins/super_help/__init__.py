from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from utils.message_builder import image
from .data_source import create_help_image, SUPERUSER_HELP_IMAGE


__zx_plugin_name__ = '超级用户帮助 [Superuser]'


if SUPERUSER_HELP_IMAGE.exists():
    SUPERUSER_HELP_IMAGE.unlink()

super_help = on_command(
    "超级用户帮助", rule=to_me(), priority=1, permission=SUPERUSER, block=True
)


@super_help.handle()
async def _():
    if not SUPERUSER_HELP_IMAGE.exists():
        await create_help_image()
    x = image(SUPERUSER_HELP_IMAGE)
    await super_help.finish(x)
