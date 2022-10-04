from telethon import events, Button
from asyncio import exceptions
from .. import jdbot, chat_id, SCRIPTS_DIR, CONFIG_DIR, logger
from .utils import press_event, backup_file, add_cron, cmd, DIY_DIR, TASK_CMD, V4


@jdbot.on(events.NewMessage(from_users=chat_id))
async def bot_get_file(event):
    """定义文件操作"""
    try:
        v4btn = [
            [
                Button.inline('放入own', data=f'/jd/own'),
                Button.inline('放入own并运行', data='node'),
            ],
            [
                Button.inline('放入raw', data=f'/jd/own/raw'),
                Button.inline('放入raw并运行', data='node2'),
            ],
            [
                Button.inline('放入zy', data=f'{SCRIPTS_DIR}/zy'),
                Button.inline('放入zy并运行', data='nodezy'),
            ],
            [
                Button.inline('放入AutoRun', data=f'{SCRIPTS_DIR}/AutoDownload'),
                Button.inline('放入AutoRun并运行', data='nodeAutoRun'),
            ],
            [
                Button.inline('放入diy', data=f'/jd/jbot/diy'),
                Button.inline('放入diy并运行', data='nodeuser'),
            ],
            [
                Button.inline('放入scripts', data=SCRIPTS_DIR),
                Button.inline('放入scripts并运行', data='node1'),
            ],
            [
                Button.inline('放入config', data=CONFIG_DIR),
                Button.inline('取消', data='cancel'),
            ]]
        btn = [
            [
                Button.inline('放入own', data=f'/jd/own'),
                Button.inline('放入own并运行', data='node'),
            ],
            [
                Button.inline('放入raw', data=f'/jd/own/raw'),
                Button.inline('放入raw并运行', data='node2'),
            ],
            [
                Button.inline('放入zy', data=f'{SCRIPTS_DIR}/zy'),
                Button.inline('放入zy并运行', data='nodezy'),
            ],
            [
                Button.inline('放入AutoRun', data=f'{SCRIPTS_DIR}/AutoDownload'),
                Button.inline('放入AutoRun并运行', data='nodeAutoRun'),
            ],
            [
                Button.inline('放入diy', data=f'/jd/jbot/diy'),
                Button.inline('放入diy并运行', data='nodeuser'),
            ],
            [
                Button.inline('放入scripts', data=SCRIPTS_DIR),
                Button.inline('放入scripts并运行', data='node1'),
            ],
            [
                Button.inline('放入config', data=CONFIG_DIR),
                Button.inline('取消', data='cancel'),
            ]]
        SENDER = event.sender_id
        if event.message.file:
            filename = event.message.file.name
            cmdtext = None
            async with jdbot.conversation(SENDER, timeout=180) as conv:
                msg = await conv.send_message('请选择您要放入的文件夹或操作：\n')
                if V4:
                    markup = v4btn
                else:
                    markup = btn
                msg = await jdbot.edit_message(msg, '请选择您要放入的文件夹或操作：', buttons=markup)
                convdata = await conv.wait_event(press_event(SENDER))
                res = bytes.decode(convdata.data)
                markup = [Button.inline('是', data='yes'),
                          Button.inline('否', data='no')]
                if res == 'cancel':
                    msg = await jdbot.edit_message(msg, '对话已取消')
                    conv.cancel()
                else:
                    msg = await jdbot.edit_message(msg, '是否尝试自动加入定时', buttons=markup)
                    convdata2 = await conv.wait_event(press_event(SENDER))
                    res2 = bytes.decode(convdata2.data)
                    if res == 'node':
                        backup_file(f'/jd/own/{filename}')
                        await jdbot.download_media(event.message, DIY_DIR)
                        cmdtext = f'{TASK_CMD} /jd/own/{filename} now'
                        with open(f'/jd/own/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, DIY_DIR)
                        else:
                            await jdbot.edit_message(msg, '脚本已保存到own文件夹，并成功运行')
                        conv.cancel()
                    elif res == 'node1':
                        backup_file(f'{SCRIPTS_DIR}/{filename}')
                        await jdbot.download_media(event.message, SCRIPTS_DIR)
                        with open(f'{SCRIPTS_DIR}/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        cmdtext = f'{TASK_CMD} {SCRIPTS_DIR}/{filename} now'
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, SCRIPTS_DIR)
                        else:
                            await jdbot.edit_message(msg, '脚本已保存到SCRIPTS文件夹，并成功运行')
                        conv.cancel()
                    elif res == 'nodezy':
                        backup_file(f'{SCRIPTS_DIR}/zy/{filename}')
                        await jdbot.download_media(event.message, f'{SCRIPTS_DIR}/zy')
                        with open(f'{SCRIPTS_DIR}/zy/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        cmdtext = f'{TASK_CMD} {SCRIPTS_DIR}/zy/{filename} now'
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, f'{SCRIPTS_DIR}/zy')
                        else:
                            await jdbot.edit_message(msg, f'脚本已保存到{SCRIPTS_DIR}/my_js文件夹，并成功运行')
                        conv.cancel()
                    elif res == 'node2':
                        backup_file(f'/jd/own/raw/{filename}')
                        await jdbot.download_media(event.message, DIY_DIR)
                        cmdtext = f'{TASK_CMD} /jd/own/raw/{filename} now'
                        with open(f'/jd/own/raw/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, DIY_DIR)
                        else:
                            await jdbot.edit_message(msg, '脚本已保存到raw文件夹，并成功运行')
                        conv.cancel()
                    elif res == 'nodeAutoRun':
                        backup_file(f'{SCRIPTS_DIR}/AutoDownload/{filename}')
                        await jdbot.download_media(event.message, f'{SCRIPTS_DIR}/AutoDownload')
                        with open(f'{SCRIPTS_DIR}/AutoDownload/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        cmdtext = f'{TASK_CMD} {SCRIPTS_DIR}/AutoDownload/{filename} now'
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, f'{SCRIPTS_DIR}/AutoDownload')
                        else:
                            await jdbot.edit_message(msg, f'脚本已保存到{SCRIPTS_DIR}/AutoDownload文件夹，并成功运行')
                        conv.cancel()
                    elif res == 'nodeuser':
                        backup_file(f'/jd/jbot/diy/{filename}')
                        await jdbot.download_media(event.message, f'/jd/jbot/diy')
                        with open(f'/jd/jbot/diy/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        cmdtext = f'{TASK_CMD} /jd/jbot/diy/{filename} now'
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, f'/jd/jbot/diy')
                        else:
                            await jdbot.edit_message(msg, f'脚本已保存到/jd/jbot/diy文件夹，并成功运行')
                        conv.cancel()
                    else:
                        backup_file(f'{res}/{filename}')
                        await jdbot.download_media(event.message, res)
                        with open(f'{res}/{filename}', 'r', encoding='utf-8') as f:
                            resp = f.read()
                        if res2 == 'yes':
                            await add_cron(jdbot, conv, resp, filename, msg, SENDER, markup, res)
                        else:
                            await jdbot.edit_message(msg, f'{filename}已保存到{res}文件夹')
            if cmdtext:
                await cmd(cmdtext)
    except exceptions.TimeoutError:
        msg = await jdbot.send_message(chat_id, '选择已超时，对话已停止')
    except Exception as e:
        await jdbot.send_message(chat_id, f'something wrong,I\'m sorry\n{str(e)}')
        logger.error(f'something wrong,I\'m sorry\n{str(e)}')
