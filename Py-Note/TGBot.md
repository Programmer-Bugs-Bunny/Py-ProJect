# 发送消息
发送消息的公共参数：
1. cid:聊天框id
2. duration:发送动画的时长，单位秒(仅存在发送文件方法)
3. reply_to_message_id:如果消息是回复消息，原始消息的ID
4. reply_markup: 内联键盘
5. timeout:超时时间
6. message_thread_id:消息线程的标识符，将在其中发送消息
7. thumb: 发送文件的缩略图(仅存在发送文件方法)
8. allow_sending_without_reply: 即使找不到指定的回复消息也应该发送消息
9. disable_notification：静默发送消息
10. protect_content: 保护发送消息的内容不被转发和保存
11. parse_mode:解析的模式(仅存在发送文件方法)
12. caption_entities: 标题中出现的特殊实体的JSON序列化列表，可以指定而不是parse_mode(仅存在发送文件方法)
13. caption:动画标题(也可能用到file_id重发动画),实体解析后0-1024个字符
```python
bot.send_animation(
    animation, width, height, has_spoiler
)  # 使用此方法发送动画文件（GIF 或 H.264/MPEG-4 AVC 无声视频）
'''
animation: 要发送的动画, 
has_spoiler: 如果动画应该作为剧透发送
'''
bot.send_audio(
    audio, performer, title
)  # 让Telegram 客户端在音乐播放器中显示音频文件
'''
audio: 要发送的音频文件, title: 曲目名称, performer: 表演者,
'''
bot.send_chat_action(
    action
)  # 当需要告诉用户机器人正在发生某些事情
# action: 要广播的动作类型, message_thread_id：将发送回复的消息的线程标识符（仅限超组）
bot.send_contact(
    phone_number, first_name, last_name, vcard
)  # 使用此方法发送电话联系人.
'''
phone_number: 联系人电话号码, first_name: 联系人的名字, last_name: 联系人的姓氏
vcard: vCard形式的联系人附加数据，0-2048字节
'''
bot.send_dice(
    emoji
)  # 使用此方法发送将显示随机值的动画表情符号。
'''
emoji: 掷骰子动画所基于的表情符号
'''
bot.send_document(
    document, visible_file_name, disable_content_type_detection
)  # 使用此方法发送一般文件。
'''
document: 要发送的文件
visible_file_name: 允许定义在电报中可见的文件名而不是原始文件名, 
disable_content_type_detection: 对使用 multipart/form-data 上传的文件禁用自动服务器端内容类型检测
'''
bot.send_game(
    game_short_name
)  # 用于发送游戏。
'''
game_short_name: 游戏的简称，作为游戏的唯一标识
'''
bot.send_invoice(
    title, description, invoice_payload, provider_token, currency, prices, start_parameter,
    photo_url, photo_size, photo_width, photo_height, need_name, need_phone_number, need_email,
    need_shipping_address, send_phone_number_to_provider, send_email_to_provider, is_flexible, 
    provider_data, max_tip_amount, suggested_tip_amounts
)  # 发送发票。
'''
title: 产品名称, 
description: 产品描述, 
invoice_payload: Bot定义的发票payload，1-128字节。 这不会显示给用户
provider_token：支付提供商令牌, 
currency: 三个字母的 ISO 4217 货币代码, prices: 价格明细, 
start_parameter：可用于生成此发票的唯一深度链接参数, 
photo_url: 发票产品照片的URL,
need_name: 如果需要用户的全名来完成订单, 
need_phone_number:如果你需要用户的电话号码来完成订单
need_email:如果你需要用户的邮箱来完成订单,
need_shipping_address:如果需要用户的送货地址才能完成订单
is_flexible: 传真，如果最终价格取决于运输方式,
send_phone_number_to_provider:如果用户的电话号码应该发送给提供者
send_email_to_provider:如果用户的电子邮件地址应该发送给提供者
max_tip_amount: 以货币的最小单位表示的最大接受小费金额,
suggested_tip_amounts: 一个 JSON 序列化的建议小费数量数组，最小的货币单位
provider_data：关于发票的 JSON 序列化数据，将与支付提供商共享。
'''
bot.send_location(
    latitude, longitude, live_period, horizontal_accuracy, heading, proximity_alert_radius
)  # 使用此方法在地图上发送点
'''
latitude、longitude: 经纬度
live_period: 更新位置的时间段（以秒为单位）（请参阅实时位置，应在 60 到 86400 之间。
horizontal_accuracy：位置的不确定性半径，以米为单位； 0-1500
heading: 对于实时位置，用户移动的方向，以度为单位。 如果指定，则必须介于 1 和 360 之间。
proximity_alert_radius：对于实时位置，关于接近另一个聊天成员的接近警报的最大距离，以米为单位。 如果指定，则必须介于 1 和 100000 之间。
'''
bot.send_media_group(
    media
)  # 使用此方法将一组照片、视频、文档或音频作为相册发送。
'''
media: 描述发送消息的JSON序列化数组，必须包含2-10项
'''
bot.send_message(
    text, entities, disable_web_page_preview
)  # 使用此方法发送文本消息。
'''
entities: 消息文本中出现的特殊实体列表，可以指定代替parse_mode
disable_web_page_preview: 禁用此消息中链接的链接预览,
'''
bot.send_photo(
    photo, has_spoiler
)  # 使用此方法发送照片。
'''
photo: 要发送的照片
has_spoiler:如果照片应该作为剧透发送
'''
bot.send_poll(
    question, is_anonymous, type, allows_multiple_answers, correct_option_id, explanation, 
    explanation_parse_mode, open_period, close_date, is_closed, explanation_entities
)  # 使用此方法发送本机轮询。
'''
question: 投票问题, options: 一个 JSON 序列化的答案选项列表，2-10 个字符串，每个字符串 1-100 个字符
is_anonymous:如果轮询需要匿名，默认为True, allows_multiple_answers:如果投票允许多个答案，在问答模式下忽略投票，默认为False
correct_option_id: 正确答案选项的基于 0 的标识符。 仅适用于测验模式下的投票，
explanation: 当用户选择不正确的答案或在测验式投票中点击灯图标时显示的文本，最多 2 个换行符
open_period: 轮询在创建后将处于活动状态的时间量（以秒为单位），5-600。 不能与 close_date 一起使用。
close_date: 轮询将自动关闭的时间点（Unix 时间戳）, is_closed:如果轮询需要立即关闭。 这对于投票预览很有用。
allow_sending_without_reply: 如果轮询允许同时对多个选项进行投票，则通过 True。
explanation_entities: 解释中出现的特殊实体的 JSON 序列化列表，可以指定而不是 parse_mode
'''
bot.send_sticker(
    sticker
)  # 使用此方法发送静态 .WEBP、动画 .TGS 或视频 .WEBM 贴纸。
'''
sticker：要发送的贴纸。
'''
bot.send_venue(
    latitude, longitude, title, address, foursquare_id, foursquare_type, google_place_id,
    google_place_type
)  # 使用此方法发送有关场所的信息。
'''
latitude、longitude: 经纬度 title: 场地名称, address: 场地地址, foursquare_id: 会场的Foursquare标识
foursquare_type：场地的四方类型，如果知道的话。
google_place_id: 地点的 Google Places 标识符, google_place_type: 场地的 Google Places 类型。
'''
bot.send_video(
    video, width, height, supports_streaming, has_spoiler
)  # 使用此方法发送视频文件
'''
video: 要发送的视频, 
supports_streaming:如果上传的视频适合流式传输
has_spoiler:如果视频应该作为剧透发送
'''
bot.send_video_note(
    data, length
)  # 使用此方法发送视频笔记消息。
'''
data：要发送的视频笔记, length: 视频宽高，即视频信息的直径
'''
bot.send_voice(
    voice
)  # 发送可播放的语音消息的音频文件
'''
voice: 要发送的音频文件,
'''
```

# 编辑信息
```python
bot.edit_forum_topic(
    chat_id, message_thread_id, name, icon_custom_emoji_id
)  # 使用此方法可以在论坛超级群聊中编辑主题的名称和图标。
# message_thread_id:要编辑的主题的标识符, name:可选，新名字,
# icon_custom_emoji_id:可选，显示为主题图标的自定义表情符号的新唯一标识符。
bot.edit_general_forum_topic(cid, name)  # 使用此方法编辑论坛超级群聊中“常规”主题的名称。
bot.edit_message_caption(
    caption, cid, msgid, inline_message_id, parse_mode,
    caption_entities, reply_markup
)  # 使用此方法编辑消息的标题。
'''
caption:消息的新标题, inline_message_id:如果未指定 inline_message_id，则为必需。
parse_mode:消息的新标题，实体解析后0-1024个字符, caption_entities:一个 JSON 序列化的对象数组
reply_markup:内联键盘的 JSON 序列化对象。
'''
bot.edit_message_live_location(
    latitude, longitude, cid, msgid, inline_message_id,
    reply_markup, timeout, horizontal_accuracy, heading,
    proximity_alert_radius
)  # 使用此方法编辑实时位置消息。
'''
latitude:新位置的纬度, longitude:新位置的经度, reply_markup:新内联键盘的 JSON 序列化对象
timeout请求的超时秒数, inline_message_id如果未指定 chat_id 和 message_id，则为必需
horizontal_accuracy位置的不确定性半径，以米为单位； 0-1500 ....?
heading: 用户移动的方向，以度为单位 ....?
proximity_alert_radius：关于接近另一个聊天成员的接近警报的最大距离，以米为单位 ....?
'''
bot.edit_message_media(
    media, cid, msgid, inline_message_id, reply_markup
)  # 使用此方法编辑动画、音频、文档、照片或视频消息。
'''
media: 消息的新媒体内容的 JSON 序列化对象, inline_message_id如果未指定cid和msgid，则为必需
reply_markup:内联键盘的 JSON 序列化对象
'''
bot.edit_message_reply_markup(
    cid, msgid, inline_message_id, reply_markup
)  # 使用此方法仅编辑消息的回复标记。
'''
inline_message_id：如果未指定 chat_id 和 message_id，则为必需,
reply_markup:内联键盘的 JSON 序列化对象
'''
bot.edit_message_text(
    text, cid, msgid, inline_message_id, parse_mode,
    entities, disable_web_page_preview, reply_markup
)  # 使用此方法编辑文本消息。
'''
text: 消息的新文本, inline_message_id：如果未指定 chat_id 和 message_id，则为必需
parse_mode: 解析消息文本中实体的模式, entities: 消息文本中出现的特殊实体列表，可以指定代替parse_mode
disable_web_page_preview: 禁用此消息中链接的链接预览, reply_markup: 内联键盘的 JSON 序列化对象
'''
```

# 装饰器
装饰器公共参数
1. func:作为过滤器执行的函数
2. commands:可选的字符串列表（要处理的命令）
3. regexp:可选的正则表达式
4. content_types:支持的消息内容类型。 必须是一个列表。 默认为 ['文本']
```python
bot.callback_query_handler()  # 处理新的传入回调查询。装饰器函数
bot.channel_post_handler()  # 处理任何类型的新传入频道帖子-文本、照片、贴纸等。装饰器函数
bot.chat_join_request_handler()  # 处理已发送的加入聊天的请求。装饰器函数
bot.chat_member_handler()  # 处理聊天中用户状态的更新。装饰器函数
bot.chosen_inline_handler()  # 处理由用户选择并发送给他们的聊天伙伴的内联查询的结果。装饰器函数
bot.edited_channel_post_handler()  # 处理机器人已知并已编辑的频道帖子的新版本。装饰器函数
bot.edited_message_handler()  # 处理机器人已知并已编辑的消息的新版本。装饰器函数
bot.inline_handler()  # 处理新传入的内联查询。装饰器函数
bot.message_handler()  # 处理任何类型的新传入消息 - 文本、照片、贴纸等。 装饰器函数
bot.middleware_handler()  # 基于函数的中间件处理程序装饰器。
bot.my_chat_member_handler()  # 处理机器人状态的更新。装饰器
bot.poll_answer_handler()  # 处理非匿名投票中用户答案的更改（当用户更改投票时）。装饰器
bot.poll_handler()  # 处理民意调查的新状态。装饰器
bot.pre_checkout_query_handler()  # 新传入的结帐前查询。装饰器
bot.shipping_query_handler(func, **kwargs)  # 处理新的进货查询。装饰器
```

# 群管理
```python
bot.approve_chat_join_request(
    cid, uid
)  # 使用此方法批准聊天加入请求。机器人必须是管理员
# cid:对话的ID, uid:用户ID
bot.ban_chat_member(
    cid, uid, until_date, revoke_messages
)  # 此方法禁止组、超级组或频道中的用户。
# cid:对话的ID, uid:用户ID, until_date:解封的时间，不到30秒或超过366天视为永久封禁, 
# revoke_messages:为True在当前聊天中删除当前用户的所有发言，否则为False
bot.ban_chat_sender_chat(
    cid, sender_chat_id
)  # 使用此方法可以禁止超级组或频道中的频道聊天
# cid:对话的ID, sender_chat_id:目标用户的聊天ID
bot.create_chat_invite_link(
    cid, name, expire_date, member_limit, creates_join_request
)  # 使用此方法为聊天创建额外的邀请链接。
'''
name:邀请链接名称; 0-32 个字符, expire_date:链接过期的时间点(Unix时间戳), 
member_limit:可以同时成为聊天成员的最大用户数,
creates_join_request:如果通过链接加入聊天的用户需要得到聊天管理员的批准。如果为True，则不能指定member_limit
'''
bot.decline_chat_join_request(cid, uid)  # 使用此方法拒绝聊天加入请求
bot.delete_chat_photo(cid)  # 使用此方法删除聊天照片
bot.delete_chat_sticker_set(cid)  # 使用此方法从超级组中删除组贴纸集。
bot.delete_forum_topic(cid, message_thread_id)  # 使用此方法删除论坛超级群聊中的主题
# message_thread_id:主题ID
bot.delete_message(cid, msgid, timeout)  # 使用此方法删除消息，包括服务消息
# timeout:请求的超时秒数
bot.delete_my_commands(scope, language_code)  # 使用此方法删除给定范围和用户语言的机器人命令列表
# scope:命令相关用户的范围, language_code:两个字母的 ISO 639-1 语言代码
bot.delete_state(uid, cid)  # 删除用户的当前状态
bot.delete_sticker_from_set(sticker)  # 使用此方法从机器人创建的集合中删除贴纸
# sticker:贴纸的文件标识符
bot.edit_chat_invite_link(
    cid, invite_link, name, expire_date, member_limit, creates_join_request
)  # 使用此方法编辑由机器人创建的非主要邀请链接
'''
invite_link:要编辑的邀请链接, name:邀请链接名称; 0-32 个字符, 
expire_date:链接过期的时间, member_limit:可以同时成为聊天成员的最大用户数,
creates_join_request:True，如果通过链接加入聊天的用户需要得到聊天管理员的批准。 如果为 True，则不能指定 member_limit
'''
bot.get_chat(cid)  # 使用此方法获取有关聊天的最新信息（一对一用户的当前名称对话、用户、组或频道的当前用户名等）。 成功时返回聊天对象。
bot.get_chat_administrators(cid)  # 使用此方法获取聊天中的管理员列表。
bot.get_chat_member(cid, uid)  # 使用此方法获取有关聊天成员的信息。
bot.get_chat_member_count(cid)  # 使用此方法获取聊天中的成员数。
bot.get_chat_menu_button(cid)  # 使用此方法获取机器人菜单按钮的当前值在私人聊天中，或默认菜单按钮。
bot.get_custom_emoji_stickers(custom_emoji_ids)  # 使用此方法通过标识符获取有关自定义表情符号贴纸的信息。
# custom_emoji_ids：自定义表情符号标识符列表。 最多可以指定 200 个自定义表情符号标识符。
bot.get_file(file_id)  # 使用此方法获取有关文件的基本信息并准备下载。
bot.get_file_url(file_id)  # 获取用于下载文件的有效 URL。
bot.get_forum_topic_icon_stickers()  # 使用此方法获取自定义表情符号贴纸，任何用户都可以将其用作论坛主题图标。
bot.get_game_high_scores(uid, cid, msg_id, inline_message_id)  # 使用此方法获取高分表的数据。
# inline_message_id：如果未指定 chat_id 和 message_id，则为必需
bot.get_my_commands(scope, language_code)  # 使用此方法获取机器人命令的当前列表。
# scope: 命令相关的用户范围, language_code: 两个字母的 ISO 639-1 语言代码
bot.get_my_default_administrator_rights(for_channels)  # 使用此方法获取机器人当前默认的管理员权限。
# for_channels: 传递 True 以获得 bot 在频道中的默认管理员权限
bot.get_state(uid, cid)  # 获取用户的当前状态。
bot.get_sticker_set(name)  # 使用此方法获取贴纸集。
# name: 贴纸集名称
bot.get_updates(
    offset, limit, timeout, allowed_updates, long_polling_timeout
)  # 使用此方法通过长轮询 (wiki) 接收传入的更新。
'''
offset: 要返回的第一个更新的标识符, limit: 限制要检索的更新数量, allowed_updates: 字符串数组
long_polling_timeout：长轮询的超时秒数
'''
bot.get_user_profile_photos(
    uid, offset, limit
)  # 使用此方法获取用户的个人资料图片列表。
# offset: 要返回的第一张照片的序号, limit: 限制要检索的照片数量
bot.promote_chat_member(
    cid, uid, can_change_info, can_post_messages, can_edit_messages, can_delete_messages,
    can_invite_users, can_restrict_members, can_pin_messages, can_promote_members, is_anonymous,
    can_manage_chat, can_manage_video_chats, can_manage_topics
)  # 使用此方法可以提升或降级超级组或频道中的用户。
'''
can_change_info:传True，管理员是否可以更改聊天标题、照片等设置, can_post_messages:如果管理员可以创建频道帖子，仅限频道,
can_edit_messages:如果管理员可以编辑其他用户的消息，仅限频道, can_delete_messages:如果管理员可以删除其他用户的消息,
can_invite_users:如果管理员可以邀请新用户加入聊天, can_restrict_members:如果管理员可以限制、禁止或取消禁止聊天成员,
can_pin_messages:如果管理员可以固定消息，仅限超级组, can_promote_members:如果管理员可以添加具有子集的新管理员,
is_anonymous:如果管理员在聊天中的存在是隐藏的,
can_manage_chat:如果管理员可以访问聊天事件日志，聊天统计，频道消息统计，查看频道成员，查看超级组中的匿名管理员,
can_manage_video_chats:如果管理员可以管理语音聊天.目前，机器人只能将此权限用于传递给其他管理员,
can_manage_topics:如果允许用户创建、重命名、关闭、并重新打开论坛主题，仅限超级群组
'''
```

# 取消禁止
```python
bot.unban_chat_member(cid, uid, only_if_banned)  # 使用此方法可以取消对超级组或频道中先前被踢出的用户的封禁。
# only_if_banned: 如果用户没有被禁止则什么也不做
bot.unban_chat_sender_chat(cid, sender_chat_id)  # 使用此方法可以取消禁止超级组或频道中先前被禁止的频道聊天。
# sender_chat_id：目标发件人聊天的唯一标识符。
bot.unhide_general_forum_topic(cid)  # 使用此方法取消隐藏论坛超级群聊天中的“常规”主题。
bot.unpin_all_chat_messages(cid)  # 使用此方法取消固定超级群聊天中的所有固定消息。
bot.unpin_all_forum_topic_messages(cid, message_thread_id)  # 使用此方法清除论坛主题中固定消息的列表。
# message_thread_id: 主题的标识符
bot.unpin_chat_message(cid, msgid)  # 使用此方法取消固定超级群聊天中的特定固定消息。
```
#
```python
bot = Bot()
bot.add_callback_query_handler(handler_dict)  # 添加回调请求处理程序
bot.add_channel_post_handler(handler_dict)  # 添加频道帖子处理程序
bot.add_chat_join_request_handler(handler_dict)  # 添加聊天加入请求处理程序
bot.add_chat_member_handler(handler_dict)  # 添加聊天成员处理程序
bot.add_chosen_inline_handler(handler_dict)  # 好像没有描述
bot.add_custom_filter(custom_filter)  # 创建自定义过滤器
# custom_filter:带有check(message)方法的类或带键的自定义过滤器类
bot.add_data(uid, cid, **kwargs)  # 向状态添加数据
# uid:用户ID, cid:对话框ID, kwargs:要添加的数据
bot.add_edited_channel_post_handler(handler_dict)  # 添加编辑频道帖子处理程序
bot.add_edited_message_handler(handler_dict)  # 添加编辑消息处理程序
bot.add_inline_handler(handler_dict)  # 添加内联调用处理程序
bot.add_message_handler(handler_dict)  # 添加消息处理程序
bot.add_middleware_handler(handler, update_types)  # 添加中间件处理程序
bot.add_my_chat_member_handler(handler_dict)  # 添加我的聊天成员处理程序
bot.add_poll_answer_handler(handler_dict)  # 添加轮询应答请求处理程序
bot.add_poll_handler(handler_dict)  # 添加轮询请求处理程序
bot.add_pre_checkout_query_handler(handler_dict)  # 添加预结帐请求处理程序
bot.add_shipping_query_handler(handler_dict)  # 添加运输请求处理程序
bot.add_sticker_to_set(
    uid, name, emojis, 
    png_sticker, tgs_sticker,
    webm_sticker, mask_position
)  # 使用此方法将新贴纸添加到机器人创建的合集
'''
uid:创建贴纸集的用户ID, name:贴纸集名称, emojis:贴纸对应的一个或多个表情, 
png_sticker:带贴纸的PNG图片!<512KB !<512px, tgs_sticker:带有贴纸的 TGS 动画,
webm_sticker:带有贴纸的 WebM 动画, mask_position:一个 JSON 序列化的对象，表示面具应该放在脸上的位置
'''
bot.answer_callback_query(
    callback_query_id, text, show_alert, url, cache_time
)  # 此方法发生对内联键盘的回调查询答复，将在聊天框的顶部通知或者警报
'''
callback_query_id:要回答的查询的唯一标识符, text:通知的文本,
show_alert:如果为True则警报否则是通知，默认为False
url:将由用户的客户端打开的 URL, cache_time:回调查询结果可以在客户端缓存的最长时间（以秒为单位）
'''
bot.answer_inline_query(
    inline_query_id, results, cache_time, is_personal, next_offset,
    switch_pm_text, switch_pm_parameter
)  # 使用此方法将答案发送到内联查询。成功时返回 True。 每个查询的结果不得超过 50
'''
inline_query_id:已回答查询的唯一标识符. results:内联查询的结果数组. cache_time:内联查询结果的最大时间量（以秒为单位）
is_personal:传递 True，如果结果可能只缓存在服务器端发送查询的用户. 
next_offset:传递客户端应该在下一个具有相同文本的查询中发送的偏移量. 
switch_pm_text:当用户按下开关按钮时发送给机器人的 /start 消息的深度链接参数. 1-64 个字符，只允许使用 A-Z、a-z、0-9、_ 和 -。
switch_pm_parameter:当用户按下开关按钮时发送给机器人的启动消息参数
'''
bot.answer_pre_checkout_query(
    pre_checkout_query_id, ok, error_message
)  # 一旦用户确认了他们的付款和运输细节，Bot API 就会以更新的形式发送最终确认
'''
pre_checkout_query_id:查询的唯一标识. ok:一切正常且机器人准备好处理则指定True，否则False. 
error_message:如果ok为False，则为必需。以人类可读形式显示的错误消息
'''
bot.answer_shipping_query(
    shipping_query_id, ok, shipping_options, error_message
)  # 要求回答运输问题
'''
shipping_query_id:查询的唯一标识. ok:可以投递到指定地址则为True，有问题则为False. 
shipping_options:如果ok为True，则为必需。可用运输选项的JSON序列化数组。
error_message:如果ok为False，则为必需。以人类可读形式显示的错误消息
'''
bot.answer_web_app_query(
    web_app_query_id, result
)  # 使用此方法设置与 Web 应用程序交互的结果，以及代表用户向聊天发送相应的消息成功时,返回一个SentWebAppMessage对象。
# web_app_query_id:查询的唯一标识. result:要发送消息的JSON对象

bot.clear_reply_handlers(message)  # 清除register_for_reply() 和register_for_reply_by_message_id() 注册的所有回调函数。
bot.clear_reply_handlers_by_message_id(message_id)  # 作用同上,参数为消息ID
bot.clear_step_handler(message)  # 清除 register_next_step_handler() 注册的所有回调函数。
bot.clear_step_handler_by_chat_id(cid)  # 作用同上,参数为对话框ID
bot.close_forum_topic(cid, message_thread_id)  # 使用此方法关闭论坛超级群聊中的开放主题。
# message_thread_id:要关闭的主题的标识符
bot.close_general_forum_topic(cid)  # 使用此方法关闭论坛超级群聊中的“常规”主题。
bot.copy_message(
    cid, from_chat_id, message_id, caption, parse_mode,
    caption_entities, disable_notification, protect_content, reply_to_message_id,
    allow_sending_without_reply, reply_markup, timeout, message_thread_id
)  # 使用此方法复制任何类型的消息
'''
from_chat_id:原始消息对话框的消息ID, message_id:from_chat_id指定的聊天的消息ID, 
caption:媒体的新标题，实体解析后的0-1024个字符, parse_mode:解析新标题中实体的模式, 
caption_entities:新标题中出现的特殊实体的JSON序列化列表, 
disable_notification:静默发送消息。 用户将收到没有声音的通知。
protect_content:保护发送消息的内容不被转发和保存, reply_to_message_id:如果消息是回复消息，填写原始消息的ID
allow_sending_without_reply：传递 True，即使找不到指定的回复消息也应该发送消息
reply_markup:额外的接口选项。 内联键盘的 JSON 序列化对象、自定义回复键盘、删除回复键盘的说明或者强制用户回复。
timeout:超时秒数, message_thread_id:消息线程的标识符，将在其中发送消息
'''
bot.create_forum_topic(
    cid, name, icon_color, icon_custom_emoji_id
)  # 使用此方法在论坛超级群聊中创建主题。
'''
name:话题名称，1-128个字符, 
icon_color:RGB 格式的主题图标颜色。 目前，必须是 0x6FB9F0、0xFFD67E、0xCB86DB、0x8EEE98、0xFF93B2 或 0xFB6F5F 之一, 
icon_custom_emoji_id:主题图标的自定义表情符号。 必须是“tgs”类型的表情符号，且长度必须恰好为 1 个字符
'''
bot.create_invoice_link(
    title, description, payload, provider_token, currency, prices, max_tip_amount,
    suggested_tip_amounts, provider_data, photo_url, photo_size, photo_width,
    photo_height, need_name, need_phone_number, need_email, need_shipping_address,
    send_phone_number_to_provider, send_email_to_provider, is_flexible
)  # 使用此方法为发票创建链接
'''
title:产品名称，1-32个字符, description:产品描述，1-255个字符, 
payload:Bot定义的发票有效载荷，1-128字节, provider_token:支付提供商令牌,
currency:三个字母的 ISO 4217 货币代码，, prices:价格明细,
max_tip_amount:以货币的最小单位表示的最大接受小费金额,
suggested_tip_amounts:个 JSON 序列化的建议小费数量数组，最小的货币单位。 最多可以指定 4 个建议的小费金额。 建议的提示金额必须为正数，以严格递增的顺序传递，并且不得超过max_tip_amount, 
provider_data:于发票的 JSON 序列化数据，将与支付提供商共享, photo_url:发票产品照片的URL,
photo_size:照片大小，以字节为单位, photo_width:图片宽度,
photo_height:照片高度, need_name:如果需要用户的全名来完成订单, need_phone_number:如果你需要用户的电话号码来完成订单, 
need_email:如果你需要用户的邮箱来完成订单, need_shipping_address:如果需要用户的送货地址才能完成订单,
send_phone_number_to_provider:传递 True，如果用户的电话号码应该发送给提供者,
send_email_to_provider:传递 True，如果用户的电子邮件地址应该发送给提供者,
is_flexible:传真，如果最终价格取决于运输方式
'''
bot.create_new_sticker_set(
    uid, name, title, emojis, png_sticker, tgs_sticker, webm_sticker,
    sticker_type, mask_position
)  # 使用此方法创建用户拥有的新贴纸集。
'''
name:贴纸集的简称，只能包含英文字母，数字和下划线, title:贴纸集标题，1-64个字符, 
emojis:贴纸对应的一个或多个表情符号, 
png_sticker:带有贴纸的 PNG 图像，大小不得超过 512 KB，尺寸不得超过 512px，宽度为或高度必须正好是 512px, 
tgs_sticker:带有贴纸的 TGS 动画, webm_sticker:带有贴纸的 WebM 动画,
sticker_type:可选，集合中贴纸的类型，传递“regular”或“mask”,
mask_position:一个 JSON 序列化的对象，表示面具应该放在脸上的位置
'''
bot.delete_webhook(drop_pending_updates, timeout)  # 如果您决定切换回 getUpdates，请使用此方法删除 Webhook 集成
# drop_pending_updates:传递 True 以删除所有挂起的更新，默认为 None
bot.download_file(file_path)  # 下载文件
bot.export_chat_invite_link(cid)  # 使用此方法将邀请链接导出到超级组或频道。
bot.forward_message(
    cid, from_chat_id, msgid, disable_notification,
    protect_content, timeout, message_thread_id
)  # 使用此方法转发任何类型的消息。
'''
disable_notification：静默发送消息, from_chat_id：发送原始消息的聊天的唯一标识符,
protect_content: 保护转发消息的内容不被转发保存, timeout：请求的超时秒数,
message_thread_id: 消息线程的标识符，将在其中发送消息
'''
bot.get_webhook_info(timeout)  # 使用此方法获取当前 webhook 状态。
bot.hide_general_forum_topic(cid)  # 使用此方法可以隐藏论坛超级群聊天中的“常规”主题。
bot.infinity_polling(
    timeout, skip_pending, long_polling_timeout, logger_level, allowed_updates,
    restart_on_change, path_to_watch, **args, **kwargs
)  # 用无限循环和异常处理包装轮询以避免机器人停止轮询。
'''
skip_pending: 跳过旧的更新, long_polling_timeout：长轮询的超时时间, logger_level：日志记录级别,
allowed_updates：您希望机器人接收的更新类型列表, restart_on_change：在文件更改时重新启动文件
path_to_watch: 监视变化的路径
'''
bot.leave_chat(cid)  # 使用此方法让您的机器人离开组、超级组或频道。
bot.pin_chat_message(cid, msgid, disable_notification)  # 使用此方法将消息固定在超级组中。
# disable_notification: 传True，如果不需要发送通知向所有组成员介绍新的固定消息
bot.register_callback_query_handler(
    callback, func, pass_bot, **kwargs
)  # 注册回调查询处理程序。
# callback:要调用的函数, func:作为过滤器执行的函数, pass_bot:如果需要将 TeleBot 实例传递给处理程序则为真
bot.register_channel_post_handler(
    callback, content_types, commands, regexp, func, pass_bot, **kwargs
)  # 注册频道发布消息处理程序。
# content_types:支持的消息内容类型。 必须是一个列表。 默认为 ['文本'], commands:命令列表, regexp:正则表达式
bot.register_chat_join_request_handler(
    callback, func, pass_bot, **kwargs
)  # 注册聊天加入请求处理程序。
bot.register_chat_member_handler(
    callback, func, pass_bot, **kwargs
)  # 注册聊天成员处理程序。
bot.register_chosen_inline_handler(
    callback, func, pass_bot, **kwargs
)  # 注册选择的内联处理程序。
bot.register_edited_channel_post_handler(
    callback, content_types, commands, regexp, func, pass_bot, **kwargs
)  # 注册已编辑的频道发布消息处理程序。
bot.register_edited_message_handler(
    callback, content_types, commands, regexp, func, chat_types, pass_bot, **kwargs
)  # 注册已编辑的消息处理程序。
# chat_types:适用于私人聊天
bot.register_for_reply(
    message, callback, *args, **kwargs
)  # 注册一个回调函数，以便在对“消息”的回复到达时得到通知。
# callback: 回复到达时调用的回调函数
bot.register_for_reply_by_message_id(
    msgid, callback, *args, **kwargs
)  # 同上，参数msg变成msgid
bot.register_inline_handler(
    callback, func, pass_bot, **kwargs
)  # 注册内联处理程序。
bot.register_message_handler(
    callback, content_types, commands, regexp, func, chat_types, pass_bot, **kwargs
)  # 注册消息处理程序。
bot.register_middleware_handler()  # 添加基于函数的中间件处理程序。
bot.register_my_chat_member_handler(
    callback, func, pass_bot, **kwargs
)  # 注册我的聊天成员处理程序。
bot.register_next_step_handler(
    message, callback, *args, **kwargs
)  # 注册一个回调函数，以便在“消息”之后收到新消息时得到通知。
bot.register_next_step_handler_by_chat_id(
    cid, callback, *args, **kwargs
)  # 注册一个回调函数，以便在新消息到达给定聊天时得到通知。
bot.register_poll_answer_handler(
    callback, func, pass_bot, **kwargs
)  # 注册轮询答案处理程序。
bot.register_poll_handler(
    callback, func, pass_bot, **kwargs
)  # 注册轮询处理程序。
bot.register_pre_checkout_query_handler(
    callback, func, pass_bot, **kwargs
)  # 注册预结帐请求处理程序。
bot.register_shipping_query_handler(
    callback, func, pass_bot, **kwargs
)  # 注册运输查询处理程序。
bot.reopen_forum_topic(
    cid, message_thread_id
)  # 使用此方法可以重新打开论坛超级群聊中关闭的主题。
# message_thread_id: 重新打开主题的标识符
bot.reopen_general_forum_topic(cid)  # 使用此方法可在论坛超级群聊中重新打开“常规”主题。
bot.reply_to(
    message, text
)  # send_message的便捷方法
bot.reset_data(uid, cid)  # 为聊天中的用户重置数据。
bot.restrict_chat_member(
    cid, uid, until_date, can_send_messages, can_send_media_messages, can_send_polls,
    can_send_other_messages, can_add_web_page_previews, can_change_info, can_invite_users,
    can_pin_messages, permissions, use_independent_chat_permissions
)  # 使用此方法限制超级组中的用户。
'''
until_date: 为用户解除限制的日期，366天<until_date<30秒则为永久限制,
can_send_messages:如果用户可以发送短信、联系人、地点和地点,
can_send_media_messages:如果用户可以发送音频、文档、照片、视频、视频笔记,
can_send_polls:同can_send_messages, can_send_other_messages:同can_send_media_messages,
can_add_web_page_previews:同can_send_media_messages,
can_change_info:如果允许用户更改聊天标题、照片和其他设置，则传递 True。在公共超级组中被忽略,
can_invite_users:如果用户允许邀请新用户加入聊天,
can_pin_messages:如果允许用户固定消息，则传递 True。 在公共超级组中被忽略,
permissions:传递 ChatPermissions 对象一次设置所有权限,
use_independent_chat_permissions:如果聊天权限是独立设置的，则传递 True
'''
bot.retrieve_data(uid, cid)  # 返回上下文管理器，其中包含聊天中用户的数据。
bot.revoke_chat_invite_link(cid, invite_link)  # 使用此方法撤销机器人创建的邀请链接。
# 要撤销的邀请链接
bot.run_webhooks()  # 此类设置 webhooks 并监听给定的 url 和端口。
bot.set_chat_administrator_custom_title(cid, uid)  # 使用此方法为机器人推广的超级组中的管理员设置自定义标题。
bot.set_chat_description(cid, description)  # 使用此方法更改超级组或频道的描述。
# description: 新的聊天描述
bot.set_chat_menu_button(cid, menu_button)  # 使用此方法在私人聊天中更改机器人的菜单按钮，
# menu_button: 新机器人菜单按钮的 JSON 序列化对象。 默认为 MenuButtonDefault
bot.set_chat_permissions(
    cid, permissions, use_independent_chat_permissions
)  # 使用此方法为所有成员设置默认聊天权限。
# permissions: 新的默认聊天权限, use_independent_chat_permissions: 如果聊天权限是独立设置的，则传递 True
bot.set_chat_photo(cid, photo)  # 使用此方法为聊天设置新的个人资料照片。
# photo:新建聊天图片
bot.set_chat_sticker_set(cid, sticker_set_name)  # 使用此方法为超级组设置新的组贴纸集。
# sticker_set_name:要设置为群组贴纸集的贴纸集名称
bot.set_chat_title(cid, title)  # 使用此方法更改聊天标题。
# title: 新的聊天标题
bot.set_game_score(
    uid, cid, score, force, msgid, inline_message_id, disable_edit_message
)  # 将游戏中的点值设置为特定用户。
'''
score: 新分数，必须为非负数, force:如果允许高分降低。 这在修复错误或禁止作弊者时很有用
inline_message_id：如果未指定 chat_id 和 message_id，则为必需
disable_edit_message:如果游戏消息不应该被自动编辑以包括当前记分牌
'''
bot.set_my_commands(
    commands, scope, language_code
)  # 使用此方法更改机器人命令列表。
'''
commands: BotCommand列表。 最多可以指定 100 个命令。
scope: 命令相关的用户范围。 language_code: 两个字母的 ISO 639-1 语言代码
'''
bot.set_my_default_administrator_rights(
    rights, for_channels
)  # 使用此方法更改 bot 请求的默认管理员权限
'''
rights：描述新的默认管理员权限的 JSON 序列化对象,如果没有指定默认管理员权限将被清除。
for_channels:以更改机器人在频道中的默认管理员权限。
'''
bot.set_state(uid, state, cid)  # 设置用户的新状态。
# state: 新状态
bot.set_sticker_position_in_set(sticker, position)  # 使用此方法将机器人创建的一组贴纸移动到特定位置。
# sticker: 贴纸的文件标识符, position: 集合中的新贴纸位置，从零开始
bot.set_sticker_set_thumb(uid, name, thumb)  # 使用此方法设置贴纸集的缩略图。
# name: 贴纸集名称, 
bot.set_update_listener(listener)  # 设置接收到新更新时要调用的侦听器函数。
# listener: 监听函数。
bot.set_webhook()  # 使用此方法指定 URL 并通过传出 webhook 接收传入更新。
bot.setup_middleware(middleware)  # 注册基于类的中间件。
# middleware: `telebot.handler_backends.BaseMiddleware` 的子类
bot.stop_message_live_location(
    cid, msgid, inline_message_id, reply_markup, timeout
)  # 使用此方法可在 live_period 到期之前停止更新实时位置消息。
bot.stop_poll(cid, msgid, reply_markup)  # 使用此方法停止机器人发送的民意调查。
bot.update_listener(listener)  # 设置接收到新更新时要调用的侦听器函数。
# listener: 监听函数。
bot.upload_sticker_file(uid, png_sticker)  # 使用此方法上传带有贴纸的 .png 文件
# png_sticker: 带有贴纸的 PNG 图像，大小不得超过 512 KB，尺寸不得超过 512px，
```