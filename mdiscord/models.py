# -*- coding: utf-8 -*-
"""
Discord Models
----------

Discord raw API types.

:copyright: (c) 2020-2024 Mmesek
:version: 2024/06/10 20:45
"""
from ctypes import c_byte, c_uint, c_ushort
from enum import IntEnum, Enum, Flag
from datetime import datetime
from typing import Annotated, Any, Optional

from msgspec import UNSET, Meta

from .base_model import DiscordObject, Snowflake, DISCORD_EPOCH, Events, Nullable, UnixTimestamp, Duration


class Limits(IntEnum):
    """
    To facilitate showing rich content, rich embeds do not follow the traditional limits of message content.
    However, some limits are still in place to prevent excessively large embeds.
    The following table describes the limits:
    Additionally, the combined sum of characters in all title, description, field.name, field.value, footer.text, and author.name fields across all embeds attached to a message must not exceed 6000 characters.
    Violating any of these constraints will result in a Bad Request response.
    Embeds are deduplicated by URL.
    If a message contains multiple embeds with the same URL, only the first is shown.
    """

    TITLE = 256
    DESCRIPTION = 4096
    FIELDS = 25
    FIELD_NAME = 256
    FIELD_VALUE = 1024
    FOOTER_TEXT = 2048
    AUTHOR_NAME = 256
    TOTAL = 6000


EmbedDescriptionConstraint = Annotated[str, Meta(max_length=Limits.DESCRIPTION.value)]
TextConstraint = Annotated[str, Meta(max_length=Limits.FOOTER_TEXT.value)]
ValueConstraint = Annotated[str, Meta(max_length=Limits.FIELD_VALUE.value)]
TitleConstraint = Annotated[str, Meta(max_length=Limits.TITLE.value)]
LongDescConstraint = Annotated[str, Meta(min_length=1, max_length=200)]
DescriptionConstraint = Annotated[str, Meta(max_length=100)]
KeyConstraint = Annotated[str, Meta(pattern=r"a-z0-9_", min_length=1, max_length=50)]
LongNameConstraint = Annotated[str, Meta(max_length=50)]
ModalTitleConstraint = Annotated[str, Meta(max_length=45)]
CommandConstraint = Annotated[str, Meta(min_length=1, max_length=32, pattern=r"^[\w-]{1,32}$")]

LargeThresholdConstraint = Annotated[int, Meta(ge=50, le=250)]
EmbedFieldsConstraint = Annotated[list["Embed_Field"], Meta(max_length=Limits.FIELDS.value)]
EmbedsConstraint = Annotated[list["Embed"], Meta(max_length=10)]
ComponentConstraint = Annotated[list["Component"], Meta(max_length=5)]


class Application(DiscordObject):
    id: Snowflake = UNSET
    """ID of the app"""
    name: str = UNSET
    """Name of the app"""
    icon: Nullable[str] = UNSET
    """Icon_Hash"""
    description: str = UNSET
    """Description of the app"""
    rpc_origins: Optional[list[str]] = UNSET
    """List of RPC origin URLs, if RPC is enabled"""
    bot_public: bool = UNSET
    """When false, only the app owner can add the app to guilds"""
    bot_require_code_grant: bool = UNSET
    """When true, the app's bot will only join upon completion of the full OAuth2 code grant flow"""
    bot: Optional["User"] = UNSET
    """Partial user  for the bot user associated with the app"""
    terms_of_service_url: Optional[str] = UNSET
    """URL of the app's Terms of Service"""
    privacy_policy_url: Optional[str] = UNSET
    """URL of the app's Privacy Policy"""
    owner: Optional["User"] = UNSET
    """Partial user  for the owner of the app"""
    summary: str = UNSET
    """deprecated and will be removed in v11. An empty string"""
    verify_key: str = UNSET
    """GetTicket"""
    team: Nullable["Team"] = UNSET
    """If the app belongs to a team, this will be a list of the members of that team"""
    guild_id: Optional[Snowflake] = UNSET
    """Guild associated with the app. For example, a developer support server"""
    guild: Optional["Guild"] = UNSET
    """Partial  of the associated guild"""
    primary_sku_id: Optional[Snowflake] = UNSET
    """If this app is a game sold on Discord, this field will be the id of the 'Game SKU' that is created, if exists"""
    slug: Optional[str] = UNSET
    """If this app is a game sold on Discord, this field will be the URL slug that links to the store page"""
    cover_image: Optional[str] = UNSET
    """Cover_Image_Hash"""
    flags: Optional["Application_Flags"] = UNSET
    """Flags"""
    approximate_guild_count: Optional[int] = UNSET
    """Approximate count of guilds the app has been added to"""
    redirect_uris: Optional[list[str]] = UNSET
    """Array of redirect URIs for the app"""
    interactions_endpoint_url: Optional[str] = UNSET
    """Interactions_Endpoint_URL"""
    role_connections_verification_url: Optional[str] = UNSET
    """Role connection verification URL for the app"""
    tags: Optional[list[str]] = UNSET
    """List of tags describing the content and functionality of the app. Max of 5 tags"""
    install_params: Optional["Install_Params"] = UNSET
    """Settings for the app's default in-app authorization link, if enabled"""
    integration_types_config: Optional["Application_Integration_Types"] = UNSET
    """In_Preview"""
    custom_install_url: Optional[str] = UNSET
    """Default custom authorization URL for the app, if enabled"""


class Application_Integration_Types(Enum):
    """
    Where an app can be installed, also called its supported [installation contexts](https://discord.com/developers/docs/resources/application#installation_context).
    """

    GUILD_INSTALL = 0
    """App is installable to servers"""
    USER_INSTALL = 1
    """App is installable to users"""


class Application_Integration_Type_Configuration(DiscordObject):
    oauth2_install_params: Optional["Install_Params"] = UNSET
    """Install params for each installation context's default in-app authorization link"""


class Application_Flags(Flag):
    APPLICATION_AUTO_MODERATION_RULE_CREATE_BADGE = 1 << 6
    """Auto_Moderation_API"""
    GATEWAY_PRESENCE = 1 << 12
    """presence_update_Events"""
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    """presence_update_Events"""
    GATEWAY_GUILD_MEMBERS = 1 << 14
    """Under_GUILD_MEMBERS"""
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    """Under_GUILD_MEMBERS"""
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    """Indicates unusual growth of an app that prevents verification"""
    EMBEDDED = 1 << 17
    """Indicates if an app is embedded within the Discord client"""
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    """Message_Content"""
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19
    """Message_Content"""
    APPLICATION_COMMAND_BADGE = 1 << 23
    """Application_Commands"""


class Install_Params(DiscordObject):
    scopes: list[str] = UNSET
    """Scopes"""
    permissions: str = UNSET
    """Permissions"""


class Application_Role_Connection_Metadata(DiscordObject):
    type: "Application_Role_Connection_Metadata_Type" = UNSET
    """type of metadata value"""
    key: KeyConstraint = UNSET
    """dictionary key for the metadata field"""
    name: DescriptionConstraint = UNSET
    """name of the metadata field"""
    name_localizations: Optional[dict["Locales", DescriptionConstraint]] = UNSET
    """translations of the name"""
    description: LongDescConstraint = UNSET
    """description of the metadata field"""
    description_localizations: Optional[dict["Locales", LongDescConstraint]] = UNSET
    """translations of the description"""


class Application_Role_Connection_Metadata_Type(Enum):
    """
    > info
    > Each metadata type offers a comparison operation that allows guilds to configure role requirements based on metadata values stored by the bot.
    Bots specify a metadata value for each user and guilds specify the required guild's configured value within the guild role settings.
    """

    INTEGER_LESS_THAN_OR_EQUAL = 1
    """the metadata value"""
    INTEGER_GREATER_THAN_OR_EQUAL = 2
    """the metadata value"""
    INTEGER_EQUAL = 3
    """the metadata value"""
    INTEGER_NOT_EQUAL = 4
    """the metadata value"""
    DATETIME_LESS_THAN_OR_EQUAL = 5
    """the metadata value"""
    DATETIME_GREATER_THAN_OR_EQUAL = 6
    """the metadata value"""
    BOOLEAN_EQUAL = 7
    """the metadata value"""
    BOOLEAN_NOT_EQUAL = 8
    """the metadata value"""


class Audit_Log(DiscordObject):
    """
    * Threads referenced in THREAD_CREATE and THREAD_UPDATE events are included in the threads map since archived threads might not be kept in memory by clients.
    """

    application_commands: list["Application_Command"] = UNSET
    """List of application commands referenced in the audit log"""
    audit_log_entries: list["Audit_Log_Entry"] = UNSET
    """List of audit log entries, sorted from most to least recent"""
    auto_moderation_rules: list["Auto_Moderation_Rule"] = UNSET
    """List of auto moderation rules referenced in the audit log"""
    guild_scheduled_events: list["Guild_Scheduled_Event"] = UNSET
    """List of guild scheduled events referenced in the audit log"""
    integrations: list["Integration"] = UNSET
    """List of  integration s"""
    threads: list["Channel"] = UNSET
    """List of threads referenced in the audit log"""
    users: list["User"] = UNSET
    """List of users referenced in the audit log"""
    webhooks: list["Webhook"] = UNSET
    """List of webhooks referenced in the audit log"""


class Audit_Log_Entry(DiscordObject):
    """
    > warn
    > For APPLICATION_COMMAND_PERMISSION_UPDATE events, the target_id is the command ID or the app ID since the changes array represents the entire permissions property on the [guild permissions](https:#/discord.com/developers/docs/interactions/application_commands#application-command-permissions-object-guild-application-command-permissions-structure) object.
    """

    target_id: Nullable[str] = UNSET
    """ID of the affected entity"""
    guild_id: Optional[Snowflake] = UNSET
    changes: Optional["Audit_Log_Change"] = UNSET
    """Changes made to the target_id"""
    user_id: Nullable[Snowflake] = UNSET
    """User"""
    id: Snowflake = UNSET
    """ID of the entry"""
    action_type: "Audit_Log_Events" = UNSET
    """Type of action that occurred"""
    options: Optional["Optional_Audit_Entry_Info"] = UNSET
    """Additional info for certain event types"""
    reason: Optional[str] = UNSET
    """Reason for the change"""


class Audit_Log_Events(Enum):
    """
    If no object is noted, there won't be a changes array in the entry, though other fields like the target_id still exist and many have fields in the [options array](https:#/discord.com/developers/docs/resources/audit_log#audit_log_entry_object_optional_audit_entry_info).The table below lists audit log events and values (the action_type field) that your app may receive.
    * Object has exception(s) to available keys.
    See the [exceptions](https:#/discord.com/developers/docs/resources/audit_log#audit-log-change-object-audit-log-change-exceptions) section below for details.
    """

    GUILD_UPDATE = 1
    """Server settings were updated"""
    CHANNEL_CREATE = 10
    """Channel was created"""
    CHANNEL_UPDATE = 11
    """Channel settings were updated"""
    CHANNEL_DELETE = 12
    """Channel was deleted"""
    CHANNEL_OVERWRITE_CREATE = 13
    """Permission overwrite was added to a channel"""
    CHANNEL_OVERWRITE_UPDATE = 14
    """Permission overwrite was updated for a channel"""
    CHANNEL_OVERWRITE_DELETE = 15
    """Permission overwrite was deleted from a channel"""
    MEMBER_KICK = 20
    """Member was removed from server"""
    MEMBER_PRUNE = 21
    """Members were pruned from server"""
    MEMBER_BAN_ADD = 22
    """Member was banned from server"""
    MEMBER_BAN_REMOVE = 23
    """Server ban was lifted for a member"""
    MEMBER_UPDATE = 24
    """Member was updated in server"""
    MEMBER_ROLE_UPDATE = 25
    """Member was added"""
    MEMBER_MOVE = 26
    """Member was moved to a different voice channel"""
    MEMBER_DISCONNECT = 27
    """Member was disconnected from a voice channel"""
    BOT_ADD = 28
    """Bot user was added to server"""
    ROLE_CREATE = 30
    """Role was created"""
    ROLE_UPDATE = 31
    """Role was edited"""
    ROLE_DELETE = 32
    """Role was deleted"""
    INVITE_CREATE = 40
    """Server invite was created"""
    INVITE_UPDATE = 41
    """Server invite was updated"""
    INVITE_DELETE = 42
    """Server invite was deleted"""
    WEBHOOK_CREATE = 50
    """Webhook was created"""
    WEBHOOK_UPDATE = 51
    """Webhook properties"""
    WEBHOOK_DELETE = 52
    """Webhook was deleted"""
    EMOJI_CREATE = 60
    """Emoji was created"""
    EMOJI_UPDATE = 61
    """Emoji name was updated"""
    EMOJI_DELETE = 62
    """Emoji was deleted"""
    MESSAGE_DELETE = 72
    """Single message was deleted"""
    MESSAGE_BULK_DELETE = 73
    """Multiple messages were deleted"""
    MESSAGE_PIN = 74
    """Message was pinned to a channel"""
    MESSAGE_UNPIN = 75
    """Message was unpinned from a channel"""
    INTEGRATION_CREATE = 80
    """App was added to server"""
    INTEGRATION_UPDATE = 81
    """App was updated"""
    INTEGRATION_DELETE = 82
    """App was removed from server"""
    STAGE_INSTANCE_CREATE = 83
    """Stage instance was created"""
    STAGE_INSTANCE_UPDATE = 84
    """Stage instance details were updated"""
    STAGE_INSTANCE_DELETE = 85
    """Stage instance was deleted"""
    STICKER_CREATE = 90
    """Sticker was created"""
    STICKER_UPDATE = 91
    """Sticker details were updated"""
    STICKER_DELETE = 92
    """Sticker was deleted"""
    GUILD_SCHEDULED_EVENT_CREATE = 100
    """Event was created"""
    GUILD_SCHEDULED_EVENT_UPDATE = 101
    """Event was updated"""
    GUILD_SCHEDULED_EVENT_DELETE = 102
    """Event was cancelled"""
    THREAD_CREATE = 110
    """Thread was created in a channel"""
    THREAD_UPDATE = 111
    """Thread was updated"""
    THREAD_DELETE = 112
    """Thread was deleted"""
    APPLICATION_COMMAND_PERMISSION_UPDATE = 121
    """Permissions were updated for a command"""
    AUTO_MODERATION_RULE_CREATE = 140
    """Auto Moderation rule was created"""
    AUTO_MODERATION_RULE_UPDATE = 141
    """Auto Moderation rule was updated"""
    AUTO_MODERATION_RULE_DELETE = 142
    """Auto Moderation rule was deleted"""
    AUTO_MODERATION_BLOCK_MESSAGE = 143
    """Message was blocked by Auto Moderation"""
    AUTO_MODERATION_FLAG_TO_CHANNEL = 144
    """Message was flagged by Auto Moderation"""
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED = 145
    """Member was timed out by Auto Moderation"""
    CREATOR_MONETIZATION_REQUEST_CREATED = 150
    """Creator monetization request was created"""
    CREATOR_MONETIZATION_TERMS_ACCEPTED = 151
    """Creator monetization terms were accepted"""
    ONBOARDING_PROMPT_CREATE = 163
    """Guild Onboarding Question was created"""
    ONBOARDING_PROMPT_UPDATE = 164
    """Guild Onboarding Question was updated"""
    ONBOARDING_PROMPT_DELETE = 165
    """Guild Onboarding Question was deleted"""
    ONBOARDING_CREATE = 166
    """Guild Onboarding was created"""
    ONBOARDING_UPDATE = 167
    """Guild Onboarding was updated"""
    HOME_SETTINGS_CREATE = 190
    """Guild Server Guide was created"""
    HOME_SETTINGS_UPDATE = 191
    """Guild Server Guide was updated"""


class Optional_Audit_Entry_Info(DiscordObject):
    application_id: Snowflake = UNSET
    """ID of the app whose permissions were targeted"""
    auto_moderation_rule_name: str = UNSET
    """Name of the Auto Moderation rule that was triggered"""
    auto_moderation_rule_trigger_type: str = UNSET
    """Trigger type of the Auto Moderation rule that was triggered"""
    channel_id: Snowflake = UNSET
    """Channel in which the entities were targeted"""
    count: str = UNSET
    """Number of entities that were targeted"""
    delete_member_days: str = UNSET
    """Number of days after which inactive members were kicked"""
    id: Snowflake = UNSET
    """ID of the overwritten entity"""
    members_removed: str = UNSET
    """Number of members removed by the prune"""
    message_id: Snowflake = UNSET
    """ID of the message that was targeted"""
    role_name: Optional[str] = UNSET
    """Name of the role if type is '0'"""
    type: str = UNSET
    """Type of overwritten entity - role (0) or member (1)"""
    integration_type: "Integration_Types" = UNSET
    """The type of integration which performed the action"""


class Audit_Log_Change(DiscordObject):
    """
    Some events don't follow the same pattern as other audit log events.
    Details about these exceptions are explained in [the next section](https://discord.com/developers/docs/resources/audit_log#audit_log_change_object_audit_log_change_exceptions).
    """

    new_value: Optional[Any] = UNSET
    """New value of the key"""
    old_value: Optional[Any] = UNSET
    """Old value of the key"""
    key: str = UNSET
    """Name of the changed entity, with a few exceptions"""


class Audit_Log_Change_Key(DiscordObject):
    name: str = UNSET
    """name changed"""
    description: str = UNSET
    """description changed"""
    icon_hash: str = UNSET
    """icon changed"""
    splash_hash: str = UNSET
    """invite splash page artwork changed"""
    discovery_splash_hash: str = UNSET
    """discovery splash changed"""
    banner_hash: str = UNSET
    """guild banner changed"""
    owner_id: Snowflake = UNSET
    """owner changed"""
    region: str = UNSET
    """region changed"""
    preferred_locale: str = UNSET
    """preferred locale changed"""
    afk_channel_id: Snowflake = UNSET
    """afk channel changed"""
    afk_timeout: Duration = UNSET
    """afk timeout duration changed"""
    rules_channel_id: Snowflake = UNSET
    """id of the rules channel changed"""
    public_updates_channel_id: Snowflake = UNSET
    """id of the public updates channel changed"""
    mfa_level: "MFA_Level" = UNSET
    """two-factor auth requirement changed"""
    verification_level: "Verification_Level" = UNSET
    """required verification level changed"""
    explicit_content_filter: "Explicit_Content_Filter_Level" = UNSET
    """Whose_Messages"""
    default_message_notifications: "Default_Message_Notification_Level" = UNSET
    """Message_Notification_Level"""
    vanity_url_code: str = UNSET
    """guild invite vanity url changed"""
    _add: "Role" = UNSET
    """new role added"""
    _remove: "Role" = UNSET
    """role removed"""
    prune_delete_days: int = UNSET
    """change in number of days after which inactive and role-unassigned members are kicked"""
    widget_enabled: bool = UNSET
    """server widget enabled/disable"""
    widget_channel_id: Snowflake = UNSET
    """channel id of the server widget changed"""
    system_channel_id: Snowflake = UNSET
    """id of the system channel changed"""
    position: int = UNSET
    """text"""
    topic: str = UNSET
    """text channel topic"""
    bitrate: int = UNSET
    """voice channel bitrate changed"""
    permission_overwrites: "Overwrite" = UNSET
    """permissions on a channel changed"""
    nsfw: bool = UNSET
    """channel nsfw restriction changed"""
    application_id: Snowflake = UNSET
    """application id of the added"""
    rate_limit_per_user: Duration = UNSET
    """amount of seconds a user has to wait before sending another message changed"""
    permissions: str = UNSET
    """Permissions"""
    color: int = UNSET
    """role color changed"""
    hoist: bool = UNSET
    """role is now displayed/no longer displayed separate from online users"""
    mentionable: bool = UNSET
    """role is now mentionable/unmentionable"""
    allow: str = UNSET
    """a permission on a text"""
    deny: str = UNSET
    """a permission on a text"""
    code: str = UNSET
    """invite code changed"""
    channel_id: Snowflake = UNSET
    """channel for invite code changed"""
    inviter_id: Snowflake = UNSET
    """person who created invite code changed"""
    max_uses: int = UNSET
    """change to max number of times invite code can be used"""
    uses: int = UNSET
    """number of times invite code used changed"""
    max_age: int = UNSET
    """how long invite code lasts changed"""
    temporary: bool = UNSET
    """invite code is temporary/never expires"""
    deaf: bool = UNSET
    """user server deafened/undeafened"""
    mute: bool = UNSET
    """user server muted/unmuted"""
    nick: str = UNSET
    """user nickname changed"""
    avatar_hash: str = UNSET
    """user avatar changed"""
    id: Snowflake = UNSET
    """the id of the changed entity - sometimes used in conjunction with other keys"""
    type: "Channel_Types" = UNSET
    """type of entity created"""
    enable_emoticons: bool = UNSET
    """integration emoticons enabled/disabled"""
    expire_behavior: "Integration_Expire_Behaviors" = UNSET
    """integration expiring subscriber behavior changed"""
    expire_grace_period: int = UNSET
    """integration expire grace period changed"""
    user_limit: int = UNSET
    """new user limit in a voice channel"""
    privacy_level: "Privacy_Level" = UNSET
    """the privacy level of the stage instance."""


class Auto_Moderation_Rule(DiscordObject):
    id: Snowflake = UNSET
    """the id of this rule"""
    guild_id: Snowflake = UNSET
    """the id of the guild which this rule belongs to"""
    name: str = UNSET
    """the rule name"""
    creator_id: Snowflake = UNSET
    """the user which first created this rule"""
    event_type: "Event_Types" = UNSET
    """Event_Type"""
    trigger_type: "Trigger_Types" = UNSET
    """Trigger_Type"""
    trigger_metadata: "Trigger_Metadata" = UNSET
    """Trigger_Metadata"""
    actions: "Auto_Moderation_Action" = UNSET
    """the actions which will execute when the rule is triggered"""
    enabled: bool = UNSET
    """whether the rule is enabled"""
    exempt_roles: list[Snowflake] = UNSET
    """the role ids that should not be affected by the rule"""
    exempt_channels: list[Snowflake] = UNSET
    """the channel ids that should not be affected by the rule"""


class Trigger_Types(Enum):
    """
    Characterizes the type of content which can trigger the rule.
    """

    CHECK_IF_CONTENT_CONTAINS_WORDS_FROM_A_USER_DEFINED_LIST_OF_KEYWORDS = 1
    CHECK_IF_CONTENT_REPRESENTS_GENERIC_SPAM = 3
    CHECK_IF_CONTENT_CONTAINS_WORDS_FROM_INTERNAL_PRE_DEFINED_WORDSETS = 4
    CHECK_IF_CONTENT_CONTAINS_MORE_UNIQUE_MENTIONS_THAN_ALLOWED = 5
    CHECK_IF_MEMBER_PROFILE_CONTAINS_WORDS_FROM_A_USER_DEFINED_LIST_OF_KEYWORDS = 6


class Trigger_Metadata(DiscordObject):
    """
    value of [trigger_type](https:##discord.com/developers/docs/resources/auto_moderation#auto_moderation_rule_object_trigger_types).Additional data used to determine whether a rule should be triggered.
    Different fields are relevant based on the
    * A keyword can be a phrase which contains multiple words.
    [Wildcard symbols](https:##discord.com/developers/docs/resources/auto_moderation#auto-moderation-rule-object-keyword-matching-strategies) can be used to customize how each keyword will be matched.
    Each keyword must be 60 characters or less.
    ** Only Rust flavored regex is currently supported, which can be tested in online editors such as [Rustexp](https:##rustexp.lpil.uk/).
    Each regex pattern must be 260 characters or less.
    *** Each allow_list keyword can be a phrase which contains multiple words.
    [Wildcard symbols](https:##discord.com/developers/docs/resources/auto_moderation#auto-moderation-rule-object-keyword-matching-strategies) can be used to customize how each keyword will be matched.
    Rules with KEYWORD [trigger_type](https:##discord.com/developers/docs/resources/auto_moderation#auto-moderation-rule-object-trigger-types) accept a maximum of 100 keywords.
    Rules with KEYWORD_PRESET [trigger_type](https:##discord.com/developers/docs/resources/auto_moderation#auto-moderation-rule-object-trigger-types) accept a maximum of 1000 keywords.
    """

    keyword_filter: list[str] = UNSET
    """substrings which will be searched for in content"""
    regex_patterns: list[str] = UNSET
    """regular expression patterns which will be matched against content"""
    presets: list["Keyword_Preset_Types"] = UNSET
    """the internally pre-defined wordsets which will be searched for in content"""
    allow_list: list[str] = UNSET
    """substrings which should not trigger the rule"""
    mention_total_limit: int = UNSET
    """total number of unique role and user mentions allowed per message"""
    mention_raid_protection_enabled: bool = UNSET
    """whether to automatically detect mention raids"""


class Trigger_Metadata_Field_Limits(Enum):
    KEYWORD_FILTER = 1000
    REGEX_PATTERNS = 10
    ALLOW_LIST = 100
    ALLOW_LIST_PRESET = 1000
    MAX_CHARS_PER_STR = 60
    MAX_CHARS_PER_PATTERN_STR = 260


class Keyword_Preset_Types(Enum):
    WORDS_THAT_MAY_BE_CONSIDERED_FORMS_OF_SWEARING = 1
    WORDS_THAT_REFER_TO_SEXUALLY_EXPLICIT_BEHAVIOR = 2
    PERSONAL_INSULTS = 3


class Event_Types(Enum):
    """
    Indicates in what event context a rule should be checked.
    """

    WHEN_A_MEMBER_SENDS = 1
    WHEN_A_MEMBER_EDITS_THEIR_PROFILE = 2


class Keyword_Matching_Strategies(DiscordObject):
    """
    Use the wildcard symbol (*) at the beginning or end of a keyword to define how it should be matched.
    All keywords are case insensitive.
    **Suffix** - word must end with the keyword
    **Anywhere** - keyword can appear anywhere in the content
    **Whole Word** - keyword is a full word or phrase and must be surrounded by whitespace.
    """


class Auto_Moderation_Action_Execution(DiscordObject):
    """
    * message_id will not exist if message was blocked by [Auto Moderation](#DOCS_RESOURCES_AUTO_MODERATION) or content was not part of any message
    ** alert_system_message_id will not exist if this event does not correspond to an action with type SEND_ALERT_MESSAGE
    *** MESSAGE_CONTENT (1 << 15) [gateway intent](https:#/discord.com/developers/docs/topics/gateway#gateway-intents) is required to receive the content and matched_content fields.
    """

    guild_id: Snowflake = UNSET
    """ID of the guild in which action was executed"""
    action: "Auto_Moderation_Action" = UNSET
    """Action which was executed"""
    rule_id: Snowflake = UNSET
    """ID of the rule which action belongs to"""
    rule_trigger_type: "Trigger_Types" = UNSET
    """Trigger type of rule which was triggered"""
    user_id: Snowflake = UNSET
    """ID of the user which generated the content which triggered the rule"""
    channel_id: Optional[Snowflake] = UNSET
    """ID of the channel in which user content was posted"""
    message_id: Optional[Snowflake] = UNSET
    """ID of any user message which content belongs to"""
    alert_system_message_id: Optional[Snowflake] = UNSET
    """ID of any system auto moderation messages posted as a result of this action"""
    content: str = UNSET
    """User-generated text content"""
    matched_keyword: Nullable[str] = UNSET
    """Word"""
    matched_content: Nullable[str] = UNSET
    """Substring in content that triggered the rule"""


class Auto_Moderation_Action(DiscordObject):
    """
    * Can be omitted based on type.
    See the Associated Action Types column in [action metadata](https:#/discord.com/developers/docs/resources/auto_moderation#auto-moderation-action-object-action-metadata) to understand which type values require metadata to be set.
    """

    type: "Action_Types" = UNSET
    """the type of action"""
    metadata: "Action_Metadata" = UNSET
    """additional metadata needed during execution for this specific action type"""


class Action_Types(Enum):
    """
    * A TIMEOUT action can only be set up for KEYWORD and MENTION_SPAM rules.
    The MODERATE_MEMBERS permission is required to use the TIMEOUT action type.
    """

    BLOCK_MESSAGE = 1
    SEND_ALERT_MESSAGE = 2
    TIMEOUT = 3
    BLOCK_MEMBER_INTERACTION = 4


class Action_Metadata(DiscordObject):
    """
    value of [action type](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_action_object_action_types).Additional data used when an action is executed.
    Different fields are relevant based on the.
    """

    channel_id: Snowflake = UNSET
    """channel to which user content should be logged"""
    duration_seconds: Duration = UNSET
    """timeout duration in seconds"""
    custom_message: Optional[str] = UNSET
    """additional explanation that will be shown to members whenever their message is blocked"""


class Channel(DiscordObject):
    """
    * `rate_limit_per_user` also applies to thread creation.
    Users can send one message and create one thread during each rate_limit_per_user interval.
    ** For threads created before July 1, 2022, the message count is inaccurate when it's greater than 50.
    """

    id: Snowflake = UNSET
    """the id of this channel"""
    type: "Channel_Types" = UNSET
    """Type_Of_Channel"""
    guild_id: Optional[Snowflake] = UNSET
    """the id of the guild"""
    position: Optional[int] = UNSET
    """sorting position of the channel"""
    permission_overwrites: Optional["Overwrite"] = UNSET
    """explicit permission overwrites for members and roles"""
    name: Optional[Nullable[str]] = UNSET
    """the name of the channel"""
    topic: Optional[Nullable[str]] = UNSET
    """the channel topic"""
    nsfw: Optional[bool] = UNSET
    """whether the channel is nsfw"""
    last_message_id: Optional[Nullable[Snowflake]] = UNSET
    """the id of the last message sent in this channel"""
    bitrate: Optional[int] = UNSET
    """the bitrate"""
    user_limit: Optional[int] = UNSET
    """the user limit of the voice channel"""
    rate_limit_per_user: Duration = UNSET
    """amount of seconds a user has to wait before sending another message"""
    recipients: Optional["User"] = UNSET
    """the recipients of the DM"""
    icon: Optional[Nullable[str]] = UNSET
    """icon hash of the group DM"""
    owner_id: Optional[Snowflake] = UNSET
    """id of the creator of the group DM"""
    application_id: Optional[Snowflake] = UNSET
    """application id of the group DM creator if it is bot-created"""
    managed: Optional[bool] = UNSET
    """for group DM channels: whether the channel is managed by an application via the gdm.join OAuth2 scope"""
    parent_id: Optional[Nullable[Snowflake]] = UNSET
    """for guild channels: id of the parent category for a channel"""
    last_pin_timestamp: Optional[Nullable[datetime]] = UNSET
    """when the last pinned message was pinned. This may be null in events such as GUILD_CREATE when a message is not pinned"""
    rtc_region: Optional[Nullable[str]] = UNSET
    """Voice_Region"""
    video_quality_mode: Optional[int] = UNSET
    """Video_Quality_Mode"""
    message_count: int = UNSET
    """number of messages"""
    member_count: Optional[int] = UNSET
    """an approximate count of users in a thread, stops counting at 50"""
    thread_metadata: Optional["Thread_Metadata"] = UNSET
    """thread-specific fields not needed by other channels"""
    member: Optional["Thread_Member"] = UNSET
    """thread member  for the current user, if they have joined the thread, only included on certain API endpoints"""
    default_auto_archive_duration: Optional[int] = UNSET
    """default duration, copied onto newly created threads, in minutes, threads will stop showing in the channel list after the specified period of inactivity, can be set to: 60, 1440, 4320, 10080"""
    permissions: Optional[str] = UNSET
    """Implicit_Permissions"""
    flags: Optional["Channel_Flags"] = UNSET
    """Channel_Flags"""
    total_message_sent: Optional[int] = UNSET
    """number of messages ever sent in a thread, it's similar to message_count on message creation, but will not decrement the number when a message is deleted"""
    available_tags: Optional[list["Forum_Tag"]] = UNSET
    """the set of tags that can be used in a GUILD_FORUM"""
    applied_tags: Optional[list[Snowflake]] = UNSET
    """the IDs of the set of tags that have been applied to a thread in a GUILD_FORUM"""
    default_reaction_emoji: Optional[Nullable["Default_Reaction"]] = UNSET
    """the emoji to show in the add reaction button on a thread in a GUILD_FORUM"""
    default_thread_rate_limit_per_user: Optional[Duration] = UNSET
    """the initial rate_limit_per_user to set on newly created threads in a channel. this field is copied to the thread at creation time and does not live update"""
    default_sort_order: Optional[Nullable["Sort_Order_Types"]] = UNSET
    """Default_Sort_Order_Type"""
    default_forum_layout: Optional["Forum_Layout_Types"] = UNSET
    """Default_Forum_Layout_View"""


class Channel_Types(Enum):
    """
    > warn
    * The GUILD_MEDIA channel type is still in active development.
    Avoid implementing any features that are not documented here, since they are subject to change without notice!.
    """

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
    GUILD_ANNOUNCEMENT = 5
    """Users_Can_Follow_And_Crosspost_Into_Their_Own_Server"""
    GUILD_STORE = 6
    """Sell_Their_Game_On_Discord"""
    ANNOUNCEMENT_THREAD = 10
    """a temporary sub-channel within a GUILD_ANNOUNCEMENT channel"""
    PUBLIC_THREAD = 11
    """a temporary sub-channel within a GUILD_TEXT"""
    PRIVATE_THREAD = 12
    """a temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the MANAGE_THREADS permission"""
    GUILD_STAGE_VOICE = 13
    """Hosting_Events_With_An_Audience"""
    GUILD_DIRECTORY = 14
    """Hub"""
    GUILD_FORUM = 15
    """Channel that can only contain threads"""
    GUILD_MEDIA = 16
    """Channel that can only contain threads, similar to GUILD_FORUM channels"""


class Video_Quality_Modes(Enum):
    AUTO = 1
    """Discord chooses the quality for optimal performance"""
    FULL = 2
    """720p"""


class Channel_Flags(Flag):
    PINNED = 1 << 1
    """this thread is pinned to the top of its parent GUILD_FORUM"""
    REQUIRE_TAG = 1 << 4
    """whether a tag is required to be specified when creating a thread in a GUILD_FORUM"""
    HIDE_MEDIA_DOWNLOAD_OPTIONS = 1 << 15
    """when set hides the embedded media download options. Available only for media channels"""


class Sort_Order_Types(Enum):
    LATEST_ACTIVITY = 0
    """Sort forum posts by activity"""
    CREATION_DATE = 1
    """Sort forum posts by creation time"""


class Forum_Layout_Types(Enum):
    NOT_SET = 0
    """No default has been set for forum channel"""
    LIST_VIEW = 1
    """Display posts as a list"""
    GALLERY_VIEW = 2
    """Display posts as a collection of tiles"""


class Message(DiscordObject):
    """
    * The author object follows the structure of the user object, but is only a valid user in the case where the message is generated by a user or bot user.
    If the message is generated by a webhook, the author object corresponds to the webhook's id, username, and avatar.
    You can tell if a message is generated by a webhook by checking for the webhook_id on the message object.
    ** An app will receive empty values in the content, embeds, attachments, and components fields while poll will be omitted if they have not configured (or been approved for) the [MESSAGE_CONTENT privileged intent (1 << 15)](https:#/discord.com/developers/docs/topics/gateway#message-content-intent).
    *** Not all channel mentions in a message will appear in mention_channels.
    Only textual channels that are visible to everyone in a lurkable guild will ever be included.
    Only crossposted messages (via Channel Following) currently include mention_channels at all.
    If no mentions in the message meet these requirements, this field will not be sent.
    **** This field is only returned for messages with a type of 19 (REPLY) or 21 (THREAD_STARTER_MESSAGE).
    If the message is a reply but the referenced_message field is not present, the backend did not attempt to fetch the message that was being replied to, so its state is unknown.
    If the field exists but is null, the referenced message was deleted.
    """

    id: Snowflake = UNSET
    """id of the message"""
    channel_id: Snowflake = UNSET
    """id of the channel the message was sent in"""
    guild_id: Optional[Snowflake] = UNSET
    """id of the guild the message was sent in"""
    author: "User" = UNSET
    """the author of this message"""
    member: Optional["Guild_Member"] = UNSET
    """member properties for this message's author"""
    content: str = UNSET
    """contents of the message"""
    timestamp: datetime = UNSET
    """when this message was sent"""
    edited_timestamp: Nullable[datetime] = UNSET
    """when this message was edited"""
    tts: bool = False
    """whether this was a TTS message"""
    mention_everyone: bool = False
    """whether this message mentions everyone"""
    mentions: list["User"] = list
    """users specifically mentioned in the message"""
    mention_roles: list["Role"] = list
    """roles specifically mentioned in this message"""
    mention_channels: list["Channel_Mention"] = list
    """channels specifically mentioned in this message"""
    attachments: list["Attachment"] = list
    """any attached files"""
    embeds: list["Embed"] = list
    """any embedded content"""
    reactions: Optional[list["Reaction"]] = list
    """reactions to the message"""
    nonce: Optional[int] = UNSET
    """used for validating a message was sent"""
    pinned: bool = False
    """whether this message is pinned"""
    webhook_id: Optional[Snowflake] = UNSET
    """if the message is generated by a webhook, this is the webhook's id"""
    type: "Message_Types" = UNSET
    """Type_Of_Message"""
    activity: Optional["Message_Activity"] = UNSET
    """sent with Rich Presence-related chat embeds"""
    application: Optional["Application"] = UNSET
    """sent with Rich Presence-related chat embeds"""
    application_id: Optional[Snowflake] = UNSET
    """Interaction"""
    message_reference: Optional["Message_Reference"] = UNSET
    """data showing the source of a crosspost, channel follow add, pin,"""
    flags: Optional["Message_Flags"] = UNSET
    """Message_Flags"""
    referenced_message: Nullable["Message"] = UNSET
    """the message associated with the message_reference"""
    interaction_metadata: Optional["Message_Interaction_Metadata"] = UNSET
    """In_Preview"""
    interaction: Optional["Interaction"] = UNSET
    """Interaction"""
    thread: Optional["Channel"] = UNSET
    """Thread_Member"""
    components: list["Component"] = UNSET
    """sent if the message contains components like buttons, action rows,"""
    sticker_items: Optional[list["Sticker"]] = UNSET
    """sent if the message contains stickers"""
    stickers: Optional[list["Sticker"]] = UNSET
    """Deprecated the stickers sent with the message"""
    position: Optional[int] = UNSET
    """A generally increasing integer"""
    role_subscription_data: Optional["Role_Subscription_Data"] = UNSET
    """data of the role subscription purchase"""
    resolved: Optional["Resolved_Data"] = UNSET
    """Auto-populated_Select_Menus"""
    poll: Optional["Poll"] = UNSET
    """A poll!"""
    call: Optional["Message_Call"] = UNSET
    """the call associated with the message"""


class Message_Types(Enum):
    """
    > warn
    * Can only be deleted by members with MANAGE_MESSAGES permission.
    """

    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44


class Message_Activity(DiscordObject):
    type: "Message_Activity_Types" = UNSET
    """Type_Of_Message_Activity"""
    party_id: Optional[str] = UNSET
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
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    """this message failed to mention some roles and add their members to the thread"""
    SUPPRESS_NOTIFICATIONS = 1 << 12
    """this message will not trigger push and desktop notifications"""
    IS_VOICE_MESSAGE = 1 << 13
    """this message is a voice message"""


class Sticker_Item(DiscordObject):
    id: Snowflake = UNSET
    """id of the sticker"""
    name: str = UNSET
    """name of the sticker"""
    format_type: "Sticker_Format_Types" = UNSET
    """Type_Of_Sticker_Format"""


class Sticker_Format_Types(Enum):
    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4


class Sticker(DiscordObject):
    """
    * A comma separated list of keywords is the format used in this field by standard stickers, but this is just a convention.
    Incidentally the client will always use a name generated from an emoji as the value of this field when creating or modifying a guild sticker.
    """

    id: Snowflake = UNSET
    """Id_Of_The_Sticker"""
    pack_id: Optional[Snowflake] = UNSET
    """for standard stickers, id of the pack the sticker is from"""
    name: str = UNSET
    """name of the sticker"""
    description: Nullable[str] = UNSET
    """description of the sticker"""
    tags: str = UNSET
    """autocomplete/suggestion tags for the sticker"""
    asset: Optional[str] = UNSET
    """Deprecated previously the sticker asset hash, now an empty string"""
    type: "Sticker_Types" = UNSET
    """Type_Of_Sticker"""
    format_type: "Sticker_Format_Types" = UNSET
    """Type_Of_Sticker_Format"""
    available: Optional[bool] = UNSET
    """whether this guild sticker can be used, may be false due to loss of Server Boosts"""
    guild_id: Optional[Snowflake] = UNSET
    """id of the guild that owns this sticker"""
    user: Optional["User"] = UNSET
    """the user that uploaded the guild sticker"""
    sort_value: Optional[int] = UNSET
    """the standard sticker's sort order within its pack"""


class Sticker_Types(Enum):
    STANDARD = 1
    """an official sticker in a pack"""
    GUILD = 2
    """a sticker uploaded to a guild for the guild's members"""


class Sticker_Pack(DiscordObject):
    id: Snowflake = UNSET
    """id of the sticker pack"""
    stickers: list["Sticker"] = UNSET
    """the stickers in the pack"""
    name: str = UNSET
    """name of the sticker pack"""
    sku_id: Snowflake = UNSET
    """id of the pack's SKU"""
    cover_sticker_id: Optional[Snowflake] = UNSET
    """id of a sticker in the pack which is shown as the pack's icon"""
    description: str = UNSET
    """description of the sticker pack"""
    banner_asset_id: Optional[Snowflake] = UNSET
    """Banner_Image"""


class Message_Call(DiscordObject):
    participants: list["list[Snowflake]"] = UNSET
    """User"""
    ended_timestamp: Optional[Nullable[datetime]] = UNSET
    """time when call ended"""


class Message_Reference(DiscordObject):
    """
    * `channel_id` is optional when creating a reply, but will always be present when receiving an event/response that includes this data model.
    """

    message_id: Optional[Snowflake] = UNSET
    """id of the originating message"""
    channel_id: Optional[Snowflake] = UNSET
    """id of the originating message's channel"""
    guild_id: Optional[Snowflake] = UNSET
    """id of the originating message's guild"""
    fail_if_not_exists: Optional[bool] = UNSET
    """when sending, whether to error if the referenced message doesn't exist instead of sending as a normal"""


class Followed_Channel(DiscordObject):
    channel_id: Snowflake = UNSET
    """source channel id"""
    webhook_id: Snowflake = UNSET
    """created target webhook id"""


class Reaction(DiscordObject):
    count: int = UNSET
    """Total number of times this emoji has been used to react"""
    count_details: "Reaction_Count_Details" = UNSET
    """Reaction_Count_Details"""
    me: bool = UNSET
    """Whether the current user reacted using this emoji"""
    me_burst: bool = UNSET
    """Whether the current user super-reacted using this emoji"""
    emoji: "Emoji" = UNSET
    """emoji information"""
    burst_colors: list = UNSET
    """HEX colors used for super reaction"""


class Reaction_Count_Details(DiscordObject):
    burst: int = UNSET
    """Count of super reactions"""
    normal: int = UNSET
    """Count of normal reactions"""


class Overwrite(DiscordObject):
    id: Snowflake = UNSET
    """role or user_id"""
    type: int = 0
    """either 0 (role) or 1 (member)"""
    allow: str = UNSET
    """permission bit set"""
    deny: str = UNSET
    """permission bit set"""


class Thread_Metadata(DiscordObject):
    """
    > Starting on March 6, threads will be able to be locked and archived independently.
    Read details about the upcoming changes to the locked field in the [Change Log entry](https://discord.com/developers/docs/change/log#update_to_locked_threads).> warn.
    """

    archived: bool = UNSET
    """whether the thread is archived"""
    auto_archive_duration: int = UNSET
    """the thread will stop showing in the channel list after auto_archive_duration minutes of inactivity, can be set to: 60, 1440, 4320, 10080"""
    archive_timestamp: datetime = UNSET
    """timestamp when the thread's archive status was last changed, used for calculating recent activity"""
    locked: bool = UNSET
    """whether the thread is locked; when a thread is locked, only users with MANAGE_THREADS can unarchive it"""
    invitable: Optional[bool] = UNSET
    """whether non-moderators can add other non-moderators to a thread; only available on private threads"""
    create_timestamp: Optional[Nullable[datetime]] = UNSET
    """timestamp when the thread was created; only populated for threads created after 2022-01-09"""


class Thread_Member(DiscordObject):
    """
    * These fields are omitted on the member sent within each thread in the [GUILD_CREATE](https:#/discord.com/developers/docs/topics/gateway_events#guild-create) event.
    ** The member field is only present when with_member is set to true when calling [List Thread Members](https:#/discord.com/developers/docs/resources/channel#list-thread-members) or [Get Thread Member](https:#/discord.com/developers/docs/resources/channel#get-thread-member).
    """

    id: Optional[Snowflake] = UNSET
    """ID of the thread"""
    user_id: Optional[Snowflake] = UNSET
    """ID of the user"""
    join_timestamp: datetime = UNSET
    """Time the user last joined the thread"""
    flags: int = UNSET
    """Any user-thread settings, currently only used for notifications"""
    member: Optional["Guild_Member"] = UNSET
    """Additional information about the user"""


class Default_Reaction(DiscordObject):
    emoji_id: Nullable[Snowflake] = UNSET
    """the id of a guild's custom emoji"""
    emoji_name: Nullable[str] = UNSET
    """the unicode character of the emoji"""


class Forum_Tag(DiscordObject):
    """
    > info
    * At most one of emoji_id and emoji_name may be set to a non-null value.
    """

    id: Snowflake = UNSET
    """the id of the tag"""
    name: str = UNSET
    """the name of the tag"""
    moderated: bool = UNSET
    """whether this tag can only be added to"""
    emoji_id: Nullable[Snowflake] = UNSET
    """the id of a guild's custom emoji"""
    emoji_name: Nullable[str] = UNSET
    """the unicode character of the emoji"""


class Forum_Message_Params(DiscordObject):
    """At least one of `content`, `embeds`, `sticker_ids`, `components`, or `files[n]` is required"""

    content: Optional[str]
    """Message contents (up to 2000 characters)"""
    embeds: Optional[list[str]]
    """Up to 10 `rich` embeds (up to 6000 characters)"""
    allowed_mentions: Optional["Allowed_Mentions"]
    """Allowed mentions for the message"""
    components: Optional[list["Component"]]
    """Components to include with the message"""
    sticker_ids: Optional[list[Snowflake]]
    """IDs of up to 3 [stickers](https://discord.com/developers/docs/resources/sticker#sticker-object) in the server to send in the message"""
    attachments: Optional[list["Attachment"]]
    """Attachment objects with `filename` and `description`"""
    flags: Optional["Message_Flags"]
    """[Message flags](https:#/discord.com/developers/docs/resources/channel#message-object-message-flags) combined as a [bitfield](https:#/en.wikipedia.org/wiki/Bit_field) (only `SUPPRESS_EMBEDS` and `SUPPRESS_NOTIFICATIONS` can be set)"""


class Embed(DiscordObject):
    title: Optional[TitleConstraint] = UNSET
    """title of embed"""
    type: Optional["Embed_Types"] = UNSET
    """Type_Of_Embed"""
    description: Optional[EmbedDescriptionConstraint] = UNSET
    """description of embed"""
    url: Optional[str] = UNSET
    """url of embed"""
    timestamp: Optional[datetime] = UNSET
    """timestamp of embed content"""
    color: Optional[int] = UNSET
    """color code of the embed"""
    footer: Optional["Embed_Footer"] = UNSET
    """footer information"""
    image: Optional["Embed_Image"] = UNSET
    """image information"""
    thumbnail: Optional["Embed_Thumbnail"] = UNSET
    """thumbnail information"""
    video: Optional["Embed_Video"] = UNSET
    """video information"""
    provider: Optional["Embed_Provider"] = UNSET
    """provider information"""
    author: Optional["Embed_Author"] = UNSET
    """author information"""
    fields: Optional[EmbedFieldsConstraint] = UNSET
    """fields information, max of 25"""


class Embed_Types(Enum):
    """
    Embed types are 'loosely defined' and, for the most part, are not used by our clients for rendering.
    Embed attributes power what is rendered.
    Embed types should be considered deprecated and might be removed in a future API version.
    """

    RICH = "generic embed rendered from embed attributes"
    IMAGE = "image embed"
    VIDEO = "video embed"
    GIFV = "animated gif image embed rendered as a video embed"
    ARTICLE = "article embed"
    LINK = "link embed"


class Embed_Thumbnail(DiscordObject):
    url: str = UNSET
    """source url of thumbnail"""
    proxy_url: Optional[str] = UNSET
    """a proxied url of the thumbnail"""
    height: Optional[int] = UNSET
    """height of thumbnail"""
    width: Optional[int] = UNSET
    """width of thumbnail"""


class Embed_Video(DiscordObject):
    url: Optional[str] = UNSET
    """source url of video"""
    proxy_url: Optional[str] = UNSET
    """a proxied url of the video"""
    height: Optional[int] = UNSET
    """height of video"""
    width: Optional[int] = UNSET
    """width of video"""


class Embed_Image(DiscordObject):
    url: str = UNSET
    """source url of image"""
    proxy_url: Optional[str] = UNSET
    """a proxied url of the image"""
    height: Optional[int] = UNSET
    """height of image"""
    width: Optional[int] = UNSET
    """width of image"""


class Embed_Provider(DiscordObject):
    name: Optional[str] = UNSET
    """name of provider"""
    url: Optional[str] = UNSET
    """url of provider"""


class Embed_Author(DiscordObject):
    name: Optional[TitleConstraint] = UNSET
    """name of author"""
    url: Optional[str] = UNSET
    """url of author"""
    icon_url: Optional[str] = UNSET
    """url of author icon"""
    proxy_icon_url: Optional[str] = UNSET
    """a proxied url of author icon"""


class Embed_Footer(DiscordObject):
    text: TextConstraint = UNSET
    """footer text"""
    icon_url: Optional[str] = UNSET
    """url of footer icon"""
    proxy_icon_url: Optional[str] = UNSET
    """a proxied url of footer icon"""


class Embed_Field(DiscordObject):
    name: TitleConstraint = UNSET
    """name of the field"""
    value: ValueConstraint = UNSET
    """value of the field"""
    inline: Optional[bool] = UNSET
    """whether"""


class Attachment(DiscordObject):
    """
    > info
    * Ephemeral attachments will automatically be removed after a set period of time.
    Ephemeral attachments on messages are guaranteed to be available as long as the message itself exists.
    """

    id: Snowflake = UNSET
    """attachment id"""
    filename: str = UNSET
    """name of file attached"""
    description: Optional[str] = UNSET
    """description for the file"""
    content_type: Optional[str] = UNSET
    """Media_Type"""
    size: int = UNSET
    """size of file in bytes"""
    url: str = UNSET
    """source url of file"""
    proxy_url: str = UNSET
    """a proxied url of file"""
    height: Optional[Nullable[int]] = UNSET
    """height of file"""
    width: Optional[Nullable[int]] = UNSET
    """width of file"""
    ephemeral: bool = UNSET
    """whether this attachment is ephemeral"""
    duration_secs: Optional[float] = UNSET
    """the duration of the audio file"""
    waveform: Optional[str] = UNSET
    """base64 encoded bytearray representing a sampled waveform"""
    flags: Optional["Attachment_Flags"] = UNSET
    """Attachment_Flags"""


class Attachment_Flags(Flag):
    IS_REMIX = 1 << 2
    """this attachment has been edited using the remix feature on mobile"""


class Channel_Mention(DiscordObject):
    id: Snowflake = UNSET
    """id of the channel"""
    guild_id: Snowflake = UNSET
    """id of the guild containing the channel"""
    type: "Channel_Types" = UNSET
    """Type_Of_Channel"""
    name: str = UNSET
    """the name of the channel"""


class Allowed_Mention_Types(Enum):
    ROLE_MENTIONS = "roles"
    """Controls role mentions"""
    USER_MENTIONS = "users"
    """Controls user mentions"""
    EVERYONE_MENTIONS = "everyone"
    """Controls @everyone and @here mentions"""


class Allowed_Mentions(DiscordObject):
    parse: list["Allowed_Mention_Types"] = list
    """Allowed_Mention_Types"""
    roles: list[Snowflake] = list
    """Array of role_ids to mention"""
    users: list[Snowflake] = list
    """Array of user_ids to mention"""
    replied_user: bool = UNSET
    """For replies, whether to mention the author of the message being replied to"""


class Role_Subscription_Data(DiscordObject):
    role_subscription_listing_id: Snowflake = UNSET
    """the id of the sku and listing that the user is subscribed to"""
    tier_name: str = UNSET
    """the name of the tier that the user is subscribed to"""
    total_months_subscribed: int = UNSET
    """the cumulative number of months that the user has been subscribed for"""
    is_renewal: bool = UNSET
    """whether this notification is for a renewal rather than a new purchase"""


class Emoji(DiscordObject):
    id: Nullable[Snowflake] = UNSET
    """Emoji_Id"""
    name: Nullable[str] = UNSET
    """emoji name"""
    roles: Optional[list["Role"]] = UNSET
    """roles allowed to use this emoji"""
    user: Optional["User"] = UNSET
    """user that created this emoji"""
    require_colons: Optional[bool] = UNSET
    """whether this emoji must be wrapped in colons"""
    managed: Optional[bool] = UNSET
    """whether this emoji is managed"""
    animated: Optional[bool] = UNSET
    """whether this emoji is animated"""
    available: Optional[bool] = UNSET
    """whether this emoji can be used, may be false due to loss of Server Boosts"""


class Guild(DiscordObject):
    """
    > Fields specific to the GUILD_CREATE event are listed in the [Gateway Events documentation](https:#/discord.com/developers/docs/topics/gateway_events#guild_create).> info
    * These fields are only sent when using the [GET Current User Guilds](https:#/discord.com/developers/docs/resources/user#get-current-user-guilds) endpoint and are relative to the requested user
    ** This field is deprecated and is replaced by [channel.rtc_region](https:#/discord.com/developers/docs/resources/channel#channel-object-channel-structure).
    """

    id: Snowflake = UNSET
    """guild id"""
    name: str = UNSET
    """guild name"""
    icon: Nullable[str] = UNSET
    """Icon_Hash"""
    icon_hash: Optional[Nullable[str]] = UNSET
    """Icon_Hash"""
    splash: Nullable[str] = UNSET
    """Splash_Hash"""
    discovery_splash: Nullable[str] = UNSET
    """Discovery_Splash_Hash"""
    owner: bool = UNSET
    """The_User"""
    owner_id: Snowflake = UNSET
    """id of owner"""
    permissions: str = UNSET
    """The_User"""
    region: Nullable[str] = UNSET
    """Voice_Region"""
    afk_channel_id: Nullable[Snowflake] = UNSET
    """id of afk channel"""
    afk_timeout: Duration = UNSET
    """afk timeout in seconds"""
    widget_enabled: Optional[bool] = UNSET
    """true if the server widget is enabled"""
    widget_channel_id: Optional[Nullable[Snowflake]] = UNSET
    """the channel id that the widget will generate an invite to,"""
    verification_level: "Verification_Level" = UNSET
    """Verification_Level"""
    default_message_notifications: "Default_Message_Notification_Level" = UNSET
    """Message_Notifications_Level"""
    explicit_content_filter: "Explicit_Content_Filter_Level" = UNSET
    """Explicit_Content_Filter_Level"""
    roles: list["Role"] = UNSET
    """roles in the guild"""
    emojis: list["Emoji"] = UNSET
    """custom guild emojis"""
    features: list["Guild_Features"] = UNSET
    """enabled guild features"""
    mfa_level: "MFA_Level" = UNSET
    """MFA_Level"""
    application_id: Nullable[Snowflake] = UNSET
    """application id of the guild creator if it is bot-created"""
    system_channel_id: Nullable[Snowflake] = UNSET
    """the id of the channel where guild notices such as welcome messages and boost events are posted"""
    system_channel_flags: "System_Channel_Flags" = UNSET
    """System_Channel_Flags"""
    rules_channel_id: Nullable[Snowflake] = UNSET
    """the id of the channel where Community guilds can display rules and/or guidelines"""
    joined_at: Optional[datetime] = UNSET
    """when this guild was joined at"""
    large: Optional[bool] = UNSET
    """true if this is considered a large guild"""
    unavailable: Optional[bool] = UNSET
    """true if this guild is unavailable due to an outage"""
    member_count: Optional[int] = UNSET
    """total number of members in this guild"""
    voice_states: Optional[list["Voice_State"]] = UNSET
    """states of members currently in voice channels; lacks the `guild_id` key"""
    members: Optional[list["Guild_Member"]] = UNSET
    """users in the guild"""
    channels: Optional[list[Channel]] = UNSET
    """channels in the guild"""
    threads: Optional[list[Channel]] = UNSET
    """all active threads in the guild that current user has permission to view"""
    presences: Optional[list["Presence_Update"]] = UNSET
    """presences of the members in the guild, will only include non-offline members if the size is greater than `large threshold`"""
    stage_instances: Optional[list["Stage_Instance"]] = UNSET
    """Stage instances in the guild"""
    guild_scheduled_events: Optional[list["Guild_Scheduled_Event"]] = UNSET
    """Scheduled events in the guild"""
    max_presences: Optional[Nullable[int]] = UNSET
    """the maximum number of presences for the guild"""
    max_members: Optional[int] = UNSET
    """the maximum number of members for the guild"""
    vanity_url_code: Nullable[str] = UNSET
    """the vanity url code for the guild"""
    description: Nullable[str] = UNSET
    """the description of a guild"""
    banner: Nullable[str] = UNSET
    """Banner_Hash"""
    premium_tier: "Premium_Tier" = UNSET
    """Premium_Tier"""
    premium_subscription_count: Optional[int] = UNSET
    """the number of boosts this guild currently has"""
    preferred_locale: "Locales" = UNSET
    """the preferred locale of a Community guild; used in server discovery and notices from Discord; defaults to 'en-US'"""
    public_updates_channel_id: Nullable[Snowflake] = UNSET
    """the id of the channel where admins and moderators of Community guilds receive notices from Discord"""
    max_video_channel_users: Optional[int] = UNSET
    """the maximum amount of users in a video channel"""
    max_stage_video_channel_users: Optional[int] = UNSET
    """the maximum amount of users in a stage video channel"""
    approximate_member_count: Optional[int] = UNSET
    """approximate number of members in this guild, returned from the GET /guilds/<id> and /users/@me/guilds endpoints when with_counts is true"""
    approximate_presence_count: Optional[int] = UNSET
    """approximate number of non-offline members in this guild, returned from the GET /guilds/<id> and /users/@me/guilds  endpoints when with_counts is true"""
    welcome_screen: Optional["Welcome_Screen"] = UNSET
    """Invite"""
    nsfw_level: "Guild_NSFW_Level" = UNSET
    """Guild_NSFW_Level"""
    stickers: Optional["Sticker"] = UNSET
    """custom guild stickers"""
    premium_progress_bar_enabled: bool = UNSET
    """whether the guild has the boost progress bar enabled"""
    safety_alerts_channel_id: Nullable[Snowflake] = UNSET
    """the id of the channel where admins and moderators of Community guilds receive safety alerts from Discord"""


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
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    """Hide member join sticker reply buttons"""
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    """Suppress role subscription purchase and renewal notifications"""
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5
    """Hide role subscription sticker reply buttons"""


class Guild_Features(Enum):
    ANIMATED_BANNER = "guild has access to set an animated guild banner image"
    ANIMATED_ICON = "guild has access to set an animated guild icon"
    APPLICATION_COMMAND_PERMISSIONS_V2 = "Old_Permissions_Configuration_Behavior"
    AUTO_MODERATION = "guild has set up auto moderation rules"
    BANNER = "guild has access to set a guild banner image"
    COMMUNITY = "guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates"
    CREATOR_MONETIZABLE_PROVISIONAL = "guild has enabled monetization"
    CREATOR_STORE_PAGE = "guild has enabled the role subscription promo page"
    DEVELOPER_SUPPORT_SERVER = "guild has been set as a support server on the App Directory"
    DISCOVERABLE = "guild is able to be discovered in the directory"
    FEATURABLE = "guild is able to be featured in the directory"
    INVITES_DISABLED = "guild has paused invites, preventing new users from joining"
    INVITE_SPLASH = "guild has access to set an invite splash background"
    MEMBER_VERIFICATION_GATE_ENABLED = "Membership_Screening"
    MORE_STICKERS = "guild has increased custom sticker slots"
    NEWS = "guild has access to create announcement channels"
    PARTNERED = "guild is partnered"
    PREVIEW_ENABLED = "guild can be previewed before joining via Membership Screening"
    RAID_ALERTS_DISABLED = "guild has disabled alerts for join raids in the configured safety alerts channel"
    ROLE_ICONS = "guild is able to set role icons"
    ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE = "guild has role subscriptions that can be purchased"
    ROLE_SUBSCRIPTIONS_ENABLED = "guild has enabled role subscriptions"
    TICKETED_EVENTS_ENABLED = "guild has enabled ticketed events"
    VANITY_URL = "guild has access to set a vanity URL"
    VERIFIED = "guild is verified"
    VIP_REGIONS = "guild has access to set 384kbps bitrate in voice"
    WELCOME_SCREEN_ENABLED = "guild has enabled the welcome screen"


class Mutable_Guild_Features(Enum):
    """
    * Server also must be passing all discovery requirements.
    """

    COMMUNITY = "Enables Community Features in the guild"
    DISCOVERABLE = "Enables discovery in the guild, making it publicly listed"
    INVITES_DISABLED = "Pauses all invites/access to the server"
    RAID_ALERTS_DISABLED = "Disables alerts for join raids"


class Guild_Preview(DiscordObject):
    id: Snowflake = UNSET
    """guild id"""
    name: str = UNSET
    """guild name"""
    icon: Nullable[str] = UNSET
    """Icon_Hash"""
    splash: Nullable[str] = UNSET
    """Splash_Hash"""
    discovery_splash: Nullable[str] = UNSET
    """Discovery_Splash_Hash"""
    emojis: list["Emoji"] = UNSET
    """custom guild emojis"""
    features: list["Guild_Features"] = UNSET
    """enabled guild features"""
    approximate_member_count: int = UNSET
    """approximate number of members in this guild"""
    approximate_presence_count: int = UNSET
    """approximate number of online members in this guild"""
    description: Nullable[str] = UNSET
    """the description for the guild"""
    stickers: list["Sticker"] = UNSET
    """custom guild stickers"""


class Guild_Widget_Settings(DiscordObject):
    enabled: bool = UNSET
    """whether the widget is enabled"""
    channel_id: Nullable[Snowflake] = UNSET
    """the widget channel id"""


class Guild_Widget(DiscordObject):
    """
    > warn
    > The fields id, discriminator and avatar are anonymized to prevent abuse.
    """

    id: Snowflake = UNSET
    """guild id"""
    name: str = UNSET
    """guild name"""
    instant_invite: Nullable[str] = UNSET
    """instant invite for the guilds specified widget invite channel"""
    channels: list["Channel"] = UNSET
    """voice and stage channels which are accessible by @everyone"""
    members: list["User"] = UNSET
    """special widget user s that includes users presence"""
    presence_count: int = UNSET
    """number of online members in this guild"""


class Guild_Member(DiscordObject):
    """
    > info
    > The field user won't be included in the member object attached to MESSAGE_CREATE and MESSAGE_UPDATE gateway events.
    > info
    > In GUILD_ events, pending will always be included as true or false.
    In non GUILD_ events which can only be triggered by non-pending users, pending will not be included.
    """

    user: Optional["User"] = UNSET
    """the user this guild member represents"""
    nick: Optional[Nullable[str]] = UNSET
    """this user's guild nickname"""
    avatar: Optional[Nullable[str]] = UNSET
    """Guild_Avatar_Hash"""
    roles: list[Snowflake] = UNSET
    """Role"""
    joined_at: datetime = UNSET
    """when the user joined the guild"""
    premium_since: Optional[Nullable[datetime]] = UNSET
    """Boosting"""
    deaf: bool = UNSET
    """whether the user is deafened in voice channels"""
    mute: bool = UNSET
    """whether the user is muted in voice channels"""
    flags: "Guild_Member_Flags" = UNSET
    """Guild_Member_Flags"""
    pending: Optional[bool] = UNSET
    """Membership_Screening"""
    permissions: Optional[str] = UNSET
    """total permissions of the member in the channel, including overwrites, returned when in the interaction"""
    communication_disabled_until: Optional[Nullable[datetime]] = UNSET
    """Timeout"""
    avatar_decoration_data: Optional[Nullable["Avatar_Decoration_Data"]] = UNSET
    """data for the member's guild avatar decoration"""


class Guild_Member_Flags(Flag):
    """
    > info
    > BYPASSES_VERIFICATION allows a member who does not meet verification requirements to participate in a server.
    """

    DID_REJOIN = 1 << 0
    """Member has left and rejoined the guild"""
    COMPLETED_ONBOARDING = 1 << 1
    """Member has completed onboarding"""
    BYPASSES_VERIFICATION = 1 << 2
    """Member is exempt from guild verification requirements"""
    STARTED_ONBOARDING = 1 << 3
    """Member has started onboarding"""


class Integration(DiscordObject):
    """
    * These fields are not provided for discord bot integrations.
    > warn
    > Some older integrations may not have an attached user.
    """

    id: Snowflake = UNSET
    """integration id"""
    name: str = UNSET
    """integration name"""
    type: str = UNSET
    """integration type (twitch, youtube, discord, or guild_subscription)"""
    enabled: bool = UNSET
    """is this integration enabled"""
    syncing: bool = UNSET
    """is this integration syncing"""
    role_id: Snowflake = UNSET
    """id that this integration uses for 'subscribers'"""
    enable_emoticons: bool = UNSET
    """whether emoticons should be synced for this integration"""
    expire_behavior: "Integration_Expire_Behaviors" = UNSET
    """the behavior of expiring subscribers"""
    expire_grace_period: int = UNSET
    """the grace period"""
    user: Optional["User"] = UNSET
    """user for this integration"""
    account: "Integration_Account" = UNSET
    """integration account information"""
    synced_at: datetime = UNSET
    """when this integration was last synced"""
    subscriber_count: int = UNSET
    """how many subscribers this integration has"""
    revoked: bool = UNSET
    """has this integration been revoked"""
    application: Optional["Application"] = UNSET
    """The bot/OAuth2 application for discord integrations"""
    scopes: Optional["OAuth2_Scopes"] = UNSET
    """the scopes the application has been authorized for"""


class Integration_Types(Enum):
    TWITCH = "twitch"
    YOUTUBE = "youtube"
    DISCORD = "discord"
    GUILD_SUBSCRIPTION = "guild_subscription"


class Integration_Expire_Behaviors(Enum):
    REMOVE_ROLE = 0
    KICK = 1


class Integration_Account(DiscordObject):
    id: str = UNSET
    """id of the account"""
    name: str = UNSET
    """name of the account"""


class Integration_Application(DiscordObject):
    id: Snowflake = UNSET
    """the id of the app"""
    name: str = UNSET
    """the name of the app"""
    icon: Nullable[str] = UNSET
    """Icon_Hash"""
    description: str = UNSET
    """the description of the app"""
    bot: Optional["User"] = UNSET
    """the bot associated with this application"""


class Ban(DiscordObject):
    reason: Nullable[str] = UNSET
    """the reason for the ban"""
    user: "User" = UNSET
    """the banned user"""


class Welcome_Screen(DiscordObject):
    description: Nullable[str] = UNSET
    """the server description shown in the welcome screen"""
    welcome_channels: list["Welcome_Screen_Channel"] = UNSET
    """the channels shown in the welcome screen, up to 5"""


class Welcome_Screen_Channel(DiscordObject):
    channel_id: Snowflake = UNSET
    """the channel's id"""
    description: str = UNSET
    """the description shown for the channel"""
    emoji_id: Nullable[Snowflake] = UNSET
    """Emoji_Id"""
    emoji_name: Nullable[str] = UNSET
    """the emoji name if custom, the unicode character if standard,"""


class Guild_Onboarding(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild this onboarding is part of"""
    prompts: list["Onboarding_Prompt"] = UNSET
    """Prompts shown during onboarding and in customize community"""
    default_channel_ids: list["list[Snowflake]"] = UNSET
    """Channel IDs that members get opted into automatically"""
    enabled: bool = UNSET
    """Whether onboarding is enabled in the guild"""
    mode: "Onboarding_Mode" = UNSET
    """Current mode of onboarding"""


class Onboarding_Prompt(DiscordObject):
    id: Snowflake = UNSET
    """ID of the prompt"""
    type: "Prompt_Types" = UNSET
    """Type of prompt"""
    options: list["Prompt_Option"] = UNSET
    """Options available within the prompt"""
    title: str = UNSET
    """Title of the prompt"""
    single_select: bool = UNSET
    """Indicates whether users are limited to selecting one option for the prompt"""
    required: bool = UNSET
    """Indicates whether the prompt is required before a user completes the onboarding flow"""
    in_onboarding: bool = UNSET
    """Indicates whether the prompt is present in the onboarding flow. If false, the prompt will only appear in the Channels & Roles tab"""


class Prompt_Option(DiscordObject):
    """
    > warn
    > When creating or updating a prompt option, the emoji_id, emoji_name, and emoji_animated fields must be used instead of the emoji object.
    """

    id: Snowflake = UNSET
    """ID of the prompt option"""
    channel_ids: list["list[Snowflake]"] = UNSET
    """IDs for channels a member is added to when the option is selected"""
    role_ids: list["list[Snowflake]"] = UNSET
    """IDs for roles assigned to a member when the option is selected"""
    emoji: Optional["Emoji"] = UNSET
    """Emoji of the option"""
    emoji_id: Optional[Snowflake] = UNSET
    """Emoji ID of the option"""
    emoji_name: Optional[str] = UNSET
    """Emoji name of the option"""
    emoji_animated: Optional[bool] = UNSET
    """Whether the emoji is animated"""
    title: str = UNSET
    """Title of the option"""
    description: Nullable[str] = UNSET
    """Description of the option"""


class Onboarding_Mode(Enum):
    """
    Defines the criteria used to satisfy Onboarding constraints that are required for enabling.
    """

    ONBOARDING_DEFAULT = 0
    """Counts only Default Channels towards constraints"""
    ONBOARDING_ADVANCED = 1
    """Counts Default Channels and Questions towards constraints"""


class Prompt_Types(Enum):
    MULTIPLE_CHOICE = 0
    DROPDOWN = 1


class Guild_Scheduled_Event(DiscordObject):
    """
    * creator_id will be null and creator will not be included for events created before October 25th, 2021, when the concept of creator_id was introduced and tracked.
    ** See [field requirements by entity type](https:#/discord.com/developers/docs/resources/guild_scheduled_event#guild-scheduled-event-object-field-requirements-by-entity-type) to understand the relationship between entity_type and the following fields: channel_id, entity_metadata, and scheduled_end_time.
    """

    id: Snowflake = UNSET
    """the id of the scheduled event"""
    guild_id: Snowflake = UNSET
    """the guild id which the scheduled event belongs to"""
    channel_id: Nullable[Snowflake] = UNSET
    """Scheduled_Entity_Type"""
    creator_id: Nullable[Snowflake] = UNSET
    """the id of the user that created the scheduled event"""
    name: str = UNSET
    """the name of the scheduled event"""
    description: Optional[Nullable[str]] = UNSET
    """the description of the scheduled event"""
    scheduled_start_time: datetime = UNSET
    """the time the scheduled event will start"""
    scheduled_end_time: Nullable[datetime] = UNSET
    """the time the scheduled event will end, required if entity_type is EXTERNAL"""
    privacy_level: "Privacy_Level" = UNSET
    """the privacy level of the scheduled event"""
    status: list["Guild_Scheduled_Event_Status"] = UNSET
    """the status of the scheduled event"""
    entity_type: "Guild_Scheduled_Event_Entity_Types" = UNSET
    """the type of the scheduled event"""
    entity_id: Nullable[Snowflake] = UNSET
    """the id of an entity associated with a guild scheduled event"""
    entity_metadata: Nullable["Guild_Scheduled_Event_Entity_Metadata"] = UNSET
    """additional metadata for the guild scheduled event"""
    creator: Optional["User"] = UNSET
    """the user that created the scheduled event"""
    user_count: Optional[int] = UNSET
    """the number of users subscribed to the scheduled event"""
    image: Optional[Nullable[str]] = UNSET
    """Cover_Image_Hash"""


class Guild_Scheduled_Event_Privacy_Level(Enum):
    GUILD_ONLY = 2
    """the scheduled event is only accessible to guild members"""


class Guild_Scheduled_Event_Entity_Types(Enum):
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3


class Guild_Scheduled_Event_Status(Enum):
    """
    * Once status is set to COMPLETED or CANCELED, the status can no longer be updated.
    """

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4


class Guild_Scheduled_Event_Entity_Metadata(DiscordObject):
    """
    * [required](https:#/discord.com/developers/docs/resources/guild_scheduled_event#guild-scheduled-event-object-guild-scheduled-event-entity-metadata) for events with 'entity_type': EXTERNAL.
    """

    location: str = UNSET
    """location of the event"""


class Guild_Scheduled_Event_User(DiscordObject):
    guild_scheduled_event_id: Snowflake = UNSET
    """the scheduled event id which the user subscribed to"""
    user: "User" = UNSET
    """user which subscribed to an event"""
    member: Optional["Guild_Member"] = UNSET
    """guild member data for this user for the guild which this event belongs to, if any"""


class Guild_Template(DiscordObject):
    code: str = UNSET
    """the template code"""
    name: str = UNSET
    """template name"""
    description: Nullable[str] = UNSET
    """the description for the template"""
    usage_count: int = UNSET
    """number of times this template has been used"""
    creator_id: Snowflake = UNSET
    """the ID of the user who created the template"""
    creator: "User" = UNSET
    """the user who created the template"""
    created_at: datetime = UNSET
    """when this template was created"""
    updated_at: datetime = UNSET
    """when this template was last synced to the source guild"""
    source_guild_id: Snowflake = UNSET
    """the ID of the guild this template is based on"""
    serialized_source_guild: "Guild" = UNSET
    """the guild snapshot this template contains"""
    is_dirty: Nullable[bool] = UNSET
    """whether the template has unsynced changes"""


class Invite_Types(Enum):
    GUILD = 0
    GROUP_DM = 1
    FRIEND = 2


class Invite(DiscordObject):
    type: "Invite_Types" = Invite_Types.GUILD
    """Type_Of_Invite"""
    code: str = UNSET
    """the invite code"""
    guild: Optional["Guild"] = UNSET
    """the guild this invite is for"""
    channel: Nullable["Channel"] = UNSET
    """the channel this invite is for"""
    inviter: Optional["User"] = UNSET
    """the user who created the invite"""
    target_type: Optional["Invite_Target_Types"] = UNSET
    """Type_Of_Target"""
    target_user: Optional["User"] = UNSET
    """the user whose stream to display for this voice channel stream invite"""
    target_application: Optional["Application"] = UNSET
    """the embedded application to open for this voice channel embedded application invite"""
    approximate_presence_count: Optional[int] = UNSET
    """approximate count of online members, returned from the GET /invites/<code> endpoint when with_counts is true"""
    approximate_member_count: Optional[int] = UNSET
    """approximate count of total members, returned from the GET /invites/<code> endpoint when with_counts is true"""
    expires_at: Optional[Nullable[datetime]] = UNSET
    """the expiration date of this invite, returned from the GET /invites/<code> endpoint when with_expiration is true"""
    stage_instance: Optional["Invite_Stage_Instance"] = UNSET
    """Public_Stage_Instance"""
    guild_scheduled_event: Optional["Guild_Scheduled_Event"] = UNSET
    """guild scheduled event data, only included if guild_scheduled_event_id contains a valid guild scheduled event id"""


class Invite_Target_Types(Enum):
    STREAM = 1
    EMBEDDED_APPLICATION = 2


class Invite_Metadata(DiscordObject):
    uses: int = UNSET
    """number of times this invite has been used"""
    max_uses: int = UNSET
    """max number of times this invite can be used"""
    max_age: Duration = UNSET
    """duration"""
    temporary: bool = UNSET
    """whether this invite only grants temporary membership"""
    created_at: datetime = UNSET
    """when this invite was created"""


class Invite_Stage_Instance(DiscordObject):
    members: list["Guild_Member"] = UNSET
    """the members speaking in the Stage"""
    participant_count: int = UNSET
    """the number of users in the Stage"""
    speaker_count: int = UNSET
    """the number of users speaking in the Stage"""
    topic: str = UNSET
    """the topic of the Stage instance"""


class Poll(DiscordObject):
    """
    expiry is marked as nullable to support non-expiring polls in the future, but all polls have an expiry currently.
    """

    question: "Poll_Media" = UNSET
    """The question of the poll. Only text is supported"""
    answers: list["Poll_Answer"] = UNSET
    """Each of the answers available in the poll"""
    expiry: Nullable[datetime] = UNSET
    """The time when the poll ends"""
    allow_multiselect: bool = UNSET
    """Whether a user can select multiple answers"""
    layout_type: "Layout_Type" = UNSET
    """Layout_Type"""
    results: Optional["Poll_Results"] = UNSET
    """The results of the poll"""


class Poll_Create_Request(DiscordObject):
    question: "Poll_Media" = UNSET
    """The question of the poll. Only text is supported"""
    answers: list["Poll_Answer"] = UNSET
    """Each of the answers available in the poll, up to 10"""
    duration: int = UNSET
    """Number of hours the poll should be open for, up to 7 days"""
    allow_multiselect: bool = UNSET
    """Whether a user can select multiple answers"""
    layout_type: Optional["Layout_Type"] = UNSET
    """Layout_Type"""


class Layout_Type(Enum):
    """
    We might have different layouts for polls in the future.
    """

    DEFAULT = 1
    """The, uhm, default layout type"""


class Poll_Media(DiscordObject):
    """
    text should always be non-null for both questions and answers, but please do not depend on that in the future.
    The maximum length of text is 300 for the question, and 55 for any answer.
    When creating a poll answer with an emoji, one only needs to send either the id (custom emoji) or name (default emoji) as the only field.
    """

    text: Optional[str] = UNSET
    """The text of the field"""
    emoji: Optional["Emoji"] = UNSET
    """The emoji of the field"""


class Poll_Answer(DiscordObject):
    """
    * Only sent as part of responses from Discord's API/Gateway.
    """

    answer_id: int = UNSET
    """The ID of the answer"""
    poll_media: "Poll_Media" = UNSET
    """The data of the answer"""


class Poll_Results(DiscordObject):
    is_finalized: bool = UNSET
    """Whether the votes have been precisely counted"""
    answer_counts: list["Poll_Answer_Count"] = UNSET
    """The counts for each answer"""


class Poll_Answer_Count(DiscordObject):
    id: int = UNSET
    """The answer_id"""
    count: int = UNSET
    """The number of votes for this answer"""
    me_voted: bool = UNSET
    """Whether the current user voted for this answer"""


class Stage_Instance(DiscordObject):
    id: Snowflake = UNSET
    """The id of this Stage instance"""
    guild_id: Snowflake = UNSET
    """The guild id of the associated Stage channel"""
    channel_id: Snowflake = UNSET
    """The id of the associated Stage channel"""
    topic: str = UNSET
    """The topic of the Stage instance"""
    privacy_level: "Privacy_Level" = UNSET
    """Privacy_Level"""
    discoverable_disabled: bool = UNSET
    """Whether"""
    guild_scheduled_event_id: Nullable[Snowflake] = UNSET
    """The id of the scheduled event for this Stage instance"""


class Privacy_Level(Enum):
    PUBLIC = 1
    """The Stage instance is visible publicly"""
    GUILD_ONLY = 2
    """The Stage instance is visible to only guild members"""


class User(DiscordObject):
    id: Snowflake = UNSET
    """the user's id"""
    username: str = UNSET
    """the user's username, not unique across the platform"""
    discriminator: str = UNSET
    """the user's Discord-tag"""
    global_name: Nullable[str] = UNSET
    """the user's display name, if it is set. For bots, this is the application name"""
    avatar: Nullable[str] = UNSET
    """Avatar_Hash"""
    bot: Optional[bool] = UNSET
    """whether the user belongs to an OAuth2 application"""
    system: Optional[bool] = UNSET
    """whether the user is an Official Discord System user"""
    mfa_enabled: Optional[bool] = UNSET
    """whether the user has two factor enabled on their account"""
    banner: Optional[Nullable[str]] = UNSET
    """Banner_Hash"""
    accent_color: Optional[Nullable[int]] = UNSET
    """the user's banner color encoded as an integer representation of hexadecimal color code"""
    locale: Optional["Locales"] = UNSET
    """Language_Option"""
    verified: Optional[bool] = UNSET
    """whether the email on this account has been verified"""
    email: Optional[Nullable[str]] = UNSET
    """the user's email"""
    flags: Optional["User_Flags"] = UNSET
    """Flags"""
    premium_type: Optional["Premium_Types"] = UNSET
    """Type_Of_Nitro_Subscription"""
    public_flags: Optional["User_Flags"] = UNSET
    """Flags"""
    avatar_decoration_data: Optional[Nullable["Avatar_Decoration_Data"]] = UNSET
    """data for the user's avatar decoration"""


class User_Flags(Flag):
    STAFF = 1 << 0
    """Discord Employee"""
    PARTNER = 1 << 1
    """Partnered Server Owner"""
    HYPESQUAD = 1 << 2
    """HypeSquad Events Member"""
    BUG_HUNTER_LEVEL_1 = 1 << 3
    """Bug Hunter Level 1"""
    HYPESQUAD_ONLINE_HOUSE_1 = 1 << 6
    """House Bravery Member"""
    HYPESQUAD_ONLINE_HOUSE_2 = 1 << 7
    """House Brilliance Member"""
    HYPESQUAD_ONLINE_HOUSE_3 = 1 << 8
    """House Balance Member"""
    PREMIUM_EARLY_SUPPORTER = 1 << 9
    """Early Nitro Supporter"""
    TEAM_PSEUDO_USER = 1 << 10
    """Team"""
    SYSTEM = 1 << 12
    BUG_HUNTER_LEVEL_2 = 1 << 14
    """Bug Hunter Level 2"""
    VERIFIED_BOT = 1 << 16
    """Verified Bot"""
    VERIFIED_DEVELOPER = 1 << 17
    """Early Verified Bot Developer"""
    CERTIFIED_MODERATOR = 1 << 18
    """Moderator Programs Alumni"""
    BOT_HTTP_INTERACTIONS = 1 << 19
    """HTTP_Interactions"""
    ACTIVE_DEVELOPER = 1 << 22
    """Active_Developer"""


class Premium_Types(Enum):
    """
    Premium types denote the level of premium a user has.
    Visit the [Nitro](https:##discord.com/nitro) page to learn more about the premium plans we currently offer.
    """

    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2
    NITRO_BASIC = 3


class Avatar_Decoration_Data(DiscordObject):
    asset: str = UNSET
    """Avatar_Decoration_Hash"""
    sku_id: Snowflake = UNSET
    """id of the avatar decoration's SKU"""


class Connection(DiscordObject):
    id: str = UNSET
    """id of the connection account"""
    name: str = UNSET
    """the username of the connection account"""
    type: "Services" = UNSET
    """the service of the connection"""
    revoked: Optional[bool] = UNSET
    """whether the connection is revoked"""
    integrations: Optional[list[Integration]] = UNSET
    """Server_Integrations"""
    verified: bool = UNSET
    """whether the connection is verified"""
    friend_sync: bool = UNSET
    """whether friend sync is enabled for this connection"""
    show_activity: bool = UNSET
    """whether activities related to this connection will be shown in presence updates"""
    two_way_link: bool = UNSET
    """whether this connection has a corresponding third party OAuth2 token"""
    visibility: "Visibility_Types" = UNSET
    """Visibility"""


class Services(DiscordObject):
    """
    * Service can no longer be added by users.
    """

    battle_net = "battlenet"
    bungie_net = "bungie"
    domain = "domain"
    ebay = "ebay"
    epic_games = "epicgames"
    facebook = "facebook"
    github = "github"
    instagram = "instagram"
    league_of_legends = "leagueoflegends"
    paypal = "paypal"
    playstation_network = "playstation"
    reddit = "reddit"
    riot_games = "riotgames"
    spotify = "spotify"
    skype = "skype"
    steam = "steam"
    tiktok = "tiktok"
    twitch = "twitch"
    x = "twitter"
    xbox = "xbox"
    youtube = "youtube"


class Visibility_Types(Enum):
    NONE = 0
    """invisible to everyone except the user themselves"""
    EVERYONE = 1
    """visible to everyone"""


class Application_Role_Connection(DiscordObject):
    platform_name: Nullable[LongNameConstraint] = UNSET
    """the vanity name of the platform a bot has connected"""
    platform_username: Nullable[DescriptionConstraint] = UNSET
    """the username on the platform a bot has connected"""
    metadata: Application_Role_Connection_Metadata = UNSET
    """Application_Role_Connection_Metadata"""


class Voice_State(DiscordObject):
    guild_id: Optional[Snowflake] = UNSET
    """the guild id this voice state is for"""
    channel_id: Nullable[Snowflake] = UNSET
    """the channel id this user is connected to"""
    user_id: Snowflake = UNSET
    """the user id this voice state is for"""
    member: Optional["Guild_Member"] = UNSET
    """the guild member this voice state is for"""
    session_id: str = UNSET
    """the session id for this voice state"""
    deaf: bool = UNSET
    """whether this user is deafened by the server"""
    mute: bool = UNSET
    """whether this user is muted by the server"""
    self_deaf: bool = UNSET
    """whether this user is locally deafened"""
    self_mute: bool = UNSET
    """whether this user is locally muted"""
    self_stream: Optional[bool] = UNSET
    """whether this user is streaming using 'Go Live'"""
    self_video: bool = UNSET
    """whether this user's camera is enabled"""
    suppress: bool = UNSET
    """whether this user's permission to speak is denied"""
    request_to_speak_timestamp: Nullable[datetime] = UNSET
    """the time at which the user requested to speak"""


class Voice_Region(DiscordObject):
    id: str = UNSET
    """unique ID for the region"""
    name: str = UNSET
    """name of the region"""
    optimal: bool = UNSET
    """true for a single server that is closest to the current user's client"""
    deprecated: bool = UNSET
    """whether this is a deprecated voice region"""
    custom: bool = UNSET
    """whether this is a custom voice region"""


class Webhook(DiscordObject):
    """
    * These fields will be absent if the webhook creator has since lost access to the guild where the followed channel resides.
    """

    id: Snowflake = UNSET
    """the id of the webhook"""
    type: "Webhook_Types" = UNSET
    """Type"""
    guild_id: Optional[Nullable[Snowflake]] = UNSET
    """the guild id this webhook is for, if any"""
    channel_id: Nullable[Snowflake] = UNSET
    """the channel id this webhook is for, if any"""
    user: Optional["User"] = UNSET
    """the user this webhook was created by"""
    name: Nullable[str] = UNSET
    """the default name of the webhook"""
    avatar: Nullable[str] = UNSET
    """Hash"""
    token: Optional[str] = UNSET
    """the secure token of the webhook"""
    application_id: Nullable[Snowflake] = UNSET
    """the bot/OAuth2 application that created this webhook"""
    source_guild: "Guild" = UNSET
    """the guild of the channel that this webhook is following"""
    source_channel: "Channel" = UNSET
    """the channel that this webhook is following"""
    url: Optional[str] = UNSET
    """Webhooks"""


class Webhook_Types(Enum):
    INCOMING = 1
    """Incoming Webhooks can post messages to channels with a generated token"""
    CHANNEL_FOLLOWER = 2
    """Channel Follower Webhooks are internal webhooks used with Channel Following to post new messages into channels"""
    APPLICATION = 3
    """Application webhooks are webhooks used with Interactions"""


class Gateway_Versions(Enum):
    _4: Nullable[None] = "recommended"
    _3: Nullable[None] = "available"
    _2: Nullable[None] = "available"
    _1: Nullable[None] = "default"


class Gateway_Payload(DiscordObject):
    """
    Gateway event payloads have a common structure, but the contents of the associated data (d) varies between the different events.
    * `s` and `t` are `null` when `op` is not `0` ([Gateway Dispatch opcode](https://discord.com/developers/docs/topics/opcodes_and_status_codes#gateway-gateway-opcodes)).
    """

    op: "Gateway_Opcodes" = UNSET
    """Gateway_Opcode"""
    d: Nullable[dict[Any, Any]] = UNSET
    """Event data"""
    s: Nullable[int] = UNSET
    """Resuming_Sessions"""
    t: Nullable[str] = UNSET
    """Event name"""


class Gateway_URL_Query_String_Params(DiscordObject):
    v: int = UNSET
    """Gateway Version to use"""
    encoding: str = UNSET
    """The encoding of received gateway packets"""
    compress: Optional[str] = UNSET
    """Transport_Compression"""


class Identify(DiscordObject):
    token: str = UNSET
    """Authentication token"""
    properties: "Identify_Connection_Properties" = UNSET
    """Connection_Properties"""
    compress: Optional[bool] = False
    """Whether this connection supports compression of packets"""
    large_threshold: Optional[LargeThresholdConstraint] = 50
    """Value between 50 and 250, total number of members where the gateway will stop sending offline members in the guild member list"""
    shard: Optional[list[int]] = UNSET
    """Guild_Sharding"""
    presence: Optional["Presence_Update"] = UNSET
    """Presence structure for initial presence information"""
    intents: "Intents" = UNSET
    """Gateway_Intents"""


class Identify_Connection_Properties(DiscordObject):
    """
    > warn
    > These fields originally were $ prefixed (i.e: $browser) but [this syntax is deprecated](https:#/discord.com/developers/docs/change/log#updated-connection-property-field-names).
    While they currently still work, it is recommended to move to non-prefixed fields.
    """

    os: str = UNSET
    """Your operating system"""
    browser: str = UNSET
    """Your library name"""
    device: str = UNSET
    """Your library name"""


class Send_Events(Enum):
    """
    Send events are Gateway events encapsulated in an [event payload](https://discord.com/developers/docs/topics/gateway_events#payload_structure), and are sent by an app to Discord through a Gateway connection.
    Identify
    Details about identifying is in the [Gateway documentation](https:#/discord.com/developers/docs/topics/gateway#identifying).Used to trigger the initial handshake with the gateway.
    Example Identify
    json.
    """

    IDENTIFY = "Triggers the initial handshake with the gateway"
    RESUME = "Resumes a dropped gateway connection"
    HEARTBEAT = "Maintains an active gateway connection"
    REQUEST_GUILD_MEMBERS = "Requests members for a guild"
    UPDATE_VOICE_STATE = "Joins, moves,"
    UPDATE_PRESENCE = "Updates an apps presence"


class Resume(DiscordObject):
    token: str = UNSET
    """Session token"""
    session_id: str = UNSET
    """Session ID"""
    seq: int = 0
    """Last sequence number received"""


class Request_Guild_Members(DiscordObject):
    """
    > info
    > Nonce can only be up to 32 bytes.
    If you send an invalid nonce it will be ignored and the reply member_chunk(s) will not have a nonce set.
    """

    guild_id: Snowflake = UNSET
    """ID of the guild to get members for"""
    query: Optional[str] = UNSET
    """string that username starts with,"""
    limit: int = UNSET
    """maximum number of members to send matching the `query`; a limit of `0` can be used with an empty string `query` to return all members"""
    presences: Optional[bool] = UNSET
    """used to specify if we want the presences of the matched members"""
    user_ids: Optional[list[Snowflake]] = UNSET
    """used to specify which users you wish to fetch"""
    nonce: Optional[str] = UNSET
    """Guild_Members_Chunk"""


class Gateway_Voice_State_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    channel_id: Nullable[Snowflake] = UNSET
    """ID of the voice channel client wants to join"""
    self_mute: bool = UNSET
    """Whether the client is muted"""
    self_deaf: bool = UNSET
    """Whether the client deafened"""


class Gateway_Presence_Update(DiscordObject):
    since: Nullable[UnixTimestamp] = UNSET
    """Unix time"""
    activities: list["Activity"] = UNSET
    """User's activities"""
    status: str = UNSET
    """Status"""
    afk: bool = UNSET
    """Whether"""


class Status_Types(Enum):
    ONLINE = "online"
    DND = "dnd"
    IDLE = "idle"
    INVISIBLE = "invisible"
    OFFLINE = "offline"


class Hello(DiscordObject):
    heartbeat_interval: int = UNSET
    """Interval"""


class Ready(DiscordObject):
    v: int = UNSET
    """API_Version"""
    user: "User" = UNSET
    """Information about the user including email"""
    guilds: list["Guild"] = UNSET
    """Guilds the user is in"""
    session_id: str = UNSET
    """Used for resuming connections"""
    resume_gateway_url: str = UNSET
    """Gateway URL for resuming connections"""
    shard: Optional[tuple[int, int]] = UNSET
    """Shard_Information"""
    application: "Application" = UNSET
    """Contains `id` and `flags`"""


class Thread_List_Sync(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    channel_ids: Optional[list[Snowflake]] = UNSET
    """Parent channel IDs whose threads are being synced. If omitted, then threads were synced for the entire guild. This array may contain channel_ids that have no active threads as well, so you know to clear that data"""
    threads: list["Channel"] = UNSET
    """All active threads in the given channels that the current user can access"""
    members: list["Thread_Member"] = UNSET
    """All thread member s from the synced threads for the current user, indicating which threads the current user has been added to"""


class Thread_Member_Update_Event(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Thread_Members_Update(DiscordObject):
    """
    * In this gateway event, the thread member objects will also include the [guild member](https:#/discord.com/developers/docs/resources/guild#guild-member-object) and nullable [presence](https:#/discord.com/developers/docs/topics/gateway_events#presence) objects for each added thread member.
    """

    id: Snowflake = UNSET
    """ID of the thread"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    member_count: int = UNSET
    """Approximate number of members in the thread, capped at 50"""
    added_members: Optional[list["Thread_Member"]] = UNSET
    """Users who were added to the thread"""
    removed_member_ids: Optional[list[Snowflake]] = UNSET
    """ID of the users who were removed from the thread"""


class Channel_Pins_Update(DiscordObject):
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    last_pin_timestamp: Optional[Nullable[datetime]] = UNSET
    """Time at which the most recent pinned message was pinned"""


class Entitlement(DiscordObject):
    id: Snowflake = UNSET
    """ID of the entitlement"""
    sku_id: Snowflake = UNSET
    """ID of the SKU"""
    application_id: Snowflake = UNSET
    """ID of the parent application"""
    user_id: Optional[Snowflake] = UNSET
    """ID of the user that is granted access to the entitlement's sku"""
    type: "Entitlement_Types" = UNSET
    """Type_Of_Entitlement"""
    deleted: bool = UNSET
    """Entitlement was deleted"""
    starts_at: Optional[datetime] = UNSET
    """Start date at which the entitlement is valid. Not present when using test entitlements"""
    ends_at: Optional[datetime] = UNSET
    """Date at which the entitlement is no longer valid. Not present when using test entitlements"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild that is granted access to the entitlement's sku"""
    consumed: Optional[bool] = UNSET
    """For consumable items, whether"""


class Entitlement_Types(Enum):
    PURCHASE = 1
    """Entitlement was purchased by user"""
    PREMIUM_SUBSCRIPTION = 2
    """Entitlement for Discord Nitro subscription"""
    DEVELOPER_GIFT = 3
    """Entitlement was gifted by developer"""
    TEST_MODE_PURCHASE = 4
    """Entitlement was purchased by a dev in application test mode"""
    FREE_PURCHASE = 5
    """Entitlement was granted when the SKU was free"""
    USER_GIFT = 6
    """Entitlement was gifted by another user"""
    PREMIUM_PURCHASE = 7
    """Entitlement was claimed by user for free as a Nitro Subscriber"""
    APPLICATION_SUBSCRIPTION = 8
    """Entitlement was purchased as an app subscription"""


class Guild_Create(DiscordObject):
    """
    > warn
    > If your bot does not have the GUILD_PRESENCES [Gateway Intent](https:#/discord.com/developers/docs/topics/gateway#gateway-intents), or if the guild has over 75k members, members and presences returned in this event will only contain your bot and users in voice channels.
    """

    joined_at: datetime = UNSET
    """When this guild was joined at"""
    large: bool = UNSET
    """true if this is considered a large guild"""
    unavailable: Optional[bool] = UNSET
    """true if this guild is unavailable due to an outage"""
    member_count: int = UNSET
    """Total number of members in this guild"""
    voice_states: list["Voice_State"] = UNSET
    """States of members currently in voice channels; lacks the guild_id key"""
    members: list["Guild_Member"] = UNSET
    """Users in the guild"""
    channels: list["Channel"] = UNSET
    """Channels in the guild"""
    threads: list["Channel"] = UNSET
    """All active threads in the guild that current user has permission to view"""
    presences: list["Presence_Update"] = UNSET
    """Presences of the members in the guild, will only include non-offline members if the size is greater than large threshold"""
    stage_instances: list["Stage_Instance"] = UNSET
    """Stage instances in the guild"""
    guild_scheduled_events: list["Guild_Scheduled_Event"] = UNSET
    """Scheduled events in the guild"""


class Guild_Audit_Log_Entry_Create_Event(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Guild_Ban_Add(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    user: "User" = UNSET
    """User who was banned"""


class Guild_Ban_Remove(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    user: "User" = UNSET
    """User who was unbanned"""


class Guild_Emojis_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    emojis: list["Emoji"] = UNSET
    """Emojis"""


class Guild_Stickers_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    stickers: list[Sticker] = UNSET
    """Stickers"""


class Guild_Integrations_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild whose integrations were updated"""


class Guild_Member_Add(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Guild_Member_Remove(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    user: "User" = UNSET
    """User who was removed"""


class Guild_Member_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    roles: list[Snowflake] = UNSET
    """User role ids"""
    user: "User" = UNSET
    """User"""
    nick: Optional[Nullable[str]] = UNSET
    """Nickname of the user in the guild"""
    avatar: Nullable[str] = UNSET
    """Guild_Avatar_Hash"""
    joined_at: Nullable[datetime] = UNSET
    """When the user joined the guild"""
    premium_since: Optional[Nullable[datetime]] = UNSET
    """Boosting"""
    deaf: Optional[bool] = UNSET
    """Whether the user is deafened in voice channels"""
    mute: Optional[bool] = UNSET
    """Whether the user is muted in voice channels"""
    pending: Optional[bool] = UNSET
    """Membership_Screening"""
    communication_disabled_until: Optional[Nullable[datetime]] = UNSET
    """Timeout"""
    flags: Optional[Guild_Member_Flags] = UNSET
    """Guild_Member_Flags"""


class Guild_Members_Chunk(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    members: list["Guild_Member"] = UNSET
    """Set of guild members"""
    chunk_index: int = UNSET
    """Chunk index in the expected chunks for this response"""
    chunk_count: int = UNSET
    """Total number of expected chunks for this response"""
    not_found: Optional[list[Snowflake]] = UNSET
    """When passing an invalid ID to REQUEST_GUILD_MEMBERS, it will be returned here"""
    presences: Optional[list["Presence_Update"]] = UNSET
    """When passing true to REQUEST_GUILD_MEMBERS, presences of the returned members will be here"""
    nonce: Optional[str] = UNSET
    """Guild_Members_Request"""


class Guild_Role_Create(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    role: "Role" = UNSET
    """Role that was created"""


class Guild_Role_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    role: "Role" = UNSET
    """Role that was updated"""


class Guild_Role_Delete(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    role_id: Snowflake = UNSET
    """ID of the role"""


class Guild_Scheduled_Event_User_Add(DiscordObject):
    guild_scheduled_event_id: Snowflake = UNSET
    """ID of the guild scheduled event"""
    user_id: Snowflake = UNSET
    """ID of the user"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Guild_Scheduled_Event_User_Remove(DiscordObject):
    guild_scheduled_event_id: Snowflake = UNSET
    """ID of the guild scheduled event"""
    user_id: Snowflake = UNSET
    """ID of the user"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Integration_Create(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Integration_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""


class Integration_Delete(DiscordObject):
    id: Snowflake = UNSET
    """Integration ID"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    application_id: Optional[Snowflake] = UNSET
    """ID of the bot/OAuth2 application for this discord integration"""


class Invite_Create(DiscordObject):
    channel_id: Snowflake = UNSET
    """Channel the invite is for"""
    code: str = UNSET
    """Code"""
    created_at: datetime = UNSET
    """Time at which the invite was created"""
    guild_id: Optional[Snowflake] = UNSET
    """Guild of the invite"""
    inviter: Optional["User"] = UNSET
    """User that created the invite"""
    max_age: int = UNSET
    """How long the invite is valid for"""
    max_uses: int = UNSET
    """Maximum number of times the invite can be used"""
    target_type: Optional[Invite_Target_Types] = UNSET
    """Type_Of_Target"""
    target_user: Optional["User"] = UNSET
    """User whose stream to display for this voice channel stream invite"""
    target_application: Optional["Application"] = UNSET
    """Embedded application to open for this voice channel embedded application invite"""
    temporary: bool = UNSET
    """Whether"""
    uses: int = UNSET
    """How many times the invite has been used"""


class Invite_Delete(DiscordObject):
    channel_id: Snowflake = UNSET
    """Channel of the invite"""
    guild_id: Optional[Snowflake] = UNSET
    """Guild of the invite"""
    code: str = UNSET
    """Code"""


class Message_Create(DiscordObject):
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild the message was sent in - unless it is an ephemeral message"""
    member: Optional["Guild_Member"] = UNSET
    """Member properties for this message's author. Missing for ephemeral messages and messages from webhooks"""
    mentions: list["User"] = UNSET
    """Users specifically mentioned in the message"""


class Message_Delete(DiscordObject):
    id: Snowflake = UNSET
    """ID of the message"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""


class Message_Delete_Bulk(DiscordObject):
    ids: list[Snowflake] = UNSET
    """IDs of the messages"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""


class Message_Reaction_Add(DiscordObject):
    user_id: Snowflake = UNSET
    """ID of the user"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    member: Optional["Guild_Member"] = UNSET
    """Member who reacted if this happened in a guild"""
    emoji: "Emoji" = UNSET
    """Example"""
    message_author_id: Optional[Snowflake] = UNSET
    """ID of the user who authored the message which was reacted to"""
    burst: bool = UNSET
    """true if this is a super-reaction"""
    burst_colors: Optional[list[str]] = UNSET
    """Colors used for super-reaction animation in '#rrggbb' format"""
    type: "Reaction_Types" = UNSET
    """Type_Of_Reaction"""


class Message_Reaction_Remove(DiscordObject):
    user_id: Snowflake = UNSET
    """ID of the user"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    emoji: "Emoji" = UNSET
    """Example"""
    burst: bool = UNSET
    """true if this was a super-reaction"""
    type: "Reaction_Types" = UNSET
    """Type_Of_Reaction"""


class Reaction_Types(Enum):
    NORMAL = 0
    BURST = 1


class Message_Reaction_Remove_All(DiscordObject):
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""


class Message_Reaction_Remove_Emoji(DiscordObject):
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    emoji: "Emoji" = UNSET
    """Emoji that was removed"""


class Presence_Update(DiscordObject):
    user: "User" = UNSET
    """User whose presence is being updated"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    status: Status_Types = UNSET
    """Either 'idle', 'dnd', 'online' or 'offline'"""
    activities: list["Activity"] = UNSET
    """User's current activities"""
    client_status: list["Client_Status"] = UNSET
    """User's platform-dependent status"""


class Message_Poll_Vote_Add_Fields(DiscordObject):
    user_id: Snowflake = UNSET
    """ID of the user"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    answer_id: int = UNSET
    """ID of the answer"""


class Message_Poll_Vote_Remove_Fields(DiscordObject):
    user_id: Snowflake = UNSET
    """ID of the user"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    message_id: Snowflake = UNSET
    """ID of the message"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    answer_id: int = UNSET
    """ID of the answer"""


class Client_Status(DiscordObject):
    """
    Active sessions are indicated with an 'online', 'idle', or 'dnd' string per platform.
    If a user is offline or invisible, the corresponding field is not present.
    """

    desktop: Optional[str] = UNSET
    """User's status set for an active desktop"""
    mobile: Optional[str] = UNSET
    """User's status set for an active mobile"""
    web: Optional[str] = UNSET
    """User's status set for an active web"""


class Bot_Activity(DiscordObject):
    name: Optional[str] = UNSET
    state: Optional[Nullable[str]] = UNSET
    type: Optional["Activity_Types"] = UNSET
    url: Optional[str] = UNSET


class Activity(DiscordObject):
    """
    > info
    > Bot users are only able to set name, state, type, and url.
    """

    name: str = UNSET
    """Activity's name"""
    type: Action_Types = UNSET
    """Activity_Type"""
    url: Optional[Nullable[str]] = UNSET
    """Stream URL, is validated when type is 1"""
    created_at: UnixTimestamp = UNSET
    """Unix timestamp"""
    timestamps: Optional["Activity_Timestamps"] = UNSET
    """Unix timestamps for start and/or end of the game"""
    application_id: Optional[Snowflake] = UNSET
    """Application ID for the game"""
    details: Optional[Nullable[str]] = UNSET
    """What the player is currently doing"""
    state: Optional[Nullable[str]] = UNSET
    """User's current party status,"""
    emoji: Optional[Nullable["Emoji"]] = UNSET
    """Emoji used for a custom status"""
    party: Optional["Activity_Party"] = UNSET
    """Information for the current party of the player"""
    assets: Optional["Activity_Assets"] = UNSET
    """Images for the presence and their hover texts"""
    secrets: Optional["Activity_Secrets"] = UNSET
    """Secrets for Rich Presence joining and spectating"""
    instance: Optional[bool] = UNSET
    """Whether"""
    flags: Optional["Activity_Flags"] = UNSET
    """Activity_Flags"""
    buttons: Optional["Activity_Buttons"] = UNSET
    """Custom buttons shown in the Rich Presence"""


class Activity_Types(Enum):
    """
    > info
    > The streaming type currently only supports Twitch and YouTube.
    Only https://twitch.tv/ and https://youtube.com/ urls will work.
    """

    GAME = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


class Activity_Timestamps(DiscordObject):
    start: Optional[UnixTimestamp] = UNSET
    """Unix time"""
    end: Optional[UnixTimestamp] = UNSET
    """Unix time"""


class Activity_Emoji(DiscordObject):
    name: str = UNSET
    """Name of the emoji"""
    id: Optional[Snowflake] = UNSET
    """ID of the emoji"""
    animated: Optional[bool] = UNSET
    """Whether the emoji is animated"""


class Activity_Party(DiscordObject):
    id: Optional[str] = UNSET
    """ID of the party"""
    size: Optional[tuple[int, int]] = UNSET
    """Used to show the party's current and maximum size"""


class Activity_Assets(DiscordObject):
    large_image: Optional["Activity_Asset_Image"] = UNSET
    """Activity_Asset_Image"""
    large_text: Optional[str] = UNSET
    """Text displayed when hovering over the large image of the activity"""
    small_image: Optional["Activity_Asset_Image"] = UNSET
    """Activity_Asset_Image"""
    small_text: Optional[str] = UNSET
    """Text displayed when hovering over the small image of the activity"""


class Activity_Asset_Image(DiscordObject):
    """
    Activity asset images are arbitrary strings which usually contain snowflake IDs or prefixed image IDs.
    Treat data within this field carefully, as it is user-specifiable and not sanitized.
    """

    application_asset: str = UNSET
    media_proxy_image: str = UNSET


class Activity_Secrets(DiscordObject):
    join: Optional[str] = UNSET
    """Secret for joining a party"""
    spectate: Optional[str] = UNSET
    """Secret for spectating a game"""
    match: Optional[str] = UNSET
    """Secret for a specific instanced match"""


class Activity_Flags(Flag):
    INSTANCE = 1 << 0
    JOIN = 1 << 1
    SPECTATE = 1 << 2
    JOIN_REQUEST = 1 << 3
    SYNC = 1 << 4
    PLAY = 1 << 5
    PARTY_PRIVACY_FRIENDS = 1 << 6
    PARTY_PRIVACY_VOICE_CHANNEL = 1 << 7
    EMBEDDED = 1 << 8


class Activity_Buttons(DiscordObject):
    """
    When received over the gateway, the buttons field is an array of strings, which are the button labels.
    Bots cannot access a user's activity button URLs.
    When sending, the buttons field must be an array of the below object:.
    """

    label: str = UNSET
    """Text shown on the button"""
    url: str = UNSET
    """URL opened when clicking the button"""


class Typing_Start(DiscordObject):
    channel_id: Snowflake = UNSET
    """ID of the channel"""
    guild_id: Optional[Snowflake] = UNSET
    """ID of the guild"""
    user_id: Snowflake = UNSET
    """ID of the user"""
    timestamp: UnixTimestamp = UNSET
    """Unix time"""
    member: Optional["Guild_Member"] = UNSET
    """Member who started typing if this happened in a guild"""


class Voice_Server_Update(DiscordObject):
    token: str = UNSET
    """Voice connection token"""
    guild_id: Snowflake = UNSET
    """Guild this voice server update is for"""
    endpoint: Nullable[str] = UNSET
    """Voice server host"""


class Webhooks_Update(DiscordObject):
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    channel_id: Snowflake = UNSET
    """ID of the channel"""


class Application_Command(DiscordObject):
    """
    * options can only be set for application commands of type CHAT_INPUT.
    > danger
    > default_permission will soon be deprecated.
    You can instead set default_member_permissions to '0' to disable the command for everyone except admins by default, and/or use contexts to disable globally-scoped commands inside of DMs with your app.
    """

    id: Snowflake = UNSET
    """Unique ID of command"""
    type: Optional["Application_Command_Types"] = UNSET
    """Type_Of_Command"""
    application_id: Snowflake = UNSET
    """ID of the parent application"""
    guild_id: Optional[Snowflake] = UNSET
    """Guild ID of the command, if not global"""
    name: CommandConstraint = UNSET
    """Name_Of_Command"""
    name_localizations: Optional[Nullable[dict["Locales", CommandConstraint]]] = UNSET
    """Localization dictionary for name field. Values follow the same restrictions as name"""
    description: DescriptionConstraint = UNSET
    """Description for CHAT_INPUT commands, 1-100 characters. Empty string for USER and MESSAGE commands"""
    description_localizations: Optional[Nullable[dict["Locales", DescriptionConstraint]]] = UNSET
    """Localization dictionary for description field. Values follow the same restrictions as description"""
    options: list["Application_Command_Option"] = UNSET
    """Parameters for the command, max of 25"""
    default_member_permissions: Nullable[str] = UNSET
    """Permissions"""
    dm_permission: Optional[bool] = UNSET
    """Deprecated"""
    default_permission: Optional[Nullable[bool]] = UNSET
    """Not recommended for use as field will soon be deprecated. Indicates whether the command is enabled by default when the app is added to a guild, defaults to true"""
    nsfw: Optional[bool] = UNSET
    """Age-restricted"""
    integration_types: Optional["Application_Integration_Types"] = UNSET
    """In_Preview"""
    contexts: Optional[Nullable["Interaction_Context_Types"]] = UNSET
    """In_Preview"""
    version: Snowflake = UNSET
    """Autoincrementing version identifier updated during substantial record changes"""


class Application_Command_Types(Enum):
    CHAT_INPUT = 1
    """Slash commands; a text-based command that shows up when a user types /"""
    USER = 2
    """A UI-based command that shows up when you right click"""
    MESSAGE = 3
    """A UI-based command that shows up when you right click"""


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
    session_start_limit: "Session_Start_Limit" = UNSET


class Session_Start_Limit(DiscordObject):
    total: int = UNSET
    """Total number of session starts the current user is allowed"""
    remaining: int = UNSET
    """Remaining number of session starts the current user is allowed"""
    reset_after: int = UNSET
    """Number of milliseconds after which the limit resets"""
    max_concurrency: int = UNSET
    """Number of identify requests allowed per 5 seconds"""


class OAuth2_URLs(Enum):
    """
    > warn
    > In accordance with the relevant RFCs, the token and token revocation URLs will **only** accept a content type of application/x-www-form-urlencoded.
    JSON content is not permitted and will return an error.
    """

    BASE_AUTHORIZATION_URL = "https://discord.com/oauth2/authorize"
    TOKEN_URL = "https://discord.com/api/oauth2/token"
    TOKEN_REVOCATION = "https://discord.com/api/oauth2/token/revoke"


class OAuth2_Scopes(Enum):
    """
    These are a list of all the OAuth2 scopes that Discord supports.
    Some scopes require approval from Discord to use.
    Requesting them from a user without approval from Discord may cause errors or undocumented behavior in the OAuth2 flow.
    > info
    > In order to add a user to a guild, your bot has to already belong to that guild.
    > role_connections.write cannot be used with the [Implicit grant type](https:#/discord.com/developers/docs/topics/oauth2#implicit-grant).
    """

    ACTIVITIES_READ = (
        "allows your app to fetch data from a users Now Playing/Recently Played list — not currently available for apps"
    )
    ACTIVITIES_WRITE = "GAMESDK_ACTIVITY_MANAGER"
    APPLICATIONS_BUILDS_READ = "allows your app to read build data for a users applications"
    APPLICATIONS_BUILDS_UPLOAD = (
        "allows your app to upload/update builds for a users applications - requires Discord approval"
    )
    APPLICATIONS_COMMANDS = "Commands"
    APPLICATIONS_COMMANDS_UPDATE = "Commands"
    APPLICATIONS_COMMANDS_PERMISSIONS_UPDATE = "Permissions_For_Its_Commands"
    APPLICATIONS_ENTITLEMENTS = "allows your app to read entitlements for a users applications"
    APPLICATIONS_STORE_UPDATE = "allows your app to read and update store data"
    BOT = "for oauth2 bots, this puts the bot in the users selected guild by default"
    CONNECTIONS = "/users/@me/connections"
    DM_CHANNELS_READ = (
        "allows your app to see information about the users DMs and group DMs - requires Discord approval"
    )
    EMAIL = "/users/@me"
    GDM_JOIN = "Join_Users_To_A_Group_Dm"
    GUILDS = "/users/@me/guilds"
    GUILDS_JOIN = "/guilds/{guild.id}/members/{user.id}"
    GUILDS_MEMBERS_READ = "/users/@me/guilds/{guild.id}/member"
    IDENTIFY = "/users/@me"
    MESSAGES_READ = "for local rpc server api access, this allows you to read messages from all client channels"
    RELATIONSHIPS_READ = (
        "allows your app to know a users friends and implicit relationships - requires Discord approval"
    )
    ROLE_CONNECTIONS_WRITE = "allows your app to update a users connection and metadata for the app"
    RPC = "for local rpc server access, this allows you to control a users local Discord client - requires Discord approval"
    RPC_ACTIVITIES_WRITE = (
        "for local rpc server access, this allows you to update a users activity - requires Discord approval"
    )
    RPC_NOTIFICATIONS_READ = "for local rpc server access, this allows you to receive notifications pushed out to the user - requires Discord approval"
    RPC_VOICE_READ = "for local rpc server access, this allows you to read a users voice settings and listen for voice events - requires Discord approval"
    RPC_VOICE_WRITE = (
        "for local rpc server access, this allows you to update a users voice settings - requires Discord approval"
    )
    VOICE = (
        "allows your app to connect to voice on users behalf and see all the voice members - requires Discord approval"
    )
    WEBHOOK_INCOMING = (
        "this generates a webhook that is returned in the oauth token response for authorization code grants"
    )


class Bot_Auth_Parameters(DiscordObject):
    client_id: str = UNSET
    """your app's client id"""
    scope: str = UNSET
    """needs to include `bot` for the bot flow"""
    permissions: str = UNSET
    """Permissions"""
    guild_id: Snowflake = UNSET
    """pre-fills the dropdown picker with a guild for the user"""
    disable_guild_select: bool = UNSET
    """`true`"""


class Gateway_Opcodes(Enum):
    DISPATCH = 0
    """An event was dispatched"""
    HEARTBEAT = 1
    """Fired periodically by the client to keep the connection alive"""
    IDENTIFY = 2
    """Starts a new session during the initial handshake"""
    PRESENCE_UPDATE = 3
    """Update the client's presence"""
    VOICE_STATE_UPDATE = 4
    """Used to join/leave"""
    RESUME = 6
    """Resume a previous session that was disconnected"""
    RECONNECT = 7
    """You should attempt to reconnect and resume immediately"""
    REQUEST_GUILD_MEMBERS = 8
    """Request information about offline guild members in a large guild"""
    INVALID_SESSION = 9
    """The session has been invalidated. You should reconnect and identify/resume accordingly"""
    HELLO = 10
    """Sent immediately after connecting, contains the `heartbeat_interval` to use"""
    HEARTBEAT_ACK = 11
    """Sent in response to receiving a heartbeat to acknowledge that it has been received"""


class Gateway_Close_Event_Codes(Enum):
    """
    In order to prevent broken reconnect loops, you should consider some close codes as a signal to stop reconnecting.
    This can be because your token expired, or your identification is invalid.
    This table explains what the application defined close codes for the gateway are, and which close codes you should not attempt to reconnect.
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
    """Begin a voice websocket connection"""
    SELECT_PROTOCOL = 1
    """Select the voice protocol"""
    READY = 2
    """Complete the websocket handshake"""
    HEARTBEAT = 3
    """Keep the websocket connection alive"""
    SESSION_DESCRIPTION = 4
    """Describe the session"""
    SPEAKING = 5
    """Indicate which users are speaking"""
    HEARTBEAT_ACK = 6
    """Sent to acknowledge a received client heartbeat"""
    RESUME = 7
    """Resume a connection"""
    HELLO = 8
    """Time to wait between sending heartbeats in milliseconds"""
    RESUMED = 9
    """Acknowledge a successful session resume"""
    CLIENT_DISCONNECT = 13
    """A client has disconnected from the voice channel"""


class Voice_Close_Event_Codes(Enum):
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
    UNKNOWN_STREAM = 10049
    UNKNOWN_PREMIUM_SERVER_SUBSCRIBE_COOLDOWN = 10050
    UNKNOWN_GUILD_TEMPLATE = 10057
    UNKNOWN_DISCOVERABLE_SERVER_CATEGORY = 10059
    UNKNOWN_STICKER = 10060
    UNKNOWN_INTERACTION = 10062
    UNKNOWN_APPLICATION_COMMAND = 10063
    UNKNOWN_VOICE_STATE = 10065
    UNKNOWN_APPLICATION_COMMAND_PERMISSIONS = 10066
    UNKNOWN_STAGE_INSTANCE = 10067
    UNKNOWN_GUILD_MEMBER_VERIFICATION_FORM = 10068
    UNKNOWN_GUILD_WELCOME_SCREEN = 10069
    UNKNOWN_GUILD_SCHEDULED_EVENT = 10070
    UNKNOWN_GUILD_SCHEDULED_EVENT_USER = 10071
    UNKNOWN_TAG = 10087
    BOTS_CANNOT_USE_THIS_ENDPOINT = 20001
    ONLY_BOTS_CAN_USE_THIS_ENDPOINT = 20002
    EXPLICIT_CONTENT_CANNOT_BE_SENT_TO_THE_DESIRED_RECIPIENT = 20009
    YOU_ARE_NOT_AUTHORIZED_TO_PERFORM_THIS_ACTION_ON_THIS_APPLICATION = 20012
    THIS_ACTION_CANNOT_BE_PERFORMED_DUE_TO_SLOWMODE_RATE_LIMIT = 20016
    ONLY_THE_OWNER_OF_THIS_ACCOUNT_CAN_PERFORM_THIS_ACTION = 20018
    THIS_MESSAGE_CANNOT_BE_EDITED_DUE_TO_ANNOUNCEMENT_RATE_LIMITS = 20022
    UNDER_MINIMUM_AGE = 20024
    THE_CHANNEL_YOU_ARE_WRITING_HAS_HIT_THE_WRITE_RATE_LIMIT = 20028
    THE_WRITE_ACTION_YOU_ARE_PERFORMING_ON_THE_SERVER_HAS_HIT_THE_WRITE_RATE_LIMIT = 20029
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
    MAXIMUM_NUMBER_OF_GROUP_DMS_REACHED = 30011
    MAXIMUM_NUMBER_OF_GUILD_CHANNELS_REACHED = 30013
    MAXIMUM_NUMBER_OF_ATTACHMENTS_IN_A_MESSAGE_REACHED = 30015
    MAXIMUM_NUMBER_OF_INVITES_REACHED = 30016
    MAXIMUM_NUMBER_OF_ANIMATED_EMOJIS_REACHED = 30018
    MAXIMUM_NUMBER_OF_SERVER_MEMBERS_REACHED = 30019
    MAXIMUM_NUMBER_OF_SERVER_CATEGORIES_HAS_BEEN_REACHED = 30030
    GUILD_ALREADY_HAS_A_TEMPLATE = 30031
    MAXIMUM_NUMBER_OF_APPLICATION_COMMANDS_REACHED = 30032
    MAXIMUM_NUMBER_OF_THREAD_PARTICIPANTS_HAS_BEEN_REACHED = 30033
    MAXIMUM_NUMBER_OF_DAILY_APPLICATION_COMMAND_CREATES_HAS_BEEN_REACHED = 30034
    MAXIMUM_NUMBER_OF_BANS_FOR_NON_GUILD_MEMBERS_HAVE_BEEN_EXCEEDED = 30035
    MAXIMUM_NUMBER_OF_BANS_FETCHES_HAS_BEEN_REACHED = 30037
    MAXIMUM_NUMBER_OF_UNCOMPLETED_GUILD_SCHEDULED_EVENTS_REACHED = 30038
    MAXIMUM_NUMBER_OF_STICKERS_REACHED = 30039
    MAXIMUM_NUMBER_OF_PRUNE_REQUESTS_HAS_BEEN_REACHED__TRY_AGAIN_LATER = 30040
    MAXIMUM_NUMBER_OF_GUILD_WIDGET_SETTINGS_UPDATES_HAS_BEEN_REACHED__TRY_AGAIN_LATER = 30042
    MAXIMUM_NUMBER_OF_EDITS_TO_MESSAGES_OLDER_THAN_1_HOUR_REACHED__TRY_AGAIN_LATER = 30046
    MAXIMUM_NUMBER_OF_PINNED_THREADS_IN_A_FORUM_CHANNEL_HAS_BEEN_REACHED = 30047
    MAXIMUM_NUMBER_OF_TAGS_IN_A_FORUM_CHANNEL_HAS_BEEN_REACHED = 30048
    BITRATE_IS_TOO_HIGH_FOR_CHANNEL_OF_THIS_TYPE = 30052
    MAXIMUM_NUMBER_OF_PREMIUM_EMOJIS_REACHED = 30056
    MAXIMUM_NUMBER_OF_WEBHOOKS_PER_GUILD_REACHED = 30058
    MAXIMUM_NUMBER_OF_CHANNEL_PERMISSION_OVERWRITES_REACHED = 30060
    THE_CHANNELS_FOR_THIS_GUILD_ARE_TOO_LARGE = 30061
    UNAUTHORIZED__PROVIDE_A_VALID_TOKEN_AND_TRY_AGAIN = 40001
    YOU_NEED_TO_VERIFY_YOUR_ACCOUNT_IN_ORDER_TO_PERFORM_THIS_ACTION = 40002
    YOU_ARE_OPENING_DIRECT_MESSAGES_TOO_FAST = 40003
    SEND_MESSAGES_HAS_BEEN_TEMPORARILY_DISABLED = 40004
    REQUEST_ENTITY_TOO_LARGE__TRY_SENDING_SOMETHING_SMALLER_IN_SIZE = 40005
    THIS_FEATURE_HAS_BEEN_TEMPORARILY_DISABLED_SERVER_SIDE = 40006
    THE_USER_IS_BANNED_FROM_THIS_GUILD = 40007
    CONNECTION_HAS_BEEN_REVOKED = 40012
    TARGET_USER_IS_NOT_CONNECTED_TO_VOICE = 40032
    THIS_MESSAGE_HAS_ALREADY_BEEN_CROSSPOSTED = 40033
    AN_APPLICATION_COMMAND_WITH_THAT_NAME_ALREADY_EXISTS = 40041
    APPLICATION_INTERACTION_FAILED_TO_SEND = 40043
    CANNOT_SEND_A_MESSAGE_IN_A_FORUM_CHANNEL = 40058
    INTERACTION_HAS_ALREADY_BEEN_ACKNOWLEDGED = 40060
    TAG_NAMES_MUST_BE_UNIQUE = 40061
    SERVICE_RESOURCE_IS_BEING_RATE_LIMITED = 40062
    THERE_ARE_NO_TAGS_AVAILABLE_THAT_CAN_BE_SET_BY_NON_MODERATORS = 40066
    A_TAG_IS_REQUIRED_TO_CREATE_A_FORUM_POST_IN_THIS_CHANNEL = 40067
    AN_ENTITLEMENT_HAS_ALREADY_BEEN_GRANTED_FOR_THIS_RESOURCE = 40074
    USER_AGENT = 40333
    MISSING_ACCESS = 50001
    INVALID_ACCOUNT_TYPE = 50002
    CANNOT_EXECUTE_ACTION_ON_A_DM_CHANNEL = 50003
    GUILD_WIDGET_DISABLED = 50004
    CANNOT_EDIT_A_MESSAGE_AUTHORED_BY_ANOTHER_USER = 50005
    CANNOT_SEND_AN_EMPTY_MESSAGE = 50006
    CANNOT_SEND_MESSAGES_TO_THIS_USER = 50007
    CANNOT_SEND_MESSAGES_IN_A_NON_TEXT_CHANNEL = 50008
    CHANNEL_VERIFICATION_LEVEL_IS_TOO_HIGH_FOR_YOU_TO_GAIN_ACCESS = 50009
    OAUTH2_APPLICATION_DOES_NOT_HAVE_A_BOT = 50010
    OAUTH2_APPLICATION_LIMIT_REACHED = 50011
    INVALID_OAUTH2_STATE = 50012
    YOU_LACK_PERMISSIONS_TO_PERFORM_THAT_ACTION = 50013
    INVALID_AUTHENTICATION_TOKEN_PROVIDED = 50014
    NOTE_WAS_TOO_LONG = 50015
    PROVIDED_TOO_FEW = 50016
    INVALID_MFA_LEVEL = 50017
    A_MESSAGE_CAN_ONLY_BE_PINNED_TO_THE_CHANNEL_IT_WAS_SENT_IN = 50019
    INVITE_CODE_WAS_EITHER_INVALID = 50020
    CANNOT_EXECUTE_ACTION_ON_A_SYSTEM_MESSAGE = 50021
    CANNOT_EXECUTE_ACTION_ON_THIS_CHANNEL_TYPE = 50024
    INVALID_OAUTH2_ACCESS_TOKEN_PROVIDED = 50025
    MISSING_REQUIRED_OAUTH2_SCOPE = 50026
    INVALID_WEBHOOK_TOKEN_PROVIDED = 50027
    INVALID_ROLE = 50028
    INVALID_RECIPIENT = 50033
    A_MESSAGE_PROVIDED_WAS_TOO_OLD_TO_BULK_DELETE = 50034
    INVALID_FORM_BODY = 50035
    AN_INVITE_WAS_ACCEPTED_TO_A_GUILD_THE_APPLICATION_S_BOT_IS_NOT_IN = 50036
    INVALID_ACTIVITY_ACTION = 50039
    INVALID_API_VERSION_PROVIDED = 50041
    FILE_UPLOADED_EXCEEDS_THE_MAXIMUM_SIZE = 50045
    INVALID_FILE_UPLOADED = 50046
    CANNOT_SELF_REDEEM_THIS_GIFT = 50054
    INVALID_GUILD = 50055
    INVALID_SKU = 50057
    INVALID_REQUEST_ORIGIN = 50067
    INVALID_MESSAGE_TYPE = 50068
    PAYMENT_SOURCE_REQUIRED_TO_REDEEM_GIFT = 50070
    CANNOT_MODIFY_A_SYSTEM_WEBHOOK = 50073
    CANNOT_DELETE_A_CHANNEL_REQUIRED_FOR_COMMUNITY_GUILDS = 50074
    CANNOT_EDIT_STICKERS_WITHIN_A_MESSAGE = 50080
    INVALID_STICKER_SENT = 50081
    TRIED_TO_PERFORM_AN_OPERATION_ON_AN_ARCHIVED_THREAD__SUCH_AS_EDITING_A_MESSAGE = 50083
    INVALID_THREAD_NOTIFICATION_SETTINGS = 50084
    _BEFORE__VALUE_IS_EARLIER_THAN_THE_THREAD_CREATION_DATE = 50085
    COMMUNITY_SERVER_CHANNELS_MUST_BE_TEXT_CHANNELS = 50086
    THE_ENTITY_TYPE_OF_THE_EVENT_IS_DIFFERENT_FROM_THE_ENTITY_YOU_ARE_TRYING_TO_START_THE_EVENT_FOR = 50091
    THIS_SERVER_IS_NOT_AVAILABLE_IN_YOUR_LOCATION = 50095
    THIS_SERVER_NEEDS_MONETIZATION_ENABLED_IN_ORDER_TO_PERFORM_THIS_ACTION = 50097
    THIS_SERVER_NEEDS_MORE_BOOSTS_TO_PERFORM_THIS_ACTION = 50101
    THE_REQUEST_BODY_CONTAINS_INVALID_JSON_ = 50109
    OWNER_CANNOT_BE_PENDING_MEMBER = 50131
    OWNERSHIP_CANNOT_BE_TRANSFERRED_TO_A_BOT_USER = 50132
    FAILED_TO_RESIZE_ASSET_BELOW_THE_MAXIMUM_SIZE__262144 = 50138
    CANNOT_MIX_SUBSCRIPTION_AND_NON_SUBSCRIPTION_ROLES_FOR_AN_EMOJI = 50144
    CANNOT_CONVERT_BETWEEN_PREMIUM_EMOJI_AND_NORMAL_EMOJI = 50145
    UPLOADED_FILE_NOT_FOUND_ = 50146
    VOICE_MESSAGES_DO_NOT_SUPPORT_ADDITIONAL_CONTENT_ = 50159
    VOICE_MESSAGES_MUST_HAVE_A_SINGLE_AUDIO_ATTACHMENT_ = 50160
    VOICE_MESSAGES_MUST_HAVE_SUPPORTING_METADATA_ = 50161
    VOICE_MESSAGES_CANNOT_BE_EDITED_ = 50162
    CANNOT_DELETE_GUILD_SUBSCRIPTION_INTEGRATION = 50163
    YOU_CANNOT_SEND_VOICE_MESSAGES_IN_THIS_CHANNEL_ = 50173
    THE_USER_ACCOUNT_MUST_FIRST_BE_VERIFIED = 50178
    YOU_DO_NOT_HAVE_PERMISSION_TO_SEND_THIS_STICKER_ = 50600
    TWO_FACTOR_IS_REQUIRED_FOR_THIS_OPERATION = 60003
    NO_USERS_WITH_DISCORDTAG_EXIST = 80004
    REACTION_WAS_BLOCKED = 90001
    USER_CANNOT_USE_BURST_REACTIONS = 90002
    APPLICATION_NOT_YET_AVAILABLE__TRY_AGAIN_LATER = 110001
    API_RESOURCE_IS_CURRENTLY_OVERLOADED__TRY_AGAIN_A_LITTLE_LATER = 130000
    THE_STAGE_IS_ALREADY_OPEN = 150006
    CANNOT_REPLY_WITHOUT_PERMISSION_TO_READ_MESSAGE_HISTORY = 160002
    A_THREAD_HAS_ALREADY_BEEN_CREATED_FOR_THIS_MESSAGE = 160004
    THREAD_IS_LOCKED = 160005
    MAXIMUM_NUMBER_OF_ACTIVE_THREADS_REACHED = 160006
    MAXIMUM_NUMBER_OF_ACTIVE_ANNOUNCEMENT_THREADS_REACHED = 160007
    INVALID_JSON_FOR_UPLOADED_LOTTIE_FILE = 170001
    UPLOADED_LOTTIES_CANNOT_CONTAIN_RASTERIZED_IMAGES_SUCH_AS_PNG = 170002
    STICKER_MAXIMUM_FRAMERATE_EXCEEDED = 170003
    STICKER_FRAME_COUNT_EXCEEDS_MAXIMUM_OF_1000_FRAMES = 170004
    LOTTIE_ANIMATION_MAXIMUM_DIMENSIONS_EXCEEDED = 170005
    STICKER_FRAME_RATE_IS_EITHER_TOO_SMALL = 170006
    STICKER_ANIMATION_DURATION_EXCEEDS_MAXIMUM_OF_5_SECONDS = 170007
    CANNOT_UPDATE_A_FINISHED_EVENT = 180000
    FAILED_TO_CREATE_STAGE_NEEDED_FOR_STAGE_EVENT = 180002
    MESSAGE_WAS_BLOCKED_BY_AUTOMATIC_MODERATION = 200000
    TITLE_WAS_BLOCKED_BY_AUTOMATIC_MODERATION = 200001
    WEBHOOKS_POSTED_TO_FORUM_CHANNELS_MUST_HAVE_A_THREAD_NAME = 220001
    WEBHOOKS_POSTED_TO_FORUM_CHANNELS_CANNOT_HAVE_BOTH_A_THREAD_NAME_AND_THREAD_ID = 220002
    WEBHOOKS_CAN_ONLY_CREATE_THREADS_IN_FORUM_CHANNELS = 220003
    WEBHOOK_SERVICES_CANNOT_BE_USED_IN_FORUM_CHANNELS = 220004
    MESSAGE_BLOCKED_BY_HARMFUL_LINKS_FILTER = 240000
    CANNOT_ENABLE_ONBOARDING__REQUIREMENTS_ARE_NOT_MET = 350000
    CANNOT_UPDATE_ONBOARDING_WHILE_BELOW_REQUIREMENTS = 350001
    FAILED_TO_BAN_USERS = 500000
    POLL_VOTING_BLOCKED = 520000
    POLL_EXPIRED = 520001
    INVALID_CHANNEL_TYPE_FOR_POLL_CREATION = 520002
    CANNOT_EDIT_A_POLL_MESSAGE = 520003
    CANNOT_USE_AN_EMOJI_INCLUDED_WITH_THE_POLL = 520004
    CANNOT_EXPIRE_A_NON_POLL_MESSAGE = 520006


class RPC_Error(Enum):
    UNKNOWN_ERROR = 1000
    """An unknown error occurred"""
    INVALID_PAYLOAD = 4000
    """You sent an invalid payload"""
    INVALID_COMMAND = 4002
    """Invalid command name specified"""
    INVALID_GUILD = 4003
    """Invalid guild ID specified"""
    INVALID_EVENT = 4004
    """Invalid event name specified"""
    INVALID_CHANNEL = 4005
    """Invalid channel ID specified"""
    INVALID_PERMISSIONS = 4006
    """You lack permissions to access the given resource"""
    INVALID_CLIENT_ID = 4007
    """An invalid OAuth2 application ID was used to authorize"""
    INVALID_ORIGIN = 4008
    """An invalid OAuth2 application origin was used to authorize"""
    INVALID_TOKEN = 4009
    """An invalid OAuth2 token was used to authorize"""
    INVALID_USER = 4010
    """The specified user ID was invalid"""
    OAUTH2_ERROR = 5000
    """A standard OAuth2 error occurred; check the data  for the OAuth2 error details"""
    SELECT_CHANNEL_TIMED_OUT = 5001
    """An asynchronous SELECT_TEXT_CHANNEL/SELECT_VOICE_CHANNEL command timed out"""
    _GET_GUILD__TIMED_OUT = 5002
    """An asynchronous GET_GUILD command timed out"""
    SELECT_VOICE_FORCE_REQUIRED = 5003
    """You tried to join a user to a voice channel but the user was already in one"""
    CAPTURE_SHORTCUT_ALREADY_LISTENING = 5004
    """You tried to capture more than one shortcut key at once"""


class RPC_Close_Event_Codes(Enum):
    INVALID_CLIENT_ID = 4000
    """You connected to the RPC server with an invalid client ID"""
    INVALID_ORIGIN = 4001
    """You connected to the RPC server with an invalid origin"""
    RATE_LIMITED = 4002
    """You are being rate limited"""
    TOKEN_REVOKED = 4003
    """The OAuth2 token associated with a connection was revoked, get a new one!"""
    INVALID_VERSION = 4004
    """The RPC Server version specified in the connection string was not valid"""
    INVALID_ENCODING = 4005
    """The encoding specified in the connection string was not valid"""


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
    MESSAGE_CONTENT = 1 << 15
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTO_MODERATION_CONFIGURATION = 1 << 20
    AUTO_MODERATION_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DIRECT_MESSAGE_POLLS = 1 << 25


class Bitwise_Permission_Flags(Flag):
    """
    *** These permissions require the owner account to use [two-factor authentication](https:#/discord.com/developers/docs/topics/oauth2#twofactor-authentication-requirement) when used on a guild that has server-wide 2FA enabled.**
    **** See [Permissions for Timed Out Members](https:#/discord.com/developers/docs/topics/permissions#permissions-for-timed-out-members) to understand how permissions are temporarily modified for timed out users.**
    Note that permission names may be referred to differently in the Discord client.
    For example, 'Manage Permissions' refers to MANAGE_ROLES, 'Use Voice Activity' refers to USE_VAD, and 'Timeout Members' refers to MODERATE_MEMBERS.
    """

    CREATE_INSTANT_INVITE = 0x0000000000000001
    """Allows creation of instant invites"""
    KICK_MEMBERS = 0x0000000000000002
    """Allows kicking members"""
    BAN_MEMBERS = 0x0000000000000004
    """Allows banning members"""
    ADMINISTRATOR = 0x0000000000000008
    """Allows all permissions and bypasses channel permission overwrites"""
    MANAGE_CHANNELS = 0x0000000000000010
    """Allows management and editing of channels"""
    MANAGE_GUILD = 0x0000000000000020
    """Allows management and editing of the guild"""
    ADD_REACTIONS = 0x0000000000000040
    """Allows for the addition of reactions to messages"""
    VIEW_AUDIT_LOG = 0x0000000000000080
    """Allows for viewing of audit logs"""
    PRIORITY_SPEAKER = 0x0000000000000100
    """Allows for using priority speaker in a voice channel"""
    STREAM = 0x0000000000000200
    """Allows the user to go live"""
    VIEW_CHANNEL = 0x0000000000000400
    """Allows guild members to view a channel, which includes reading messages in text channels and joining voice channels"""
    SEND_MESSAGES = 0x0000000000000800
    """Allows for sending messages in a channel and creating threads in a forum"""
    SEND_TTS_MESSAGES = 0x0000000000001000
    """Allows for sending of /tts messages"""
    MANAGE_MESSAGES = 0x0000000000002000
    """Allows for deletion of other users messages"""
    EMBED_LINKS = 0x0000000000004000
    """Links sent by users with this permission will be auto-embedded"""
    ATTACH_FILES = 0x0000000000008000
    """Allows for uploading images and files"""
    READ_MESSAGE_HISTORY = 0x0000000000010000
    """Allows for reading of message history"""
    MENTION_EVERYONE = 0x0000000000020000
    """Allows for using the @everyone tag to notify all users in a channel, and the @here tag to notify all online users in a channel"""
    USE_EXTERNAL_EMOJIS = 0x0000000000040000
    """Allows the usage of custom emojis from other servers"""
    VIEW_GUILD_INSIGHTS = 0x0000000000080000
    """Allows for viewing guild insights"""
    CONNECT = 0x0000000000100000
    """Allows for joining of a voice channel"""
    SPEAK = 0x0000000000200000
    """Allows for speaking in a voice channel"""
    MUTE_MEMBERS = 0x0000000000400000
    """Allows for muting members in a voice channel"""
    DEAFEN_MEMBERS = 0x0000000000800000
    """Allows for deafening of members in a voice channel"""
    MOVE_MEMBERS = 0x0000000001000000
    """Allows for moving of members between voice channels"""
    USE_VAD = 0x0000000002000000
    """Allows for using voice-activity-detection in a voice channel"""
    CHANGE_NICKNAME = 0x0000000004000000
    """Allows for modification of own nickname"""
    MANAGE_NICKNAMES = 0x0000000008000000
    """Allows for modification of other users nicknames"""
    MANAGE_ROLES = 0x0000000010000000
    """Allows management and editing of roles"""
    MANAGE_WEBHOOKS = 0x0000000020000000
    """Allows management and editing of webhooks"""
    MANAGE_GUILD_EXPRESSIONS = 0x0000000040000000
    """Allows for editing and deleting emojis, stickers, and soundboard sounds created by all users"""
    USE_APPLICATION_COMMANDS = 0x0000000080000000
    """Allows members to use application commands, including slash commands and context menu commands"""
    REQUEST_TO_SPEAK = 0x0000000100000000
    """Allows for requesting to speak in stage channels"""
    MANAGE_EVENTS = 0x0000000200000000
    """Allows for editing and deleting scheduled events created by all users"""
    MANAGE_THREADS = 0x0000000400000000
    """Allows for deleting and archiving threads, and viewing all private threads"""
    CREATE_PUBLIC_THREADS = 0x0000000800000000
    """Allows for creating public and announcement threads"""
    CREATE_PRIVATE_THREADS = 0x0000001000000000
    """Allows for creating private threads"""
    USE_EXTERNAL_STICKERS = 0x0000002000000000
    """Allows the usage of custom stickers from other servers"""
    SEND_MESSAGES_IN_THREADS = 0x0000004000000000
    """Allows for sending messages in threads"""
    USE_EMBEDDED_ACTIVITIES = 0x0000008000000000
    """Allows for using Activities"""
    MODERATE_MEMBERS = 0x0000010000000000
    """Allows for timing out users to prevent them from sending"""
    VIEW_CREATOR_MONETIZATION_ANALYTICS = 0x0000020000000000
    """Allows for viewing role subscription insights"""
    USE_SOUNDBOARD = 0x0000040000000000
    """Allows for using soundboard in a voice channel"""
    CREATE_GUILD_EXPRESSIONS = 0x0000080000000000
    """See_Changelog"""
    CREATE_EVENTS = 0x0000100000000000
    """See_Changelog"""
    USE_EXTERNAL_SOUNDS = 0x0000200000000000
    """Allows the usage of custom soundboard sounds from other servers"""
    SEND_VOICE_MESSAGES = 0x0000400000000000
    """Allows sending voice messages"""
    SEND_POLLS = 0x0002000000000000
    """Allows sending polls"""


class Role(DiscordObject):
    """
    Roles without colors (`color == 0`) do not count towards the final computed color in the user list.
    """

    id: Snowflake = UNSET
    """role id"""
    name: str = UNSET
    """role name"""
    color: int = UNSET
    """integer representation of hexadecimal color code"""
    hoist: bool = UNSET
    """if this role is pinned in the user listing"""
    icon: Optional[Nullable[str]] = UNSET
    """Icon_Hash"""
    unicode_emoji: Optional[Nullable[str]] = UNSET
    """role unicode emoji"""
    position: int = UNSET
    """position of this role"""
    permissions: str = UNSET
    """permission bit set"""
    managed: bool = UNSET
    """whether this role is managed by an integration"""
    mentionable: bool = UNSET
    """whether this role is mentionable"""
    tags: Optional["Role_Tags"] = UNSET
    """the tags this role has"""
    flags: "Role_Flags" = UNSET
    """Role_Flags"""


class Role_Tags(DiscordObject):
    """
    Tags with type null represent booleans.
    They will be present and set to null if they are 'true', and will be not present if they are 'false'.
    """

    bot_id: Optional[Snowflake] = UNSET
    """the id of the bot this role belongs to"""
    integration_id: Optional[Snowflake] = UNSET
    """the id of the integration this role belongs to"""
    premium_subscriber: Nullable[bool] = UNSET
    """whether this is the guild's Booster role"""
    subscription_listing_id: Optional[Snowflake] = UNSET
    """the id of this role's subscription sku and listing"""
    available_for_purchase: Nullable[bool] = UNSET
    """whether this role is available for purchase"""
    guild_connections: Nullable[bool] = UNSET
    """whether this role is a guild's linked role"""


class Role_Flags(Flag):
    IN_PROMPT = 1 << 0
    """Onboarding"""


class Rate_Limit(DiscordObject):
    """
    Note that normal route rate-limiting headers will also be sent in this response.
    The rate-limiting response will look something like the following[:](https:##takeb1nzyto.space/).
    """

    message: str = UNSET
    """A message saying you are being rate limited"""
    retry_after: float = UNSET
    """The number of seconds to wait before submitting another request"""
    _global: bool = UNSET
    """A value indicating if you are being globally rate limited"""
    code: Optional[int] = UNSET
    """Error_Code"""


class Team_Member_Role_Types(Enum):
    """
    * The owner role is not represented in the role field on the [team member object](https:#/discord.com/developers/docs/topics/teams#data-models-team-member-object).
    Instead, the owner_user_id field  on the [team object](https:#/discord.com/developers/docs/topics/teams#data-models-team-object) should be used to identify which user has the owner role for the team.
    """

    ADMINS_HAVE_SIMILAR_ACCESS_AS_OWNERS__EXCEPT_THEY_CANNOT_TAKE_DESTRUCTIVE_ACTIONS_ON_THE_TEAM = "admin"
    DEVELOPERS_CAN_ACCESS_INFORMATION_ABOUT_TEAM_OWNED_APPS__LIKE_THE_CLIENT_SECRET = "developer"
    READ_ONLY_MEMBERS_CAN_ACCESS_INFORMATION_ABOUT_A_TEAM_AND_ANY_TEAM_OWNED_APPS__SOME_EXAMPLES_INCLUDE_GETTING_THE_IDS_OF_APPLICATIONS_AND_EXPORTING_PAYOUT_RECORDS__MEMBERS_CAN_ALSO_INVITE_BOTS_ASSOCIATED_WITH_TEAM_OWNED_APPS_THAT_ARE_MARKED_PRIVATE_ = (
        "read_only"
    )


class Team(DiscordObject):
    icon: Nullable[str] = UNSET
    """Hash of the image of the team's icon"""
    id: Snowflake = UNSET
    """Unique ID of the team"""
    members: list["Team_Member"] = UNSET
    """Members of the team"""
    name: str = UNSET
    """Name of the team"""
    owner_user_id: Snowflake = UNSET
    """User ID of the current team owner"""


class Team_Member(DiscordObject):
    membership_state: int = UNSET
    """Membership_State"""
    team_id: Snowflake = UNSET
    """ID of the parent team of which they are a member"""
    user: "User" = UNSET
    """Avatar, discriminator, ID, and username of the user"""
    role: str = UNSET
    """Role"""


class Membership_State_Enum(Enum):
    INVITED = 1
    ACCEPTED = 2


class Encryption_Modes(Enum):
    """
    >warn
    >The nonce has to be stripped from the payload before encrypting and before decrypting the audio data
    Finally, the voice server will respond with a [Opcode 4 Session Description](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) that includes the mode and secret_key, a 32 byte array used for [encrypting and sending](https:#/discord.com/developers/docs/topics/voice_connections#encrypting-and-sending-voice) voice data:.
    """

    NORMAL = "xsalsa20_poly1305"
    SUFFIX = "xsalsa20_poly1305_suffix"
    LITE = "xsalsa20_poly1305_lite"


class Voice_Packet(DiscordObject):
    version_flags: c_byte = 0x80
    payload_type: c_byte = 0x78
    sequence: c_ushort = 0x0
    timestamp: c_uint = 0x0
    ssrc: c_uint = 0x0
    encrypted_audio: bytearray = 0x0


class Speaking(Enum):
    """
    Speaking updates are used to update the **speaking modes** used by the client.
    This speaking mode is set using a [Opcode 5 Speaking](https://discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload.
    The client must send this at least once before sending audio to update the SSRC and set the initial speaking mode.
    Example Speaking Payload
    > You must send at least one [Opcode 5 Speaking](https:#/discord.com/developers/docs/topics/opcodes_and_status_codes#voice) payload before sending voice data, or you will be disconnected with an invalid SSRC error.json.
    """

    MICROPHONE = 1 << 0
    """Normal transmission of voice audio"""
    SOUNDSHARE = 1 << 1
    """Transmission of context audio for video, no speaking indicator"""
    PRIORITY = 1 << 2
    """Priority speaker, lowering audio of other speakers"""


class IP_Discovery(DiscordObject):
    """
    Generally routers on the Internet mask or obfuscate UDP ports through a process called NAT.
    Most users who implement voice will want to utilize IP discovery to find their external IP and port which will then be used for receiving voice communications.
    To retrieve your external IP and port, send the following UDP packet to your voice port (all numeric are big endian):.
    """

    type: int = UNSET
    """Values 0x1 and 0x2 indicate request and response, respectively"""
    length: int = UNSET
    """Message length excluding Type and Length fields"""
    ssrc: c_uint = UNSET
    """Unsigned integer"""
    address: str = UNSET
    """Null-terminated string in response"""
    port: c_ushort = UNSET
    """Unsigned short"""


class API_Versions(Enum):
    _10 = "Available"
    _9 = "Available"
    _8 = "Deprecated"
    _7 = "Deprecated"
    _6 = "Deprecated"
    _5 = "Discontinued"
    _4 = "Discontinued"
    _3 = "Discontinued"


class Snowflake_ID_Format(Enum):
    TIMESTAMP = (0 >> 22) + DISCORD_EPOCH
    """Milliseconds since Discord Epoch, the first second of 2015"""
    INTERNAL_WORKER_ID = (0 & 0x3E0000) >> 17
    INTERNAL_PROCESS_ID = (0 & 0x1F000) >> 12
    INCREMENT = 0 & 0xFFF
    """For every ID that is generated on that process, this number is incremented"""


class Formats(Enum):
    """
    Using the markdown for either users, roles, or channels will usually mention the target(s) accordingly, but this can be suppressed using the allowed_mentions parameter when creating a message.
    Standard emoji are currently rendered using [Twemoji](https:##twemoji.twitter.com/) for Desktop/Android and Apple's native emoji on iOS.
    Timestamps are expressed in seconds and display the given timestamp in the user's timezone and locale.
    * User mentions with an exclamation mark are deprecated and should be handled like any other user mention.
    ** Subcommands and subcommand groups can also be mentioned by using respectively </NAME SUBCOMMAND:ID> and </NAME SUBCOMMAND_GROUP SUBCOMMAND:ID>.
    """

    USER = "<@{USER_ID}>"
    NICKNAME = "<@!{user_id}>"
    CHANNEL = "<#{channel_id}>"
    ROLE = "<@&{role_id}>"
    SLASH_COMMAND = "</{name}:{command_id}>"
    STANDARD_EMOJI = "Unicode Characters"
    CUSTOM_EMOJI = "<:{name}:{id}>"
    CUSTOM_ANIMATED_EMOJI = "<a:{name}:{id}>"
    UNIX_TIMESTAMP = "<t:{TIMESTAMP}>"
    UNIX_TIMESTAMP_STYLED = "<t:{TIMESTAMP}:{STYLE}>"
    GUILD_NAVIGATION = "<{id}:{TYPE}>"


class Timestamp_Styles(Enum):
    SHORT_TIME = "t"
    """Short Time: 16:20"""
    LONG_TIME = "T"
    """Long Time: 16:20:30"""
    SHORT_DATE = "d"
    """Short Date: 20/04/2021"""
    LONG_DATE = "D"
    """Long Date: 20 April 2021"""
    SHORT_DATE_TIME = "f"
    """Short Date/Time: 20 April 2021 16:20"""
    LONG_DATE_TIME = "F"
    """Long Date/Time: Tuesday, 20 April 2021 16:20"""
    RELATIVE_TIME = "R"
    """Relative Time: 2 months ago"""


class Guild_Navigation_Types(Enum):
    """
    Guild navigation types link to the corresponding resource in the current server.
    """

    CUSTOMIZE = "Onboarding_Prompts"
    BROWSE = "Browse Channels_ tab"
    GUIDE = "Server_Guide"


class Image_Formats(Enum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    WEBP = "webp"
    GIF = "gif"
    LOTTIE = "json"


class CDN_Endpoints(Enum):
    """
    * In the case of endpoints that support GIFs, the hash will begin with a_ if it is available in GIF format.
    (example: a_1269e74af4df7417b13759eae50c83dc)
    ** In the case of the Default User Avatar endpoint, the value for index depends on whether the user is [migrated to the new username system](https:##discord.com/developers/docs/change/log#unique-usernames-on-discord).
    For users on the new username system, index will be (user_id >> 22) % 6.
    For users on the *legacy* username system, index will be discriminator % 5.
    *** In the case of the Default User Avatar and Sticker endpoints, the size of images returned is constant with the 'size' querystring parameter being ignored.
    **** In the case of the Sticker endpoint, the sticker will be available as PNG if its [format_type](https:##discord.com/developers/docs/resources/sticker#sticker-object) is PNG or APNG, GIF if its format_type is GIF, and as [Lottie](https:##airbnb.io/lottie/#/) if its format_type is LOTTIE.
    > info
    > Sticker GIFs do not use the CDN base url, and can be accessed at https:##media.discordapp.net/stickers/<sticker_id>.gif.
    """

    CUSTOM_EMOJI = "emojis/{emoji_id}.png"
    GUILD_ICON = "icons/{guild_id}/{guild_icon}.png"
    GUILD_SPLASH = "splashes/{guild_id}/{guild_splash}.png"
    GUILD_DISCOVERY_SPLASH = "discovery-splashes/{guild_id}/{guild_discovery_splash}.png"
    GUILD_BANNER = "banners/{guild_id}/{guild_banner}.png"
    USER_BANNER = "banners/{user_id}/{user_banner}.png"
    DEFAULT_USER_AVATAR = "embed/avatars/{user_discriminator}.png"
    USER_AVATAR = "avatars/{user_id}/{user_avatar}.png"
    GUILD_MEMBER_AVATAR = "guilds/{guild_id}/users/{user_id}/avatars/{member_avatar}.png"
    AVATAR_DECORATION = "avatar-decoration-presets/{avatar_decoration_data_asset}.png"
    APPLICATION_ICON = "app-icons/{application_id}/{icon}.png"
    APPLICATION_COVER = "app-assets/{application_id}/cover_image.png"
    APPLICATION_ASSET = "app-assets/{application_id}/{asset_id}.png"
    ACHIEVEMENT_ICON = "app-assets/{application_id}/achievements/{achievement_id}/icons/{icon_hash}.png"
    STORE_PAGE_ASSET = "app-assets/{application_id}/store/asset_id"
    STICKER_PACK_BANNER = "app-assets/710982414301790216/store/{sticker_pack_banner_asset_id}.png"
    TEAM_ICON = "team-icons/{team_id}/{team_icon}.png"
    STICKER = "stickers/{sticker_id}.png"
    ROLE_ICON = "role-icons/{role_id}/{role_icon}.png"
    GUILD_SCHEDULED_EVENT_COVER = "guild-events/{scheduled_event_id}/{scheduled_event_cover_image}.png"
    GUILD_MEMBER_BANNER = "guilds/{guild_id}/users/{user_id}/banners/{member_banner}.png"


class Attachment_CDN_URL_Parameters(DiscordObject):
    ex: str = UNSET
    """Hex timestamp indicating when an attachment CDN URL will expire"""
    is_: str = UNSET
    """Hex timestamp indicating when the URL was issued"""
    hm: str = UNSET
    """Unique signature that remains valid until the URL's expiration"""


class Locales(Enum):
    INDONESIAN = "id"  # Bahasa Indonesia
    DANISH = "da"  # Dansk
    GERMAN = "de"  # Deutsch
    ENGLISH_UK = "en-GB"  # English, UK
    ENGLISH_US = "en-US"  # English, US
    SPANISH = "es-ES"  # Español
    SPANISH_LATAM = "es-419"  # Español, LATAM
    FRENCH = "fr"  # Français
    CROATIAN = "hr"  # Hrvatski
    ITALIAN = "it"  # Italiano
    LITHUANIAN = "lt"  # Lietuviškai
    HUNGARIAN = "hu"  # Magyar
    DUTCH = "nl"  # Nederlands
    NORWEGIAN = "no"  # Norsk
    POLISH = "pl"  # Polski
    PORTUGUESE_BRAZILIAN = "pt-BR"  # Português do Brasil
    ROMANIAN_ROMANIA = "ro"  # Română
    FINNISH = "fi"  # Suomi
    SWEDISH = "sv-SE"  # Svenska
    VIETNAMESE = "vi"  # Tiếng Việt
    TURKISH = "tr"  # Türkçe
    CZECH = "cs"  # Čeština
    GREEK = "el"  # Ελληνικά
    BULGARIAN = "bg"  # български
    RUSSIAN = "ru"  # Pусский
    UKRAINIAN = "uk"  # Українська
    HINDI = "hi"  # हिन्दी
    THAI = "th"  # ไทย
    CHINESE_CHINA = "zh-CN"  # 中文
    JAPANESE = "ja"  # 日本語
    CHINESE_TAIWAN = "zh-TW"  # 繁體中文
    KOREAN = "ko"  # 한국어


class Component(DiscordObject):
    type: "Component_Types" = UNSET
    """Component_Type"""
    style: Optional["Button_Styles"] = UNSET
    """Button_Styles"""
    label: Optional[str] = UNSET
    """text that appears on the button, max 80 characters"""
    emoji: Optional[Emoji] = UNSET
    """`name`, `id`, and `animated`"""
    custom_id: Optional[str] = UNSET
    """a developer-defined identifier for the button, max 100 characters"""
    url: Optional[str] = UNSET
    """a url for link-style buttons"""
    disabled: Optional[bool] = UNSET
    """whether the button is disabled, default `false`"""
    components: Optional[list["Component"]] = UNSET
    """a list of child components"""
    options: list["Select_Option"] = UNSET
    placeholder: str = UNSET
    min_values: int = UNSET
    max_values: int = UNSET
    value: str = UNSET
    required: bool = UNSET
    min_length: int = UNSET
    max_length: int = UNSET


class Component_Types(Enum):
    """
    The structure of each component type is described in detail below.
    """

    ACTION_ROW = 1
    """Container for other components"""
    BUTTON = 2
    """Button"""
    STRING_SELECT = 3
    """Select menu for picking from defined text options"""
    TEXT_INPUT = 4
    """Text input"""
    USER_SELECT = 5
    """Select menu for users"""
    ROLE_SELECT = 6
    """Select menu for roles"""
    MENTIONABLE_SELECT = 7
    """Select menu for mentionables"""
    CHANNEL_SELECT = 8
    """Select menu for channels"""


class Button_Styles(Enum):
    """
    ![An image showing the different button styles](button-styles.png)
    When a user clicks on a button, your app will receive an [interaction](https://discord.com/developers/docs/interactions/receiving_and_responding#interaction-object) including the message the button was on:.
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


class Button(DiscordObject):
    """
    Buttons come in a variety of styles to convey different types of actions.
    These styles also define what fields are valid for a button.
    - Non-link buttons **must** have a custom_id, and cannot have a url
    - Link buttons **must** have a url, and cannot have a custom_id
    - Link buttons do not send an [interaction](https:#/discord.com/developers/docs/interactions/receiving_and_responding#interaction-object) to your app when clicked.
    """

    type: Component_Types = Component_Types.BUTTON
    """2 for a button"""
    style: "Button_Styles" = Button_Styles.PRIMARY
    """Button_Style"""
    label: Optional[str] = UNSET
    """Text that appears on the button; max 80 characters"""
    emoji: Optional["Emoji"] = UNSET
    """name, id, and animated"""
    custom_id: Optional[str] = UNSET
    """Developer-defined identifier for the button; max 100 characters"""
    url: Optional[str] = UNSET
    """URL for link-style buttons"""
    disabled: Optional[bool] = UNSET
    """Whether the button is disabled"""


class Select_Menu(DiscordObject):
    """
    * options is required for string select menus (component type 3), and unavailable for all other select menu components.
    ** channel_types can only be used for channel select menu components.
    *** default_values is only available for auto-populated select menu components, which include user (5), role (6), mentionable (7), and channel (8) [components](https:#/discord.com/developers/docs/interactions/message_components#component-object-component-types).
    """

    type: Component_Types = Component_Types.STRING_SELECT
    """Type"""
    custom_id: DescriptionConstraint = UNSET
    """ID for the select menu; max 100 characters"""
    options: Annotated[list["Select_Option"], Meta(max_length=25)] = UNSET
    """Specified choices in a select menu"""
    channel_types: list["Channel_Types"] = UNSET
    """List of channel types to include in the channel select component"""
    placeholder: Optional[str] = UNSET
    """Placeholder text if nothing is selected; max 150 characters"""
    default_values: list["Select_Default_Value"] = UNSET
    """List of default values for auto-populated select menu components; number of default values must be in the range defined by min_values and max_values"""
    min_values: Optional[Annotated[int, Meta(ge=0, le=25)]] = UNSET
    """Minimum number of items that must be chosen"""
    max_values: Optional[Annotated[int, Meta(ge=1, le=25)]] = UNSET
    """Maximum number of items that can be chosen"""
    disabled: Optional[bool] = UNSET
    """Whether select menu is disabled"""


class Select_Option(DiscordObject):
    label: DescriptionConstraint = UNSET
    """User-facing name of the option; max 100 characters"""
    value: DescriptionConstraint = UNSET
    """Dev-defined value of the option; max 100 characters"""
    description: Optional[DescriptionConstraint] = UNSET
    """Additional description of the option; max 100 characters"""
    emoji: Optional["Emoji"] = UNSET
    """`id`, `name`, and `animated`"""
    default: Optional[bool] = UNSET
    """Will show this option as selected by default"""


class Select_Default_Value(DiscordObject):
    id: Snowflake = UNSET
    """ID of a user, role or channel"""
    type: str = UNSET
    """Type of value that `id` represents. Either `user`, `role`, or `channel`"""


class Application_Command_Option(DiscordObject):
    """
    > warn
    * name must be unique within an array of [application command options](https:#/discord.com/developers/docs/interactions/application_commands#application-command-object-application-command-option-structure).
    ** autocomplete may not be set to true if choices are present.
    > info
    > Options using autocomplete are not confined to only use choices given by the application.
    """

    type: "Application_Command_Option_Type" = UNSET
    """Type of option"""
    name: CommandConstraint = UNSET
    """1-32_Character_Name"""
    name_localizations: Optional[Nullable[dict["Locales", CommandConstraint]]] = UNSET
    """Localization dictionary for the name field. Values follow the same restrictions as name"""
    description: DescriptionConstraint = UNSET
    """1-100 character description"""
    description_localizations: Optional[Nullable[dict["Locales", DescriptionConstraint]]] = UNSET
    """Localization dictionary for the description field. Values follow the same restrictions as description"""
    required: Optional[bool] = UNSET
    """Whether the parameter is required"""
    choices: Optional["Application_Command_Option_Choice"] = UNSET
    """Choices for the user to pick from, max 25"""
    options: Optional["Application_Command_Option"] = UNSET
    """If the option is a subcommand"""
    channel_types: Optional["Channel_Types"] = UNSET
    """The channels shown will be restricted to these types"""
    min_value: Optional[int | float] = UNSET
    """The minimum value permitted"""
    max_value: Optional[int | float] = UNSET
    """The maximum value permitted"""
    min_length: Optional[int] = UNSET
    """The minimum allowed length"""
    max_length: Optional[int] = UNSET
    """The maximum allowed length"""
    autocomplete: bool = UNSET
    """If autocomplete interactions are enabled for this option"""


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
    > info
    * Type of value depends on the [option type](https:#/discord.com/developers/docs/interactions/application_commands#application-command-object-application-command-option-type) that the choice belongs to.
    """

    name: DescriptionConstraint = UNSET
    """1-100 character choice name"""
    name_localizations: Optional[Nullable[dict["Locales", DescriptionConstraint]]] = UNSET
    """Localization dictionary for the name field. Values follow the same restrictions as name"""
    value: DescriptionConstraint | int = UNSET
    """Value for the choice, up to 100 characters if string"""


class Guild_Application_Command_Permissions(DiscordObject):
    """
    Returned when fetching the permissions for an app's command(s) in a guild.
    When the id field is the application ID instead of a command ID, the permissions apply to all commands that do not contain explicit overwrites.
    """

    id: Snowflake = UNSET
    """ID of the command"""
    application_id: Snowflake = UNSET
    """ID of the application the command belongs to"""
    guild_id: Snowflake = UNSET
    """ID of the guild"""
    permissions: Annotated[list["Application_Command_Permissions"], Meta(max_length=100)] = UNSET
    """Permissions for the command in the guild, max of 100"""


class Application_Command_Permissions(DiscordObject):
    """
    Application command permissions allow you to enable or disable commands for specific users, roles, or channels within a guild.
    """

    id: Snowflake = UNSET
    """ID of the role, user, or channel. 
    It can also be a permission constant like `guild_id` for everyone or `guild_id - 1` for all channels"""
    type: "Application_Command_Permission_Type" = UNSET
    """role"""
    permission: bool = UNSET
    """`true` to allow, `false`, to disallow"""


class Application_Command_Permission_Type(Enum):
    """
    To allow for fine-tuned access to commands, application command permissions are supported for guild and global commands of all types.
    Guild members and apps with the [necessary permissions](https:#/discord.com/developers/docs/interactions/application_commands#permissions) can allow or deny specific users and roles from using a command, or toggle commands for entire channels.
    Similar to how threads [inherit user and role permissions from the parent channel](https:#/discord.com/developers/docs/topics/threads#permissions), any command permissions for a channel will apply to the threads it contains.
    > info
    > If you don't have permission to use a command, it will not show up in the command picker.
    Members with the Administrator permission can use all commands.
    """

    ROLE = 1
    USER = 2
    CHANNEL = 3


class Text_Input(DiscordObject):
    type: int = UNSET
    """4 for a text input"""
    custom_id: str = UNSET
    """Developer-defined identifier for the input; max 100 characters"""
    style: int = UNSET
    """Text_Input_Style"""
    label: str = UNSET
    """Label for this component; max 45 characters"""
    min_length: Optional[int] = UNSET
    """Minimum input length for a text input; min 0, max 4000"""
    max_length: Optional[int] = UNSET
    """Maximum input length for a text input; min 1, max 4000"""
    required: Optional[bool] = UNSET
    """Whether this component is required to be filled"""
    value: Optional[str] = UNSET
    """Pre-filled value for this component; max 4000 characters"""
    placeholder: Optional[str] = UNSET
    """Custom placeholder text if the input is empty; max 100 characters"""


class Text_Input_Styles(Enum):
    SHORT = 1
    """Single-line input"""
    PARAGRAPH = 2
    """Multi-line input"""


class Interaction(DiscordObject):
    """
    * This is always present on application command, message component, and modal submit interaction types.
    It is optional for future-proofing against new interaction types
    ** member is sent when the interaction is invoked in a guild, and user is sent when invoked in a DM
    **** This is available on all interaction types except PING.
    """

    id: Snowflake = UNSET
    """ID of the interaction"""
    application_id: Snowflake = UNSET
    """ID of the application this interaction is for"""
    type: "Interaction_Type" = UNSET
    """Type of interaction"""
    data: "Application_Command_Data" = UNSET
    """Interaction data payload"""
    guild: Optional["Guild"] = UNSET
    """Guild that the interaction was sent from"""
    guild_id: Optional[Snowflake] = UNSET
    """Guild that the interaction was sent from"""
    channel: Optional["Channel"] = UNSET
    """Channel that the interaction was sent from"""
    channel_id: Optional[Snowflake] = UNSET
    """Channel that the interaction was sent from"""
    member: "Guild_Member" = UNSET
    """Guild member data for the invoking user, including permissions"""
    user: Optional["User"] = UNSET
    """User  for the invoking user, if invoked in a DM"""
    token: str = UNSET
    """Continuation token for responding to the interaction"""
    version: int = UNSET
    """Read-only property, always 1"""
    message: Optional["Message"] = UNSET
    """For components, the message they were attached to"""
    app_permissions: Bitwise_Permission_Flags = UNSET
    """Bitwise set of permissions the app has in the source location of the interaction"""
    locale: Locales = UNSET
    """Language"""
    guild_locale: Optional[Locales] = UNSET
    """Guild's_Preferred_Locale"""
    entitlements: list["Entitlement"] = UNSET
    """Monetized_Apps"""
    authorizing_integration_owners: list["Application_Integration_Types"] = UNSET
    """Authorizing_Integration_Owners"""
    context: Optional["Interaction_Context_Types"] = UNSET
    """Context where the interaction was triggered from"""


class Message_Interaction_Metadata(DiscordObject):
    id: Snowflake = UNSET
    """ID of the interaction"""
    type: "Interaction_Type" = UNSET
    """Type of interaction"""
    user: "User" = UNSET
    """User who triggered the interaction"""
    authorizing_integration_owners: list["Application_Integration_Types"] = UNSET
    """Authorizing_Integration_Owners"""
    original_response_message_id: Optional[Snowflake] = UNSET
    """Follow-up_Messages"""
    interacted_message_id: Optional[Snowflake] = UNSET
    """ID of the message that contained interactive component, present only on messages created from component interactions"""
    triggering_interaction_metadata: Optional["Message_Interaction_Metadata"] = UNSET
    """Metadata for the interaction that was used to open the modal, present only on modal submit interactions"""


class Interaction_Type(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class Interaction_Context_Types(Enum):
    """
    Context in Discord where an interaction can be used, or where it was triggered from.
    Details about using interaction contexts for application commands is in the [commands context documentation](https://discord.com/developers/docs/interactions/application_commands#interaction_contexts).
    """

    GUILD = 0
    """Interaction can be used within servers"""
    BOT_DM = 1
    """Interaction can be used within DMs with the app's bot user"""
    PRIVATE_CHANNEL = 2
    """Interaction can be used within Group DMs and DMs other than the app's bot user"""


class Application_Command_Data(DiscordObject):
    """
    > info
    * This [can be partial](https:#/discord.com/developers/docs/interactions/application_commands#autocomplete) when in response to APPLICATION_COMMAND_AUTOCOMPLETE.
    """

    id: Snowflake = UNSET
    """ID of the invoked command"""
    name: str = UNSET
    """Name of the invoked command"""
    type: Interaction_Type = UNSET
    """type"""
    resolved: Optional["Resolved_Data"] = UNSET
    """converted users + roles + channels + attachments"""
    options: Optional[list["Application_Command_Interaction_Data_Option"]] = list
    """the params + values from the user"""
    guild_id: Optional[Snowflake] = UNSET
    """the id of the guild the command is registered to"""
    target_id: Optional[Snowflake] = UNSET
    """User"""


class Message_Component_Data(DiscordObject):
    """
    * This is always present for select menu components.
    """

    custom_id: str = UNSET
    """custom_id"""
    component_type: int = UNSET
    """Type"""
    values: list["Select_Option"] = UNSET
    """Select_Menu"""
    resolved: Optional["Resolved_Data"] = UNSET
    """resolved entities from selected options"""


class Modal_Submit_Data(DiscordObject):
    custom_id: str = UNSET
    """custom_id"""
    components: list[Component] = UNSET
    """the values submitted by the user"""


class Resolved_Data(DiscordObject):
    """
    > info
    * Partial Member objects are missing user, deaf and mute fields
    ** Partial Channel objects only have id, name, type and permissions fields.
    Threads will also have thread_metadata and parent_id fields.
    """

    users: Optional[dict[Snowflake, User]] = UNSET
    """the ids and Users"""
    members: Optional[dict[Snowflake, Guild_Member]] = UNSET
    """the ids and Members"""
    roles: Optional[dict[Snowflake, Role]] = UNSET
    """the ids and Roles"""
    channels: Optional[dict[Snowflake, Channel]] = UNSET
    """the ids and Channels"""
    messages: Optional[dict[Snowflake, Message]] = UNSET
    """the ids and Messages"""
    attachments: Optional[dict[Snowflake, Attachment]] = UNSET
    """the ids and attachments"""


class Application_Command_Interaction_Data_Option(DiscordObject):
    """
    All options have names, and an option can either be a parameter and input value--in which case value will be set--or it can denote a subcommand or group--in which case it will contain a top-level key and another array of options.
    """

    name: str = UNSET
    """Name of the parameter"""
    type: Application_Command_Option_Type = UNSET
    """Application_Command_Option_Type"""
    value: Optional[str | int | float] = UNSET
    """Value of the option resulting from user input"""
    options: Optional[list["Application_Command_Interaction_Data_Option"]] = UNSET
    """Present if this option is a group"""
    focused: Optional[bool] = UNSET
    """true if this option is the currently focused option for autocomplete"""


class Interaction_Response(DiscordObject):
    type: "Interaction_Callback_Type" = UNSET
    """the type of response"""
    data: Optional["Interaction_Application_Command_Callback_Data"] = UNSET
    """an optional response message"""


class Interaction_Callback_Type(Enum):
    """
    * Only valid for [component-based](https:#/discord.com/developers/docs/interactions/message_components#) interactions
    ** Not available for MODAL_SUBMIT and PING interactions.
    *** Not available for APPLICATION_COMMAND_AUTOCOMPLETE and PING interactions.
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
    """respond to an autocomplete interaction with suggested choices"""
    MODAL = 9
    """respond to an interaction with a popup modal"""
    PREMIUM_REQUIRED = 10
    """respond to an interaction with an upgrade button, only available for apps with monetization enabled"""


class Interaction_Application_Command_Callback_Data(DiscordObject):
    """
    Not all message fields are currently supported.
    * See [Uploading Files](https:#/discord.com/developers/docs/reference#uploading-files) for details.
    """

    tts: Optional[bool] = UNSET
    """is the response TTS"""
    content: Optional[str] = UNSET
    """message content"""
    embeds: Optional[EmbedsConstraint] = UNSET
    """supports up to 10 embeds"""
    allowed_mentions: Optional["Allowed_Mentions"] = UNSET
    """Allowed_Mentions"""
    flags: Optional["Message_Flags"] = UNSET
    """Message_Flags"""
    components: Optional[ComponentConstraint] = UNSET
    """message components"""
    attachments: list["Attachment"] = UNSET
    """attachment s with filename and description"""
    poll: Optional["Poll"] = UNSET
    """A poll!"""
    choices: list[Application_Command_Option_Choice] = UNSET
    """autocomplete choices"""
    custom_id: str = UNSET
    """a developer-defined identifier for the modal, max 100 characters"""
    title: str = UNSET
    """the title of the popup modal, max 45 characters"""


class Interaction_Application_Command_Callback_Data_Flags(Flag):
    EPHEMERAL = 1 << 6
    """only the user receiving the message can see it"""


class Autocomplete(DiscordObject):
    choices: list["Application_Command_Option_Choice"] = UNSET
    """autocomplete choices"""


class Modal(DiscordObject):
    """
    > warn
    > warn
    > If your application responds with user data, you should use [allowed_mentions](https:#/discord.com/developers/docs/resources/channel#allowed-mentions-object) to filter which mentions in the content actually ping.
    When responding to an interaction received **via webhook**, your server can simply respond to the received POST request.
    You'll want to respond with a 200 status code (if everything went well), as well as specifying a type and data, which is an [Interaction Response](https:#/discord.com/developers/docs/interactions/receiving_and_responding#interaction-response-object) object:
    py
    @app.route('/', methods=['POST'])
    def my_command():
    if request.json['type'] == 1:
    return jsonify({
    'type': 1
    })
    else:
    return jsonify({
    'type': 4,
    'data': {
    'tts': False,
    'content': 'Congrats on sending your command!',
    'embeds': [],
    'allowed_mentions': { 'parse': [] }
    }
    })

    If you are receiving Interactions over the gateway, you will **also need to respond via HTTP**.
    Responses to Interactions **are not sent as commands over the gateway**.
    To respond to a gateway Interaction, make a POST request like this.
    interaction_id is the unique id of that individual Interaction from the received payload.
    interaction_token is the unique token for that interaction from the received payload.
    **This endpoint is only valid for Interactions received over the gateway.
    Otherwise, respond to the POST request to issue an initial response.**
    py
    import requests
    url = 'https:#/discord.com/api/v10/interactions/<interaction_id>/<interaction_token>/callback'
    json = {
    'type': 4,
    'data': {
    'content': 'Congrats on sending your command!'
    }
    }
    r = requests.post(url, json=json)

    > info
    > Interaction tokens are valid for **15 minutes** and can be used to send followup messages but you **must send an initial response within 3 seconds of receiving the event**.
    If the 3 second deadline is exceeded, the token will be invalidated.
    """

    custom_id: DescriptionConstraint = UNSET
    """a developer-defined identifier for the modal, max 100 characters"""
    title: ModalTitleConstraint = UNSET
    """the title of the popup modal, max 45 characters"""
    components: list["Component"] = UNSET
    """between 1 and 5"""


class Message_Interaction(DiscordObject):
    id: Snowflake = UNSET
    """ID of the interaction"""
    type: "Interaction_Type" = UNSET
    """Type of interaction"""
    name: str = UNSET
    """Application_Command"""
    user: "User" = UNSET
    """User who invoked the interaction"""
    member: Optional["Guild_Member"] = UNSET
    """Member who invoked the interaction in the guild"""


class SKU(DiscordObject):
    id: Snowflake = UNSET
    """ID of SKU"""
    type: "SKU_Types" = UNSET
    """Type_Of_SKU"""
    application_id: Snowflake = UNSET
    """ID of the parent application"""
    name: str = UNSET
    """Customer-facing name of your premium offering"""
    slug: str = UNSET
    """System-generated URL slug based on the SKU's name"""
    flags: "SKU_Flags" = UNSET
    """SKU_Flags"""


class SKU_Types(Enum):
    """
    For subscriptions, SKUs will have a type of either SUBSCRIPTION represented by type: 5 or SUBSCRIPTION_GROUP represented by type:6.
    For any current implementations, you will want to use the SKU defined by type: 5.
    A SUBSCRIPTION_GROUP is automatically created for each SUBSCRIPTION SKU and are not used at this time.
    """

    DURABLE = 2
    """Durable one-time purchase"""
    CONSUMABLE = 3
    """Consumable one-time purchase"""
    SUBSCRIPTION = 5
    """Represents a recurring subscription"""
    SUBSCRIPTION_GROUP = 6
    """System-generated group for each SUBSCRIPTION SKU created"""


class SKU_Flags(Flag):
    """
    For subscriptions, there are two types of access levels you can offer to users:.
    """

    AVAILABLE = 1 << 2
    """SKU is available for purchase"""
    GUILD_SUBSCRIPTION = 1 << 7
    """Recurring SKU that can be purchased by a user and applied to a single server. Grants access to every user in that server"""
    USER_SUBSCRIPTION = 1 << 8
    """Recurring SKU purchased by a user for themselves. Grants access to the purchasing user in every server"""


class Gateway_Commands(Events):
    """
    Events are payloads sent over the socket to a client that correspond to events in Discord.
    """

    Identify = staticmethod(Identify)
    """triggers the initial handshake with the gateway"""
    Resume = staticmethod(Resume)
    """resumes a dropped gateway connection"""
    Heartbeat = staticmethod(int)
    """maintains an active gateway connection"""
    Request_Guild_Members = staticmethod(Request_Guild_Members)
    """requests members for a guild"""
    Update_Voice_State = staticmethod(Gateway_Voice_State_Update)
    """joins, moves"""
    Update_Status = staticmethod(Gateway_Presence_Update)
    """updates a client's presence"""
