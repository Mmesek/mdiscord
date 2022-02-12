# -*- coding: utf-8 -*-
'''
Discord Models
----------

Discord raw API types.

:copyright: (c) 2020 Mmesek

'''

#Generated structure from docs at 16:34 2021/07/07
#Generated source code at 16:34 2021/07/07
from __future__ import annotations
from enum import IntEnum
from typing import List, Dict, Tuple
from datetime import datetime
from ctypes import c_byte, c_uint, c_ushort
from dataclasses import dataclass
# HACK: add `+ ["**kwargs"]` to a second argument for _create_fn in _init_fn to allow additional arguments in auto generated constructors 
from .base_model import *

@dataclass
class Application(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the app
    name:
        the name of the app
    icon:
        Icon_Hash
    description:
        the description of the app
    rpc_origins:
        an  rpc origin urls, if rpc is enabled
    bot_public:
        when false only app owner can join the app's bot to guilds
    bot_require_code_grant:
        when true the app's bot will only join upon completion of the full oauth2 code grant flow
    terms_of_service_url:
        the url of the app's terms of service
    privacy_policy_url:
        the url of the app's privacy policy
    owner:
        user  containing info on the owner of the application
    summary:
        if this application is a game sold on Discord, this field will be the summary field for the store page of its primary sku
    verify_key:
        GetTicket
    team:
        if the application belongs to a team, this will be a list of the members of that team
    guild_id:
        if this application is a game sold on Discord, this field will be the guild to which it has been linked
    primary_sku_id:
        if this application is a game sold on Discord, this field will be the id of the "Game SKU" that is created, if exists
    slug:
        if this application is a game sold on Discord, this field will be the URL slug that links to the store page
    cover_image:
        Cover_Image_Hash
    flags:
        Flags
    '''
    id: Snowflake = None
    name: str = ''
    icon: str = ''
    description: str = ''
    rpc_origins: List[str] = None
    bot_public: bool = False
    bot_require_code_grant: bool = False
    terms_of_service_url: str = ''
    privacy_policy_url: str = ''
    owner: User = None
    summary: str = ''
    verify_key: str = ''
    team: Team = None
    guild_id: Snowflake = None
    primary_sku_id: Snowflake = None
    slug: str = ''
    cover_image: str = ''
    flags: int = 0


class Application_Flags(Flag):
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17


@dataclass
class Audit_Log(DiscordObject):
    '''
    Atrributes
    ----------
    webhooks:
        list of webhooks found in the audit log
    users:
        list of users found in the audit log
    audit_log_entries:
        list of audit log entries
    integrations:
        list of  integration s
    '''
    webhooks: List[Webhook] = list
    users: List[User] = list
    audit_log_entries: List[Audit_Log_Entry] = list
    integrations: List[Integration] = list


@dataclass
class Audit_Log_Entry(DiscordObject):
    '''
    Atrributes
    ----------
    target_id:
        id of the affected entity
    changes:
        changes made to the target_id
    user_id:
        the user who made the changes
    id:
        id of the entry
    action_type:
        type of action that occurred
    options:
        additional info for certain action types
    reason:
        the reason for the change
    '''
    target_id: str = ''
    changes: List[Audit_Log_Change] = list
    user_id: Snowflake = 0
    id: Snowflake = 0
    action_type: Audit_Log_Events = None
    options: Optional_Audit_Entry_Info = None
    reason: str = ''


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


@dataclass
class Optional_Audit_Entry_Info(DiscordObject):
    '''
    Atrributes
    ----------
    delete_member_days:
        number of days after which inactive members were kicked
    members_removed:
        number of members removed by the prune
    channel_id:
        channel in which the entities were targeted
    message_id:
        id of the message that was targeted
    count:
        number of entities that were targeted
    id:
        id of the overwritten entity
    type:
        type of overwritten entity - "0" for "role"
    role_name:
        name of the role if type is "0"
    '''
    delete_member_days: str = ''
    members_removed: str = ''
    channel_id: Snowflake = 0
    message_id: Snowflake = 0
    count: str = ''
    id: Snowflake = 0
    type: str = ''
    role_name: str = ''


@dataclass
class Audit_Log_Change(DiscordObject):
    '''
    > info
    
    Atrributes
    ----------
    new_value:
        new value of the key
    old_value:
        old value of the key
    key:
        Change_Key
    '''
    new_value: dict = dict
    old_value: dict = dict
    key: str = ''


@dataclass
class Audit_Log_Change_Key(DiscordObject):
    '''
    Atrributes
    ----------
    name:
        name changed
    description:
        description changed
    icon_hash:
        icon changed
    splash_hash:
        invite splash page artwork changed
    discovery_splash_hash:
        discovery splash changed
    banner_hash:
        guild banner changed
    owner_id:
        owner changed
    region:
        region changed
    preferred_locale:
        preferred locale changed
    afk_channel_id:
        afk channel changed
    afk_timeout:
        afk timeout duration changed
    rules_channel_id:
        id of the rules channel changed
    public_updates_channel_id:
        id of the public updates channel changed
    mfa_level:
        two-factor auth requirement changed
    verification_level:
        required verification level changed
    explicit_content_filter:
        Whose_Messages
    default_message_notifications:
        Message_Notification_Level
    vanity_url_code:
        guild invite vanity url changed
    $add:
        new role added
    $remove:
        role removed
    prune_delete_days:
        change in number of days after which inactive and role-unassigned members are kicked
    widget_enabled:
        server widget enabled/disable
    widget_channel_id:
        channel id of the server widget changed
    system_channel_id:
        id of the system channel changed
    position:
        text
    topic:
        text channel topic
    bitrate:
        voice channel bitrate changed
    permission_overwrites:
        permissions on a channel changed
    nsfw:
        channel nsfw restriction changed
    application_id:
        application id of the added
    rate_limit_per_user:
        amount of seconds a user has to wait before sending another message changed
    permissions:
        Permissions
    color:
        role color changed
    hoist:
        role is now displayed/no longer displayed separate from online users
    mentionable:
        role is now mentionable/unmentionable
    allow:
        a permission on a text
    deny:
        a permission on a text
    code:
        invite code changed
    channel_id:
        channel for invite code changed
    inviter_id:
        person who created invite code changed
    max_uses:
        change to max number of times invite code can be used
    uses:
        number of times invite code used changed
    max_age:
        how long invite code lasts changed
    temporary:
        invite code is temporary/never expires
    deaf:
        user server deafened/undeafened
    mute:
        user server muted/unmuted
    nick:
        user nickname changed
    avatar_hash:
        user avatar changed
    id:
        the id of the changed entity - sometimes used in conjunction with other keys
    type:
        type of entity created
    enable_emoticons:
        integration emoticons enabled/disabled
    expire_behavior:
        integration expiring subscriber behavior changed
    expire_grace_period:
        integration expire grace period changed
    user_limit:
        new user limit in a voice channel
    privacy_level:
        the privacy level of the stage instance.
    '''
    name: str = ''
    description: str = None
    icon_hash: str = ''
    splash_hash: str = ''
    discovery_splash_hash: str = None
    banner_hash: str = None
    owner_id: Snowflake = 0
    region: str = ''
    preferred_locale: str = ''
    afk_channel_id: Snowflake = 0
    afk_timeout: int = 0
    rules_channel_id: Snowflake = 0
    public_updates_channel_id: Snowflake = 0
    mfa_level: int = 0
    verification_level: int = 0
    explicit_content_filter: int = 0
    default_message_notifications: int = 0
    vanity_url_code: str = ''
    add: List[Role] = list
    remove: List[Role] = list
    prune_delete_days: int = 0
    widget_enabled: bool = False
    widget_channel_id: Snowflake = 0
    system_channel_id: Snowflake = 0
    position: int = 0
    topic: str = ''
    bitrate: int = 0
    permission_overwrites: List[Overwrite] = list
    nsfw: bool = False
    application_id: Snowflake = 0
    rate_limit_per_user: int = 0
    permissions: str = ''
    color: int = 0
    hoist: bool = False
    mentionable: bool = False
    allow: str = ''
    deny: str = ''
    code: str = ''
    channel_id: Snowflake = 0
    inviter_id: Snowflake = 0
    max_uses: int = 0
    uses: int = 0
    max_age: int = 0
    temporary: bool = False
    deaf: bool = False
    mute: bool = False
    nick: str = ''
    avatar_hash: str = ''
    id: Snowflake = 0
    type: Channel_Types = None
    enable_emoticons: bool = False
    expire_behavior: int = 0
    expire_grace_period: int = 0
    user_limit: int = 0
    privacy_level: Privacy_Level = None


@dataclass
class Channel(DiscordObject):
    '''
    * `rate_limit_per_user` also applies to thread creation. Users can send one message and create one thread during each `rate_limit_per_user` interval.
    
    Atrributes
    ----------
    id:
        the id of this channel
    type:
        Type_Of_Channel
    guild_id:
        the id of the guild
    position:
        sorting position of the channel
    permission_overwrites:
        explicit permission overwrites for members and roles
    name:
        the name of the channel
    topic:
        the channel topic
    nsfw:
        whether the channel is nsfw
    last_message_id:
        the id of the last message sent in this channel
    bitrate:
        the bitrate
    user_limit:
        the user limit of the voice channel
    rate_limit_per_user:
        amount of seconds a user has to wait before sending another message
    recipients:
        the recipients of the DM
    icon:
        icon hash
    owner_id:
        id of the creator of the group DM
    application_id:
        application id of the group DM creator if it is bot-created
    parent_id:
        for guild channels: id of the parent category for a channel
    last_pin_timestamp:
        when the last pinned message was pinned. This may be `null` in events such as `GUILD_CREATE` when a message is not pinned.
    rtc_region:
        Voice_Region
    video_quality_mode:
        Video_Quality_Mode
    message_count:
        an approximate count of messages in a thread, stops counting at 50
    member_count:
        an approximate count of users in a thread, stops counting at 50
    thread_metadata:
        thread-specific fields not needed by other channels
    member:
        thread member  for the current user, if they have joined the thread, only included on certain API endpoints
    default_auto_archive_duration:
        default duration for newly created threads, in minutes, to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
    '''
    id: Snowflake = 0
    type: int = 0
    guild_id: Snowflake = 0
    position: int = 0
    permission_overwrites: List[Overwrite] = list
    name: str = ''
    topic: str = ''
    nsfw: bool = False
    last_message_id: Snowflake = 0
    bitrate: int = 0
    user_limit: int = 0
    rate_limit_per_user: int = 0
    recipients: List[User] = None
    icon: str = ''
    owner_id: Snowflake = 0
    application_id: Snowflake = 0
    parent_id: Snowflake = 0
    last_pin_timestamp: datetime = datetime.now().isoformat()
    rtc_region: str = None
    video_quality_mode: int = None
    message_count: int = 0
    member_count: int = 0
    thread_metadata: Thread_Metadata = None
    member: Thread_Member = None
    default_auto_archive_duration: int = 0


class Channel_Types(Enum):
    '''
    > warn
    
    Atrributes
    ----------
    GUILD_TEXT:
        a text channel within a server
    DM:
        a direct message between users
    GUILD_VOICE:
        a voice channel within a server
    GROUP_DM:
        a direct message between multiple users
    GUILD_CATEGORY:
        Organizational_Category
    GUILD_NEWS:
        Users_Can_Follow_And_Crosspost_Into_Their_Own_Server
    GUILD_STORE:
        Sell_Their_Game_On_Discord
    GUILD_NEWS_THREAD:
        a temporary sub-channel within a GUILD_NEWS channel
    GUILD_PUBLIC_THREAD:
        a temporary sub-channel within a GUILD_TEXT channel
    GUILD_PRIVATE_THREAD:
        a temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the MANAGE_THREADS permission
    GUILD_STAGE_VOICE:
        Hosting_Events_With_An_Audience
    '''
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13


class Video_Quality_Modes(Enum):
    '''
    Atrributes
    ----------
    AUTO:
        Discord chooses the quality for optimal performance
    FULL:
        720p
    '''
    AUTO = 1
    FULL = 2


@dataclass
class Message(DiscordObject):
    '''
    * The author object follows the structure of the user object, but is only a valid user in the case where the message is generated by a user or bot user. If the message is generated by a webhook, the author object corresponds to the webhook's id, username, and avatar. You can tell if a message is generated by a webhook by checking for the `webhook_id` on the message object.
** The member object exists in [MESSAGE_CREATE](https:#/discord.com/developers/docs/topics/gateway#message-create) and [MESSAGE_UPDATE](https:#/discord.com/developers/docs/topics/gateway#message-update) events from text-based guild channels, provided that the author of the message is not a webhook. This allows bots to obtain real-time member data without requiring bots to store member state in memory.
*** The user objects in the mentions array will only have the partial `member` field present in [MESSAGE_CREATE](https:#/discord.com/developers/docs/topics/gateway#message-create) and [MESSAGE_UPDATE](https:#/discord.com/developers/docs/topics/gateway#message-update) events from text-based guild channels.
    **** Not all channel mentions in a message will appear in `mention_channels`. Only textual channels that are visible to everyone in a lurkable guild will ever be included. Only crossposted messages (via Channel Following) currently include `mention_channels` at all. If no mentions in the message meet these requirements, this field will not be sent.
    ***** This field is only returned for messages with a `type` of `19` (REPLY) or `21` (THREAD_STARTER_MESSAGE). If the message is a reply but the `referenced_message` field is not present, the backend did not attempt to fetch the message that was being replied to, so its state is unknown. If the field exists but is null, the referenced message was deleted.
****** Bots cannot send stickers.
    
    Atrributes
    ----------
    id:
        id of the message
    channel_id:
        id of the channel the message was sent in
    guild_id:
        id of the guild the message was sent in
    author:
        the author of this message
    member:
        member properties for this message's author
    content:
        contents of the message
    timestamp:
        when this message was sent
    edited_timestamp:
        when this message was edited
    tts:
        whether this was a TTS message
    mention_everyone:
        whether this message mentions everyone
    mentions:
        users specifically mentioned in the message
    mention_roles:
        roles specifically mentioned in this message
    mention_channels:
        channels specifically mentioned in this message
    attachments:
        any attached files
    embeds:
        any embedded content
    reactions:
        reactions to the message
    nonce:
        used for validating a message was sent
    pinned:
        whether this message is pinned
    webhook_id:
        if the message is generated by a webhook, this is the webhook's id
    type:
        Type_Of_Message
    activity:
        sent with Rich Presence-related chat embeds
    application:
        sent with Rich Presence-related chat embeds
    application_id:
        Interaction
    message_reference:
        data showing the source of a crosspost, channel follow add, pin,
    flags:
        Message_Flags
    referenced_message:
        the message associated with the message_reference
    interaction:
        Interaction
    thread:
        Thread_Member
    components:
        sent if the message contains components like buttons, action rows,
    sticker_items:
        sent if the message contains stickers
    stickers:
        Deprecated the stickers sent with the message
    '''
    id: Snowflake = 0
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0
    author: User = None
    member: Guild_Member = None
    content: str = ""
    timestamp: datetime = datetime.now().isoformat()
    edited_timestamp: datetime = datetime.now().isoformat()
    tts: bool = False
    mention_everyone: bool = False
    mentions: List[User] = list
    mention_roles: List[Role] = list
    mention_channels: List[Channel_Mention] = list
    attachments: List[Attachment] = list
    embeds: List[Embed] = list
    reactions: List[Reaction] = list
    nonce: int = 0
    pinned: bool = False
    webhook_id: Snowflake = 0
    type: int = 0
    activity: Message_Activity = None
    application: Application = None
    application_id: Snowflake = 0
    message_reference: Message_Reference = None
    flags: int = 0
    stickers: List[Message_Sticker] = list
    referenced_message: Message = None
    interaction: Message_Interaction = None
    thread: Channel = None
    components: List[Component] = None
    sticker_items: Message_Sticker_Item = None


class Message_Types(Enum):
    '''
    > warn
    '''
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


@dataclass
class Message_Activity(DiscordObject):
    '''
    Atrributes
    ----------
    type:
        Type_Of_Message_Activity
    party_id:
        Rich_Presence_Event
    '''
    type: int = 0
    party_id: str = ''


class Message_Activity_Types(Enum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class Message_Flags(Flag):
    '''
    Atrributes
    ----------
    CROSSPOSTED:
        this message has been published to subscribed channels
    IS_CROSSPOST:
        this message originated from a message in another channel
    SUPPRESS_EMBEDS:
        do not include any embeds when serializing this message
    SOURCE_MESSAGE_DELETED:
        the source message for this crosspost has been deleted
    URGENT:
        this message came from the urgent message system
    HAS_THREAD:
        this message has an associated thread, with the same id as the message
    EPHEMERAL:
        this message is only visible to the user who invoked the Interaction
    LOADING:
        this message is an Interaction Response and the bot is "thinking"
    '''
    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4
    HAS_THREAD = 1 << 5
    EPHEMERAL = 1 << 6
    LOADING = 1 << 7


@dataclass
class Message_Sticker_Item(DiscordObject):
    '''
    The smallest amount of data required to render a sticker.
    
    Atrributes
    ----------
    id:
        id of the sticker
    name:
        name of the sticker
    format_type:
        Type_Of_Sticker_Format
    '''
    id: Snowflake = None
    name: str = ''
    format_type: int = 0


class Message_Sticker_Format_Types(Enum):
    PNG = 1
    APNG = 2
    LOTTIE = 3


@dataclass
class Message_Sticker(DiscordObject):
    '''
    * The URL for fetching sticker assets is currently private.
    
    Atrributes
    ----------
    id:
        id of the sticker
    pack_id:
        id of the pack the sticker is from
    name:
        name of the sticker
    description:
        description of the sticker
    tags:
        for guild stickers, a unicode emoji representing the sticker's expression. for nitro stickers, a comma-separated list of related expressions.
    asset:
        Deprecated previously the sticker asset hash, now an empty string
    format_type:
        Type_Of_Sticker_Format
    available:
        whether
    guild_id:
        id of the guild that owns this sticker
    user:
        the user that uploaded the sticker
    sort_value:
        a sticker's sort order within a pack
    '''
    id: Snowflake = 0
    pack_id: Snowflake = 0
    name: str = ''
    description: str = ''
    tags: List[str] = list
    asset: str = ''
    format_type: int = 0
    available: bool = False
    guild_id: Snowflake = None
    user: User = None
    sort_value: int = 0


@dataclass
class Message_Reference(DiscordObject):
    '''
    * `channel_id` is optional when creating a reply, but will always be present when receiving an event/response that includes this data model.
    
    Atrributes
    ----------
    message_id:
        id of the originating message
    channel_id:
        id of the originating message's channel
    guild_id:
        id of the originating message's guild
    fail_if_not_exists:
        when sending, whether to error if the referenced message doesn't exist instead of sending as a normal
    '''
    message_id: Snowflake = None
    channel_id: Snowflake = None
    guild_id: Snowflake = None
    fail_if_not_exists: bool = False


@dataclass
class Followed_Channel(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        source channel id
    webhook_id:
        created target webhook id
    '''
    channel_id: Snowflake = 0
    webhook_id: Snowflake = 0


@dataclass
class Reaction(DiscordObject):
    '''
    Atrributes
    ----------
    count:
        times this emoji has been used to react
    me:
        whether the current user reacted using this emoji
    emoji:
        emoji information
    '''
    count: int = 0
    me: bool = False
    emoji: Emoji = None


@dataclass
class Overwrite(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        role
    type:
        either 0
    allow:
        permission bit set
    deny:
        permission bit set
    '''
    id: Snowflake = 0
    type: int = 0
    allow: str = 0x0
    deny: str = 0x0


@dataclass
class Thread_Metadata(DiscordObject):
    '''
    Atrributes
    ----------
    archived:
        whether the thread is archived
    auto_archive_duration:
        duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
    archive_timestamp:
        timestamp when the thread's archive status was last changed, used for calculating recent activity
    locked:
        when a thread is locked, only users with MANAGE_THREADS can unarchive it
    '''
    archived: bool = False
    auto_archive_duration: int = 0
    archive_timestamp: datetime = None
    locked: bool = False


@dataclass
class Thread_Member(DiscordObject):
    '''
    ** * These fields are ommitted on the member sent within each thread in the [GUILD_CREATE](https:#/discord.com/developers/docs/topics/gateway#guild-create) event **
    
    Atrributes
    ----------
    id:
        the id of the thread
    user_id:
        the id of the user
    join_timestamp:
        the time the current user last joined the thread
    flags:
        any user-thread settings, currently only used for notifications
    '''
    id: Snowflake = None
    user_id: Snowflake = None
    join_timestamp: datetime = None
    flags: int = 0


@dataclass
class Embed(DiscordObject):
    '''
    Atrributes
    ----------
    title:
        title of embed
    type:
        Type_Of_Embed
    description:
        description of embed
    url:
        url of embed
    timestamp:
        timestamp of embed content
    color:
        color code of the embed
    footer:
        footer information
    image:
        image information
    thumbnail:
        thumbnail information
    video:
        video information
    provider:
        provider information
    author:
        author information
    fields:
        fields information
    '''
    title: str = None
    type: str = None
    description: str = None
    url: str = None
    timestamp: datetime = None
    color: int = None
    footer: Embed_Footer = None
    image: Embed_Image = None
    thumbnail: Embed_Thumbnail = None
    video: Embed_Video = None
    provider: Embed_Provider = None
    author: Embed_Author = None
    fields: List[Embed_Field] = list


class Embed_Types(Enum):
    '''
    Embed types are "loosely defined" and, for the most part, are not used by our clients for rendering. Embed attributes power what is rendered. Embed types should be considered deprecated and might be removed in a future API version.
    
    Atrributes
    ----------
    rich:
        generic embed rendered from embed attributes
    image:
        image embed
    video:
        video embed
    gifv:
        animated gif image embed rendered as a video embed
    article:
        article embed
    link:
        link embed
    '''
    rich = "Generic_Embed_Rendered_From_Embed_Attributes"
    image = "Image_Embed"
    video = "Video_Embed"
    gifv = "Animated_Gif_Image_Embed_Rendered_As_A_Video_Embed"
    article = "Article_Embed"
    link = "Link_Embed"


@dataclass
class Embed_Thumbnail(DiscordObject):
    '''
    Atrributes
    ----------
    url:
        source url of thumbnail
    proxy_url:
        a proxied url of the thumbnail
    height:
        height of thumbnail
    width:
        width of thumbnail
    '''
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None


@dataclass
class Embed_Video(DiscordObject):
    '''
    Atrributes
    ----------
    url:
        source url of video
    proxy_url:
        a proxied url of the video
    height:
        height of video
    width:
        width of video
    '''
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None


@dataclass
class Embed_Image(DiscordObject):
    '''
    Atrributes
    ----------
    url:
        source url of image
    proxy_url:
        a proxied url of the image
    height:
        height of image
    width:
        width of image
    '''
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None


@dataclass
class Embed_Provider(DiscordObject):
    '''
    Atrributes
    ----------
    name:
        name of provider
    url:
        url of provider
    '''
    name: str = ''
    url: str = ''


@dataclass
class Embed_Author(DiscordObject):
    '''
    Atrributes
    ----------
    name:
        name of author
    url:
        url of author
    icon_url:
        url of author icon
    proxy_icon_url:
        a proxied url of author icon
    '''
    name: str = ''
    url: str = ''
    icon_url: str = ''
    proxy_icon_url: str = ''


@dataclass
class Embed_Footer(DiscordObject):
    '''
    Atrributes
    ----------
    text:
        footer text
    icon_url:
        url of footer icon
    proxy_icon_url:
        a proxied url of footer icon
    '''
    text: str = ''
    icon_url: str = ''
    proxy_icon_url: str = ''


@dataclass
class Embed_Field(DiscordObject):
    '''
    Atrributes
    ----------
    name:
        name of the field
    value:
        value of the field
    inline:
        whether
    '''
    name: str = ''
    value: str = ''
    inline: bool = False


@dataclass
class Attachment(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        attachment id
    filename:
        name of file attached
    content_type:
        Media_Type
    size:
        size of file in bytes
    url:
        source url of file
    proxy_url:
        a proxied url of file
    height:
        height of file
    width:
        width of file
    '''
    id: Snowflake = None
    filename: str = ''
    content_type: str = ''
    size: int = 0
    url: str = ''
    proxy_url: str = ''
    height: int = 0
    width: int = 0


@dataclass
class Channel_Mention(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        id of the channel
    guild_id:
        id of the guild containing the channel
    type:
        Type_Of_Channel
    name:
        the name of the channel
    '''
    id: Snowflake = 0
    guild_id: Snowflake = 0
    type: int = 0
    name: str = ''


class Allowed_Mention_Types(Enum):
    '''
    Atrributes
    ----------
    Role Mentions:
        Controls role mentions
    User Mentions:
        Controls user mentions
    Everyone Mentions:
        Controls @everyone and @here mentions
    '''
    Role_Mentions = "roles"
    User_Mentions = "users"
    Everyone_Mentions = "everyone"


@dataclass
class Allowed_Mentions(DiscordObject):
    '''
    Atrributes
    ----------
    parse:
        Allowed_Mention_Types
    roles:
        Array of role_ids to mention
    users:
        Array of user_ids to mention
    replied_user:
        For replies, whether to mention the author of the message being replied to
    '''
    parse: List[Allowed_Mention_Types] = list
    roles: List[Snowflake] = list
    users: List[Snowflake] = list
    replied_user: bool = False


class Limits(IntEnum):
    '''
    All of the following limits are measured inclusively. Leading and trailing whitespace characters are not included (they are trimmed automatically).
    Additionally, the characters in all `title`, `description`, `field.name`, `field.value`, `footer.text`, and `author.name` fields must not exceed 6000 characters in total. Violating any of these constraints will result in a `Bad Request` response.
    '''
    TITLE = 256
    DESCRIPTION = 2048
    FIELDS = 25
    FIELD_NAME = 256
    FIELD_VALUE = 1024
    FOOTER_TEXT = 2048
    AUTHOR_NAME = 256
    TOTAL = 6000


@dataclass
class Thread_List(DiscordObject):
    '''
    Params
    ------
    threads:
        the active threads
        the public, archived threads
        the private, archived threads
        the private, archived threads the current user has joined
    members:
        a thread member  for each returned thread the current user has joined
    has_more:
        whether there are potentially additional threads that could be returned on a subsequent call
    '''
    threads: List[Channel] = list
    members: List[Thread_Member] = list
    has_more: bool = False


@dataclass
class Emoji(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        Emoji_Id
    name:
        emoji name
    roles:
        roles allowed to use this emoji
    user:
        user that created this emoji
    require_colons:
        whether this emoji must be wrapped in colons
    managed:
        whether this emoji is managed
    animated:
        whether this emoji is animated
    available:
        whether this emoji can be used, may be false due to loss of Server Boosts
    '''
    id: Snowflake = 0
    name: str = ""
    roles: List[Role] = list
    user: User = None
    require_colons: bool = False
    managed: bool = False
    animated: bool = False
    available: bool = False


@dataclass
class Guild(DiscordObject):
    '''
    ** * These fields are only sent within the [GUILD_CREATE](https:#/discord.com/developers/docs/topics/gateway#guild-create) event **
** ** These fields are only sent when using the [GET Current User Guilds](https:#/discord.com/developers/docs/resources/user#get-current-user-guilds) endpoint and are relative to the requested user **
** *** This field is deprecated and will be removed in v9 and is replaced by [rtc_region](https:#/discord.com/developers/docs/resources/channel#channel-object-channel-structure)**
    
    Atrributes
    ----------
    id:
        guild id
    name:
        guild name
    icon:
        Icon_Hash
    icon_hash:
        Icon_Hash
    splash:
        Splash_Hash
    discovery_splash:
        Discovery_Splash_Hash
    owner:
        The_User
    owner_id:
        id of owner
    permissions:
        The_User
    region:
        Voice_Region
    afk_channel_id:
        id of afk channel
    afk_timeout:
        afk timeout in seconds
    widget_enabled:
        true if the server widget is enabled
    widget_channel_id:
        the channel id that the widget will generate an invite to,
    verification_level:
        Verification_Level
    default_message_notifications:
        Message_Notifications_Level
    explicit_content_filter:
        Explicit_Content_Filter_Level
    roles:
        roles in the guild
    emojis:
        custom guild emojis
    features:
        enabled guild features
    mfa_level:
        MFA_Level
    application_id:
        application id of the guild creator if it is bot-created
    system_channel_id:
        the id of the channel where guild notices such as welcome messages and boost events are posted
    system_channel_flags:
        System_Channel_Flags
    rules_channel_id:
        the id of the channel where Community guilds can display rules and/or guidelines
    joined_at:
        when this guild was joined at
    large:
        true if this is considered a large guild
    unavailable:
        true if this guild is unavailable due to an outage
    member_count:
        total number of members in this guild
    voice_states:
        states of members currently in voice channels; lacks the `guild_id` key
    members:
        users in the guild
    channels:
        channels in the guild
    threads:
        all active threads in the guild that current user has permission to view
    presences:
        presences of the members in the guild, will only include non-offline members if the size is greater than `large threshold`
    max_presences:
        the maximum number of presences for the guild
    max_members:
        the maximum number of members for the guild
    vanity_url_code:
        the vanity url code for the guild
    description:
        the description of a Community guild
    banner:
        Banner_Hash
    premium_tier:
        Premium_Tier
    premium_subscription_count:
        the number of boosts this guild currently has
    preferred_locale:
        the preferred locale of a Community guild; used in server discovery and notices from Discord; defaults to "en-US"
    public_updates_channel_id:
        the id of the channel where admins and moderators of Community guilds receive notices from Discord
    max_video_channel_users:
        the maximum amount of users in a video channel
    approximate_member_count:
        approximate number of members in this guild, returned from the `GET /guilds/<id>` endpoint when `with_counts` is `true`
    approximate_presence_count:
        approximate number of non-offline members in this guild, returned from the `GET /guilds/<id>` endpoint when `with_counts` is `true`
    welcome_screen:
        Invite
    nsfw_level:
        Guild_NSFW_Level
    stage_instances:
        Stage instances in the guild
    '''
    id: Snowflake = 0
    name: str = ""
    icon: str = ""
    icon_hash: str = ""
    splash: str = ""
    discovery_splash: str = ""
    owner: bool = False
    owner_id: Snowflake = 0
    permissions: str = 0x0
    region: str = ""
    afk_channel_id: Snowflake = 0
    afk_timeout: int = 0
    widget_enabled: bool = False
    widget_channel_id: Snowflake = 0
    verification_level: int = 0
    default_message_notifications: int = 0
    explicit_content_filter: int = 0
    roles: List[Role] = list
    emojis: List[Emoji] = list
    features: List[Guild_Features] = list
    mfa_level: int = 0
    application_id: Snowflake = 0
    system_channel_id: Snowflake = 0
    system_channel_flags: int = 0
    rules_channel_id: Snowflake = 0
    joined_at: datetime = None
    large: bool = False
    unavailable: bool = False
    member_count: int = 0
    voice_states: List[Voice_State] = list
    members: List[Guild_Member] = list
    channels: List[Channel] = list
    threads: List[Channel] = list
    presences: List[Presence_Update] = list
    max_presences: int = 0
    max_members: int = 0
    vanity_url_code: str = ''
    description: str = ''
    banner: str = ''
    premium_tier: int = 0
    premium_subscription_count: int = 0
    preferred_locale: str = ''
    public_updates_channel_id: Snowflake = 0
    max_video_channel_users: int = 0
    approximate_member_count: int = 0
    approximate_presence_count: int = 0
    welcome_screen: Welcome_Screen = None
    nsfw_level: int = 0
    stage_instances: Stage_Instance = None


class Default_Message_Notification_Level(Enum):
    '''
    Atrributes
    ----------
    ALL_MESSAGES:
        members will receive notifications for all messages by default
    ONLY_MENTIONS:
        members will receive notifications only for messages that @mention them by default
    '''
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class Explicit_Content_Filter_Level(Enum):
    '''
    Atrributes
    ----------
    DISABLED:
        media content will not be scanned
    MEMBERS_WITHOUT_ROLES:
        media content sent by members without roles will be scanned
    ALL_MEMBERS:
        media content sent by all members will be scanned
    '''
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class MFA_Level(Enum):
    '''
    Atrributes
    ----------
    NONE:
        guild has no MFA/2FA requirement for moderation actions
    ELEVATED:
        guild has a 2FA requirement for moderation actions
    '''
    NONE = 0
    ELEVATED = 1


class Verification_Level(Enum):
    '''
    Atrributes
    ----------
    NONE:
        unrestricted
    LOW:
        must have verified email on account
    MEDIUM:
        must be registered on Discord for longer than 5 minutes
    HIGH:
        must be a member of the server for longer than 10 minutes
    VERY_HIGH:
        must have a verified phone number
    '''
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class Guild_NSFW_Level(Enum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class Premium_Tier(Enum):
    '''
    Atrributes
    ----------
    NONE:
        guild has not unlocked any Server Boost perks
    TIER_1:
        guild has unlocked Server Boost level 1 perks
    TIER_2:
        guild has unlocked Server Boost level 2 perks
    TIER_3:
        guild has unlocked Server Boost level 3 perks
    '''
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class System_Channel_Flags(Flag):
    '''
    Atrributes
    ----------
    SUPPRESS_JOIN_NOTIFICATIONS:
        Suppress member join notifications
    SUPPRESS_PREMIUM_SUBSCRIPTIONS:
        Suppress server boost notifications
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS:
        Suppress server setup tips
    '''
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2


class Guild_Features(Enum):
    '''
    Atrributes
    ----------
    ANIMATED_ICON:
        guild has access to set an animated guild icon
    BANNER:
        guild has access to set a guild banner image
    COMMERCE:
        guild has access to use commerce features
    COMMUNITY:
        guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates
    DISCOVERABLE:
        guild is able to be discovered in the directory
    FEATURABLE:
        guild is able to be featured in the directory
    INVITE_SPLASH:
        guild has access to set an invite splash background
    MEMBER_VERIFICATION_GATE_ENABLED:
        Membership_Screening
    NEWS:
        guild has access to create news channels
    PARTNERED:
        guild is partnered
    PREVIEW_ENABLED:
        guild can be previewed before joining via Membership Screening
    VANITY_URL:
        guild has access to set a vanity URL
    VERIFIED:
        guild is verified
    VIP_REGIONS:
        guild has access to set 384kbps bitrate in voice
    WELCOME_SCREEN_ENABLED:
        guild has enabled the welcome screen
    TICKETED_EVENTS_ENABLED:
        guild has enabled ticketed events
    MONETIZATION_ENABLED:
        guild has enabled monetization
    MORE_STICKERS:
        guild has increased custom sticker slots
    THREE_DAY_THREAD_ARCHIVE:
        guild has access to the three day archive time for threads
    SEVEN_DAY_THREAD_ARCHIVE:
        guild has access to the seven day archive time for threads
    PRIVATE_THREADS:
        guild has access to create private threads
    '''
    ANIMATED_ICON = "Guild has access to Set An Animated Guild Icon"
    BANNER = "Guild has access to Set A Guild Banner Image"
    COMMERCE = "Guild has access to Use Commerce Features"
    COMMUNITY = "Guild Can Enable Welcome Screen and Discovery, and Receives Community Updates"
    DISCOVERABLE = "Guild Is Lurkable and Able to Be Discovered In The Directory"
    FEATURABLE = "Guild Is Able to Be Featured In The Directory"
    INVITE_SPLASH = "Guild has access to Set An Invite Splash Background"
    MEMBER_VERIFICATION_GATE_ENABLED = "Membership Screening"
    NEWS = "Guild has access to Create News Channels"
    PARTNERED = "Guild Is Partnered"
    PREVIEW_ENABLED = "Guild can be previewed before joining via Membership Screening"
    VANITY_URL = "Guild has access to Set A Vanity Url"
    VERIFIED = "Guild Is Verified"
    VIP_REGIONS = "Guild has access to Set 384 Kbps Bitrate In Voice"
    WELCOME_SCREEN_ENABLED = "Guild has Enabled The Welcome Screen"
    TICKETED_EVENTS_ENABLED = "Guild_Has_Enabled_Ticketed_Events"
    MONETIZATION_ENABLED = "Guild_Has_Enabled_Monetization"
    MORE_STICKERS = "Guild_Has_Increased_Custom_Sticker_Slots"
    THREE_DAY_THREAD_ARCHIVE = "Guild_Has_Access_To_The_Three_Day_Archive_Time_For_Threads"
    SEVEN_DAY_THREAD_ARCHIVE = "Guild_Has_Access_To_The_Seven_Day_Archive_Time_For_Threads"
    PRIVATE_THREADS = "Guild_Has_Access_To_Create_Private_Threads"


@dataclass
class Guild_Preview(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        guild id
    name:
        guild name
    icon:
        Icon_Hash
    splash:
        Splash_Hash
    discovery_splash:
        Discovery_Splash_Hash
    emojis:
        custom guild emojis
    features:
        enabled guild features
    approximate_member_count:
        approximate number of members in this guild
    approximate_presence_count:
        approximate number of online members in this guild
    description:
        the description for the guild, if the guild is discoverable
    '''
    id: Snowflake = 0
    name: str = ''
    icon: str = ''
    splash: str = ''
    discovery_splash: str = ''
    emojis: List[Emoji] = list
    features: List[Guild_Features] = list
    approximate_member_count: int = 0
    approximate_presence_count: int = 0
    description: str = ''


@dataclass
class Guild_Widget(DiscordObject):
    '''
    Atrributes
    ----------
    enabled:
        whether the widget is enabled
    channel_id:
        the widget channel id
    '''
    enabled: bool = False
    channel_id: Snowflake = 0


@dataclass
class Guild_Member(DiscordObject):
    '''
    > info
    > The field `user` won't be included in the member object attached to `MESSAGE_CREATE` and `MESSAGE_UPDATE` gateway events.
    > info
    > In `GUILD_` events, `pending` will always be included as true or false. In non `GUILD_` events which can only be triggered by non-`pending` users, `pending` will not be included.
    
    Atrributes
    ----------
    user:
        the user this guild member represents
    nick:
        this users guild nickname
    roles:
        Role
    joined_at:
        when the user joined the guild
    premium_since:
        Boosting
    deaf:
        whether the user is deafened in voice channels
    mute:
        whether the user is muted in voice channels
    pending:
        Membership_Screening
    permissions:
        total permissions of the member in the channel, including overwrites, returned when in the interaction
    '''
    user: User = None
    nick: str = None
    roles: List[Snowflake] = list
    joined_at: datetime = datetime.now().isoformat()
    premium_since: datetime = datetime.now().isoformat()
    deaf: bool = False
    mute: bool = False
    pending: bool = False
    permissions: str = 0x0


@dataclass
class Integration(DiscordObject):
    '''
    ** * These fields are not provided for discord bot integrations. **
    
    Atrributes
    ----------
    id:
        integration id
    name:
        integration name
    type:
        integration type
    enabled:
        is this integration enabled
    syncing:
        is this integration syncing
    role_id:
        id that this integration uses for "subscribers"
    enable_emoticons:
        whether emoticons should be synced for this integration
    expire_behavior:
        the behavior of expiring subscribers
    expire_grace_period:
        the grace period
    user:
        user for this integration
    account:
        integration account information
    synced_at:
        when this integration was last synced
    subscriber_count:
        how many subscribers this integration has
    revoked:
        has this integration been revoked
    application:
        The bot/OAuth2 application for discord integrations
    '''
    id: Snowflake = 0
    name: str = ''
    type: str = ''
    enabled: bool = False
    syncing: bool = False
    role_id: Snowflake = 0
    enable_emoticons: bool = False
    expire_behavior: Integration_Expire_Behaviors = None
    expire_grace_period: int = 0
    user: User = None
    account: Integration_Account = None
    synced_at: datetime = datetime.now().isoformat()
    subscriber_count: int = 0
    revoked: bool = False
    application: Integration_Application = None


class Integration_Expire_Behaviors(Enum):
    REMOVE_ROLE = 0
    KICK = 1


@dataclass
class Integration_Account(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        id of the account
    name:
        name of the account
    '''
    id: str = ''
    name: str = ''


@dataclass
class Integration_Application(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the app
    name:
        the name of the app
    icon:
        Icon_Hash
    description:
        the description of the app
    summary:
        the summary of the app
    bot:
        the bot associated with this application
    '''
    id: Snowflake = 0
    name: str = ''
    icon: str = ''
    description: str = ''
    summary: str = ''
    bot: User = None


@dataclass
class Ban(DiscordObject):
    '''
    Atrributes
    ----------
    reason:
        the reason for the ban
    user:
        the banned user
    '''
    reason: str = ''
    user: User = None


@dataclass
class Welcome_Screen(DiscordObject):
    '''
    Atrributes
    ----------
    description:
        the server description shown in the welcome screen
    welcome_channels:
        the channels shown in the welcome screen, up to 5
    '''
    description: str = ''
    welcome_channels: List[Welcome_Screen_Channel] = list


@dataclass
class Welcome_Screen_Channel(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        the channel's id
    description:
        the description shown for the channel
    emoji_id:
        Emoji_Id
    emoji_name:
        the emoji name if custom, the unicode character if standard,
    '''
    channel_id: Snowflake = None
    description: str = ''
    emoji_id: Snowflake = None
    emoji_name: str = ''


@dataclass
class Invite(DiscordObject):
    '''
    Atrributes
    ----------
    code:
        the invite code
    guild:
        the guild this invite is for
    channel:
        the channel this invite is for
    inviter:
        the user who created the invite
    target_type:
        Type_Of_Target
    target_user:
        the user whose stream to display for this voice channel stream invite
    target_application:
        the embedded application to open for this voice channel embedded application invite
    approximate_presence_count:
        approximate count of online members, returned from the `GET /invites/<code>` endpoint when `with_counts` is `true`
    approximate_member_count:
        approximate count of total members, returned from the `GET /invites/<code>` endpoint when `with_counts` is `true`
    expires_at:
        the expiration date of this invite, returned from the `GET /invites/<code>` endpoint when `with_expiration` is `true`
    stage_instance:
        Public_Stage_Instance
    '''
    code: str = ''
    guild: Guild = None
    channel: Channel = None
    inviter: User = None
    target_type: Invite_Target_Types = 0
    target_user: User = None
    target_application: Application = None
    approximate_presence_count: int = 0
    approximate_member_count: int = 0
    expires_at: datetime = None
    stage_instance: Invite_Stage_Instance = None


class Invite_Target_Types(Enum):
    STREAM = 1
    EMBEDDED_APPLICATION = 2


@dataclass
class Invite_Metadata(DiscordObject):
    '''
    Atrributes
    ----------
    uses:
        number of times this invite has been used
    max_uses:
        max number of times this invite can be used
    max_age:
        duration
    temporary:
        whether this invite only grants temporary membership
    created_at:
        when this invite was created
    '''
    uses: int = 0
    max_uses: int = 0
    max_age: int = 0
    temporary: bool = False
    created_at: datetime = None


@dataclass
class Invite_Stage_Instance(DiscordObject):
    '''
    Atrributes
    ----------
    members:
        the members speaking in the Stage
    participant_count:
        the number of users in the Stage
    speaker_count:
        the number of users speaking in the Stage
    topic:
        the topic of the Stage instance
    '''
    members: Guild_Member = None
    participant_count: int = 0
    speaker_count: int = 0
    topic: str = ''


@dataclass
class Stage_Instance(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        The id of this Stage instance
    guild_id:
        The guild id of the associated Stage channel
    channel_id:
        The id of the associated Stage channel
    topic:
        The topic of the Stage instance
    privacy_level:
        Privacy_Level
    discoverable_disabled:
        Whether
    '''
    id: Snowflake = None
    guild_id: Snowflake = None
    channel_id: Snowflake = None
    topic: str = ''
    privacy_level: int = 0
    discoverable_disabled: bool = False


class Privacy_Level(Enum):
    '''
    Atrributes
    ----------
    PUBLIC:
        The Stage instance is visible publicly, such as on Stage discovery.
    GUILD_ONLY:
        The Stage instance is visible to only guild members.
    '''
    PUBLIC = 1
    GUILD_ONLY = 2


@dataclass
class User(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the user's id
    username:
        the user's username, not unique across the platform
    discriminator:
        the user's 4-digit discord-tag
    avatar:
        Avatar_Hash
    bot:
        whether the user belongs to an OAuth2 application
    system:
        whether the user is an Official Discord System user
    mfa_enabled:
        whether the user has two factor enabled on their account
    locale:
        the user's chosen language option
    verified:
        whether the email on this account has been verified
    email:
        the user's email
    flags:
        Flags
    premium_type:
        Type_Of_Nitro_Subscription
    public_flags:
        Flags
    '''
    id: Snowflake = 0
    username: str = ""
    discriminator: int = 0000
    avatar: str = ""
    bot: bool = False
    system: bool = False
    mfa_enabled: bool = False
    locale: str = ""
    verified: bool = False
    email: str = ""
    flags: int = 0
    premium_type: int = 0
    public_flags: int = 0


class User_Flags(Flag):
    '''
    Atrributes
    ----------
    None:
        None
    Discord Employee:
        Discord Employee
    Partnered Server Owner:
        Partnered Server Owner
    HypeSquad Events:
        HypeSquad Events
    Bug Hunter Level 1:
        Bug Hunter Level 1
    House Bravery:
        House Bravery
    House Brilliance:
        House Brilliance
    House Balance:
        House Balance
    Early Supporter:
        Early Supporter
    Team User:
        Team User
    Bug Hunter Level 2:
        Bug Hunter Level 2
    Verified Bot:
        Verified Bot
    Early Verified Bot Developer:
        Early Verified Bot Developer
    Discord Certified Moderator:
        Discord Certified Moderator
    '''
    NONE = 0
    DISCORD_EMPLOYEE = 1 << 0
    PARTNERED_SERVER_OWNER = 1 << 1
    HYPESQUAD_EVENTS = 1 << 2
    BUG_HUNTER_LEVEL_1 = 1 << 3
    HOUSE_BRAVERY = 1 << 6
    HOUSE_BRILLIANCE = 1 << 7
    HOUSE_BALANCE = 1 << 8
    EARLY_SUPPORTER = 1 << 9
    TEAM_USER = 1 << 10
    SYSTEM = 1 << 12
    BUG_HUNTER_LEVEL_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    EARLY_VERIFIED_BOT_DEVELOPER = 1 << 17
    DISCORD_CERTIFIED_MODERATOR = 1 << 18


class Premium_Types(Enum):
    '''
    Premium types denote the level of premium a user has. Visit the [Nitro](https:##discord.com/nitro) page to learn more about the premium plans we currently offer.
    '''
    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2


@dataclass
class Connection(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        id of the connection account
    name:
        the username of the connection account
    type:
        the service of the connection
    revoked:
        whether the connection is revoked
    integrations:
        Server_Integrations
    verified:
        whether the connection is verified
    friend_sync:
        whether friend sync is enabled for this connection
    show_activity:
        whether activities related to this connection will be shown in presence updates
    visibility:
        Visibility
    '''
    id: str = ''
    name: str = ''
    type: str = ''
    revoked: bool = False
    integrations: List[Integration] = list
    verified: bool = False
    friend_sync: bool = False
    show_activity: bool = False
    visibility: int = 0


class Visibility_Types(Enum):
    '''
    Atrributes
    ----------
    None:
        invisible to everyone except the user themselves
    Everyone:
        visible to everyone
    '''
    NONE = 0
    EVERYONE = 1


@dataclass
class Voice_State(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the guild id this voice state is for
    channel_id:
        the channel id this user is connected to
    user_id:
        the user id this voice state is for
    member:
        the guild member this voice state is for
    session_id:
        the session id for this voice state
    deaf:
        whether this user is deafened by the server
    mute:
        whether this user is muted by the server
    self_deaf:
        whether this user is locally deafened
    self_mute:
        whether this user is locally muted
    self_stream:
        whether this user is streaming using "Go Live"
    self_video:
        whether this user's camera is enabled
    suppress:
        whether this user is muted by the current user
    request_to_speak_timestamp:
        the time at which the user requested to speak
    '''
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0
    user_id: Snowflake = None
    member: Guild_Member = None
    session_id: str = None
    deaf: bool = False
    mute: bool = False
    self_deaf: bool = False
    self_mute: bool = False
    self_stream: bool = False
    self_video: bool = False
    suppress: bool = False
    request_to_speak_timestamp: datetime = None


@dataclass
class Voice_Region(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        unique ID for the region
    name:
        name of the region
    vip:
        true if this is a vip-only server
    optimal:
        true for a single server that is closest to the current user's client
    deprecated:
        whether this is a deprecated voice region
    custom:
        whether this is a custom voice region
    '''
    id: str = ''
    name: str = ''
    vip: bool = False
    optimal: bool = False
    deprecated: bool = False
    custom: bool = False


@dataclass
class Webhook(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the webhook
    type:
        Type
    guild_id:
        the guild id this webhook is for, if any
    channel_id:
        the channel id this webhook is for, if any
    user:
        the user this webhook was created by
    name:
        the default name of the webhook
    avatar:
        Hash
    token:
        the secure token of the webhook
    application_id:
        the bot/OAuth2 application that created this webhook
    source_guild:
        the guild of the channel that this webhook is following
    source_channel:
        the channel that this webhook is following
    url:
        Webhooks
    '''
    id: Snowflake = 0
    type: int = 0
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0
    user: User = None
    name: str = ''
    avatar: str = ''
    token: str = ''
    application_id: Snowflake = 0
    source_guild: Guild = None
    source_channel: Channel = None
    url: str = ''


class Webhook_Types(Enum):
    '''
    Atrributes
    ----------
    Incoming:
        Incoming Webhooks can post messages to channels with a generated token
    Channel Follower:
        Channel Follower Webhooks are internal webhooks used with Channel Following to post new messages into channels
    Application:
        Application webhooks are webhooks used with Interactions
    '''
    INCOMING = 1
    CHANNEL_FOLLOWER = 2
    APPLICATION = 3


@dataclass
class Gateway_Payload(DiscordObject):
    '''
    * `s` and `t` are `null` when `op` is not `0` (Gateway Dispatch Opcode).
    
    Atrributes
    ----------
    op:
        Opcode
    d:
        event data
    s:
        sequence number, used for resuming sessions and heartbeats
    t:
        the event name for this payload
    '''
    op: int = 0
    d: dict = dict
    s: int = 0
    t: str = None


@dataclass
class Gateway_URL_Query_String_Params(DiscordObject):
    '''
    The first step in establishing connectivity to the gateway is requesting a valid websocket endpoint from the API. This can be done through either the [Get Gateway](https:#/discord.com/developers/docs/topics/gateway#get-gateway) or the [Get Gateway Bot](https:#/discord.com/developers/docs/topics/gateway#get-gateway-bot) endpoint.
With the resulting payload, you can now open a websocket connection to the "url" (or endpoint) specified. Generally, it is a good idea to explicitly pass the gateway version and encoding. For example, we may connect to `wss://gateway.discord.gg/?v=9&encoding=json`.
Once connected, the client should immediately receive an [Opcode 10 Hello](https:#/discord.com/developers/docs/topics/gateway#hello) payload, with information on the connection's heartbeat interval:
    
    Atrributes
    ----------
    v:
        Gateway Version to use
    encoding:
        The encoding of received gateway packets
    compress:
        The
    '''
    v: int = 0
    encoding: str = ''
    compress: str = ''


@dataclass
class Identify(DiscordObject):
    '''
    Atrributes
    ----------
    token:
        authentication token
    properties:
        Connection_Properties
    compress:
        whether this connection supports compression of packets
    large_threshold:
        value between 50 and 250, total number of members where the gateway will stop sending offline members in the guild member list
    shard:
        Guild_Sharding
    presence:
        presence structure for initial presence information
    intents:
        Gateway_Intents
    '''
    token: str = ""
    properties: dict = None
    compress: bool = False
    large_threshold: int = 50
    shard: Tuple[int, int] = list
    presence: Gateway_Presence_Update = None
    intents: int = 0


@dataclass
class Identify_Connection_Properties(DiscordObject):
    '''
    Atrributes
    ----------
    $os:
        your operating system
    $browser:
        your library name
    $device:
        your library name
    '''
    os: str = ''
    browser: str = ''
    device: str = ''


@dataclass
class Resume(DiscordObject):
    '''
    Atrributes
    ----------
    token:
        session token
    session_id:
        session id
    seq:
        last sequence number received
    '''
    token: str = ''
    session_id: str = ''
    seq: int = 0


@dataclass
class Guild_Request_Members(DiscordObject):
    '''
    > info
    > Nonce can only be up to 32 bytes. If you send an invalid nonce it will be ignored and the reply member_chunk(s) will not have a nonce set.
    
    Atrributes
    ----------
    guild_id:
        id of the guild to get members for
    query:
        string that username starts with,
    limit:
        maximum number of members to send matching the `query`; a limit of `0` can be used with an empty string `query` to return all members
    presences:
        used to specify if we want the presences of the matched members
    user_ids:
        used to specify which users you wish to fetch
    nonce:
        Guild_Members_Chunk
    '''
    guild_id: Snowflake = 0
    query: str = ''
    limit: int = 0
    presences: bool = False
    user_ids: List[Snowflake] = list
    nonce: str = ''


@dataclass
class Gateway_Voice_State_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    channel_id:
        id of the voice channel client wants to join
    self_mute:
        is the client muted
    self_deaf:
        is the client deafened
    '''
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0
    self_mute: bool = False
    self_deaf: bool = False


@dataclass
class Gateway_Presence_Update(DiscordObject):
    '''
    Atrributes
    ----------
    since:
        unix time
    activities:
        the user's activities
    status:
        Status
    afk:
        whether
    '''
    since: int = 0
    activities: List[Bot_Activity] = list
    status: str = ''
    afk: bool = False


class Status_Types(Enum):
    '''
    Atrributes
    ----------
    online:
        Online
    dnd:
        Do Not Disturb
    idle:
        AFK
    invisible:
        Invisible and shown as offline
    offline:
        Offline
    '''
    ONLINE = "online"
    DND = "dnd"
    IDLE = "idle"
    INVISIBLE = "invisible"
    OFFLINE = "offline"


@dataclass
class Hello(DiscordObject):
    '''
    Atrributes
    ----------
    heartbeat_interval:
        the interval
    '''
    heartbeat_interval: int = 0


@dataclass
class Ready(DiscordObject):
    '''
    Atrributes
    ----------
    v:
        Gateway_Version
    user:
        information about the user including email
    guilds:
        the guilds the user is in
    session_id:
        used for resuming connections
    shard:
        Shard_Information
    application:
        contains `id` and `flags`
    '''
    v: int = 0
    user: User = None
    guilds: List[Guild] = list
    session_id: str = ''
    shard: Tuple[int, int] = list
    application: Application = None


@dataclass
class Thread_List_Sync(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    channel_ids:
        the parent channel ids whose threads are being synced.  If omitted, then threads were synced for the entire guild.  This array may contain channel_ids that have no active threads as well, so you know to clear that data.
    threads:
        all active threads in the given channels that the current user can access
    members:
        all thread member s from the synced threads for the current user, indicating which threads the current user has been added to
    '''
    guild_id: Snowflake = None
    channel_ids: List[Snowflake] = list
    threads: List[Channel] = list
    members: List[Thread_Member] = list


@dataclass
class Thread_Members_Update(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the thread
    guild_id:
        the id of the guild
    member_count:
        the approximate number of members in the thread, capped at 50
    added_members:
        the users who were added to the thread
    removed_member_ids:
        the id of the users who were removed from the thread
    '''
    id: Snowflake = None
    guild_id: Snowflake = None
    member_count: int = 0
    added_members: List[Thread_Member] = list
    removed_member_ids: List[Snowflake] = list


@dataclass
class Channel_Pins_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    channel_id:
        the id of the channel
    last_pin_timestamp:
        the time at which the most recent pinned message was pinned
    '''
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0
    last_pin_timestamp: datetime = None


@dataclass
class Guild_Ban_Add(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    user:
        the banned user
    '''
    guild_id: Snowflake = 0
    user: User = None


@dataclass
class Guild_Ban_Remove(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    user:
        the unbanned user
    '''
    guild_id: Snowflake = 0
    user: User = None


@dataclass
class Guild_Emojis_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    emojis:
        Emojis
    '''
    guild_id: Snowflake = 0
    emojis: List[Emoji] = list


@dataclass
class Guild_Integrations_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild whose integrations were updated
    '''
    guild_id: Snowflake = 0


@dataclass
class Guild_Member_Add(Guild_Member):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    '''
    guild_id: Snowflake = 0


@dataclass
class Guild_Member_Remove(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    user:
        the user who was removed
    '''
    guild_id: Snowflake = 0
    user: User = None


@dataclass
class Guild_Member_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    roles:
        user role ids
    user:
        the user
    nick:
        nickname of the user in the guild
    joined_at:
        when the user joined the guild
    premium_since:
        Boosting
    deaf:
        whether the user is deafened in voice channels
    mute:
        whether the user is muted in voice channels
    pending:
        Membership_Screening
    '''
    guild_id: Snowflake = 0
    roles: List[Snowflake] = list
    user: User = None
    nick: str = ''
    joined_at: datetime = datetime.now().isoformat()
    premium_since: datetime = datetime.now().isoformat()
    deaf: bool = None
    mute: bool = None
    pending: bool = False
    communication_disabled_until: datetime = None


@dataclass
class Guild_Members_Chunk(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    members:
        set of guild members
    chunk_index:
        the chunk index in the expected chunks for this response
    chunk_count:
        the total number of expected chunks for this response
    not_found:
        if passing an invalid id to `REQUEST_GUILD_MEMBERS`, it will be returned here
    presences:
        if passing true to `REQUEST_GUILD_MEMBERS`, presences of the returned members will be here
    nonce:
        Guild_Members_Request
    '''
    guild_id: Snowflake = 0
    members: List[Guild_Member] = list
    chunk_index: int = 0
    chunk_count: int = 0
    not_found: list = list
    presences: List[Presence_Update] = list
    nonce: str = ''


@dataclass
class Guild_Role_Create(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    role:
        the role created
    '''
    guild_id: Snowflake = 0
    role: Role = None


@dataclass
class Guild_Role_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        the id of the guild
    role:
        the role updated
    '''
    guild_id: Snowflake = 0
    role: Role = None


@dataclass
class Guild_Role_Delete(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    role_id:
        id of the role
    '''
    guild_id: Snowflake = 0
    role_id: Snowflake = 0


@dataclass
class Integration_Create(Integration):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    '''
    guild_id: Snowflake = None


@dataclass
class Integration_Update(Integration):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    '''
    guild_id: Snowflake = None


@dataclass
class Integration_Delete(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        integration id
    guild_id:
        id of the guild
    application_id:
        id of the bot/OAuth2 application for this discord integration
    '''
    id: Snowflake = None
    guild_id: Snowflake = None
    application_id: Snowflake = None


@dataclass
class Invite_Create(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        the channel the invite is for
    code:
        Code
    created_at:
        the time at which the invite was created
    guild_id:
        the guild of the invite
    inviter:
        the user that created the invite
    max_age:
        how long the invite is valid for
    max_uses:
        the maximum number of times the invite can be used
    target_type:
        Type_Of_Target
    target_user:
        the user whose stream to display for this voice channel stream invite
    target_application:
        the embedded application to open for this voice channel embedded application invite
    temporary:
        whether
    uses:
        how many times the invite has been used
    '''
    channel_id: Snowflake = 0
    code: str = ''
    created_at: datetime = datetime.now().isoformat()
    guild_id: Snowflake = 0
    inviter: User = None
    max_age: int = 0
    max_uses: int = 0
    target_type: int = 0
    target_user: User = None
    target_application: Application = None
    temporary: bool = False
    uses: int = 0


@dataclass
class Invite_Delete(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        the channel of the invite
    guild_id:
        the guild of the invite
    code:
        Code
    '''
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0
    code: str = ''


@dataclass
class Message_Delete(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the message
    channel_id:
        the id of the channel
    guild_id:
        the id of the guild
    '''
    id: Snowflake = 0
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0


@dataclass
class Message_Delete_Bulk(DiscordObject):
    '''
    Atrributes
    ----------
    ids:
        the ids of the messages
    channel_id:
        the id of the channel
    guild_id:
        the id of the guild
    '''
    ids: List[Snowflake] = list
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0


@dataclass
class Message_Reaction_Add(DiscordObject):
    '''
    Atrributes
    ----------
    user_id:
        the id of the user
    channel_id:
        the id of the channel
    message_id:
        the id of the message
    guild_id:
        the id of the guild
    member:
        the member who reacted if this happened in a guild
    emoji:
        Example
    '''
    user_id: Snowflake = 0
    channel_id: Snowflake = 0
    message_id: Snowflake = 0
    guild_id: Snowflake = 0
    member: Guild_Member = None
    emoji: Emoji = None


@dataclass
class Message_Reaction_Remove(DiscordObject):
    '''
    Atrributes
    ----------
    user_id:
        the id of the user
    channel_id:
        the id of the channel
    message_id:
        the id of the message
    guild_id:
        the id of the guild
    emoji:
        Example
    '''
    user_id: Snowflake = 0
    channel_id: Snowflake = 0
    message_id: Snowflake = 0
    guild_id: Snowflake = 0
    emoji: Emoji = None


@dataclass
class Message_Reaction_Remove_All(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        the id of the channel
    message_id:
        the id of the message
    guild_id:
        the id of the guild
    '''
    channel_id: Snowflake = 0
    message_id: Snowflake = 0
    guild_id: Snowflake = 0


@dataclass
class Message_Reaction_Remove_Emoji(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        the id of the channel
    guild_id:
        the id of the guild
    message_id:
        the id of the message
    emoji:
        the emoji that was removed
    '''
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0
    message_id: Snowflake = 0
    emoji: Emoji = None


@dataclass
class Presence_Update(DiscordObject):
    '''
    Atrributes
    ----------
    user:
        the user presence is being updated for
    guild_id:
        id of the guild
    status:
        either "idle", "dnd", "online",
    activities:
        user's current activities
    client_status:
        user's platform-dependent status
    '''
    user: User = None
    guild_id: Snowflake = 0
    status: str = ''
    activities: List[Activity] = list
    client_status: Client_Status = None


@dataclass
class Client_Status(DiscordObject):
    '''
    Active sessions are indicated with an "online", "idle", or "dnd" string per platform. If a user is offline or invisible, the corresponding field is not present.
    
    Atrributes
    ----------
    desktop:
        the user's status set for an active desktop
    mobile:
        the user's status set for an active mobile
    web:
        the user's status set for an active web
    '''
    desktop: str = ''
    mobile: str = ''
    web: str = ''


@dataclass
class Bot_Activity(DiscordObject):
    name: str = ''
    type: Activity_Types = None
    url: str = ''

@dataclass
class Activity(DiscordObject):
    '''
    > info
    > Bots are only able to send `name`, `type`, and optionally `url`.
    
    Atrributes
    ----------
    name:
        the activity's name
    type:
        Activity_Type
    url:
        stream url, is validated when type is 1
    created_at:
        unix timestamp
    timestamps:
        unix timestamps for start and/or end of the game
    application_id:
        application id for the game
    details:
        what the player is currently doing
    state:
        the user's current party status
    emoji:
        the emoji used for a custom status
    party:
        information for the current party of the player
    assets:
        images for the presence and their hover texts
    secrets:
        secrets for Rich Presence joining and spectating
    instance:
        whether
    flags:
        Activity_Flags
    buttons:
        the custom buttons shown in the Rich Presence
    '''
    name: str = ''
    type: Activity_Types = None
    url: str = ''
    created_at: int = 0
    timestamps: Activity_Timestamps = None
    application_id: Snowflake = 0
    details: str = ''
    state: str = ''
    emoji: Emoji = None
    party: Activity_Party = None
    assets: Activity_Assets = None
    secrets: Activity_Secrets = None
    instance: bool = False
    flags: Activity_Flags = None
    buttons: List[Activity_Buttons] = list


class Activity_Types(Enum):
    '''
    > info
    > The streaming type currently only supports Twitch and YouTube. Only `https://twitch.tv/` and `https://youtube.com/` urls will work.
    '''
    GAME = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


@dataclass
class Activity_Timestamps(DiscordObject):
    '''
    Atrributes
    ----------
    start:
        unix time
    end:
        unix time
    '''
    start: int = 0
    end: int = 0


@dataclass
class Activity_Emoji(DiscordObject):
    '''
    Atrributes
    ----------
    name:
        the name of the emoji
    id:
        the id of the emoji
    animated:
        whether this emoji is animated
    '''
    name: str = ""
    id: Snowflake = 0
    animated: bool = False


@dataclass
class Activity_Party(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the id of the party
    size:
        used to show the party's current and maximum size
    '''
    id: str = ""
    size: Tuple[int, int] = list


@dataclass
class Activity_Assets(DiscordObject):
    '''
    Atrributes
    ----------
    large_image:
        the id for a large asset of the activity, usually a snowflake
    large_text:
        text displayed when hovering over the large image of the activity
    small_image:
        the id for a small asset of the activity, usually a snowflake
    small_text:
        text displayed when hovering over the small image of the activity
    '''
    large_image: str = ''
    large_text: str = ''
    small_image: str = ''
    small_text: str = ''


@dataclass
class Activity_Secrets(DiscordObject):
    '''
    Atrributes
    ----------
    join:
        the secret for joining a party
    spectate:
        the secret for spectating a game
    match:
        the secret for a specific instanced match
    '''
    join: str = ''
    spectate: str = ''
    match: str = ''


class Activity_Flags(Flag):
    INSTANCE = 1 << 0
    JOIN = 1 << 1
    SPECTATE = 1 << 2
    JOIN_REQUEST = 1 << 3
    SYNC = 1 << 4
    PLAY = 1 << 5


@dataclass
class Activity_Buttons(DiscordObject):
    '''
    When received over the gateway, the `buttons` field is an array of strings, which are the button labels. Bots cannot access a user's activity button URLs. When sending, the `buttons` field must be an array of the below object:
    
    Atrributes
    ----------
    label:
        the text shown on the button
    url:
        the url opened when clicking the button
    '''
    label: str = ''
    url: str = ''


@dataclass
class Typing_Start(DiscordObject):
    '''
    Atrributes
    ----------
    channel_id:
        id of the channel
    guild_id:
        id of the guild
    user_id:
        id of the user
    timestamp:
        unix time
    member:
        the member who started typing if this happened in a guild
    '''
    channel_id: Snowflake = 0
    guild_id: Snowflake = 0
    user_id: Snowflake = 0
    timestamp: int = 0
    member: Guild_Member = None


@dataclass
class Voice_Server_Update(DiscordObject):
    '''
    Atrributes
    ----------
    token:
        voice connection token
    guild_id:
        the guild this voice server update is for
    endpoint:
        the voice server host
    '''
    token: str = ''
    guild_id: Snowflake = 0
    endpoint: str = ''


@dataclass
class Webhook_Update(DiscordObject):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild
    channel_id:
        id of the channel
    '''
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0

@dataclass
class Application_Command(DiscordObject):
    '''
    > info
    > warn
    > Required `options` must be listed before optional options
    
    Atrributes
    ----------
    id:
        unique id of the command
    application_id:
        unique id of the parent application
    guild_id:
        guild id of the command, if not global
    name:
        1-32 lowercase character name matching `^[\w-]{1,32}$`
    description:
        1-100 character description
    options:
        the parameters for the command
    default_permission:
        whether the command is enabled by default when the app is added to a guild
    '''
    id: Snowflake = None
    type: Application_Command_Type = 1
    application_id: Snowflake = None
    guild_id: Snowflake = None
    name: str = ''
    description: str = ''
    options: List[Application_Command_Option] = list
    default_permission: bool = False

class Application_Command_Type(Enum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3

@dataclass
class Application_Command_Extra_Fields(Application_Command):
    '''
    Atrributes
    ----------
    guild_id:
        id of the guild the command is in
    '''
    guild_id: Snowflake = None

@dataclass
class Application_Command_Create(Application_Command_Extra_Fields):
    pass

@dataclass
class Application_Command_Update(Application_Command_Extra_Fields):
    pass

@dataclass
class Application_Command_Delete(Application_Command_Extra_Fields):
    pass

@dataclass
class Gateway_Bot(DiscordObject):
    '''
    Params
    ------
    url:
        The WSS URL that can be used for connecting to the gateway
    shards:
        Shards
    session_start_limit:
        Information on the current session start limit
    '''
    url: str = ''
    shards: int = 0
    session_start_limit: Session_Start_Limit = None


@dataclass
class Session_Start_Limit(DiscordObject):
    '''
    Atrributes
    ----------
    total:
        The total number of session starts the current user is allowed
    remaining:
        The remaining number of session starts the current user is allowed
    reset_after:
        The number of milliseconds after which the limit resets
    max_concurrency:
        The number of identify requests allowed per 5 seconds
    '''
    total: int = 0
    remaining: int = 0
    reset_after: int = 0
    max_concurrency: int = 0


class O_Auth2_UR_Ls(Enum):
    '''
    > warn
    > In accordance with the relevant RFCs, the token and token revocation URLs will **only** accept a content type of `x-www-form-urlencoded`. JSON content is not permitted and will return an error.
    
    Atrributes
    ----------
    Base authorization URL:
        Base authorization URL
    Token URL:
        Token URL
    Token_Revocation:
        Token_Revocation
    '''
    Base_authorization_URL = "https://discord.com/api/oauth2/authorize"
    Token_URL = "https://discord.com/api/oauth2/token"
    Token_Revocation = "https://discord.com/api/oauth2/token/revoke"



class Gateway_Opcodes(Enum):
    '''
    Atrributes
    ----------
    Dispatch:
        An event was dispatched.
    Heartbeat:
        Fired periodically by the client to keep the connection alive.
    Identify:
        Starts a new session during the initial handshake.
    Presence Update:
        Update the client's presence.
    Voice State Update:
        Used to join/leave
    Resume:
        Resume a previous session that was disconnected.
    Reconnect:
        You should attempt to reconnect and resume immediately.
    Request Guild Members:
        Request information about offline guild members in a large guild.
    Invalid Session:
        The session has been invalidated. You should reconnect and identify/resume accordingly.
    Hello:
        Sent immediately after connecting, contains the `heartbeat_interval` to use.
    Heartbeat ACK:
        Sent in response to receiving a heartbeat to acknowledge that it has been received.
    '''
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILD_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11


class Gateway_Close_Event_Codes(Enum):
    '''
    Atrributes
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
    '''
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
    '''
    Atrributes
    ----------
    Identify:
        Begin a voice websocket connection.
    Select Protocol:
        Select the voice protocol.
    Ready:
        Complete the websocket handshake.
    Heartbeat:
        Keep the websocket connection alive.
    Session Description:
        Describe the session.
    Speaking:
        Indicate which users are speaking.
    Heartbeat ACK:
        Sent to acknowledge a received client heartbeat.
    Resume:
        Resume a connection.
    Hello:
        Time to wait between sending heartbeats in milliseconds.
    Resumed:
        Acknowledge a successful session resume.
    Client Disconnect:
        A client has disconnected from the voice channel
    '''
    IDENTIFY = 0
    SELECT_PROTOCOL = 1
    READY = 2
    HEARTBEAT = 3
    SESSION_DESCRIPTION = 4
    SPEAKING = 5
    HEARTBEAT_ACK = 6
    RESUME = 7
    HELLO = 8
    RESUMED = 9
    CLIENT_DISCONNECT = 13


class Voice_Close_Event_Codes(Enum):
    '''
    Atrributes
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
    '''
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

class RPC_Error_Codes(Enum):
    '''
    Atrributes
    ----------
    Unknown error:
        An unknown error occurred.
    Invalid payload:
        You sent an invalid payload.
    Invalid command:
        Invalid command name specified.
    Invalid guild:
        Invalid guild ID specified.
    Invalid event:
        Invalid event name specified.
    Invalid channel:
        Invalid channel ID specified.
    Invalid permissions:
        You lack permissions to access the given resource.
    Invalid client ID:
        An invalid OAuth2 application ID was used to authorize
    Invalid origin:
        An invalid OAuth2 application origin was used to authorize
    Invalid token:
        An invalid OAuth2 token was used to authorize
    Invalid user:
        The specified user ID was invalid.
    OAuth2 error:
        A standard OAuth2 error occurred; check the data  for the OAuth2 error details.
    Select channel timed out:
        An asynchronous `SELECT_TEXT_CHANNEL`/`SELECT_VOICE_CHANNEL` command timed out.
    `GET_GUILD` timed out:
        An asynchronous `GET_GUILD` command timed out.
    Select voice force required:
        You tried to join a user to a voice channel but the user was already in one.
    Capture shortcut already listening:
        You tried to capture more than one shortcut key at once.
    '''
    UNKNOWN_ERROR = 1000
    INVALID_PAYLOAD = 4000
    INVALID_COMMAND = 4002
    INVALID_GUILD = 4003
    INVALID_EVENT = 4004
    INVALID_CHANNEL = 4005
    INVALID_PERMISSIONS = 4006
    INVALID_CLIENT_ID = 4007
    INVALID_ORIGIN = 4008
    INVALID_TOKEN = 4009
    INVALID_USER = 4010
    OAUTH2_ERROR = 5000
    SELECT_CHANNEL_TIMED_OUT = 5001
    GET_GUILD_TIMED_OUT = 5002
    SELECT_VOICE_FORCE_REQUIRED = 5003
    CAPTURE_SHORTCUT_ALREADY_LISTENING = 5004


class RPC_Close_Event_Codes(Enum):
    '''
    Atrributes
    ----------
    Invalid client ID:
        You connected to the RPC server with an invalid client ID.
    Invalid origin:
        You connected to the RPC server with an invalid origin.
    Rate limited:
        You are being rate limited.
    Token revoked:
        The OAuth2 token associated with a connection was revoked, get a new one!
    Invalid version:
        The RPC Server version specified in the connection string was not valid.
    Invalid encoding:
        The encoding specified in the connection string was not valid.
    '''
    INVALID_CLIENT_ID = 4000
    INVALID_ORIGIN = 4001
    RATE_LIMITED = 4002
    TOKEN_REVOKED = 4003
    INVALID_VERSION = 4004
    INVALID_ENCODING = 4005

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
    '''
    *** These permissions require the owner account to use [two-factor authentication](https:#/discord.com/developers/docs/topics/oauth2#twofactor-authentication-requirement) when used on a guild that has server-wide 2FA enabled.**
    Note that these internal permission names may be referred to differently by the Discord client. For example, "Manage Permissions" refers to MANAGE_ROLES and "Use Voice Activity" refers to USE_VAD.
    
    Atrributes
    ----------
    CREATE_INSTANT_INVITE:
        Allows creation of instant invites
    KICK_MEMBERS:
        Allows kicking members
    BAN_MEMBERS:
        Allows banning members
    ADMINISTRATOR:
        Allows all permissions and bypasses channel permission overwrites
    MANAGE_CHANNELS:
        Allows management and editing of channels
    MANAGE_GUILD:
        Allows management and editing of the guild
    ADD_REACTIONS:
        Allows for the addition of reactions to messages
    VIEW_AUDIT_LOG:
        Allows for viewing of audit logs
    PRIORITY_SPEAKER:
        Allows for using priority speaker in a voice channel
    STREAM:
        Allows the user to go live
    VIEW_CHANNEL:
        Allows guild members to view a channel, which includes reading messages in text channels
    SEND_MESSAGES:
        Allows for sending messages in a channel
    SEND_TTS_MESSAGES:
        Allows for sending of `/tts` messages
    MANAGE_MESSAGES:
        Allows for deletion of other users messages
    EMBED_LINKS:
        Links sent by users with this permission will be auto-embedded
    ATTACH_FILES:
        Allows for uploading images and files
    READ_MESSAGE_HISTORY:
        Allows for reading of message history
    MENTION_EVERYONE:
        Allows for using the `@everyone` tag to notify all users in a channel, and the `@here` tag to notify all online users in a channel
    USE_EXTERNAL_EMOJIS:
        Allows the usage of custom emojis from other servers
    VIEW_GUILD_INSIGHTS:
        Allows for viewing guild insights
    CONNECT:
        Allows for joining of a voice channel
    SPEAK:
        Allows for speaking in a voice channel
    MUTE_MEMBERS:
        Allows for muting members in a voice channel
    DEAFEN_MEMBERS:
        Allows for deafening of members in a voice channel
    MOVE_MEMBERS:
        Allows for moving of members between voice channels
    USE_VAD:
        Allows for using voice-activity-detection in a voice channel
    CHANGE_NICKNAME:
        Allows for modification of own nickname
    MANAGE_NICKNAMES:
        Allows for modification of other users nicknames
    MANAGE_ROLES:
        Allows management and editing of roles
    MANAGE_WEBHOOKS:
        Allows management and editing of webhooks
    MANAGE_EMOJIS:
        Allows management and editing of emojis
    USE_SLASH_COMMANDS:
        Allows members to use slash commands in text channels
    REQUEST_TO_SPEAK:
        Allows for requesting to speak in stage channels.
    MANAGE_THREADS:
        Allows for deleting and archiving threads, and viewing all private threads
    USE_PUBLIC_THREADS:
        Allows for creating and participating in threads
    USE_PRIVATE_THREADS:
        Allows for creating and participating in private threads
    '''
    CREATE_INSTANT_INVITE = 0X0000000001
    KICK_MEMBERS = 0X0000000002
    BAN_MEMBERS = 0X0000000004
    ADMINISTRATOR = 0X0000000008
    MANAGE_CHANNELS = 0X0000000010
    MANAGE_GUILD = 0X0000000020
    ADD_REACTIONS = 0X0000000040
    VIEW_AUDIT_LOG = 0X0000000080
    PRIORITY_SPEAKER = 0X0000000100
    STREAM = 0X0000000200
    VIEW_CHANNEL = 0X0000000400
    SEND_MESSAGES = 0X0000000800
    SEND_TTS_MESSAGES = 0X0000001000
    MANAGE_MESSAGES = 0X0000002000
    EMBED_LINKS = 0X0000004000
    ATTACH_FILES = 0X0000008000
    READ_MESSAGE_HISTORY = 0X0000010000
    MENTION_EVERYONE = 0X0000020000
    USE_EXTERNAL_EMOJIS = 0X0000040000
    VIEW_GUILD_INSIGHTS = 0X0000080000
    CONNECT = 0X0000100000
    SPEAK = 0X0000200000
    MUTE_MEMBERS = 0X0000400000
    DEAFEN_MEMBERS = 0X0000800000
    MOVE_MEMBERS = 0X0001000000
    USE_VAD = 0X0002000000
    CHANGE_NICKNAME = 0X0004000000
    MANAGE_NICKNAMES = 0X0008000000
    MANAGE_ROLES = 0X0010000000
    MANAGE_WEBHOOKS = 0X0020000000
    MANAGE_EMOJIS = 0X0040000000
    USE_SLASH_COMMANDS = 0X0080000000
    REQUEST_TO_SPEAK = 0X0100000000
    MANAGE_THREADS = 0X0400000000
    USE_PUBLIC_THREADS = 0X0800000000
    USE_PRIVATE_THREADS = 0X1000000000


@dataclass
class Role(DiscordObject):
    '''
    Roles without colors (`color == 0`) do not count towards the final computed color in the user list.
    
    Atrributes
    ----------
    id:
        role id
    name:
        role name
    color:
        integer representation of hexadecimal color code
    hoist:
        if this role is pinned in the user listing
    position:
        position of this role
    permissions:
        permission bit set
    managed:
        whether this role is managed by an integration
    mentionable:
        whether this role is mentionable
    tags:
        the tags this role has
    '''
    id: Snowflake = 0
    name: str = ''
    color: int = 0
    hoist: bool = False
    icon: str = None
    unicode_emoji: str = None
    position: int = 0
    permissions: str = ''
    managed: bool = False
    mentionable: bool = False
    tags: Role_Tags = None


@dataclass
class Role_Tags(DiscordObject):
    '''
    Atrributes
    ----------
    bot_id:
        the id of the bot this role belongs to
    integration_id:
        the id of the integration this role belongs to
    premium_subscriber:
        whether this is the guild's premium subscriber role
    '''
    bot_id: Snowflake = 0
    integration_id: Snowflake = 0
    premium_subscriber: bool = False


@dataclass
class Rate_Limit_Response(DiscordObject):
    '''
    Note that the normal rate-limiting headers will be sent in this response. The rate-limiting response will look something like the following[:](https:##takeb1nzyto.space/)
    
    Atrributes
    ----------
    message:
        A message saying you are being rate limited.
    retry_after:
        The number of seconds to wait before submitting another request.
    _global:
        A value indicating if you are being globally rate limited
    '''
    message: str = ''
    retry_after: float = 0.0
    _global: bool = False


@dataclass
class Team(DiscordObject):
    '''
    Atrributes
    ----------
    icon:
        a hash of the image of the team's icon
    id:
        the unique id of the team
    members:
        the members of the team
    name:
        the name of the team
    owner_user_id:
        the user id of the current team owner
    '''
    icon: str = ''
    id: Snowflake = 0
    members: List[Team_Members] = list
    name: str = ''
    owner_user_id: Snowflake = 0


@dataclass
class Team_Members(DiscordObject):
    '''
    Atrributes
    ----------
    membership_state:
        Membership_State
    permissions:
        will always be `[""]`
    team_id:
        the id of the parent team of which they are a member
    user:
        the avatar, discriminator, id, and username of the user
    '''
    membership_state: int = 0
    permissions: List[str] = list
    team_id: Snowflake = 0
    user: User = None


class Membership_State_Enum(Enum):
    INVITED = 1
    ACCEPTED = 2


class Encryption_Modes(Enum):
    '''
    >warn
    >The nonce has to be stripped from the payload before encrypting and before decrypting the audio data
    Finally, the voice server will respond with a [Opcode 4 Session Description](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) that includes the `mode` and `secret_key`, a 32 byte array used for [encrypting and sending](https:#/discord.com/developers/docs/topics/voice_connections#encrypting-and-sending-voice) voice data:
    '''
    Normal = "xsalsa20_poly1305"
    Suffix = "xsalsa20_poly1305_suffix"
    Lite = "xsalsa20_poly1305_lite"


@dataclass
class Voice_Packet(DiscordObject):
    Version__Flags: c_byte = 0x80
    Payload_Type: c_byte = 0x78
    Sequence: c_ushort = 0x0
    Timestamp: c_uint = 0x0
    SSRC: c_uint = 0x0
    Encrypted_audio: bytearray = 0x0


class Speaking(Enum):
    '''
    To notify clients that you are speaking or have stopped speaking, send an [Opcode 5 Speaking](https://discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload:
    Example Speaking Payload
    > You must send at least one [Opcode 5 Speaking](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload before sending voice data, or you will be disconnected with an invalid SSRC error.```json
    '''
    MICROPHONE = 1 << 0
    SOUNDSHARE = 1 << 1
    PRIORITY = 1 << 2


@dataclass
class IP_Discovery(DiscordObject):
    '''
    Generally routers on the Internet mask or obfuscate UDP ports through a process called NAT. Most users who implement voice will want to utilize IP discovery to find their external IP and port which will then be used for receiving voice communications. To retrieve your external IP and port, send the following UDP packet to your voice port (all numeric are big endian):
    
    Atrributes
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
    '''
    Type: int = 0x1 or 0x2
    Length: int = None
    SSRC: c_uint = None
    Address: str = None
    Port: c_ushort = None


class Snowflake_ID_Format(Enum):
    '''
    Params
    ------
    Timestamp:
        Milliseconds since Discord Epoch, the first second of 2015
    Internal worker ID:
        `
    Internal process ID:
        `
    Increment:
        For every ID that is generated on that process, this number is incremented
    '''
    Timestamp = (0 >> 22) + DISCORD_EPOCH
    Internal_worker_ID = (0 & 0x3E0000) >> 17
    Internal_process_ID = (0 & 0x1F000) >> 12
    Increment = 0 & 0xFFF


class Formats(Enum):
    '''
    Using the markdown for either users, roles, or channels will usually mention the target(s) accordingly, but this can be suppressed using the `allowed_mentions` parameter when creating a message. Standard emoji are currently rendered using [Twemoji](https:##twemoji.twitter.com/) for Desktop/Android and Apple's native emoji on iOS.
    Timestamps will display the given timestamp in the user's timezone and locale.
    '''
    Nickname = "<@!{user_id}>"
    Channel = "<#{channel_id}>"
    Role = "<@&{role_id}>"
    Standard_Emoji = "Unicode Characters"
    Custom_Emoji = "<:{name}:{id}>"
    Custom_Animated_Emoji = "<a:{name}:{id}>"
    Unix_Timestamp = "<t:{TIMESTAMP}>"
    Unix_Timestamp_Styled = "<t:{TIMESTAMP}:{STYLE}>"


class Timestamp_Styles(Enum):
    '''
    *default
    
    Atrributes
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
    '''
    Short_Time = "t"
    Long_Time = "T"
    Short_Date = "d"
    Long_Date = "D"
    Short_DateTime = "f"
    Long_DateTime = "F"
    Relative_Time = "R"


class Image_Formats(Enum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    WebP = "webp"
    GIF = "gif"


class CDN_Endpoints(Enum):
    '''
    * In the case of endpoints that support GIFs, the hash will begin with `a_` if it is available in GIF format. (example: `a_1269e74af4df7417b13759eae50c83dc`)
    ** In the case of the Default User Avatar endpoint, the value for `user_discriminator` in the path should be the user's discriminator modulo 5—Test#1337 would be `1337 % 5`, which evaluates to 2.
    *** In the case of the Default User Avatar endpoint, the size of images returned is constant with the "size" querystring parameter being ignored.
    '''
    Custom_Emoji = "emojis/{emoji_id}.png"
    Guild_Icon = "icons/{guild_id}/{guild_icon}.png"
    Guild_Splash = "splashes/{guild_id}/{guild_splash}.png"
    Guild_Discovery_Splash = "discovery-splashes/{guild_id}/{guild_discovery_splash}.png"
    Guild_Banner = "banners/{guild_id}/{guild_banner}.png"
    Default_User_Avatar = "embed/avatars/{user_discriminator}.png"
    User_Avatar = "avatars/{user_id}/{user_avatar}.png"
    Application_Icon = "app-icons/{application_id}/{icon}.png"
    Application_Cover = "app-assets/{application_id}/cover_image.png"
    Application_Asset = "app-assets/{application_id}/{asset_id}.png"
    Achievement_Icon = "app-assets/{application_id}/achievements/{achievement_id}/icons/{icon_hash}.png"
    Team_Icon = "team-icons/{team_id}/{team_icon}.png"
    Sticker = "stickers/{sticker_id}.png"
    Role_Icon = "role-icons/{role_id}/{role_icon}.png"


@dataclass
class Component(DiscordObject):
    '''
    Atrributes
    ----------
    type:
        Component_Type
    style:
        Button_Styles
    label:
        text that appears on the button, max 80 characters
    emoji:
        `name`, `id`, and `animated`
    custom_id:
        a developer-defined identifier for the button, max 100 characters
    url:
        a url for link-style buttons
    disabled:
        whether the button is disabled, default `false`
    components:
        a list of child components
    '''
    type: Component_Types = 0
    style: Button_Styles = None
    label: str = None
    emoji: Emoji = None
    custom_id: str = None
    url: str = None
    disabled: bool = False
    components: List[Component] = None
    options: List[Select_Option] = None
    placeholder: str = None
    min_values: int = None
    max_values: int = None
    value: str = None
    required: bool = None
    min_length: int = None
    max_length: int = None


class Component_Types(Enum):
    '''
    Atrributes
    ----------
    Action Row:
        A container for other components
    Button:
        A button
    Select Menu:
        A select menu for picking from choices
    '''
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4

class Text_Input_Styles(Enum):
    Short = 1
    Paragraph = 2


@dataclass
class Button(DiscordObject):
    '''
    Buttons come in a variety of styles to convey different types of actions. These styles also define what fields are valid for a button.
    - Non-link buttons **must** have a `custom_id`, and cannot have a `url`
    - Link buttons **must** have a `url`, and cannot have a `custom_id`
    - Link buttons do not send an [interaction](https:#/discord.com/developers/docs/interactions/slash_commands#interaction-object) to your app when clicked
    
    Atrributes
    ----------
    type:
        `2` for a button
    style:
        Button_Styles
    label:
        text that appears on the button, max 80 characters
    emoji:
        `name`, `id`, and `animated`
    custom_id:
        a developer-defined identifier for the button, max 100 characters
    url:
        a url for link-style buttons
    disabled:
        whether the button is disabled
    '''
    type: Component_Types = Component_Types.BUTTON
    style: Button_Styles = 1
    label: str = ''
    emoji: Emoji = None
    custom_id: str = ''
    url: str = ''
    disabled: bool = False


class Button_Styles(Enum):
    '''
    ![An image showing the different button styles](button-styles.png)
    When a user clicks on a button, your app will receive an [interaction](https:#/discord.com/developers/docs/interactions/slash_commands#interaction-object) including the message the button was on:

    Attributes
    ----------
    Primary:
        Blurple, requires `custom_id`
    Secondary:
        Grey, requires `custom_id`
    Success:
        Green, requires `custom_id`
    Danger:
        Red, requires `custom_id`
    Link:
        Grey, requires `url`
    '''
    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5


@dataclass
class Select_Menu(DiscordObject):
    '''
    Atrributes
    ----------
    custom_id:
        a developer-defined identifier for the button, max 100 characters
    options:
        the choices in the select, max 25
    placeholder:
        custom placeholder text if nothing is selected, max 100 characters
    min_values:
        the minimum number of items that must be chosen; default 1, min 0, max 25
    max_values:
        the maximum number of items that can be chosen; default 1, max 25
    disabled:
        disable the select, default false
    '''
    type: Component_Types = Component_Types.SELECT_MENU
    custom_id: str = ''
    options: List[Select_Option] = None
    placeholder: str = ''
    min_values: int = 0
    max_values: int = 0
    disabled: bool = False


@dataclass
class Select_Option(DiscordObject):
    '''
    Atrributes
    ----------
    label:
        the user-facing name of the option, max 25 characters
    value:
        the dev-define value of the option, max 100 characters
    description:
        an additional description of the option, max 50 characters
    emoji:
        `id`, `name`, and `animated`
    default:
        will render this option as selected by default
    '''
    label: str = ''
    value: str = ''
    description: str = ''
    emoji: Emoji = None
    default: bool = False


@dataclass
class Application_Command_Option(DiscordObject):
    '''
    > info
    
    Atrributes
    ----------
    type:
        Application_Command_Option_Type
    name:
        1-32 lowercase character name matching `^[\w-]{1,32}$`
    description:
        1-100 character description
    required:
        if the parameter is required
    choices:
        choices for `string` and `int` types for the user to pick from
    options:
        if the option is a subcommand
    '''
    type: Application_Command_Option_Type = 0
    name: str = ''
    description: str = ''
    #default: bool = False
    required: bool = False
    choices: List[Application_Command_Option_Choice] = list
    options: List[Application_Command_Option] = list
    channel_types: List[Channel_Types] = list


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


@dataclass
class Application_Command_Option_Choice(DiscordObject):
    '''
    If you specify `choices` for an option, they are the **only** valid values for a user to pick
    
    Atrributes
    ----------
    name:
        1-100 character choice name
    value:
        value of the choice, up to 100 characters if string
    '''
    name: str = ''
    value: str = ''


@dataclass
class Guild_Application_Command_Permissions(DiscordObject):
    '''
    Returned when fetching the permissions for a command in a guild.
    
    Atrributes
    ----------
    id:
        the id of the command
    application_id:
        the id of the application the command belongs to
    guild_id:
        the id of the guild
    permissions:
        the permissions for the command in the guild
    '''
    id: Snowflake = None
    application_id: Snowflake = None
    guild_id: Snowflake = None
    permissions: List[Application_Command_Permissions] = list


@dataclass
class Application_Command_Permissions(DiscordObject):
    '''
    Application command permissions allow you to enable or disable commands for specific users or roles within a guild.
    
    Atrributes
    ----------
    id:
        the id of the role
    type:
        role
    permission:
        `true` to allow, `false`, to disallow
    '''
    id: Snowflake = None
    type: Application_Command_Permission_Type = None
    permission: bool = False


class Application_Command_Permission_Type(Enum):
    ROLE = 1
    USER = 2


@dataclass
class Interaction(DiscordObject):
    '''
    * This is always present on application command interaction types. It is optional for future-proofing against new interaction types
    ** `member` is sent when the command is invoked in a guild, and `user` is sent when invoked in a DM
    
    Atrributes
    ----------
    id:
        id of the interaction
    application_id:
        id of the application this interaction is for
    type:
        the type of interaction
    data:
        the command data payload
    guild_id:
        the guild it was sent from
    channel_id:
        the channel it was sent from
    member:
        guild member data for the invoking user, including permissions
    user:
        user  for the invoking user, if invoked in a DM
    token:
        a continuation token for responding to the interaction
    version:
        read-only property, always `1`
    message:
        for components, the message they were attached to
    '''
    id: Snowflake = 0
    application_id: Snowflake = 0
    type: Interaction_Type = None
    data: Application_Command_Interaction_Data = None
    guild_id: Snowflake = 0
    channel_id: Snowflake = 0
    member: Guild_Member = None
    user: User = None
    token: str = ''
    version: int = 0
    message: Message = None
    locale: str = None
    guild_locale: str = None


class Interaction_Type(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


@dataclass
class Application_Command_Interaction_Data(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        the ID of the invoked command
    name:
        the name of the invoked command
    resolved:
        converted users + roles + channels
    options:
        the params + values from the user
    custom_id:
        `custom_id`
    component_type:
        Type
    '''
    id: Snowflake = 0
    name: str = ''
    type: Interaction_Type = None
    resolved: Application_Command_Interaction_Data_Resolved = None
    options: List[Application_Command_Interaction_Data_Option] = list
    custom_id: str = ''
    component_type: Component_Types = None
    values: List[str] = list
    target_id: Snowflake = 0
    components: List[Component] = list


@dataclass
class Application_Command_Interaction_Data_Resolved(DiscordObject):
    '''
    > info
    * Partial `Member` objects are missing `user`, `deaf` and `mute` fields
    ** Partial `Channel` objects only have `id`, `name`, `type` and `permissions` fields
    
    Atrributes
    ----------
    users:
        the ids and User s
    members:
        the ids and  Member s
    roles:
        the ids and Role s
    channels:
        the ids and  Channel s
    '''
    users: Dict[Snowflake, User] = dict
    members: Dict[Snowflake, Guild_Member] = dict
    roles: Dict[Snowflake, Role] = dict
    channels: Dict[Snowflake, Channel] = dict
    messages: Dict[Snowflake, Message] = dict
    attachments: Dict[Snowflake, Attachment] = dict


@dataclass
class Application_Command_Interaction_Data_Option(DiscordObject):
    '''
    All options have names, and an option can either be a parameter and input value--in which case `value` will be set--or it can denote a subcommand or group--in which case it will contain a top-level key and another array of `options`.
    
    Atrributes
    ----------
    name:
        the name of the parameter
    type:
        Application_Command_Option_Type
    value:
        the value of the pair
    options:
        present if this option is a group
    '''
    name: str = ""
    type: Application_Command_Option_Type = 0
    value: dict = dict
    options: List[Application_Command_Interaction_Data_Option] = list


@dataclass
class Interaction_Response(DiscordObject):
    '''
    Atrributes
    ----------
    type:
        the type of response
    data:
        an optional response message
    '''
    type: Interaction_Callback_Type = None
    data: Interaction_Application_Command_Callback_Data = None


class Interaction_Callback_Type(Enum):
    '''
    * Only valid for [component-based](https:#/discord.com/developers/docs/interactions/message_components#) interactions
    
    Atrributes
    ----------
    PONG:
        ACK a `Ping`
    CHANNEL_MESSAGE_WITH_SOURCE:
        respond to an interaction with a message
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE:
        ACK an interaction and edit a response later, the user sees a loading state
    DEFERRED_UPDATE_MESSAGE:
        for components, ACK an interaction and edit the original message later; the user does not see a loading state
    UPDATE_MESSAGE:
        for components, edit the message the component was attached to
    '''
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9


@dataclass
class Interaction_Application_Command_Callback_Data(DiscordObject):
    '''
    Not all message fields are currently supported.
    
    Atrributes
    ----------
    tts:
        is the response TTS
    content:
        message content
    embeds:
        supports up to 10 embeds
    allowed_mentions:
        Allowed_Mentions
    flags:
        Interaction_Application_Command_Callback_Data_Flags
    components:
        message components
    '''
    tts: bool = None
    content: str = None
    embeds: List[Embed] = None
    allowed_mentions: Allowed_Mentions = None
    flags: Message_Flags = None
    components: List[Component] = None
    attachments: List[Attachment] = None
    choices: List[Application_Command_Option_Choice] = None
    custom_id: str = None
    title: str = None


class Interaction_Application_Command_Callback_Data_Flags(Flag):
    '''
    Atrributes
    ----------
    EPHEMERAL:
        only the user receiving the message can see it
    '''
    EPHEMERAL = 1 << 6


@dataclass
class Message_Interaction(DiscordObject):
    '''
    Atrributes
    ----------
    id:
        id of the interaction
    type:
        the type of interaction
    name:
        Application_Command
    user:
        the user who invoked the interaction
    '''
    id: Snowflake = None
    type: Interaction_Type = None
    name: str = None
    user: User = None


class Gateway_Commands(Events):
    '''
    Events are payloads sent over the socket to a client that correspond to events in Discord.
    
    Params:
        :Identify: triggers the initial handshake with the gateway
        :Resume: resumes a dropped gateway connection
        :Heartbeat: maintains an active gateway connection
        :Request_Guild_Members: requests members for a guild
        :Update_Voice_State: joins, moves,
        :Update_Status: updates a client's presence
    '''
    Identify = staticmethod(Identify)
    Resume = staticmethod(Resume)
    Heartbeat = staticmethod(int)
    Request_Guild_Members = staticmethod(Guild_Request_Members)
    Update_Voice_State = staticmethod(Gateway_Voice_State_Update)
    Update_Status = staticmethod(Gateway_Presence_Update)

