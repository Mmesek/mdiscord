# -*- coding: utf-8 -*-
"""
Discord Models
----------

Discord raw API types.

:copyright: (c) 2020-2024 Mmesek
:version: 2024/06/10 04:48
"""
from ctypes import c_byte, c_uint, c_ushort
from enum import IntEnum, Enum, Flag
from datetime import datetime
from typing import Annotated, Any, Optional, Union

from msgspec import UnsetType, UNSET, Meta

from .base_model import DiscordObject, Snowflake, DISCORD_EPOCH, Events


class Application(DiscordObject):
    id: Snowflake = None
    """the id of the app"""
    name: str = None
    """the name of the app"""
    icon: str | UnsetType = UNSET
    """Icon_Hash"""
    description: str = None
    """the description of the app"""
    rpc_origins: Optional[list[str]] = None
    """an  rpc origin urls, if rpc is enabled"""
    bot_public: bool = None
    """when false only app owner can join the app's bot to guilds"""
    bot_require_code_grant: bool = None
    """when true the app's bot will only join upon completion of the full oauth2 code grant flow"""
    terms_of_service_url: Optional[str] = None
    """the url of the app's terms of service"""
    privacy_policy_url: Optional[str] = None
    """the url of the app's privacy policy"""
    owner: Optional["User"] = None
    """user  containing info on the owner of the application"""
    summary: str = None
    """if this application is a game sold on Discord, this field will be the summary field for the store page of its primary sku"""
    verify_key: str = None
    """GetTicket"""
    team: Union["Team", UnsetType] = UNSET
    """if the application belongs to a team, this will be a list of the members of that team"""
    guild_id: Optional[Snowflake] = None
    """if this application is a game sold on Discord, this field will be the guild to which it has been linked"""
    primary_sku_id: Optional[Snowflake] = None
    """if this application is a game sold on Discord, this field will be the id of the 'Game SKU' that is created, if exists"""
    slug: Optional[str] = None
    """if this application is a game sold on Discord, this field will be the URL slug that links to the store page"""
    cover_image: Optional[str] = None
    """Cover_Image_Hash"""
    flags: Optional[int] = None
    """Flags"""


class Application_Flags(Flag):
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17


class Audit_Log(DiscordObject):
    webhooks: list["Webhook"] = list
    """list of webhooks found in the audit log"""
    users: list["User"] = list
    """list of users found in the audit log"""
    audit_log_entries: list["Audit_Log_Entry"] = list
    """list of audit log entries"""
    integrations: list["Integration"] = list
    """list of integrations"""


class Audit_Log_Entry(DiscordObject):
    target_id: str | UnsetType = UNSET
    """id of the affected entity"""
    changes: Optional["Audit_Log_Change"] = None
    """changes made to the target_id"""
    user_id: Snowflake | UnsetType = UNSET
    """the user who made the changes"""
    id: Snowflake = None
    """id of the entry"""
    action_type: "Audit_Log_Events" = None
    """type of action that occurred"""
    options: Optional["Optional_Audit_Entry_Info"] = None
    """additional info for certain action types"""
    reason: Optional[str] = None
    """the reason for the change"""


class Audit_Log_Events(Enum):
    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT = 27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75
    INTEGRATION_CREATE = 80
    INTEGRATION_UPDATE = 81
    INTEGRATION_DELETE = 82
    STAGE_INSTANCE_CREATE = 83
    STAGE_INSTANCE_UPDATE = 84
    STAGE_INSTANCE_DELETE = 85


class Optional_Audit_Entry_Info(DiscordObject):
    delete_member_days: str = None
    """number of days after which inactive members were kicked"""
    members_removed: str = None
    """number of members removed by the prune"""
    channel_id: Snowflake = None
    """channel in which the entities were targeted"""
    message_id: Snowflake = None
    """id of the message that was targeted"""
    count: str = None
    """number of entities that were targeted"""
    id: Snowflake = None
    """id of the overwritten entity"""
    type: str = None
    """type of overwritten entity - '0' for 'role'"""
    role_name: str = None
    """name of the role if type is '0'"""


class Audit_Log_Change(DiscordObject):
    new_value: Optional[Any] = None
    """new value of the key"""
    old_value: Optional[Any] = None
    """old value of the key"""
    key: str = None
    """Change_Key"""


class Audit_Log_Change_Key(DiscordObject):
    name: str = None
    """name changed"""
    description: str = None
    """description changed"""
    icon_hash: str = None
    """icon changed"""
    splash_hash: str = None
    """invite splash page artwork changed"""
    discovery_splash_hash: str = None
    """discovery splash changed"""
    banner_hash: str = None
    """guild banner changed"""
    owner_id: Snowflake = None
    """owner changed"""
    region: str = None
    """region changed"""
    preferred_locale: str = None
    """preferred locale changed"""
    afk_channel_id: Snowflake = None
    """afk channel changed"""
    afk_timeout: int = None
    """afk timeout duration changed"""
    rules_channel_id: Snowflake = None
    """id of the rules channel changed"""
    public_updates_channel_id: Snowflake = None
    """id of the public updates channel changed"""
    mfa_level: int = None
    """two-factor auth requirement changed"""
    verification_level: int = None
    """required verification level changed"""
    explicit_content_filter: int = None
    """Whose_Messages"""
    default_message_notifications: int = None
    """Message_Notification_Level"""
    vanity_url_code: str = None
    """guild invite vanity url changed"""
    _add: "Role" = None
    """new role added"""
    _remove: "Role" = None
    """role removed"""
    prune_delete_days: int = None
    """change in number of days after which inactive and role-unassigned members are kicked"""
    widget_enabled: bool = None
    """server widget enabled/disable"""
    widget_channel_id: Snowflake = None
    """channel id of the server widget changed"""
    system_channel_id: Snowflake = None
    """id of the system channel changed"""
    position: int = None
    """text"""
    topic: str = None
    """text channel topic"""
    bitrate: int = None
    """voice channel bitrate changed"""
    permission_overwrites: "Overwrite" = None
    """permissions on a channel changed"""
    nsfw: bool = None
    """channel nsfw restriction changed"""
    application_id: Snowflake = None
    """application id of the added"""
    rate_limit_per_user: int = None
    """amount of seconds a user has to wait before sending another message changed"""
    permissions: str = None
    """Permissions"""
    color: int = None
    """role color changed"""
    hoist: bool = None
    """role is now displayed/no longer displayed separate from online users"""
    mentionable: bool = None
    """role is now mentionable/unmentionable"""
    allow: str = None
    """a permission on a text"""
    deny: str = None
    """a permission on a text"""
    code: str = None
    """invite code changed"""
    channel_id: Snowflake = None
    """channel for invite code changed"""
    inviter_id: Snowflake = None
    """person who created invite code changed"""
    max_uses: int = None
    """change to max number of times invite code can be used"""
    uses: int = None
    """number of times invite code used changed"""
    max_age: int = None
    """how long invite code lasts changed"""
    temporary: bool = None
    """invite code is temporary/never expires"""
    deaf: bool = None
    """user server deafened/undeafened"""
    mute: bool = None
    """user server muted/unmuted"""
    nick: str = None
    """user nickname changed"""
    avatar_hash: str = None
    """user avatar changed"""
    id: Snowflake = None
    """the id of the changed entity - sometimes used in conjunction with other keys"""
    type: "Channel_Types" = None
    """type of entity created"""
    enable_emoticons: bool = None
    """integration emoticons enabled/disabled"""
    expire_behavior: int = None
    """integration expiring subscriber behavior changed"""
    expire_grace_period: int = None
    """integration expire grace period changed"""
    user_limit: int = None
    """new user limit in a voice channel"""
    privacy_level: "Privacy_Level" = None
    """the privacy level of the stage instance."""


class Channel(DiscordObject):
    """
    * `rate_limit_per_user` also applies to thread creation. Users can send one message and create one thread during each `rate_limit_per_user` interval.
    """

    id: Snowflake = None
    """the id of this channel"""
    type: int = None
    """Type_Of_Channel"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""
    position: Optional[int] = None
    """sorting position of the channel"""
    permission_overwrites: Optional["Overwrite"] = None
    """explicit permission overwrites for members and roles"""
    name: Optional[str] = None
    """the name of the channel"""
    topic: Optional[str | UnsetType] = UNSET
    """the channel topic"""
    nsfw: Optional[bool] = None
    """whether the channel is nsfw"""
    last_message_id: Optional[Snowflake | UnsetType] = UNSET
    """the id of the last message sent in this channel"""
    bitrate: Optional[int] = None
    """the bitrate"""
    user_limit: Optional[int] = None
    """the user limit of the voice channel"""
    rate_limit_per_user: int = None
    """amount of seconds a user has to wait before sending another message"""
    recipients: Optional[list["User"]] = None
    """the recipients of the DM"""
    icon: Optional[str | UnsetType] = UNSET
    """icon hash"""
    owner_id: Optional[Snowflake] = None
    """id of the creator of the group DM"""
    application_id: Optional[Snowflake] = None
    """application id of the group DM creator if it is bot-created"""
    parent_id: Optional[Snowflake | UnsetType] = UNSET
    """for guild channels: id of the parent category for a channel"""
    last_pin_timestamp: Optional[datetime | UnsetType] = UNSET
    """when the last pinned message was pinned. This may be `null` in events such as `GUILD_CREATE` when a message is not pinned."""
    rtc_region: Optional[str | UnsetType] = UNSET
    """Voice_Region"""
    video_quality_mode: Optional[int] = None
    """Video_Quality_Mode"""
    message_count: Optional[int] = None
    """an approximate count of messages in a thread, stops counting at 50"""
    member_count: Optional[int] = None
    """an approximate count of users in a thread, stops counting at 50"""
    thread_metadata: Optional["Thread_Metadata"] = None
    """thread-specific fields not needed by other channels"""
    member: Optional["Thread_Member"] = None
    """thread member for the current user, if they have joined the thread, only included on certain API endpoints"""
    default_auto_archive_duration: Optional[int] = None
    """default duration for newly created threads, in minutes, to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080"""


class Channel_Types(Enum):
    GUILD_TEXT = 0
    """a text channel within a server"""
    DM = 1
    """a direct message between users"""
    GUILD_VOICE = 2
    """a voice channel within a server"""
    GROUP_DM = 3
    """a direct message between multiple users"""
    GUILD_CATEGORY = 4
    """Organizational_Category"""
    GUILD_NEWS = 5
    """Users_Can_Follow_And_Crosspost_Into_Their_Own_Server"""
    GUILD_STORE = 6
    """Sell_Their_Game_On_Discord"""
    GUILD_NEWS_THREAD = 10
    """a temporary sub-channel within a GUILD_NEWS channel"""
    GUILD_PUBLIC_THREAD = 11
    """a temporary sub-channel within a GUILD_TEXT channel"""
    GUILD_PRIVATE_THREAD = 12
    """a temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the MANAGE_THREADS permission"""
    GUILD_STAGE_VOICE = 13
    """Hosting_Events_With_An_Audience"""


class Video_Quality_Modes(Enum):
    AUTO = 1
    """Discord chooses the quality for optimal performance"""
    FULL = 2
    """720p"""


class Message(DiscordObject):
    """
    * The author object follows the structure of the user object, but is only a valid user in the case where the message is generated by a user or bot user. If the message is generated by a webhook, the author object corresponds to the webhook's id, username, and avatar. You can tell if a message is generated by a webhook by checking for the `webhook_id` on the message object.
    ** The member object exists in [MESSAGE_CREATE](https:#/discord.com/developers/docs/topics/gateway#message-create) and [MESSAGE_UPDATE](https:#/discord.com/developers/docs/topics/gateway#message-update) events from text-based guild channels, provided that the author of the message is not a webhook. This allows bots to obtain real-time member data without requiring bots to store member state in memory.
    *** The user objects in the mentions array will only have the partial `member` field present in [MESSAGE_CREATE](https:#/discord.com/developers/docs/topics/gateway#message-create) and [MESSAGE_UPDATE](https:#/discord.com/developers/docs/topics/gateway#message-update) events from text-based guild channels.
    **** Not all channel mentions in a message will appear in `mention_channels`. Only textual channels that are visible to everyone in a lurkable guild will ever be included. Only crossposted messages (via Channel Following) currently include `mention_channels` at all. If no mentions in the message meet these requirements, this field will not be sent.
    ***** This field is only returned for messages with a `type` of `19` (REPLY) or `21` (THREAD_STARTER_MESSAGE). If the message is a reply but the `referenced_message` field is not present, the backend did not attempt to fetch the message that was being replied to, so its state is unknown. If the field exists but is null, the referenced message was deleted.
    ****** Bots cannot send stickers.
    """

    id: Snowflake = None
    """id of the message"""
    channel_id: Snowflake = None
    """id of the channel the message was sent in"""
    guild_id: Optional[Snowflake] = None
    """id of the guild the message was sent in"""
    author: "User" = None
    """the author of this message"""
    member: "Guild_Member" = None
    """member properties for this message's author"""
    content: str = None
    """contents of the message"""
    timestamp: datetime = None
    """when this message was sent"""
    edited_timestamp: datetime | UnsetType = UNSET
    """when this message was edited"""
    tts: bool = None
    """whether this was a TTS message"""
    mention_everyone: bool = None
    """whether this message mentions everyone"""
    mentions: list["User"] = None
    """users specifically mentioned in the message"""
    mention_roles: list["Role"] = None
    """roles specifically mentioned in this message"""
    mention_channels: list["Channel_Mention"] = None
    """channels specifically mentioned in this message"""
    attachments: list["Attachment"] = None
    """any attached files"""
    embeds: list["Embed"] = None
    """any embedded content"""
    reactions: Optional[list["Reaction"]] = None
    """reactions to the message"""
    nonce: Optional[int] = None
    """used for validating a message was sent"""
    pinned: bool = None
    """whether this message is pinned"""
    webhook_id: Optional[Snowflake] = None
    """if the message is generated by a webhook, this is the webhook's id"""
    type: int = None
    """Type_Of_Message"""
    activity: Optional["Message_Activity"] = None
    """sent with Rich Presence-related chat embeds"""
    application: Optional[Application] = None
    """sent with Rich Presence-related chat embeds"""
    application_id: Optional[Snowflake] = None
    """Interaction"""
    message_reference: Optional["Message_Reference"] = None
    """data showing the source of a crosspost, channel follow add, pin,"""
    flags: Optional[int] = None
    """Message_Flags"""
    referenced_message: "Message" | UnsetType = UNSET
    """the message associated with the message_reference"""
    interaction: Optional["Interaction"] = None
    """Interaction"""
    thread: Optional[Channel] = None
    """Thread_Member"""
    components: Optional[list["Component"]] = None
    """sent if the message contains components like buttons, action rows,"""
    sticker_items: list["Message_Sticker"] = None
    """sent if the message contains stickers"""
    stickers: Optional[list["Message_Sticker"]] = None
    """Deprecated the stickers sent with the message"""


class Message_Types(Enum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    GUILD_MEMBER_JOIN = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1 = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2 = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    APPLICATION_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22


class Message_Activity(DiscordObject):
    type: int = None
    """Type_Of_Message_Activity"""
    party_id: Optional[str] = None
    """Rich_Presence_Event"""


class Message_Activity_Types(Enum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class Message_Flags(Flag):
    CROSSPOSTED = 1 << 0
    """this message has been published to subscribed channels"""
    IS_CROSSPOST = 1 << 1
    """this message originated from a message in another channel"""
    SUPPRESS_EMBEDS = 1 << 2
    """do not include any embeds when serializing this message"""
    SOURCE_MESSAGE_DELETED = 1 << 3
    """the source message for this crosspost has been deleted"""
    URGENT = 1 << 4
    """this message came from the urgent message system"""
    HAS_THREAD = 1 << 5
    """this message has an associated thread, with the same id as the message"""
    EPHEMERAL = 1 << 6
    """this message is only visible to the user who invoked the Interaction"""
    LOADING = 1 << 7
    """this message is an Interaction Response and the bot is 'thinking'"""


class Message_Sticker_Item(DiscordObject):
    """
    The smallest amount of data required to render a sticker.
    """

    id: Snowflake = None
    """id of the sticker"""
    name: str = None
    """name of the sticker"""
    format_type: int = None
    """Type_Of_Sticker_Format"""


class Message_Sticker_Format_Types(Enum):
    PNG = 1
    APNG = 2
    LOTTIE = 3


class Message_Sticker(DiscordObject):
    """
    * The URL for fetching sticker assets is currently private.
    """

    id: Snowflake = None
    """id of the sticker"""
    pack_id: Optional[Snowflake] = None
    """id of the pack the sticker is from"""
    name: str = None
    """name of the sticker"""
    description: str = None
    """description of the sticker"""
    tags: str = None
    """for guild stickers, a unicode emoji representing the sticker's expression. for nitro stickers, a comma-separated list of related expressions."""
    asset: str = None
    """Deprecated previously the sticker asset hash, now an empty string"""
    format_type: int = None
    """Type_Of_Sticker_Format"""
    available: Optional[bool] = None
    """whether"""
    guild_id: Optional[Snowflake] = None
    """id of the guild that owns this sticker"""
    user: Optional["User"] = None
    """the user that uploaded the sticker"""
    sort_value: Optional[int] = None
    """a sticker's sort order within a pack"""


class Message_Reference(DiscordObject):
    """
    * `channel_id` is optional when creating a reply, but will always be present when receiving an event/response that includes this data model.
    """

    message_id: Optional[Snowflake] = None
    """id of the originating message"""
    channel_id: Snowflake = None
    """id of the originating message's channel"""
    guild_id: Optional[Snowflake] = None
    """id of the originating message's guild"""
    fail_if_not_exists: Optional[bool] = None
    """when sending, whether to error if the referenced message doesn't exist instead of sending as a normal"""


class Followed_Channel(DiscordObject):
    channel_id: Snowflake = None
    """source channel id"""
    webhook_id: Snowflake = None
    """created target webhook id"""


class Reaction(DiscordObject):
    count: int = None
    """times this emoji has been used to react"""
    me: bool = None
    """whether the current user reacted using this emoji"""
    emoji: "Emoji" = None
    """emoji information"""


class Overwrite(DiscordObject):
    id: Snowflake = None
    """role"""
    type: int = 0
    """either 0"""
    allow: str = None
    """permission bit set"""
    deny: str = None
    """permission bit set"""


class Thread_Metadata(DiscordObject):
    archived: bool = None
    """whether the thread is archived"""
    auto_archive_duration: int = None
    """duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080"""
    archive_timestamp: datetime = None
    """timestamp when the thread's archive status was last changed, used for calculating recent activity"""
    locked: Optional[bool] = None
    """when a thread is locked, only users with MANAGE_THREADS can unarchive it"""


class Thread_Member(DiscordObject):
    """
    ** * These fields are ommitted on the member sent within each thread in the [GUILD_CREATE](https:#/discord.com/developers/docs/topics/gateway#guild-create) event **
    """

    id: Snowflake = None
    """the id of the thread"""
    user_id: Snowflake = None
    """the id of the user"""
    join_timestamp: datetime = None
    """the time the current user last joined the thread"""
    flags: int = None
    """any user-thread settings, currently only used for notifications"""


class Embed(DiscordObject):
    title: Optional[str] = None
    """title of embed"""
    type: Optional[str] = None
    """Type_Of_Embed"""
    description: Optional[str] = None
    """description of embed"""
    url: Optional[str] = None
    """url of embed"""
    timestamp: Optional[datetime] = None
    """timestamp of embed content"""
    color: Optional[int] = None
    """color code of the embed"""
    footer: Optional["Embed_Footer"] = None
    """footer information"""
    image: Optional["Embed_Image"] = None
    """image information"""
    thumbnail: Optional["Embed_Thumbnail"] = None
    """thumbnail information"""
    video: Optional["Embed_Video"] = None
    """video information"""
    provider: Optional["Embed_Provider"] = None
    """provider information"""
    author: Optional["Embed_Author"] = None
    """author information"""
    fields: Optional[list["Embed_Field"]] = None
    """fields information"""


class Embed_Types(Enum):
    """
    Embed types are 'loosely defined' and, for the most part, are not used by our clients for rendering. Embed attributes power what is rendered. Embed types should be considered deprecated and might be removed in a future API version.
    """

    RICH = "generic embed rendered from embed attributes"
    IMAGE = "image embed"
    VIDEO = "video embed"
    GIFV = "animated gif image embed rendered as a video embed"
    ARTICLE = "article embed"
    LINK = "link embed"


class Embed_Thumbnail(DiscordObject):
    url: Optional[str] = None
    """source url of thumbnail"""
    proxy_url: Optional[str] = None
    """a proxied url of the thumbnail"""
    height: Optional[int] = None
    """height of thumbnail"""
    width: Optional[int] = None
    """width of thumbnail"""


class Embed_Video(DiscordObject):
    url: Optional[str] = None
    """source url of video"""
    proxy_url: Optional[str] = None
    """a proxied url of the video"""
    height: Optional[int] = None
    """height of video"""
    width: Optional[int] = None
    """width of video"""


class Embed_Image(DiscordObject):
    url: Optional[str] = None
    """source url of image"""
    proxy_url: Optional[str] = None
    """a proxied url of the image"""
    height: Optional[int] = None
    """height of image"""
    width: Optional[int] = None
    """width of image"""


class Embed_Provider(DiscordObject):
    name: Optional[str] = None
    """name of provider"""
    url: Optional[str] = None
    """url of provider"""


class Embed_Author(DiscordObject):
    name: Optional[str] = None
    """name of author"""
    url: Optional[str] = None
    """url of author"""
    icon_url: Optional[str] = None
    """url of author icon"""
    proxy_icon_url: Optional[str] = None
    """a proxied url of author icon"""


class Embed_Footer(DiscordObject):
    text: str = None
    """footer text"""
    icon_url: Optional[str] = None
    """url of footer icon"""
    proxy_icon_url: Optional[str] = None
    """a proxied url of footer icon"""


class Embed_Field(DiscordObject):
    name: str = None
    """name of the field"""
    value: str = None
    """value of the field"""
    inline: Optional[bool] = None
    """whether"""


class Attachment(DiscordObject):
    id: Snowflake = None
    """attachment id"""
    filename: str = None
    """name of file attached"""
    content_type: Optional[str] = None
    """Media_Type"""
    size: int = None
    """size of file in bytes"""
    url: str = None
    """source url of file"""
    proxy_url: str = None
    """a proxied url of file"""
    height: Optional[int | UnsetType] = UNSET
    """height of file"""
    width: Optional[int | UnsetType] = UNSET
    """width of file"""


class Channel_Mention(DiscordObject):
    id: Snowflake = None
    """id of the channel"""
    guild_id: Snowflake = None
    """id of the guild containing the channel"""
    type: int = None
    """Type_Of_Channel"""
    name: str = None
    """the name of the channel"""


class Allowed_Mention_Types(Enum):
    ROLE_MENTIONS = "roles"
    """Controls role mentions"""
    USER_MENTIONS = "users"
    """Controls user mentions"""
    EVERYONE_MENTIONS = "everyone"
    """Controls @everyone and @here mentions"""


class Allowed_Mentions(DiscordObject):
    parse: list[Allowed_Mention_Types] = None
    """Allowed_Mention_Types"""
    roles: list[Snowflake] = list
    """Array of role_ids to mention"""
    users: list[Snowflake] = list
    """Array of user_ids to mention"""
    replied_user: bool = None
    """For replies, whether to mention the author of the message being replied to"""


class Limits(IntEnum):
    """
    All of the following limits are measured inclusively. Leading and trailing whitespace characters are not included (they are trimmed automatically).
    Additionally, the characters in all `title`, `description`, `field.name`, `field.value`, `footer.text`, and `author.name` fields must not exceed 6000 characters in total. Violating any of these constraints will result in a `Bad Request` response.
    """

    TITLE = 256
    DESCRIPTION = 4096
    FIELDS = 25
    FIELD_NAME = 256
    FIELD_VALUE = 1024
    FOOTER_TEXT = 2048
    AUTHOR_NAME = 256


class Emoji(DiscordObject):
    id: Snowflake | UnsetType = UNSET
    """Emoji_Id"""
    name: str | UnsetType = UNSET
    """emoji name"""
    roles: Optional[list["Role"]] = None
    """roles allowed to use this emoji"""
    user: Optional["User"] = None
    """user that created this emoji"""
    require_colons: Optional[bool] = None
    """whether this emoji must be wrapped in colons"""
    managed: Optional[bool] = None
    """whether this emoji is managed"""
    animated: Optional[bool] = None
    """whether this emoji is animated"""
    available: Optional[bool] = None
    """whether this emoji can be used, may be false due to loss of Server Boosts"""


class Guild(DiscordObject):
    """
    ** * These fields are only sent within the [GUILD_CREATE](https:#/discord.com/developers/docs/topics/gateway#guild-create) event **
    ** ** These fields are only sent when using the [GET Current User Guilds](https:#/discord.com/developers/docs/resources/user#get-current-user-guilds) endpoint and are relative to the requested user **
    ** *** This field is deprecated and will be removed in v9 and is replaced by [rtc_region](https:#/discord.com/developers/docs/resources/channel#channel-object-channel-structure)**
    """

    id: Snowflake = None
    """guild id"""
    name: str = None
    """guild name"""
    icon: str | UnsetType = UNSET
    """Icon_Hash"""
    icon_hash: Optional[str | UnsetType] = UNSET
    """Icon_Hash"""
    splash: str | UnsetType = UNSET
    """Splash_Hash"""
    discovery_splash: str | UnsetType = UNSET
    """Discovery_Splash_Hash"""
    owner: bool = None
    """The_User"""
    owner_id: Snowflake = None
    """id of owner"""
    permissions: str = None
    """The_User"""
    region: str | UnsetType = UNSET
    """Voice_Region"""
    afk_channel_id: Snowflake | UnsetType = UNSET
    """id of afk channel"""
    afk_timeout: int = None
    """afk timeout in seconds"""
    widget_enabled: Optional[bool] = None
    """true if the server widget is enabled"""
    widget_channel_id: Optional[Snowflake | UnsetType] = UNSET
    """the channel id that the widget will generate an invite to,"""
    verification_level: int = None
    """Verification_Level"""
    default_message_notifications: int = None
    """Message_Notifications_Level"""
    explicit_content_filter: int = None
    """Explicit_Content_Filter_Level"""
    roles: list["Role"] = None
    """roles in the guild"""
    emojis: list[Emoji] = None
    """custom guild emojis"""
    features: list["Guild_Features"] = None
    """enabled guild features"""
    mfa_level: int = None
    """MFA_Level"""
    application_id: Snowflake | UnsetType = UNSET
    """application id of the guild creator if it is bot-created"""
    system_channel_id: Snowflake | UnsetType = UNSET
    """the id of the channel where guild notices such as welcome messages and boost events are posted"""
    system_channel_flags: int = None
    """System_Channel_Flags"""
    rules_channel_id: Snowflake | UnsetType = UNSET
    """the id of the channel where Community guilds can display rules and/or guidelines"""
    joined_at: datetime = None
    """when this guild was joined at"""
    large: bool = None
    """true if this is considered a large guild"""
    unavailable: bool = None
    """true if this guild is unavailable due to an outage"""
    member_count: int = None
    """total number of members in this guild"""
    voice_states: list["Voice_State"] = None
    """states of members currently in voice channels; lacks the `guild_id` key"""
    members: list["Guild_Member"] = None
    """users in the guild"""
    channels: list[Channel] = None
    """channels in the guild"""
    threads: list[Channel] = None
    """all active threads in the guild that current user has permission to view"""
    presences: list["Presence_Update"] = None
    """presences of the members in the guild, will only include non-offline members if the size is greater than `large threshold`"""
    max_presences: Optional[int | UnsetType] = UNSET
    """the maximum number of presences for the guild"""
    max_members: Optional[int] = None
    """the maximum number of members for the guild"""
    vanity_url_code: str | UnsetType = UNSET
    """the vanity url code for the guild"""
    description: str | UnsetType = UNSET
    """the description of a Community guild"""
    banner: str | UnsetType = UNSET
    """Banner_Hash"""
    premium_tier: int = None
    """Premium_Tier"""
    premium_subscription_count: Optional[int] = None
    """the number of boosts this guild currently has"""
    preferred_locale: str = None
    """the preferred locale of a Community guild; used in server discovery and notices from Discord; defaults to 'en-US'"""
    public_updates_channel_id: Snowflake | UnsetType = UNSET
    """the id of the channel where admins and moderators of Community guilds receive notices from Discord"""
    max_video_channel_users: Optional[int] = None
    """the maximum amount of users in a video channel"""
    approximate_member_count: Optional[int] = None
    """approximate number of members in this guild, returned from the `GET /guilds/<id>` endpoint when `with_counts` is `true`"""
    approximate_presence_count: Optional[int] = None
    """approximate number of non-offline members in this guild, returned from the `GET /guilds/<id>` endpoint when `with_counts` is `true`"""
    welcome_screen: Optional["Welcome_Screen"] = None
    """Invite"""
    nsfw_level: int = None
    """Guild_NSFW_Level"""
    stage_instances: list["Stage_Instance"] = None
    """Stage instances in the guild"""


class Default_Message_Notification_Level(Enum):
    ALL_MESSAGES = 0
    """members will receive notifications for all messages by default"""
    ONLY_MENTIONS = 1
    """members will receive notifications only for messages that @mention them by default"""


class Explicit_Content_Filter_Level(Enum):
    DISABLED = 0
    """media content will not be scanned"""
    MEMBERS_WITHOUT_ROLES = 1
    """media content sent by members without roles will be scanned"""
    ALL_MEMBERS = 2
    """media content sent by all members will be scanned"""


class MFA_Level(Enum):
    NONE = 0
    """guild has no MFA/2FA requirement for moderation actions"""
    ELEVATED = 1
    """guild has a 2FA requirement for moderation actions"""


class Verification_Level(Enum):
    NONE = 0
    """unrestricted"""
    LOW = 1
    """must have verified email on account"""
    MEDIUM = 2
    """must be registered on Discord for longer than 5 minutes"""
    HIGH = 3
    """must be a member of the server for longer than 10 minutes"""
    VERY_HIGH = 4
    """must have a verified phone number"""


class Guild_NSFW_Level(Enum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class Premium_Tier(Enum):
    NONE = 0
    """guild has not unlocked any Server Boost perks"""
    TIER_1 = 1
    """guild has unlocked Server Boost level 1 perks"""
    TIER_2 = 2
    """guild has unlocked Server Boost level 2 perks"""
    TIER_3 = 3
    """guild has unlocked Server Boost level 3 perks"""


class System_Channel_Flags(Flag):
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    """Suppress member join notifications"""
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    """Suppress server boost notifications"""
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    """Suppress server setup tips"""


class Guild_Features(Enum):
    ANIMATED_ICON = "guild has access to set an animated guild icon"
    BANNER = "guild has access to set a guild banner image"
    COMMERCE = "guild has access to use commerce features"
    COMMUNITY = "guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates"
    DISCOVERABLE = "guild is able to be discovered in the directory"
    FEATURABLE = "guild is able to be featured in the directory"
    INVITE_SPLASH = "guild has access to set an invite splash background"
    MEMBER_VERIFICATION_GATE_ENABLED = "Membership_Screening"
    NEWS = "guild has access to create news channels"
    PARTNERED = "guild is partnered"
    PREVIEW_ENABLED = "guild can be previewed before joining via Membership Screening"
    VANITY_URL = "guild has access to set a vanity URL"
    VERIFIED = "guild is verified"
    VIP_REGIONS = "guild has access to set 384kbps bitrate in voice"
    WELCOME_SCREEN_ENABLED = "guild has enabled the welcome screen"
    TICKETED_EVENTS_ENABLED = "guild has enabled ticketed events"
    MONETIZATION_ENABLED = "guild has enabled monetization"
    MORE_STICKERS = "guild has increased custom sticker slots"
    THREE_DAY_THREAD_ARCHIVE = "guild has access to the three day archive time for threads"
    SEVEN_DAY_THREAD_ARCHIVE = "guild has access to the seven day archive time for threads"
    PRIVATE_THREADS = "guild has access to create private threads"


class Guild_Preview(DiscordObject):
    id: Snowflake = None
    """guild id"""
    name: str = None
    """guild name"""
    icon: str | UnsetType = UNSET
    """Icon_Hash"""
    splash: str | UnsetType = UNSET
    """Splash_Hash"""
    discovery_splash: str | UnsetType = UNSET
    """Discovery_Splash_Hash"""
    emojis: list[Emoji] = None
    """custom guild emojis"""
    features: list[Guild_Features] = None
    """enabled guild features"""
    approximate_member_count: int = None
    """approximate number of members in this guild"""
    approximate_presence_count: int = None
    """approximate number of online members in this guild"""
    description: str | UnsetType = UNSET
    """the description for the guild, if the guild is discoverable"""


class Guild_Widget(DiscordObject):
    enabled: bool = None
    """whether the widget is enabled"""
    channel_id: Snowflake | UnsetType = UNSET
    """the widget channel id"""


class Guild_Member(DiscordObject):
    """
    > info
    > The field `user` won't be included in the member object attached to `MESSAGE_CREATE` and `MESSAGE_UPDATE` gateway events.
    > info
    > In `GUILD_` events, `pending` will always be included as true or false. In non `GUILD_` events which can only be triggered by non-`pending` users, `pending` will not be included.
    """

    user: Optional["User"] = None
    """the user this guild member represents"""
    nick: Optional[str | UnsetType] = UNSET
    """this users guild nickname"""
    roles: list[Snowflake] = None
    """Role"""
    joined_at: datetime = None
    """when the user joined the guild"""
    premium_since: Optional[datetime | UnsetType] = UNSET
    """Boosting"""
    deaf: bool = None
    """whether the user is deafened in voice channels"""
    mute: bool = None
    """whether the user is muted in voice channels"""
    pending: Optional[bool] = None
    """Membership_Screening"""
    permissions: Optional[str] = None
    """total permissions of the member in the channel, including overwrites, returned when in the interaction"""


class Integration(DiscordObject):
    """
    ** * These fields are not provided for discord bot integrations. **
    """

    id: Snowflake = None
    """integration id"""
    name: str = None
    """integration name"""
    type: str = None
    """integration type"""
    enabled: bool = None
    """is this integration enabled"""
    syncing: bool = None
    """is this integration syncing"""
    role_id: Snowflake = None
    """id that this integration uses for 'subscribers'"""
    enable_emoticons: bool = None
    """whether emoticons should be synced for this integration"""
    expire_behavior: "Integration_Expire_Behaviors" = None
    """the behavior of expiring subscribers"""
    expire_grace_period: int = None
    """the grace period"""
    user: "User" = None
    """user for this integration"""
    account: "Integration_Account" = None
    """integration account information"""
    synced_at: datetime = None
    """when this integration was last synced"""
    subscriber_count: int = None
    """how many subscribers this integration has"""
    revoked: bool = None
    """has this integration been revoked"""
    application: Optional[Application] = None
    """The bot/OAuth2 application for discord integrations"""


class Integration_Expire_Behaviors(Enum):
    REMOVE_ROLE = 0
    KICK = 1


class Integration_Account(DiscordObject):
    id: str = None
    """id of the account"""
    name: str = None
    """name of the account"""


class Integration_Application(DiscordObject):
    id: Snowflake = None
    """the id of the app"""
    name: str = None
    """the name of the app"""
    icon: str | UnsetType = UNSET
    """Icon_Hash"""
    description: str = None
    """the description of the app"""
    summary: str = None
    """the summary of the app"""
    bot: Optional["User"] = None
    """the bot associated with this application"""


class Ban(DiscordObject):
    reason: str | UnsetType = UNSET
    """the reason for the ban"""
    user: "User" = None
    """the banned user"""


class Welcome_Screen(DiscordObject):
    description: str | UnsetType = UNSET
    """the server description shown in the welcome screen"""
    welcome_channels: "Welcome_Screen_Channel" = None
    """the channels shown in the welcome screen, up to 5"""


class Welcome_Screen_Channel(DiscordObject):
    channel_id: Snowflake = None
    """the channel's id"""
    description: str = None
    """the description shown for the channel"""
    emoji_id: Snowflake | UnsetType = UNSET
    """Emoji_Id"""
    emoji_name: str | UnsetType = UNSET
    """the emoji name if custom, the unicode character if standard,"""


class Invite(DiscordObject):
    code: str = None
    """the invite code"""
    guild: Optional[Guild] = None
    """the guild this invite is for"""
    channel: Channel = None
    """the channel this invite is for"""
    inviter: Optional["User"] = None
    """the user who created the invite"""
    target_type: Optional[int] = None
    """Type_Of_Target"""
    target_user: Optional["User"] = None
    """the user whose stream to display for this voice channel stream invite"""
    target_application: Optional[Application] = None
    """the embedded application to open for this voice channel embedded application invite"""
    approximate_presence_count: Optional[int] = None
    """approximate count of online members, returned from the `GET /invites/<code>` endpoint when `with_counts` is `true`"""
    approximate_member_count: Optional[int] = None
    """approximate count of total members, returned from the `GET /invites/<code>` endpoint when `with_counts` is `true`"""
    expires_at: Optional[datetime | UnsetType] = UNSET
    """the expiration date of this invite, returned from the `GET /invites/<code>` endpoint when `with_expiration` is `true`"""
    stage_instance: Optional["Invite_Stage_Instance"] = None
    """Public_Stage_Instance"""


class Invite_Target_Types(Enum):
    STREAM = 1
    EMBEDDED_APPLICATION = 2


class Invite_Metadata(DiscordObject):
    uses: int = None
    """number of times this invite has been used"""
    max_uses: int = None
    """max number of times this invite can be used"""
    max_age: int = None
    """duration"""
    temporary: bool = None
    """whether this invite only grants temporary membership"""
    created_at: datetime = None
    """when this invite was created"""


class Invite_Stage_Instance(DiscordObject):
    members: list[Guild_Member] = None
    """the members speaking in the Stage"""
    participant_count: int = None
    """the number of users in the Stage"""
    speaker_count: int = None
    """the number of users speaking in the Stage"""
    topic: str = None
    """the topic of the Stage instance"""


class Stage_Instance(DiscordObject):
    id: Snowflake = None
    """The id of this Stage instance"""
    guild_id: Snowflake = None
    """The guild id of the associated Stage channel"""
    channel_id: Snowflake = None
    """The id of the associated Stage channel"""
    topic: str = None
    """The topic of the Stage instance"""
    privacy_level: int = None
    """Privacy_Level"""
    discoverable_disabled: bool = None
    """Whether"""


class Privacy_Level(Enum):
    PUBLIC = 1
    """The Stage instance is visible publicly, such as on Stage discovery."""
    GUILD_ONLY = 2
    """The Stage instance is visible to only guild members."""


class User(DiscordObject):
    id: Snowflake = None
    """the user's id"""
    username: str = None
    """the user's username, not unique across the platform"""
    discriminator: str = None
    """the user's 4-digit discord-tag"""
    avatar: str | UnsetType = UNSET
    """Avatar_Hash"""
    bot: Optional[bool] = None
    """whether the user belongs to an OAuth2 application"""
    system: Optional[bool] = None
    """whether the user is an Official Discord System user"""
    mfa_enabled: Optional[bool] = None
    """whether the user has two factor enabled on their account"""
    locale: Optional[str] = None
    """the user's chosen language option"""
    verified: Optional[bool] = None
    """whether the email on this account has been verified"""
    email: Optional[str | UnsetType] = UNSET
    """the user's email"""
    flags: Optional[int] = None
    """Flags"""
    premium_type: Optional[int] = None
    """Type_Of_Nitro_Subscription"""
    public_flags: Optional[int] = None
    """Flags"""


class User_Flags(Flag):
    NONE = 0
    """None"""
    DISCORD_EMPLOYEE = 1 << 0
    """Discord Employee"""
    PARTNERED_SERVER_OWNER = 1 << 1
    """Partnered Server Owner"""
    HYPESQUAD_EVENTS = 1 << 2
    """HypeSquad Events"""
    BUG_HUNTER_LEVEL_1 = 1 << 3
    """Bug Hunter Level 1"""
    HOUSE_BRAVERY = 1 << 6
    """House Bravery"""
    HOUSE_BRILLIANCE = 1 << 7
    """House Brilliance"""
    HOUSE_BALANCE = 1 << 8
    """House Balance"""
    EARLY_SUPPORTER = 1 << 9
    """Early Supporter"""
    TEAM_USER = 1 << 10
    """Team User"""
    SYSTEM = 1 << 12
    BUG_HUNTER_LEVEL_2 = 1 << 14
    """Bug Hunter Level 2"""
    VERIFIED_BOT = 1 << 16
    """Verified Bot"""
    EARLY_VERIFIED_BOT_DEVELOPER = 1 << 17
    """Early Verified Bot Developer"""
    DISCORD_CERTIFIED_MODERATOR = 1 << 18
    """Discord Certified Moderator"""


class Premium_Types(Enum):
    """
    Premium types denote the level of premium a user has. Visit the [Nitro](https:##discord.com/nitro) page to learn more about the premium plans we currently offer.
    """

    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2


class Connection(DiscordObject):
    id: str = None
    """id of the connection account"""
    name: str = None
    """the username of the connection account"""
    type: str = None
    """the service of the connection"""
    revoked: Optional[bool] = None
    """whether the connection is revoked"""
    integrations: Optional[list[Integration]] = None
    """Server_Integrations"""
    verified: bool = None
    """whether the connection is verified"""
    friend_sync: bool = None
    """whether friend sync is enabled for this connection"""
    show_activity: bool = None
    """whether activities related to this connection will be shown in presence updates"""
    visibility: int = None
    """Visibility"""


class Visibility_Types(Enum):
    NONE = 0
    """invisible to everyone except the user themselves"""
    EVERYONE = 1
    """visible to everyone"""


class Voice_State(DiscordObject):
    guild_id: Optional[Snowflake] = None
    """the guild id this voice state is for"""
    channel_id: Snowflake | UnsetType = UNSET
    """the channel id this user is connected to"""
    user_id: Snowflake = None
    """the user id this voice state is for"""
    member: Optional[Guild_Member] = None
    """the guild member this voice state is for"""
    session_id: str = None
    """the session id for this voice state"""
    deaf: bool = None
    """whether this user is deafened by the server"""
    mute: bool = None
    """whether this user is muted by the server"""
    self_deaf: bool = None
    """whether this user is locally deafened"""
    self_mute: bool = None
    """whether this user is locally muted"""
    self_stream: Optional[bool] = None
    """whether this user is streaming using 'Go Live'"""
    self_video: bool = None
    """whether this user's camera is enabled"""
    suppress: bool = None
    """whether this user is muted by the current user"""
    request_to_speak_timestamp: datetime | UnsetType = UNSET
    """the time at which the user requested to speak"""


class Voice_Region(DiscordObject):
    id: str = None
    """unique ID for the region"""
    name: str = None
    """name of the region"""
    vip: bool = None
    """true if this is a vip-only server"""
    optimal: bool = None
    """true for a single server that is closest to the current user's client"""
    deprecated: bool = None
    """whether this is a deprecated voice region"""
    custom: bool = None
    """whether this is a custom voice region"""


class Webhook(DiscordObject):
    id: Snowflake = None
    """the id of the webhook"""
    type: int = None
    """Type"""
    guild_id: Optional[Snowflake | UnsetType] = UNSET
    """the guild id this webhook is for, if any"""
    channel_id: Snowflake | UnsetType = UNSET
    """the channel id this webhook is for, if any"""
    user: Optional[User] = None
    """the user this webhook was created by"""
    name: str | UnsetType = UNSET
    """the default name of the webhook"""
    avatar: str | UnsetType = UNSET
    """Hash"""
    token: Optional[str] = None
    """the secure token of the webhook"""
    application_id: Snowflake | UnsetType = UNSET
    """the bot/OAuth2 application that created this webhook"""
    source_guild: Optional[Guild] = None
    """the guild of the channel that this webhook is following"""
    source_channel: Optional[Channel] = None
    """the channel that this webhook is following"""
    url: Optional[str] = None
    """Webhooks"""


class Webhook_Types(Enum):
    INCOMING = 1
    """Incoming Webhooks can post messages to channels with a generated token"""
    CHANNEL_FOLLOWER = 2
    """Channel Follower Webhooks are internal webhooks used with Channel Following to post new messages into channels"""
    APPLICATION = 3
    """Application webhooks are webhooks used with Interactions"""


class Gateway_Versions(Enum):
    _4: None | UnsetType = "recommended"
    _3: None | UnsetType = "available"
    _2: None | UnsetType = "available"
    _1: None | UnsetType = "default"


class Gateway_Payload(DiscordObject):
    """
    * `s` and `t` are `null` when `op` is not `0` (Gateway Dispatch Opcode).
    """

    op: int = None
    """Opcode"""
    d: dict | UnsetType = UNSET
    """event data"""
    s: int | UnsetType = UNSET
    """sequence number, used for resuming sessions and heartbeats"""
    t: str | UnsetType = UNSET
    """the event name for this payload"""


class Gateway_URL_Query_String_Params(DiscordObject):
    """
    The first step in establishing connectivity to the gateway is requesting a valid websocket endpoint from the API. This can be done through either the [Get Gateway](https:#/discord.com/developers/docs/topics/gateway#get-gateway) or the [Get Gateway Bot](https:#/discord.com/developers/docs/topics/gateway#get-gateway-bot) endpoint.
    With the resulting payload, you can now open a websocket connection to the 'url' (or endpoint) specified. Generally, it is a good idea to explicitly pass the gateway version and encoding. For example, we may connect to `wss://gateway.discord.gg/?v=9&encoding=json`.
    Once connected, the client should immediately receive an [Opcode 10 Hello](https:#/discord.com/developers/docs/topics/gateway#hello) payload, with information on the connection's heartbeat interval:
    """

    v: int = None
    """Gateway Version to use"""
    encoding: str = None
    """The encoding of received gateway packets"""
    compress: Optional[str] = None
    """The"""


class Identify(DiscordObject):
    token: str = None
    """authentication token"""
    properties: "Identify_Connection_Properties" = None
    """Connection_Properties"""
    compress: Optional[bool] = False
    """whether this connection supports compression of packets"""
    large_threshold: Optional[int] = 50
    """value between 50 and 250, total number of members where the gateway will stop sending offline members in the guild member list"""
    shard: Optional[list[int]] = None
    """Guild_Sharding"""
    presence: Optional["Presence_Update"] = None
    """presence structure for initial presence information"""
    intents: int = None
    """Gateway_Intents"""


class Identify_Connection_Properties(DiscordObject):
    os: str = None
    """your operating system"""
    browser: str = None
    """your library name"""
    device: str = None
    """your library name"""


class Resume(DiscordObject):
    token: str = None
    """session token"""
    session_id: str = None
    """session id"""
    seq: int = 0
    """last sequence number received"""


class Guild_Request_Members(DiscordObject):
    """
    > info
    > Nonce can only be up to 32 bytes. If you send an invalid nonce it will be ignored and the reply member_chunk(s) will not have a nonce set.
    """

    guild_id: Snowflake = None
    """id of the guild to get members for"""
    query: Optional[str] = None
    """string that username starts with,"""
    limit: int = None
    """maximum number of members to send matching the `query`; a limit of `0` can be used with an empty string `query` to return all members"""
    presences: Optional[bool] = None
    """used to specify if we want the presences of the matched members"""
    user_ids: Optional[list[Snowflake]] = None
    """used to specify which users you wish to fetch"""
    nonce: Optional[str] = None
    """Guild_Members_Chunk"""


class Gateway_Voice_State_Update(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    channel_id: Snowflake | UnsetType = UNSET
    """id of the voice channel client wants to join"""
    self_mute: bool = None
    """is the client muted"""
    self_deaf: bool = None
    """is the client deafened"""


class Gateway_Presence_Update(DiscordObject):
    since: int | UnsetType = UNSET
    """unix time"""
    activities: "Activity" = None
    """the user's activities"""
    status: str = None
    """Status"""
    afk: bool = None
    """whether"""


class Status_Types(Enum):
    ONLINE = "Online"
    DND = "Do Not Disturb"
    IDLE = "AFK"
    INVISIBLE = "Invisible and shown as offline"
    OFFLINE = "Offline"


class Hello(DiscordObject):
    heartbeat_interval: int = None
    """the interval"""


class Ready(DiscordObject):
    v: int = None
    """Gateway_Version"""
    user: User = None
    """information about the user including email"""
    guilds: list[Guild] = None
    """the guilds the user is in"""
    session_id: str = None
    """used for resuming connections"""
    shard: Optional[tuple[int, int]] = None
    """Shard_Information"""
    application: Application = None
    """contains `id` and `flags`"""


class Thread_List_Sync(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    channel_ids: Optional[list[Snowflake]] = None
    """the parent channel ids whose threads are being synced.  If omitted, then threads were synced for the entire guild.  This array may contain channel_ids that have no active threads as well, so you know to clear that data."""
    threads: list[Channel] = None
    """all active threads in the given channels that the current user can access"""
    members: list[Thread_Member] = None
    """all thread member s from the synced threads for the current user, indicating which threads the current user has been added to"""


class Thread_Members_Update(DiscordObject):
    id: Snowflake = None
    """the id of the thread"""
    guild_id: Snowflake = None
    """the id of the guild"""
    member_count: int = None
    """the approximate number of members in the thread, capped at 50"""
    added_members: Optional[Thread_Member] = None
    """the users who were added to the thread"""
    removed_member_ids: Optional[list[Snowflake]] = None
    """the id of the users who were removed from the thread"""


class Channel_Pins_Update(DiscordObject):
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""
    channel_id: Snowflake = None
    """the id of the channel"""
    last_pin_timestamp: Optional[datetime | UnsetType] = UNSET
    """the time at which the most recent pinned message was pinned"""


class Guild_Ban_Add(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    user: User = None
    """the banned user"""


class Guild_Ban_Remove(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    user: User = None
    """the unbanned user"""


class Guild_Emojis_Update(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    emojis: list[Emoji] = None
    """Emojis"""


class Guild_Integrations_Update(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild whose integrations were updated"""


class Guild_Member_Add(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""


class Guild_Member_Remove(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    user: User = None
    """the user who was removed"""


class Guild_Member_Update(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    roles: list[Snowflake] = None
    """user role ids"""
    user: User = None
    """the user"""
    nick: Optional[str | UnsetType] = UNSET
    """nickname of the user in the guild"""
    joined_at: datetime | UnsetType = UNSET
    """when the user joined the guild"""
    premium_since: Optional[datetime | UnsetType] = UNSET
    """Boosting"""
    deaf: Optional[bool] = None
    """whether the user is deafened in voice channels"""
    mute: Optional[bool] = None
    """whether the user is muted in voice channels"""
    pending: Optional[bool] = None
    """Membership_Screening"""
    communication_disabled_until: datetime = None


class Guild_Members_Chunk(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    members: list[Guild_Member] = None
    """set of guild members"""
    chunk_index: int = None
    """the chunk index in the expected chunks for this response"""
    chunk_count: int = None
    """the total number of expected chunks for this response"""
    not_found: Optional[list] = None
    """if passing an invalid id to `REQUEST_GUILD_MEMBERS`, it will be returned here"""
    presences: Optional[list["Presence_Update"]] = None
    """if passing true to `REQUEST_GUILD_MEMBERS`, presences of the returned members will be here"""
    nonce: Optional[str] = None
    """Guild_Members_Request"""


class Guild_Role_Create(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    role: "Role" = None
    """the role created"""


class Guild_Role_Update(DiscordObject):
    guild_id: Snowflake = None
    """the id of the guild"""
    role: "Role" = None
    """the role updated"""


class Guild_Role_Delete(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    role_id: Snowflake = None
    """id of the role"""


class Integration_Create(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""


class Integration_Update(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""


class Integration_Delete(DiscordObject):
    id: Snowflake = None
    """integration id"""
    guild_id: Snowflake = None
    """id of the guild"""
    application_id: Optional[Snowflake] = None
    """id of the bot/OAuth2 application for this discord integration"""


class Invite_Create(DiscordObject):
    channel_id: Snowflake = None
    """the channel the invite is for"""
    code: str = None
    """Code"""
    created_at: datetime = None
    """the time at which the invite was created"""
    guild_id: Optional[Snowflake] = None
    """the guild of the invite"""
    inviter: Optional[User] = None
    """the user that created the invite"""
    max_age: int = None
    """how long the invite is valid for"""
    max_uses: int = None
    """the maximum number of times the invite can be used"""
    target_type: Optional[int] = None
    """Type_Of_Target"""
    target_user: Optional[User] = None
    """the user whose stream to display for this voice channel stream invite"""
    target_application: Optional[Application] = None
    """the embedded application to open for this voice channel embedded application invite"""
    temporary: bool = None
    """whether"""
    uses: int = None
    """how many times the invite has been used"""


class Invite_Delete(DiscordObject):
    channel_id: Snowflake = None
    """the channel of the invite"""
    guild_id: Optional[Snowflake] = None
    """the guild of the invite"""
    code: str = None
    """Code"""


class Message_Delete(DiscordObject):
    id: Snowflake = None
    """the id of the message"""
    channel_id: Snowflake = None
    """the id of the channel"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""


class Message_Delete_Bulk(DiscordObject):
    ids: list[Snowflake] = None
    """the ids of the messages"""
    channel_id: Snowflake = None
    """the id of the channel"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""


class Message_Reaction_Add(DiscordObject):
    user_id: Snowflake = None
    """the id of the user"""
    channel_id: Snowflake = None
    """the id of the channel"""
    message_id: Snowflake = None
    """the id of the message"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""
    member: Optional[Guild_Member] = None
    """the member who reacted if this happened in a guild"""
    emoji: Emoji = None
    """Example"""


class Message_Reaction_Remove(DiscordObject):
    user_id: Snowflake = None
    """the id of the user"""
    channel_id: Snowflake = None
    """the id of the channel"""
    message_id: Snowflake = None
    """the id of the message"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""
    emoji: Emoji = None
    """Example"""


class Message_Reaction_Remove_All(DiscordObject):
    channel_id: Snowflake = None
    """the id of the channel"""
    message_id: Snowflake = None
    """the id of the message"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""


class Message_Reaction_Remove_Emoji(DiscordObject):
    channel_id: Snowflake = None
    """the id of the channel"""
    guild_id: Optional[Snowflake] = None
    """the id of the guild"""
    message_id: Snowflake = None
    """the id of the message"""
    emoji: Emoji = None
    """the emoji that was removed"""


class Presence_Update(DiscordObject):
    user: User = None
    """the user presence is being updated for"""
    guild_id: Snowflake = None
    """id of the guild"""
    status: str = None
    """either 'idle', 'dnd', 'online',"""
    activities: list["Activity"] = None
    """user's current activities"""
    client_status: "Client_Status" = None
    """user's platform-dependent status"""


class Client_Status(DiscordObject):
    """
    Active sessions are indicated with an 'online', 'idle', or 'dnd' string per platform. If a user is offline or invisible, the corresponding field is not present.
    """

    desktop: Optional[str] = None
    """the user's status set for an active desktop"""
    mobile: Optional[str] = None
    """the user's status set for an active mobile"""
    web: Optional[str] = None
    """the user's status set for an active web"""


class Bot_Activity(DiscordObject):
    name: str = ""
    type: "Activity_Types" = None
    url: str = ""


class Activity(DiscordObject):
    """
    > info
    > Bots are only able to send `name`, `type`, and optionally `url`.
    """

    name: str = None
    """the activity's name"""
    type: int = None
    """Activity_Type"""
    url: Optional[str | UnsetType] = UNSET
    """stream url, is validated when type is 1"""
    created_at: int = None
    """unix timestamp"""
    timestamps: Optional["Activity_Timestamps"] = None
    """unix timestamps for start and/or end of the game"""
    application_id: Optional[Snowflake] = None
    """application id for the game"""
    details: Optional[str | UnsetType] = UNSET
    """what the player is currently doing"""
    state: Optional[str | UnsetType] = UNSET
    """the user's current party status"""
    emoji: Optional[Emoji | UnsetType] = UNSET
    """the emoji used for a custom status"""
    party: Optional["Activity_Party"] = None
    """information for the current party of the player"""
    assets: Optional["Activity_Assets"] = None
    """images for the presence and their hover texts"""
    secrets: Optional["Activity_Secrets"] = None
    """secrets for Rich Presence joining and spectating"""
    instance: Optional[bool] = None
    """whether"""
    flags: Optional[int] = None
    """Activity_Flags"""
    buttons: Optional["Activity_Buttons"] = None
    """the custom buttons shown in the Rich Presence"""


class Activity_Types(Enum):
    """
    > info
    > The streaming type currently only supports Twitch and YouTube. Only `https://twitch.tv/` and `https://youtube.com/` urls will work.
    """

    GAME = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


class Activity_Timestamps(DiscordObject):
    start: Optional[int] = None
    """unix time"""
    end: Optional[int] = None
    """unix time"""


class Activity_Emoji(DiscordObject):
    name: str = None
    """the name of the emoji"""
    id: Optional[Snowflake] = None
    """the id of the emoji"""
    animated: Optional[bool] = None
    """whether this emoji is animated"""


class Activity_Party(DiscordObject):
    id: Optional[str] = None
    """the id of the party"""
    size: Optional[tuple[int, int]] = None
    """used to show the party's current and maximum size"""


class Activity_Assets(DiscordObject):
    large_image: Optional[str] = None
    """the id for a large asset of the activity, usually a snowflake"""
    large_text: Optional[str] = None
    """text displayed when hovering over the large image of the activity"""
    small_image: Optional[str] = None
    """the id for a small asset of the activity, usually a snowflake"""
    small_text: Optional[str] = None
    """text displayed when hovering over the small image of the activity"""


class Activity_Secrets(DiscordObject):
    join: Optional[str] = None
    """the secret for joining a party"""
    spectate: Optional[str] = None
    """the secret for spectating a game"""
    match: Optional[str] = None
    """the secret for a specific instanced match"""


class Activity_Flags(Flag):
    INSTANCE = 1 << 0
    JOIN = 1 << 1
    SPECTATE = 1 << 2
    JOIN_REQUEST = 1 << 3
    SYNC = 1 << 4
    PLAY = 1 << 5


class Activity_Buttons(DiscordObject):
    """
    When received over the gateway, the `buttons` field is an array of strings, which are the button labels. Bots cannot access a user's activity button URLs. When sending, the `buttons` field must be an array of the below object:
    """

    label: str = None
    """the text shown on the button"""
    url: str = None
    """the url opened when clicking the button"""


class Typing_Start(DiscordObject):
    channel_id: Snowflake = None
    """id of the channel"""
    guild_id: Optional[Snowflake] = None
    """id of the guild"""
    user_id: Snowflake = None
    """id of the user"""
    timestamp: int = None
    """unix time"""
    member: Optional[Guild_Member] = None
    """the member who started typing if this happened in a guild"""


class Voice_Server_Update(DiscordObject):
    token: str = None
    """voice connection token"""
    guild_id: Snowflake = None
    """the guild this voice server update is for"""
    endpoint: str | UnsetType = UNSET
    """the voice server host"""


class Webhook_Update(DiscordObject):
    guild_id: Snowflake = None
    """id of the guild"""
    channel_id: Snowflake = None
    """id of the channel"""


class Application_Command(DiscordObject):
    id: Snowflake = None
    type: "Application_Command_Type" = 1
    application_id: Snowflake = None
    guild_id: Snowflake = None
    """id of the guild the command is in"""
    name: str = ""
    name_localizations: dict[str, str] = dict
    description: str = ""
    description_localizations: dict[str, str] = dict
    options: list["Application_Command_Option"] = list
    default_member_permissions: str = None
    dm_permissions: bool = True
    default_permission: bool = False
    version: int = None


class Application_Command_Type(Enum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


class Application_Command_Extra_Fields(Application_Command):
    """
    Attributes
    ----------
    guild_id:
        id of the guild the command is in
    """

    guild_id: Snowflake = None


class Application_Command_Create(Application_Command_Extra_Fields):
    pass


class Application_Command_Update(Application_Command_Extra_Fields):
    pass


class Application_Command_Delete(Application_Command_Extra_Fields):
    pass


class Gateway_Bot(DiscordObject):
    """
    Parameters
    ----------
    url:
        The WSS URL that can be used for connecting to the gateway
    shards:
        Shards
    session_start_limit:
        Information on the current session start limit
    """

    url: str = ""
    shards: int = 0
    session_start_limit: "Session_Start_Limit" = None


class Session_Start_Limit(DiscordObject):
    total: int = None
    """The total number of session starts the current user is allowed"""
    remaining: int = None
    """The remaining number of session starts the current user is allowed"""
    reset_after: int = None
    """The number of milliseconds after which the limit resets"""
    max_concurrency: int = None
    """The number of identify requests allowed per 5 seconds"""


class OAuth2_URLs(Enum):
    """
    > warn
    > In accordance with the relevant RFCs, the token and token revocation URLs will **only** accept a content type of `x-www-form-urlencoded`. JSON content is not permitted and will return an error.
    """

    BASE_AUTHORIZATION_URL = "https://discord.com/api/oauth2/authorize"
    TOKEN_URL = "https://discord.com/api/oauth2/token"
    TOKEN_REVOCATION = "https://discord.com/api/oauth2/token/revoke"


class OAuth2_Scopes(Enum):
    """
    These are a list of all the OAuth2 scopes that Discord supports. Some scopes require approval from Discord to use. Requesting them from a user without approval from Discord may cause undocumented/error behavior in the OAuth2 flow.
    > info
    > `guilds.join` and `bot` require you to have a bot account linked to your application. Also, in order to add a user to a guild, your bot has to already belong to that guild.
    """

    ACTIVITIES_READ = (
        "allows your app to fetch data from a users Now Playing/Recently Played list - requires Discord approval"
    )
    ACTIVITIES_WRITE = "GAMESDK_ACTIVITY_MANAGER"
    APPLICATIONS_BUILDS_READ = "allows your app to read build data for a users applications"
    APPLICATIONS_BUILDS_UPLOAD = (
        "allows your app to upload/update builds for a users applications - requires Discord approval"
    )
    APPLICATIONS_COMMANDS = "Slash_Commands"
    APPLICATIONS_COMMANDS_UPDATE = "Slash_Commands"
    APPLICATIONS_ENTITLEMENTS = "allows your app to read entitlements for a users applications"
    APPLICATIONS_STORE_UPDATE = "allows your app to read and update store data"
    BOT = "for oauth2 bots, this puts the bot in the users selected guild by default"
    CONNECTIONS = "/users/@me/connections"
    EMAIL = "/users/@me"
    GDM_JOIN = "Join_Users_To_A_Group_Dm"
    GUILDS = "/users/@me/guilds"
    GUILDS_JOIN = "/guilds/{guild.id}/members/{user.id}"
    IDENTIFY = "/users/@me"
    MESSAGES_READ = "for local rpc server api access, this allows you to read messages from all client channels"
    RELATIONSHIPS_READ = (
        "allows your app to know a users friends and implicit relationships - requires Discord approval"
    )
    RPC = "for local rpc server access, this allows you to control a users local Discord client - requires Discord approval"
    RPC_ACTIVITIES_WRITE = (
        "for local rpc server access, this allows you to update a users activity - requires Discord approval"
    )
    RPC_NOTIFICATIONS_READ = "for local rpc server access, this allows you to receive notifications pushed out to the user - requires Discord approval"
    RPC_VOICE_READ = "for local rpc server access, this allows you to read a users voice settings and listen for voice events - requires Discord approval"
    RPC_VOICE_WRITE = (
        "for local rpc server access, this allows you to update a users voice settings - requires Discord approval"
    )
    WEBHOOK_INCOMING = (
        "this generates a webhook that is returned in the oauth token response for authorization code grants"
    )


class Bot_Auth_Parameters(DiscordObject):
    client_id: str = None
    """your app's client id"""
    scope: str = None
    """needs to include `bot` for the bot flow"""
    permissions: str = None
    """Permissions"""
    guild_id: Snowflake = None
    """pre-fills the dropdown picker with a guild for the user"""
    disable_guild_select: bool = None
    """`true`"""


class Gateway_Opcodes(Enum):
    DISPATCH = 0
    """An event was dispatched."""
    HEARTBEAT = 1
    """Fired periodically by the client to keep the connection alive."""
    IDENTIFY = 2
    """Starts a new session during the initial handshake."""
    PRESENCE_UPDATE = 3
    """Update the client's presence."""
    VOICE_STATE_UPDATE = 4
    """Used to join/leave"""
    RESUME = 6
    """Resume a previous session that was disconnected."""
    RECONNECT = 7
    """You should attempt to reconnect and resume immediately."""
    REQUEST_GUILD_MEMBERS = 8
    """Request information about offline guild members in a large guild."""
    INVALID_SESSION = 9
    """The session has been invalidated. You should reconnect and identify/resume accordingly."""
    HELLO = 10
    """Sent immediately after connecting, contains the `heartbeat_interval` to use."""
    HEARTBEAT_ACK = 11
    """Sent in response to receiving a heartbeat to acknowledge that it has been received."""


class Gateway_Close_Event_Codes(Enum):
    """
    Attributes
    ----------
    4000:
        Unknown error
    4001:
        Unknown opcode
    4002:
        Decode error
    4003:
        Not authenticated
    4004:
        Authentication failed
    4005:
        Already authenticated
    4007:
        Invalid `seq`
    4008:
        Rate limited
    4009:
        Session timed out
    4010:
        Invalid shard
    4011:
        Sharding required
    4012:
        Invalid API version
    4013:
        Invalid intent
    4014:
        Disallowed intent
    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQ = 4007
    RATE_LIMITED = 4008
    SESSION_TIMED_OUT = 4009
    INVALID_SHARD = 4010
    SHARDING_REQUIRED = 4011
    INVALID_API_VERSION = 4012
    INVALID_INTENT = 4013
    DISALLOWED_INTENT = 4014


class Voice_Opcodes(Enum):
    IDENTIFY = 0
    """Begin a voice websocket connection."""
    SELECT_PROTOCOL = 1
    """Select the voice protocol."""
    READY = 2
    """Complete the websocket handshake."""
    HEARTBEAT = 3
    """Keep the websocket connection alive."""
    SESSION_DESCRIPTION = 4
    """Describe the session."""
    SPEAKING = 5
    """Indicate which users are speaking."""
    HEARTBEAT_ACK = 6
    """Sent to acknowledge a received client heartbeat."""
    RESUME = 7
    """Resume a connection."""
    HELLO = 8
    """Time to wait between sending heartbeats in milliseconds."""
    RESUMED = 9
    """Acknowledge a successful session resume."""
    CLIENT_DISCONNECT = 13
    """A client has disconnected from the voice channel"""


class Voice_Close_Event_Codes(Enum):
    """
    Attributes
    ----------
    4001:
        Unknown opcode
    4002:
        Failed to decode payload
    4003:
        Not authenticated
    4004:
        Authentication failed
    4005:
        Already authenticated
    4006:
        Session no longer valid
    4009:
        Session timeout
    4011:
        Server not found
    4012:
        Unknown protocol
    4014:
        Disconnected
    4015:
        Voice server crashed
    4016:
        Unknown encryption mode
    """

    UNKNOWN_OPCODE = 4001
    FAILED_TO_DECODE_PAYLOAD = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    SESSION_NO_LONGER_VALID = 4006
    SESSION_TIMEOUT = 4009
    SERVER_NOT_FOUND = 4011
    UNKNOWN_PROTOCOL = 4012
    DISCONNECTED = 4014
    VOICE_SERVER_CRASHED = 4015
    UNKNOWN_ENCRYPTION_MODE = 4016


class HTTP_Response_Codes(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TOO_MANY_REQUESTS = 429
    SERVER_ERROR = 500
    GATEWAY_UNAVAILABLE = 502


class JSON_Error(Enum):
    GENERAL_ERROR = 0
    UNKNOWN_ACCOUNT = 10001
    UNKNOWN_APPLICATION = 10002
    UNKNOWN_CHANNEL = 10003
    UNKNOWN_GUILD = 10004
    UNKNOWN_INTEGRATION = 10005
    UNKNOWN_INVITE = 10006
    UNKNOWN_MEMBER = 10007
    UNKNOWN_MESSAGE = 10008
    UNKNOWN_PERMISSION_OVERWRITE = 10009
    UNKNOWN_PROVIDER = 10010
    UNKNOWN_ROLE = 10011
    UNKNOWN_TOKEN = 10012
    UNKNOWN_USER = 10013
    UNKNOWN_EMOJI = 10014
    UNKNOWN_WEBHOOK = 10015
    UNKNOWN_WEBHOOK_SERVICE = 10016
    UNKNOWN_SESSION = 10020
    UNKNOWN_BAN = 10026
    UNKNOWN_SKU = 10027
    UNKNOWN_STORE_LISTING = 10028
    UNKNOWN_ENTITLEMENT = 10029
    UNKNOWN_BUILD = 10030
    UNKNOWN_LOBBY = 10031
    UNKNOWN_BRANCH = 10032
    UNKNOWN_STORE_DIRECTORY_LAYOUT = 10033
    UNKNOWN_REDISTRIBUTABLE = 10036
    UNKNOWN_GIFT_CODE = 10038
    UNKNOWN_GUILD_TEMPLATE = 10057
    UNKNOWN_DISCOVERABLE_SERVER_CATEGORY = 10059
    UNKNOWN_STICKER = 10060
    UNKNOWN_INTERACTION = 10062
    UNKNOWN_APPLICATION_COMMAND = 10063
    UNKNOWN_APPLICATION_COMMAND_PERMISSIONS = 10066
    UNKNOWN_STAGE_INSTANCE = 10067
    UNKNOWN_GUILD_MEMBER_VERIFICATION_FORM = 10068
    UNKNOWN_GUILD_WELCOME_SCREEN = 10069
    BOTS_CANNOT_USE_THIS_ENDPOINT = 20001
    ONLY_BOTS_CAN_USE_THIS_ENDPOINT = 20002
    EXPLICIT_CONTENT_CANNOT_BE_SENT_TO_THE_DESIRED_RECIPIENT = 20009
    YOU_ARE_NOT_AUTHORIZED_TO_PERFORM_THIS_ACTION_ON_THIS_APPLICATION = 20012
    THIS_ACTION_CANNOT_BE_PERFORMED_DUE_TO_SLOWMODE_RATE_LIMIT = 20016
    ONLY_THE_OWNER_OF_THIS_ACCOUNT_CAN_PERFORM_THIS_ACTION = 20018
    THIS_MESSAGE_CANNOT_BE_EDITED_DUE_TO_ANNOUNCEMENT_RATE_LIMITS = 20022
    THE_CHANNEL_YOU_ARE_WRITING_HAS_HIT_THE_WRITE_RATE_LIMIT = 20028
    YOUR_STAGE_TOPIC__SERVER_NAME__SERVER_DESCRIPTION_ = 20031
    GUILD_PREMIUM_SUBSCRIPTION_LEVEL_TOO_LOW = 20035
    MAXIMUM_NUMBER_OF_GUILDS_REACHED = 30001
    MAXIMUM_NUMBER_OF_FRIENDS_REACHED = 30002
    MAXIMUM_NUMBER_OF_PINS_REACHED_FOR_THE_CHANNEL = 30003
    MAXIMUM_NUMBER_OF_RECIPIENTS_REACHED = 30004
    MAXIMUM_NUMBER_OF_GUILD_ROLES_REACHED = 30005
    MAXIMUM_NUMBER_OF_WEBHOOKS_REACHED = 30007
    MAXIMUM_NUMBER_OF_EMOJIS_REACHED = 30008
    MAXIMUM_NUMBER_OF_REACTIONS_REACHED = 30010
    MAXIMUM_NUMBER_OF_GUILD_CHANNELS_REACHED = 30013
    MAXIMUM_NUMBER_OF_ATTACHMENTS_IN_A_MESSAGE_REACHED = 30015
    MAXIMUM_NUMBER_OF_INVITES_REACHED = 30016
    MAXIMUM_NUMBER_OF_ANIMATED_EMOJIS_REACHED = 30018
    MAXIMUM_NUMBER_OF_SERVER_MEMBERS_REACHED = 30019
    MAXIMUM_NUMBER_OF_SERVER_CATEGORIES_HAS_BEEN_REACHED = 30030
    GUILD_ALREADY_HAS_A_TEMPLATE = 30031
    MAX_NUMBER_OF_THREAD_PARTICIPANTS_HAS_BEEN_REACHED = 30033
    MAXIMUM_NUMBER_OF_BANS_FOR_NON_GUILD_MEMBERS_HAVE_BEEN_EXCEEDED = 30035
    MAXIMUM_NUMBER_OF_BANS_FETCHES_HAS_BEEN_REACHED = 30037
    MAXIMUM_NUMBER_OF_STICKERS_REACHED = 30039
    UNAUTHORIZED__PROVIDE_A_VALID_TOKEN_AND_TRY_AGAIN = 40001
    YOU_NEED_TO_VERIFY_YOUR_ACCOUNT_IN_ORDER_TO_PERFORM_THIS_ACTION = 40002
    YOU_ARE_OPENING_DIRECT_MESSAGES_TOO_FAST = 40003
    REQUEST_ENTITY_TOO_LARGE__TRY_SENDING_SOMETHING_SMALLER_IN_SIZE = 40005
    THIS_FEATURE_HAS_BEEN_TEMPORARILY_DISABLED_SERVER_SIDE = 40006
    THE_USER_IS_BANNED_FROM_THIS_GUILD = 40007
    TARGET_USER_IS_NOT_CONNECTED_TO_VOICE = 40032
    THIS_MESSAGE_HAS_ALREADY_BEEN_CROSSPOSTED = 40033
    AN_APPLICATION_COMMAND_WITH_THAT_NAME_ALREADY_EXISTS = 40041
    MISSING_ACCESS = 50001
    INVALID_ACCOUNT_TYPE = 50002
    CANNOT_EXECUTE_ACTION_ON_A_DM_CHANNEL = 50003
    GUILD_WIDGET_DISABLED = 50004
    CANNOT_EDIT_A_MESSAGE_AUTHORED_BY_ANOTHER_USER = 50005
    CANNOT_SEND_AN_EMPTY_MESSAGE = 50006
    CANNOT_SEND_MESSAGES_TO_THIS_USER = 50007
    CANNOT_SEND_MESSAGES_IN_A_VOICE_CHANNEL = 50008
    CHANNEL_VERIFICATION_LEVEL_IS_TOO_HIGH_FOR_YOU_TO_GAIN_ACCESS = 50009
    OAUTH2_APPLICATION_DOES_NOT_HAVE_A_BOT = 50010
    OAUTH2_APPLICATION_LIMIT_REACHED = 50011
    INVALID_OAUTH2_STATE = 50012
    YOU_LACK_PERMISSIONS_TO_PERFORM_THAT_ACTION = 50013
    INVALID_AUTHENTICATION_TOKEN_PROVIDED = 50014
    NOTE_WAS_TOO_LONG = 50015
    PROVIDED_TOO_FEW = 50016
    A_MESSAGE_CAN_ONLY_BE_PINNED_TO_THE_CHANNEL_IT_WAS_SENT_IN = 50019
    INVITE_CODE_WAS_EITHER_INVALID = 50020
    CANNOT_EXECUTE_ACTION_ON_A_SYSTEM_MESSAGE = 50021
    CANNOT_EXECUTE_ACTION_ON_THIS_CHANNEL_TYPE = 50024
    INVALID_OAUTH2_ACCESS_TOKEN_PROVIDED = 50025
    MISSING_REQUIRED_OAUTH2_SCOPE = 50026
    INVALID_WEBHOOK_TOKEN_PROVIDED = 50027
    INVALID_ROLE = 50028
    _INVALID_RECIPIENT = 50033
    A_MESSAGE_PROVIDED_WAS_TOO_OLD_TO_BULK_DELETE = 50034
    INVALID_FORM_BODY = 50035
    AN_INVITE_WAS_ACCEPTED_TO_A_GUILD_THE_APPLICATION_S_BOT_IS_NOT_IN = 50036
    INVALID_API_VERSION_PROVIDED = 50041
    CANNOT_SELF_REDEEM_THIS_GIFT = 50054
    PAYMENT_SOURCE_REQUIRED_TO_REDEEM_GIFT = 50070
    CANNOT_DELETE_A_CHANNEL_REQUIRED_FOR_COMMUNITY_GUILDS = 50074
    INVALID_STICKER_SENT = 50081
    TRIED_TO_PERFORM_AN_OPERATION_ON_AN_ARCHIVED_THREAD__SUCH_AS_EDITING_A_MESSAGE = 50083
    INVALID_THREAD_NOTIFICATION_SETTINGS = 50084
    _BEFORE__VALUE_IS_EARLIER_THAN_THE_THREAD_CREATION_DATE = 50085
    TWO_FACTOR_IS_REQUIRED_FOR_THIS_OPERATION = 60003
    NO_USERS_WITH_DISCORDTAG_EXIST = 80004
    REACTION_WAS_BLOCKED = 90001
    API_RESOURCE_IS_CURRENTLY_OVERLOADED__TRY_AGAIN_A_LITTLE_LATER = 130000
    THE_STAGE_IS_ALREADY_OPEN = 150006
    A_THREAD_HAS_ALREADY_BEEN_CREATED_FOR_THIS_MESSAGE = 160004
    THREAD_IS_LOCKED = 160005
    MAXIMUM_NUMBER_OF_ACTIVE_THREADS_REACHED = 160006
    MAXIMUM_NUMBER_OF_ACTIVE_ANNOUNCEMENT_THREADS_REACHED = 160007


class RPC_Error(Enum):
    UNKNOWN_ERROR = 1000
    """An unknown error occurred."""
    INVALID_PAYLOAD = 4000
    """You sent an invalid payload."""
    INVALID_COMMAND = 4002
    """Invalid command name specified."""
    INVALID_GUILD = 4003
    """Invalid guild ID specified."""
    INVALID_EVENT = 4004
    """Invalid event name specified."""
    INVALID_CHANNEL = 4005
    """Invalid channel ID specified."""
    INVALID_PERMISSIONS = 4006
    """You lack permissions to access the given resource."""
    INVALID_CLIENT_ID = 4007
    """An invalid OAuth2 application ID was used to authorize"""
    INVALID_ORIGIN = 4008
    """An invalid OAuth2 application origin was used to authorize"""
    INVALID_TOKEN = 4009
    """An invalid OAuth2 token was used to authorize"""
    INVALID_USER = 4010
    """The specified user ID was invalid."""
    OAUTH2_ERROR = 5000
    """A standard OAuth2 error occurred; check the data  for the OAuth2 error details."""
    SELECT_CHANNEL_TIMED_OUT = 5001
    """An asynchronous `SELECT_TEXT_CHANNEL`/`SELECT_VOICE_CHANNEL` command timed out."""
    GET_GUILD_TIMED_OUT = 5002
    """An asynchronous `GET_GUILD` command timed out."""
    SELECT_VOICE_FORCE_REQUIRED = 5003
    """You tried to join a user to a voice channel but the user was already in one."""
    CAPTURE_SHORTCUT_ALREADY_LISTENING = 5004
    """You tried to capture more than one shortcut key at once."""


class RPC_Close_Event_Codes(Enum):
    INVALID_CLIENT_ID = 4000
    """You connected to the RPC server with an invalid client ID."""
    INVALID_ORIGIN = 4001
    """You connected to the RPC server with an invalid origin."""
    RATE_LIMITED = 4002
    """You are being rate limited."""
    TOKEN_REVOKED = 4003
    """The OAuth2 token associated with a connection was revoked, get a new one!"""
    INVALID_VERSION = 4004
    """The RPC Server version specified in the connection string was not valid."""
    INVALID_ENCODING = 4005
    """The encoding specified in the connection string was not valid."""


class Intents(Flag):
    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_BANS = 1 << 2
    GUILD_EMOJIS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14


class Bitwise_Permission_Flags(Flag):
    """
    *** These permissions require the owner account to use [two-factor authentication](https:#/discord.com/developers/docs/topics/oauth2#twofactor-authentication-requirement) when used on a guild that has server-wide 2FA enabled.**
    Note that these internal permission names may be referred to differently by the Discord client. For example, 'Manage Permissions' refers to MANAGE_ROLES and 'Use Voice Activity' refers to USE_VAD.
    """

    CREATE_INSTANT_INVITE = 0x0000000001
    """Allows creation of instant invites"""
    KICK_MEMBERS = 0x0000000002
    """Allows kicking members"""
    BAN_MEMBERS = 0x0000000004
    """Allows banning members"""
    ADMINISTRATOR = 0x0000000008
    """Allows all permissions and bypasses channel permission overwrites"""
    MANAGE_CHANNELS = 0x0000000010
    """Allows management and editing of channels"""
    MANAGE_GUILD = 0x0000000020
    """Allows management and editing of the guild"""
    ADD_REACTIONS = 0x0000000040
    """Allows for the addition of reactions to messages"""
    VIEW_AUDIT_LOG = 0x0000000080
    """Allows for viewing of audit logs"""
    PRIORITY_SPEAKER = 0x0000000100
    """Allows for using priority speaker in a voice channel"""
    STREAM = 0x0000000200
    """Allows the user to go live"""
    VIEW_CHANNEL = 0x0000000400
    """Allows guild members to view a channel, which includes reading messages in text channels"""
    SEND_MESSAGES = 0x0000000800
    """Allows for sending messages in a channel"""
    SEND_TTS_MESSAGES = 0x0000001000
    """Allows for sending of `/tts` messages"""
    MANAGE_MESSAGES = 0x0000002000
    """Allows for deletion of other users messages"""
    EMBED_LINKS = 0x0000004000
    """Links sent by users with this permission will be auto-embedded"""
    ATTACH_FILES = 0x0000008000
    """Allows for uploading images and files"""
    READ_MESSAGE_HISTORY = 0x0000010000
    """Allows for reading of message history"""
    MENTION_EVERYONE = 0x0000020000
    """Allows for using the `@everyone` tag to notify all users in a channel, and the `@here` tag to notify all online users in a channel"""
    USE_EXTERNAL_EMOJIS = 0x0000040000
    """Allows the usage of custom emojis from other servers"""
    VIEW_GUILD_INSIGHTS = 0x0000080000
    """Allows for viewing guild insights"""
    CONNECT = 0x0000100000
    """Allows for joining of a voice channel"""
    SPEAK = 0x0000200000
    """Allows for speaking in a voice channel"""
    MUTE_MEMBERS = 0x0000400000
    """Allows for muting members in a voice channel"""
    DEAFEN_MEMBERS = 0x0000800000
    """Allows for deafening of members in a voice channel"""
    MOVE_MEMBERS = 0x0001000000
    """Allows for moving of members between voice channels"""
    USE_VAD = 0x0002000000
    """Allows for using voice-activity-detection in a voice channel"""
    CHANGE_NICKNAME = 0x0004000000
    """Allows for modification of own nickname"""
    MANAGE_NICKNAMES = 0x0008000000
    """Allows for modification of other users nicknames"""
    MANAGE_ROLES = 0x0010000000
    """Allows management and editing of roles"""
    MANAGE_WEBHOOKS = 0x0020000000
    """Allows management and editing of webhooks"""
    MANAGE_EMOJIS = 0x0040000000
    """Allows management and editing of emojis"""
    USE_SLASH_COMMANDS = 0x0080000000
    """Allows members to use slash commands in text channels"""
    REQUEST_TO_SPEAK = 0x0100000000
    """Allows for requesting to speak in stage channels."""
    MANAGE_THREADS = 0x0400000000
    """Allows for deleting and archiving threads, and viewing all private threads"""
    USE_PUBLIC_THREADS = 0x0800000000
    """Allows for creating and participating in threads"""
    USE_PRIVATE_THREADS = 0x1000000000
    """Allows for creating and participating in private threads"""


class Role(DiscordObject):
    """
    Roles without colors (`color == 0`) do not count towards the final computed color in the user list.
    """

    id: Snowflake = None
    """role id"""
    name: str = None
    """role name"""
    color: int = None
    """integer representation of hexadecimal color code"""
    hoist: bool = None
    """if this role is pinned in the user listing"""
    icon: str = None
    unicode_emoji: str = None
    position: int = None
    """position of this role"""
    permissions: str = None
    """permission bit set"""
    managed: bool = None
    """whether this role is managed by an integration"""
    mentionable: bool = None
    """whether this role is mentionable"""
    tags: Optional[list["Role_Tags"]] = None
    """the tags this role has"""


class Role_Tags(DiscordObject):
    bot_id: Optional[Snowflake] = None
    """the id of the bot this role belongs to"""
    integration_id: Optional[Snowflake] = None
    """the id of the integration this role belongs to"""
    premium_subscriber: Optional[bool] = None
    """whether this is the guild's premium subscriber role"""


class Rate_Limit_Response(DiscordObject):
    """
    Note that the normal rate-limiting headers will be sent in this response. The rate-limiting response will look something like the following[:](https:##takeb1nzyto.space/)
    """

    message: str = None
    """A message saying you are being rate limited."""
    retry_after: float = None
    """The number of seconds to wait before submitting another request."""
    _global: bool = None
    """A value indicating if you are being globally rate limited"""


class Team(DiscordObject):
    icon: str | UnsetType = UNSET
    """a hash of the image of the team's icon"""
    id: Snowflake = None
    """the unique id of the team"""
    members: list["Team_Members"] = None
    """the members of the team"""
    name: str = None
    """the name of the team"""
    owner_user_id: Snowflake = None
    """the user id of the current team owner"""


class Team_Members(DiscordObject):
    membership_state: int = None
    """Membership_State"""
    permissions: list[str] = None
    """will always be `['']`"""
    team_id: Snowflake = None
    """the id of the parent team of which they are a member"""
    user: User = None
    """the avatar, discriminator, id, and username of the user"""


class Membership_State_Enum(Enum):
    INVITED = 1
    ACCEPTED = 2


class Encryption_Modes(Enum):
    """
    >warn
    >The nonce has to be stripped from the payload before encrypting and before decrypting the audio data
    Finally, the voice server will respond with a [Opcode 4 Session Description](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) that includes the `mode` and `secret_key`, a 32 byte array used for [encrypting and sending](https:#/discord.com/developers/docs/topics/voice_connections#encrypting-and-sending-voice) voice data:
    """

    NORMAL = "xsalsa20_poly1305"
    SUFFIX = "xsalsa20_poly1305_suffix"
    LITE = "xsalsa20_poly1305_lite"


class Voice_Packet(DiscordObject):
    Version_Flags: c_byte = 0x80
    Payload_Type: c_byte = 0x78
    Sequence: c_ushort = 0x0
    Timestamp: c_uint = 0x0
    SSRC: c_uint = 0x0
    Encrypted_audio: bytearray = 0x0


class Speaking(Enum):
    """
    To notify clients that you are speaking or have stopped speaking, send an [Opcode 5 Speaking](https://discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload:
    Example Speaking Payload
    > You must send at least one [Opcode 5 Speaking](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload before sending voice data, or you will be disconnected with an invalid SSRC error.```json
    """

    MICROPHONE = 1 << 0
    """Normal transmission of voice audio"""
    SOUNDSHARE = 1 << 1
    """Transmission of context audio for video, no speaking indicator"""
    PRIORITY = 1 << 2
    """Priority speaker, lowering audio of other speakers"""


class IP_Discovery(DiscordObject):
    """
    Generally routers on the Internet mask or obfuscate UDP ports through a process called NAT. Most users who implement voice will want to utilize IP discovery to find their external IP and port which will then be used for receiving voice communications. To retrieve your external IP and port, send the following UDP packet to your voice port (all numeric are big endian):

    Attributes
    ----------
    Type:
        Values 0x1 and 0x2 indicate request and response, respectively
    Length:
        Message length excluding Type and Length fields
    SSRC:
        Unsigned integer
    Address:
        Null-terminated string in response
    Port:
        Unsigned short
    """

    Type: int = 0x1 or 0x2
    Length: int = None
    SSRC: c_uint = None
    Address: str = None
    Port: c_ushort = None


class API_Versions(Enum):
    _9 = "Available"
    _8 = "Available"
    _7 = "Doesnt look like anything to me"
    _6 = "Deprecated"
    _5 = "Discontinued"
    _4 = "Discontinued"
    _3 = "Discontinued"


class Snowflake_ID_Format(Enum):
    """
    Parameters
    ----------
    Timestamp:
        Milliseconds since Discord Epoch, the first second of 2015
    Internal worker ID:
        `
    Internal process ID:
        `
    Increment:
        For every ID that is generated on that process, this number is incremented
    """

    Timestamp = (0 >> 22) + DISCORD_EPOCH
    Internal_worker_ID = (0 & 0x3E0000) >> 17
    Internal_process_ID = (0 & 0x1F000) >> 12
    Increment = 0 & 0xFFF


class Formats(Enum):
    """
    Using the markdown for either users, roles, or channels will usually mention the target(s) accordingly, but this can be suppressed using the `allowed_mentions` parameter when creating a message. Standard emoji are currently rendered using [Twemoji](https:##twemoji.twitter.com/) for Desktop/Android and Apple's native emoji on iOS.
    Timestamps will display the given timestamp in the user's timezone and locale.
    """

    User = "<@USER_ID>"
    Nickname = "<@!{user_id}>"
    Channel = "<#{channel_id}>"
    Role = "<@&{role_id}>"
    Standard_Emoji = "Unicode Characters"
    Custom_Emoji = "<:{name}:{id}>"
    Custom_Animated_Emoji = "<a:{name}:{id}>"
    Unix_Timestamp = "<t:{TIMESTAMP}>"
    Unix_Timestamp_Styled = "<t:{TIMESTAMP}:{STYLE}>"


class Timestamp_Styles(Enum):
    """
    *default

    Attributes
    ----------
    Short Time:
        16:20
    Long Time:
        16:20:30
    Short Date:
        20/04/2021
    Long Date:
        20 April 2021
    Short Date/Time:
        20 April 2021 16:20
    Long Date/Time:
        Tuesday, 20 April 2021 16:20
    Relative Time:
        2 months ago
    """

    SHORT_TIME = "t"
    LONG_TIME = "T"
    SHORT_DATE = "d"
    LONG_DATE = "D"
    SHORT_DATE_TIME = "f"
    LONG_DATE_TIME = "F"
    RELATIVE_TIME = "R"


class Image_Formats(Enum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    WEBP = "webp"
    GIF = "gif"


class CDN_Endpoints(Enum):
    """
    * In the case of endpoints that support GIFs, the hash will begin with `a_` if it is available in GIF format. (example: `a_1269e74af4df7417b13759eae50c83dc`)
    ** In the case of the Default User Avatar endpoint, the value for `user_discriminator` in the path should be the user's discriminator modulo 5—Test#1337 would be `1337 % 5`, which evaluates to 2.
    *** In the case of the Default User Avatar endpoint, the size of images returned is constant with the 'size' querystring parameter being ignored.
    """

    CUSTOM_EMOJI = "emojis/{emoji_id}.png"
    GUILD_ICON = "icons/{guild_id}/{guild_icon}.png"
    GUILD_SPLASH = "splashes/{guild_id}/{guild_splash}.png"
    GUILD_DISCOVERY_SPLASH = "discovery-splashes/{guild_id}/{guild_discovery_splash}.png"
    GUILD_BANNER = "banners/{guild_id}/{guild_banner}.png"
    DEFAULT_USER_AVATAR = "embed/avatars/{user_discriminator}.png"
    USER_AVATAR = "avatars/{user_id}/{user_avatar}.png"
    APPLICATION_ICON = "app-icons/{application_id}/{icon}.png"
    APPLICATION_COVER = "app-assets/{application_id}/cover_image.png"
    APPLICATION_ASSET = "app-assets/{application_id}/{asset_id}.png"
    ACHIEVEMENT_ICON = "app-assets/{application_id}/achievements/{achievement_id}/icons/{icon_hash}.png"
    TEAM_ICON = "team-icons/{team_id}/{team_icon}.png"
    STICKER = "stickers/{sticker_id}.png"
    ROLE_ICON = "role-icons/{role_id}/{role_icon}.png"


class Component(DiscordObject):
    type: "Component_Types" = None
    """Component_Type"""
    style: Optional["Button_Styles"] = None
    """Button_Styles"""
    label: Optional[str] = None
    """text that appears on the button, max 80 characters"""
    emoji: Optional[Emoji] = None
    """`name`, `id`, and `animated`"""
    custom_id: Optional[str] = None
    """a developer-defined identifier for the button, max 100 characters"""
    url: Optional[str] = None
    """a url for link-style buttons"""
    disabled: Optional[bool] = None
    """whether the button is disabled, default `false`"""
    components: Optional[list["Component"]] = None
    """a list of child components"""
    options: list["Select_Option"] = None
    placeholder: str = None
    min_values: int = None
    max_values: int = None
    value: str = None
    required: bool = None
    min_length: int = None
    max_length: int = None


class Component_Types(Enum):
    ACTION_ROW = 1
    """A container for other components"""
    BUTTON = 2
    """A button"""
    SELECT_MENU = 3
    """A select menu for picking from choices"""
    TEXT_INPUT = 4


class Text_Input_Styles(Enum):
    Short = 1
    Paragraph = 2


class Button(DiscordObject):
    """
    Buttons come in a variety of styles to convey different types of actions. These styles also define what fields are valid for a button.
    - Non-link buttons **must** have a `custom_id`, and cannot have a `url`
    - Link buttons **must** have a `url`, and cannot have a `custom_id`
    - Link buttons do not send an [interaction](https:#/discord.com/developers/docs/interactions/slash_commands#interaction-object) to your app when clicked
    """

    type: Component_Types = Component_Types.BUTTON
    """`2` for a button"""
    style: "Button_Styles" = None
    """Button_Styles"""
    label: Optional[str] = None
    """text that appears on the button, max 80 characters"""
    emoji: Optional[Emoji] = None
    """`name`, `id`, and `animated`"""
    custom_id: Optional[str] = None
    """a developer-defined identifier for the button, max 100 characters"""
    url: Optional[str] = None
    """a url for link-style buttons"""
    disabled: Optional[bool] = None
    """whether the button is disabled"""


class Button_Styles(Enum):
    """
    ![An image showing the different button styles](button-styles.png)
    When a user clicks on a button, your app will receive an [interaction](https:#/discord.com/developers/docs/interactions/slash_commands#interaction-object) including the message the button was on:
    """

    PRIMARY = 1
    """Blurple, requires `custom_id`"""
    SECONDARY = 2
    """Grey, requires `custom_id`"""
    SUCCESS = 3
    """Green, requires `custom_id`"""
    DANGER = 4
    """Red, requires `custom_id`"""
    LINK = 5
    """Grey, requires `url`"""


class Select_Menu(DiscordObject):
    type: Component_Types = Component_Types.SELECT_MENU
    custom_id: str = None
    """a developer-defined identifier for the button, max 100 characters"""
    options: Annotated[list["Select_Option"], Meta(max_length=25)] = None
    """the choices in the select, max 25"""
    placeholder: Optional[str] = None
    """custom placeholder text if nothing is selected, max 100 characters"""
    min_values: Optional[Annotated[int, Meta(ge=0, le=25)]] = None
    """the minimum number of items that must be chosen; default 1, min 0, max 25"""
    max_values: Optional[Annotated[int, Meta(ge=1, le=25)]] = None
    """the maximum number of items that can be chosen; default 1, max 25"""
    disabled: Optional[bool] = None
    """disable the select, default false"""


class Select_Option(DiscordObject):
    label: Annotated[str, Meta(max_length=25)] = None
    """the user-facing name of the option, max 25 characters"""
    value: Annotated[str, Meta(max_length=100)] = None
    """the dev-define value of the option, max 100 characters"""
    description: Optional[Annotated[str, Meta(max_length=50)]] = None
    """an additional description of the option, max 50 characters"""
    emoji: Optional[Emoji] = None
    """`id`, `name`, and `animated`"""
    default: Optional[bool] = None
    """will render this option as selected by default"""


class Application_Command(DiscordObject):
    """
    > info
    > warn
    > Required `options` must be listed before optional options
    """

    id: Snowflake = None
    """unique id of the command"""
    application_id: Snowflake = None
    """unique id of the parent application"""
    guild_id: Optional[Snowflake] = None
    """guild id of the command, if not global"""
    name: Annotated[str, Meta(min_length=1, max_length=32, pattern=r"^[\w-]{1,32}$")] = None
    """1-32 lowercase character name matching `^[\\w-]{1,32}$`"""
    description: Annotated[str, Meta(min_length=1, max_length=100)] = None
    """1-100 character description"""
    options: Optional[list["Application_Command_Option"]] = None
    """the parameters for the command"""
    default_permission: Optional[bool] = None
    """whether the command is enabled by default when the app is added to a guild"""


class Application_Command_Option(DiscordObject):
    """
    > info
    """

    type: int = None
    """Application_Command_Option_Type"""
    name: Annotated[str, Meta(min_length=1, max_length=32, pattern=r"^[\w-]{1,32}$")] = None
    """1-32 lowercase character name matching `^[\\w-]{1,32}$`"""
    name_localizations: dict[str, str] = None
    description: Annotated[str, Meta(min_length=1, max_length=100)] = None
    """1-100 character description"""
    description_localizations: dict[str, str] = None
    required: Optional[bool] = None
    """if the parameter is required"""
    choices: Optional[list["Application_Command_Option_Choice"]] = None
    """choices for `string` and `int` types for the user to pick from"""
    options: Optional[list["Application_Command_Option"]] = None
    """if the option is a subcommand"""
    channel_types: list[Channel_Types] = list
    min_value: Union[int, float] = None
    max_value: Union[int, float] = None
    autocomplete: bool = False


class Application_Command_Option_Type(Enum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10
    ATTACHMENT = 11


class Application_Command_Option_Choice(DiscordObject):
    """
    If you specify `choices` for an option, they are the **only** valid values for a user to pick
    """

    name: str = None
    """1-100 character choice name"""
    name_localizations: dict[str, str] = dict
    value: str = None
    """value of the choice, up to 100 characters if string"""


class Guild_Application_Command_Permissions(DiscordObject):
    """
    Returned when fetching the permissions for a command in a guild.
    """

    id: Snowflake = None
    """the id of the command"""
    application_id: Snowflake = None
    """the id of the application the command belongs to"""
    guild_id: Snowflake = None
    """the id of the guild"""
    permissions: list["Application_Command_Permissions"] = None
    """the permissions for the command in the guild"""


class Application_Command_Permissions(DiscordObject):
    """
    Application command permissions allow you to enable or disable commands for specific users or roles within a guild.
    """

    id: Snowflake = None
    """the id of the role"""
    type: "Application_Command_Permission_Type" = None
    """role"""
    permission: bool = None
    """`true` to allow, `false`, to disallow"""


class Application_Command_Permission_Type(Enum):
    ROLE = 1
    USER = 2
    CHANNEL = 3


class Interaction(DiscordObject):
    """
    * This is always present on application command interaction types. It is optional for future-proofing against new interaction types
    ** `member` is sent when the command is invoked in a guild, and `user` is sent when invoked in a DM
    """

    id: Snowflake = None
    """id of the interaction"""
    application_id: Snowflake = None
    """id of the application this interaction is for"""
    type: "Interaction_Request_Type" = None
    """the type of interaction"""
    data: "Application_Command_Interaction_Data" = None
    """the command data payload"""
    guild_id: Optional[Snowflake] = None
    """the guild it was sent from"""
    channel_id: Optional[Snowflake] = None
    """the channel it was sent from"""
    member: Guild_Member = None
    """guild member data for the invoking user, including permissions"""
    user: Optional[User] = None
    """user  for the invoking user, if invoked in a DM"""
    token: str = None
    """a continuation token for responding to the interaction"""
    version: int = None
    """read-only property, always `1`"""
    message: Optional[Message] = None
    """for components, the message they were attached to"""
    locale: str = None
    guild_locale: str = None


class Interaction_Request_Type(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class Application_Command_Interaction_Data(DiscordObject):
    id: Snowflake = None
    """the ID of the invoked command"""
    name: str = None
    """the name of the invoked command"""
    type: Interaction_Request_Type = None
    resolved: Optional["Application_Command_Interaction_Data_Resolved"] = None
    """converted users + roles + channels"""
    options: Optional[list["Application_Command_Interaction_Data_Option"]] = None
    """the params + values from the user"""
    custom_id: str = None
    """`custom_id`"""
    component_type: int = None
    """Type"""
    values: list[str] = list
    target_id: Snowflake = 0
    components: list[Component] = list


class Application_Command_Interaction_Data_Resolved(DiscordObject):
    """
    > info
    * Partial `Member` objects are missing `user`, `deaf` and `mute` fields
    ** Partial `Channel` objects only have `id`, `name`, `type` and `permissions` fields
    """

    users: Optional[dict[Snowflake, User]] = None
    """the ids and User s"""
    members: dict[Snowflake, Guild_Member] = None
    """the ids and  Member s"""
    roles: Optional[dict[Snowflake, Role]] = None
    """the ids and Role s"""
    channels: dict[Snowflake, Channel] = None
    """the ids and  Channel s"""
    messages: dict[Snowflake, Message] = dict
    attachments: dict[Snowflake, Attachment] = dict


class Application_Command_Interaction_Data_Option(DiscordObject):
    """
    All options have names, and an option can either be a parameter and input value--in which case `value` will be set--or it can denote a subcommand or group--in which case it will contain a top-level key and another array of `options`.
    """

    name: str = None
    """the name of the parameter"""
    type: int = None
    """Application_Command_Option_Type"""
    value: Optional[Application_Command_Option_Type] = None
    """the value of the pair"""
    options: Optional["Application_Command_Interaction_Data_Option"] = None
    """present if this option is a group"""
    focused: bool = None


class Interaction_Callback_Type(Enum):
    """
    * Only valid for [component-based](https:#/discord.com/developers/docs/interactions/message_components#) interactions
    """

    PONG = 1
    """ACK a `Ping`"""
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    """respond to an interaction with a message"""
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    """ACK an interaction and edit a response later, the user sees a loading state"""
    DEFERRED_UPDATE_MESSAGE = 6
    """for components, ACK an interaction and edit the original message later; the user does not see a loading state"""
    UPDATE_MESSAGE = 7
    """for components, edit the message the component was attached to"""
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9


class Interaction_Application_Command_Callback_Data(DiscordObject):
    """
    Not all message fields are currently supported.
    """

    tts: Optional[bool] = None
    """is the response TTS"""
    content: Optional[str] = None
    """message content"""
    embeds: Optional[list[Embed]] = None
    """supports up to 10 embeds"""
    allowed_mentions: Optional[Allowed_Mentions] = None
    """Allowed_Mentions"""
    flags: Optional[int] = None
    """Interaction_Application_Command_Callback_Data_Flags"""
    components: Optional[list[Component]] = None
    """message components"""
    attachments: list[Attachment] = None
    choices: list[Application_Command_Option_Choice] = None
    custom_id: str = None
    title: str = None


class Interaction_Application_Command_Callback_Data_Flags(Flag):
    EPHEMERAL = 1 << 6
    """only the user receiving the message can see it"""


class Message_Interaction(DiscordObject):
    id: Snowflake = None
    """id of the interaction"""
    type: Interaction_Request_Type = None
    """the type of interaction"""
    name: str = None
    """Application_Command"""
    user: User = None
    """the user who invoked the interaction"""


class Gateway_Commands(Events):
    """
    Events are payloads sent over the socket to a client that correspond to events in Discord.

    Parameters
    ----------
    Identify:
        triggers the initial handshake with the gateway
    Resume:
        resumes a dropped gateway connection
    Heartbeat:
        maintains an active gateway connection
    Request_Guild_Members:
        requests members for a guild
    Update_Voice_State:
        joins, moves,
    Update_Status:
        updates a client's presence
    """

    Identify = staticmethod(Identify)
    Resume = staticmethod(Resume)
    Heartbeat = staticmethod(int)
    Request_Guild_Members = staticmethod(Guild_Request_Members)
    Update_Voice_State = staticmethod(Gateway_Voice_State_Update)
    Update_Status = staticmethod(Gateway_Presence_Update)
