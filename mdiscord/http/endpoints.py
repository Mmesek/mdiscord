# -*- coding: utf-8 -*-
"""
Discord Endpoints
----------

Discord API endpoints.

:copyright: (c) 2021-2024 Mmesek
:version: 2024/06/26 16:14
"""

from datetime import datetime
from typing import Any, Optional

from msgspec import UNSET

from mdiscord.types import (
    SKU,
    Allowed_Mentions,
    Application,
    Application_Command,
    Application_Command_Option,
    Application_Command_Permissions,
    Application_Command_Type,
    Application_Integration_Types,
    Application_Role_Connection,
    Application_Role_Connection_Metadata,
    Attachment,
    Audit_Log,
    Audit_Log_Events,
    Authorization_Information,
    Auto_Moderation_Action,
    Auto_Moderation_Rule,
    Ban,
    Bitwise_Permission_Flags,
    Channel,
    Channel_Flags,
    Channel_Types,
    Component,
    Connection,
    Default_Message_Notification_Level,
    Default_Reaction,
    Embed,
    Emoji,
    Entitlement,
    Entitlement_Subscription_Types,
    Explicit_Content_Filter_Level,
    Followed_Channel,
    Forum_Tag,
    Gateway_Bot,
    Guild,
    Guild_Application_Command_Permissions,
    Guild_Features,
    Guild_Member,
    Guild_Member_Flags,
    Guild_Onboarding,
    Guild_Preview,
    Guild_Scheduled_Event,
    Guild_Scheduled_Event_Entity_Metadata,
    Guild_Scheduled_Event_Entity_Types,
    Guild_Scheduled_Event_Status,
    Guild_Scheduled_Event_User,
    Guild_Template,
    Guild_Widget,
    Guild_Widget_Settings,
    Install_Params,
    Integration,
    Interaction_Context_Types,
    Interaction_Callback_Type,
    Interaction_Application_Command_Callback_Data,
    Invite,
    Layout_Type,
    Locales,
    Message,
    Message_Flags,
    Message_Reference,
    MFA_Level,
    Nullable,
    Onboarding_Mode,
    Onboarding_Prompt,
    Overwrite,
    Poll,
    Poll_Answer,
    Privacy_Level,
    Reaction_Types,
    Role,
    Snowflake,
    Sort_Order_Types,
    Stage_Instance,
    Sticker,
    Sticker_Pack,
    System_Channel_Flags,
    Thread_List,
    Thread_Member,
    User,
    Verification_Level,
    Video_Quality_Modes,
    Voice_Region,
    Webhook,
    Welcome_Screen,
    Welcome_Screen_Channel,
)
from mdiscord.utils.routes import route
from mdiscord.utils.utils import Permissions as permissions


class Endpoints:
    @route(method="GET", path="/applications/@me")
    async def get_current_application(self) -> Application:
        """
        Returns the [application](https://discord.com/developers/docs/resources/application#application_object) object associated with the requesting bot user.
        """

    @route(method="PATCH", path="/applications/@me")
    async def edit_current_application(
        self,
        custom_install_url: str = None,
        description: str = None,
        role_connections_verification_url: str = None,
        install_params: Install_Params = None,
        integration_types_config: Application_Integration_Types = None,
        flags: int = None,
        interactions_endpoint_url: str = None,
        tags: list[str] = None,
        icon: Nullable[str] = UNSET,
        cover_image: Nullable[str] = UNSET,
    ) -> Application:
        """
        Edit properties of the app associated with the requesting bot user.
        Only properties that are passed will be updated.
        Returns the updated [application](https://discord.com/developers/docs/resources/application#application_object) object on success.

        Parameters
        ----------
        custom_install_url:
            Default custom authorization URL for the app, if enabled
        description:
            Description of the app
        role_connections_verification_url:
            Role connection verification URL for the app
        install_params:
            Settings for the app's default in-app authorization link, if enabled
        integration_types_config:
            In_Preview
        flags:
            Flags
        interactions_endpoint_url:
            Interactions_Endpoint_URL
        tags:
            List of tags describing the content and functionality of the app
        icon:
            Icon for the app
        cover_image:
            Default rich presence invite cover image for the app
        """

    @route(method="GET", path="/applications/{application_id}/role-connections/metadata")
    async def get_application_role_connection_metadata_records(
        self, application_id: Snowflake
    ) -> list[Application_Role_Connection_Metadata]:
        """
        Returns a list of [application role connection metadata](https://discord.com/developers/docs/resources/application_role_connection_metadata#application_role_connection_metadata_object) objects for the given application.
        """

    @route(method="PUT", path="/applications/{application_id}/role-connections/metadata")
    async def update_application_role_connection_metadata_records(
        self,
        application_id: Snowflake,
        application_role_connection_metadata: list[Application_Role_Connection_Metadata],
    ) -> list[Application_Role_Connection_Metadata]:
        """
        Updates and returns a list of [application role connection metadata](https://discord.com/developers/docs/resources/application_role_connection_metadata#application_role_connection_metadata_object) objects for the given application.
        """

    @permissions(Bitwise_Permission_Flags.VIEW_AUDIT_LOG)
    @route(method="GET", path="/guilds/{guild_id}/audit-logs")
    async def get_guild_audit_log(
        self,
        guild_id: Snowflake,
        *,
        user_id: Optional[Snowflake] = None,
        action_type: Optional[Audit_Log_Events] = None,
        before: Optional[Snowflake] = None,
        after: Optional[Snowflake] = None,
        limit: Optional[int] = None,
    ) -> Audit_Log:
        """
        Returns an [audit log](https://discord.com/developers/docs/resources/audit_log#audit_log_object) object for the guild.
        Requires the [VIEW_AUDIT_LOG](https://discord.com/developers/docs/topics/permissions#permissions_bitwise_permission_flags) permission.

        Parameters
        ----------
        user_id:
            Entries from a specific user ID
        action_type:
            Audit_Log_Event
        before:
            Entries with ID less than a specific audit log entry ID
        after:
            Entries with ID greater than a specific audit log entry ID
        limit:
            Maximum number of entries
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/auto-moderation/rules")
    async def list_auto_moderation_rules_for_guild(self, guild_id: Snowflake) -> list[Auto_Moderation_Rule]:
        """
        > This endpoint requires the `MANAGE_GUILD` [permission](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_permission_requirements).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/auto-moderation/rules/{auto_moderation_rule_id}")
    async def get_auto_moderation_rule(
        self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake
    ) -> Auto_Moderation_Rule:
        """
        > This endpoint requires the `MANAGE_GUILD` [permission](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_permission_requirements).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/auto-moderation/rules")
    async def create_auto_moderation_rule(
        self,
        guild_id: Snowflake,
        name: str = None,
        event_type: int = None,
        trigger_type: int = None,
        trigger_metadata: dict = None,
        actions: Auto_Moderation_Action = None,
        enabled: Optional[bool] = None,
        exempt_roles: Optional[list[Snowflake]] = None,
        exempt_channels: Optional[list[Snowflake]] = None,
        reason: str = None,
    ) -> Auto_Moderation_Rule:
        """
        > This endpoint requires the `MANAGE_GUILD` [permission](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_permission_requirements).

        Parameters
        ----------
        name:
            the rule name
        event_type:
            Event_Type
        trigger_type:
            Trigger_Type
        trigger_metadata:
            Trigger_Metadata
        actions:
            the actions which will execute when the rule is triggered
        enabled:
            whether the rule is enabled
        exempt_roles:
            the role ids that should not be affected by the rule
        exempt_channels:
            the channel ids that should not be affected by the rule
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/auto-moderation/rules/{auto_moderation_rule_id}")
    async def modify_auto_moderation_rule(
        self,
        guild_id: Snowflake,
        auto_moderation_rule_id: Snowflake,
        name: str = None,
        event_type: int = None,
        trigger_metadata: dict = None,
        actions: Auto_Moderation_Action = None,
        enabled: bool = None,
        exempt_roles: list[Snowflake] = None,
        exempt_channels: list[Snowflake] = None,
        reason: str = None,
    ) -> Auto_Moderation_Rule:
        """
        > Requires `MANAGE_GUILD` [permissions](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_permission_requirements).

        Parameters
        ----------
        name:
            the rule name
        event_type:
            Event_Type
        trigger_metadata:
            Trigger_Metadata
        actions:
            the actions which will execute when the rule is triggered
        enabled:
            whether the rule is enabled
        exempt_roles:
            the role ids that should not be affected by the rule
        exempt_channels:
            the channel ids that should not be affected by the rule
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="DELETE", path="/guilds/{guild_id}/auto-moderation/rules/{auto_moderation_rule_id}")
    async def delete_auto_moderation_rule(
        self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake, reason: str = None
    ) -> None:
        """
        > This endpoint requires the MANAGE_GUILD [permission](https://discord.com/developers/docs/resources/auto_moderation#auto_moderation_permission_requirements).
        """

    @route(method="GET", path="/channels/{channel_id}")
    async def get_channel(self, channel_id: Snowflake) -> Channel:
        """
        Get a channel by ID.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) object.
        If the channel is a thread, a [thread member](https://discord.com/developers/docs/resources/channel#thread_member_object) object is included in the returned result.
        """

    @route(method="PATCH", path="/channels/{channel_id}")
    async def modify_channel_dm(self, channel_id: Snowflake, name: str = None, icon: bytearray = None) -> Channel:
        """
        Update a channel's settings. Returns a [channel](https://discord.com/developers/docs/resources/channel#channel-object) on success, and a 400 BAD REQUEST on invalid parameters. All JSON parameters are optional.

        Params
        ------
        name:
            1-100 character channel name
        icon:
            base64 encoded icon
        """

    @route(method="PATCH", path="/channels/{channel_id}")
    async def modify_channel(
        self,
        channel_id: Snowflake,
        name: str = None,
        icon: bytearray = None,
        type: int = None,
        archived: bool = None,
        auto_archive_duration: int = None,
        locked: bool = None,
        invitable: bool = None,
        position: Nullable[int] = UNSET,
        topic: Nullable[str] = UNSET,
        nsfw: Nullable[bool] = UNSET,
        rate_limit_per_user: Nullable[int] = UNSET,
        bitrate: Nullable[int] = UNSET,
        user_limit: Nullable[int] = UNSET,
        permission_overwrites: Nullable[Overwrite] = UNSET,
        parent_id: Nullable[Snowflake] = UNSET,
        rtc_region: Nullable[str] = UNSET,
        video_quality_mode: Nullable[int] = UNSET,
        default_auto_archive_duration: Nullable[int] = UNSET,
        flags: Optional[Channel_Flags] = None,
        available_tags: Optional[Forum_Tag] = None,
        default_reaction_emoji: Optional[Nullable[Default_Reaction]] = UNSET,
        default_thread_rate_limit_per_user: Optional[int] = None,
        default_sort_order: Optional[Nullable[int]] = UNSET,
        default_forum_layout: Optional[int] = None,
        applied_tags: Optional[list[Snowflake]] = None,
    ) -> Channel:
        """
        Update a channel's settings.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) on success, and a 400 BAD REQUEST on invalid parameters.
        All JSON parameters are optional.

        Parameters
        ----------
        name:
            1-100 character channel name
        icon:
            base64 encoded icon
        type:
            Type_Of_Channel
        archived:
            whether the thread is archived
        auto_archive_duration:
            the thread will stop showing in the channel list after `auto_archive_duration` minutes of inactivity, can be set to: 60, 1440, 4320, 10080
        locked:
            whether the thread is locked; when a thread is locked, only users with MANAGE_THREADS can unarchive it
        invitable:
            whether non-moderators can add other non-moderators to a thread; only available on private threads
        position:
            the position of the channel in the left-hand listing
        topic:
            0-1024 character channel topic
        nsfw:
            whether the channel is nsfw
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        bitrate:
            the bitrate
        user_limit:
            the user limit of the voice
        permission_overwrites:
            channel
        parent_id:
            id of the new parent category for a channel
        rtc_region:
            Voice_Region
        video_quality_mode:
            Video_Quality_Mode
        default_auto_archive_duration:
            the default duration that the clients use
        flags:
            Channel_Flags
        available_tags:
            the set of tags that can be used in a `GUILD_FORUM`
        default_reaction_emoji:
            the emoji to show in the add reaction button on a thread in a `GUILD_FORUM`
        default_thread_rate_limit_per_user:
            the initial `rate_limit_per_user` to set on newly created threads in a channel. this field is copied to the thread at creation time and does not live update.
        default_sort_order:
            Default_Sort_Order_Type
        default_forum_layout:
            Default_Forum_Layout_Type
        applied_tags:
            the IDs of the set of tags that have been applied to a thread in a `GUILD_FORUM`
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="PATCH", path="/channels/{channel_id}")
    async def modify_channel_thread(
        self,
        channel_id: Snowflake,
        name: str = None,
        archived: bool = False,
        default_auto_archive_duration: int = None,
        auto_archive_duration: int = None,
        locked: bool = False,
        rate_limit_per_user: int = None,
        reason: str = None,
    ) -> Channel:
        """
        Update a channel's settings. Returns a [channel](https://discord.com/developers/docs/resources/channel#channel-object) on success, and a 400 BAD REQUEST on invalid parameters. All JSON parameters are optional.

        Params
        ------
        name:
            2-100 character channel name
        archived:
            whether the channel is archived
        default_auto_archive_duration:
            the default duration for newly created threads in the channel, in minutes, to automatically archive the thread after recent activity
        auto_archive_duration:
            duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
        locked:
            when a thread is locked, only users with MANAGE_THREADS can unarchive it
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="DELETE", path="/channels/{channel_id}")
    async def delete_close_channel(self, channel_id: Snowflake, reason: str = None) -> Channel:
        """
        Delete a channel, or close a private message.
        Requires the MANAGE_CHANNELS permission for the guild, or MANAGE_THREADS if the channel is a thread.
        Deleting a category does not delete its child channels; they will have their parent_id removed and a [Channel Update](https://discord.com/developers/docs/topics/gateway_events#channel_update) Gateway event will fire for each of them.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) object on success.
        Fires a [Channel Delete](https://discord.com/developers/docs/topics/gateway_events#channel_delete) Gateway event (or [Thread Delete](https://discord.com/developers/docs/topics/gateway_events#thread_delete) if the channel was a thread).
        """

    @permissions(Bitwise_Permission_Flags.VIEW_CHANNEL, Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/messages")
    async def get_channel_messages(
        self,
        channel_id: Snowflake,
        *,
        around: Optional[Snowflake] = None,
        before: Optional[Snowflake] = None,
        after: Optional[Snowflake] = None,
        limit: Optional[int] = 50,
    ) -> list[Message]:
        """
        Retrieves the messages in a channel.
        Returns an array of [message](https://discord.com/developers/docs/resources/channel#message_object) objects on success.

        Parameters
        ----------
        around:
            Get messages around this message ID
        before:
            Get messages before this message ID
        after:
            Get messages after this message ID
        limit:
            Max number of messages to return
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/messages/{message_id}")
    async def get_channel_message(self, channel_id: Snowflake, message_id: Snowflake) -> Message:
        """
        Retrieves a specific message in the channel.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object on success.
        """

    @route(method="POST", path="/channels/{channel_id}/messages")
    async def create_message(
        self,
        channel_id: Snowflake,
        content: str = None,
        nonce: Optional[int] = None,
        tts: Optional[bool] = None,
        embeds: Optional[list[Embed]] = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        message_reference: Optional[Message_Reference] = None,
        components: Optional[list[Component]] = None,
        attachments: Optional[list[Attachment]] = None,
        sticker_ids: Optional[list[Snowflake]] = None,
        flags: Optional[Message_Flags] = None,
        enforce_nonce: Optional[bool] = None,
        poll: Optional[Poll] = None,
    ) -> Message:
        """
        Files must be attached using a multipart/form_data body as described in [Uploading Files](https://discord.com/developers/docs/reference#uploading_files).
        > warn
        Limitations
        - When operating on a guild channel, the current user must have the `SEND_MESSAGES` permission.
        - When sending a message with `tts` (text-to-speech) set to `true`, the current user must have the `SEND_TTS_MESSAGES` permission.
        - When creating a message as a reply to another message, the current user must have the `READ_MESSAGE_HISTORY` permission.
        - The referenced message must exist and cannot be a system message.
        - The maximum request size when sending a message is **25 MiB**
        - For the embed object, you can set every field except `type` (it will be `rich` regardless of if you try to set it), `provider`, `video`, and any `height`, `width`, or `proxy_url` values for images.

        Parameters
        ----------
        content:
            Message contents
        tts:
            `true` if this is a TTS message
        embeds:
            Up to 10 `rich` embeds
        payload_json:
            JSON encoded body of non-file params
        allowed_mentions:
            Allowed mentions for the message
        message_reference:
            Include to make your message a reply
        components:
            Components to include with the message
        attachments:
            Uploading_Files
        sticker_ids:
            Stickers
        files[n]:
            Uploading_Files
        nonce:
            Message_Create_Event
        flags:
            Message_Flags
        enforce_nonce:
            If true and nonce is present, it will be checked for uniqueness in the past few minutes. If another message was created by the same author with the same nonce, that message will be returned and no new message will be created.
        poll:
            A poll!
        """

    @permissions(Bitwise_Permission_Flags.SEND_MESSAGES)
    @route(method="POST", path="/channels/{channel_id}/messages/{message_id}/crosspost")
    async def crosspost_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> Message:
        """
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object.
        Fires a [Message Update](https://discord.com/developers/docs/topics/gateway_events#message_update) Gateway event.
        Crosspost a message in an Announcement Channel to following channels.
        This endpoint requires the `SEND_MESSAGES` permission, if the current user sent the message, or additionally the `MANAGE_MESSAGES` permission, for all other messages, to be present for the current user.
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY | Bitwise_Permission_Flags.ADD_REACTIONS)
    @route(method="PUT", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me")
    async def create_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> None:
        """
        Create a reaction for the message.
        This endpoint requires the `READ_MESSAGE_HISTORY` permission to be present on the current user.
        Additionally, if nobody else has reacted to the message using this emoji, this endpoint requires the ADD_REACTIONS permission to be present on the current user.
        Returns a `204 empty response` on success.
        Fires a [Message Reaction Add](https://discord.com/developers/docs/topics/gateway_events#message_reaction_add) Gateway event.
        """

    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me")
    async def delete_own_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> None:
        """
        Delete a reaction the current user has made for the message.
        Returns a 204 empty response on success.
        Fires a [Message Reaction Remove](https://discord.com/developers/docs/topics/gateway_events#message_reaction_remove) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}")
    async def delete_user_reaction(
        self, channel_id: Snowflake, message_id: Snowflake, emoji: str, user_id: Snowflake, reason: str = None
    ) -> None:
        """
        Deletes another user's reaction.
        This endpoint requires the `MANAGE_MESSAGES` permission to be present on the current user.
        Returns a 204 empty response on success.
        Fires a [Message Reaction Remove](https://discord.com/developers/docs/topics/gateway_events#message_reaction_remove) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}")
    async def get_reactions(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        emoji: str,
        *,
        type: Optional[Reaction_Types] = Reaction_Types.NORMAL,
        after: Optional[Snowflake] = None,
        limit: Optional[int] = 25,
    ) -> list[User]:
        """
        Get a list of users that reacted with this emoji.
        Returns an array of [user](https://discord.com/developers/docs/resources/user#user_object) objects on success.

        Parameters
        ----------
        type:
            Type_Of_Reaction
        after:
            Get users after this user ID
        limit:
            Max number of users to return
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions")
    async def delete_all_reactions(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Deletes all reactions on a message.
        This endpoint requires the `MANAGE_MESSAGES` permission to be present on the current user.
        Fires a [Message Reaction Remove All](https://discord.com/developers/docs/topics/gateway_events#message_reaction_remove_all) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}")
    async def delete_all_reactions_for_emoji(
        self, channel_id: Snowflake, message_id: Snowflake, emoji: str, reason: str = None
    ) -> None:
        """
        Deletes all the reactions for a given emoji on a message.
        This endpoint requires the `MANAGE_MESSAGES` permission to be present on the current user.
        Fires a [Message Reaction Remove Emoji](https://discord.com/developers/docs/topics/gateway_events#message_reaction_remove_emoji) Gateway event.
        """

    @route(method="PATCH", path="/channels/{channel_id}/messages/{message_id}")
    async def edit_message(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        content: str = None,
        embeds: list[Embed] = None,
        flags: Message_Flags = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        attachments: list[Attachment] = None,
        components: list[Component] = None,
    ) -> Message:
        """
        Refer to [Uploading Files](https://discord.com/developers/docs/reference#uploading_files) for details on attachments and multipart/form_data requests.
        Edit a previously sent message.
        The fields `content`, `embeds`, and `flags` can be edited by the original message author.
        Other users can only edit `flags` and only if they have the `MANAGE_MESSAGES` permission in the corresponding channel.
        When specifying flags, ensure to include all previously set flags/bits in addition to ones that you are modifying.
        Only `flags` documented in the table below may be modified by users (unsupported flag changes are currently ignored without error).

        Parameters
        ----------
        content:
            Message contents
        embeds:
            Up to 10 `rich` embeds
        flags:
            Flags
        allowed_mentions:
            Allowed mentions for the message
        attachments:
            Uploading_Files
        components:
            Components to include with the message
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}")
    async def delete_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Delete a message.
        If operating on a guild channel and trying to delete a message that was not sent by the current user, this endpoint requires the MANAGE_MESSAGES permission.
        Returns a 204 empty response on success.
        Fires a [Message Delete](https://discord.com/developers/docs/topics/gateway_events#message_delete) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="POST", path="/channels/{channel_id}/messages/bulk-delete")
    async def bulk_delete_messages(
        self, channel_id: Snowflake, messages: list[Snowflake] = None, reason: str = None
    ) -> None:
        """
        Delete multiple messages in a single request.
        This endpoint can only be used on guild channels and requires the MANAGE_MESSAGES permission.
        Returns a 204 empty response on success.
        Fires a [Message Delete Bulk](https://discord.com/developers/docs/topics/gateway_events#message_delete_bulk) Gateway event.

        Parameters
        ----------
        messages:
            an  message ids to delete
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PUT", path="/channels/{channel_id}/permissions/{overwrite_id}")
    async def edit_channel_permissions(
        self,
        channel_id: Snowflake,
        overwrite_id: Snowflake,
        allow: Optional[Bitwise_Permission_Flags] = None,
        deny: Optional[Bitwise_Permission_Flags] = None,
        type: int = 0,
        reason: str = None,
    ) -> None:
        """
        Edit the channel permission overwrites for a user or role in a channel.
        Only usable for guild channels.
        Requires the MANAGE_ROLES permission.
        Only permissions your bot has in the guild or parent channel (if applicable) can be allowed/denied (unless your bot has a MANAGE_ROLES overwrite in the channel).
        Returns a 204 empty response on success.
        Fires a [Channel Update](https://discord.com/developers/docs/topics/gateway_events#channel_update) Gateway event.
        For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions).

        Parameters
        ----------
        allow:
            the bitwise value of all allowed permissions
        deny:
            the bitwise value of all disallowed permissions
        type:
            0 for a role, 1 for a member
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="GET", path="/channels/{channel_id}/invites")
    async def get_channel_invites(self, channel_id: Snowflake) -> list[Invite]:
        """
        Returns a list of [invite](https://discord.com/developers/docs/resources/invite#invite_object) objects (with [invite metadata](https://discord.com/developers/docs/resources/invite#invite_metadata_object)) for the channel.
        Only usable for guild channels.
        Requires the MANAGE_CHANNELS permission.
        """

    @permissions(Bitwise_Permission_Flags.CREATE_INSTANT_INVITE)
    @route(method="POST", path="/channels/{channel_id}/invites")
    async def create_channel_invite(
        self,
        channel_id: Snowflake,
        max_age: int = 86400,
        max_uses: int = None,
        temporary: bool = False,
        unique: bool = False,
        target_type: int = None,
        target_user_id: Snowflake = None,
        target_application_id: Snowflake = None,
        reason: str = None,
    ) -> Invite:
        """
        Create a new [invite](https://discord.com/developers/docs/resources/invite#invite_object) object for the channel.
        Only usable for guild channels.
        Requires the CREATE_INSTANT_INVITE permission.
        All JSON parameters for this route are optional, however the request body is not.
        If you are not sending any fields, you still have to send an empty JSON object ({}).
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite_object) object.
        Fires an [Invite Create](https://discord.com/developers/docs/topics/gateway_events#invite_create) Gateway event.

        Parameters
        ----------
        max_age:
            duration of invite in seconds before expiry,
        max_uses:
            max number of uses
        temporary:
            whether this invite only grants temporary membership
        unique:
            if true, don't try to reuse a similar invite
        target_type:
            Type_Of_Target
        target_user_id:
            the id of the user whose stream to display for this invite, required if `target_type` is 1, the user must be streaming in the channel
        target_application_id:
            the id of the embedded application to open for this invite, required if `target_type` is 2, the application must have the `EMBEDDED` flag
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="DELETE", path="/channels/{channel_id}/permissions/{overwrite_id}")
    async def delete_channel_permission(
        self, channel_id: Snowflake, overwrite_id: Snowflake, reason: str = None
    ) -> None:
        """
        Delete a channel permission overwrite for a user or role in a channel.
        Only usable for guild channels.
        Requires the `MANAGE_ROLES` permission.
        Returns a 204 empty response on success.
        Fires a [Channel Update](https://discord.com/developers/docs/topics/gateway_events#channel_update) Gateway event.
        For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="POST", path="/channels/{channel_id}/followers")
    async def follow_announcement_channel(
        self, channel_id: Snowflake, webhook_channel_id: Snowflake = None, reason: str = None
    ) -> Followed_Channel:
        """
        Follow an Announcement Channel to send messages to a target channel.
        Requires the MANAGE_WEBHOOKS permission in the target channel.
        Returns a [followed channel](https://discord.com/developers/docs/resources/channel#followed_channel_object) object.
        Fires a [Webhooks Update](https://discord.com/developers/docs/topics/gateway_events#webhooks_update) Gateway event for the target channel.

        Parameters
        ----------
        webhook_channel_id:
            id of target channel
        """

    @route(method="POST", path="/channels/{channel_id}/typing")
    async def trigger_typing_indicator(self, channel_id: Snowflake) -> None:
        """
        Post a typing indicator for the specified channel, which expires after 10 seconds.
        Returns a 204 empty response on success.
        Fires a [Typing Start](https://discord.com/developers/docs/topics/gateway_events#typing_start) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/pins")
    async def get_pinned_messages(self, channel_id: Snowflake) -> list[Message]:
        """
        Returns all pinned messages in the channel as an array of [message](https://discord.com/developers/docs/resources/channel#message_object) objects.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="PUT", path="/channels/{channel_id}/pins/{message_id}")
    async def pin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Pin a message in a channel.
        Requires the `MANAGE_MESSAGES` permission.
        Returns a 204 empty response on success.
        Fires a [Channel Pins Update](https://discord.com/developers/docs/topics/gateway_events#channel_pins_update) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/pins/{message_id}")
    async def unpin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Unpin a message in a channel.
        Requires the `MANAGE_MESSAGES` permission.
        Returns a 204 empty response on success.
        Fires a [Channel Pins Update](https://discord.com/developers/docs/topics/gateway_events#channel_pins_update) Gateway event.
        """

    @route(method="PUT", path="/channels/{channel_id}/recipients/{user_id}")
    async def group_dm_add_recipient(
        self, channel_id: Snowflake, user_id: Snowflake, access_token: str = None, nick: str = None
    ) -> None:
        """
        Adds a recipient to a Group DM using their access token.

        Parameters
        ----------
        access_token:
            access token of a user that has granted your app the `gdm.join` scope
        nick:
            nickname of the user being added
        """

    @route(method="DELETE", path="/channels/{channel_id}/recipients/{user_id}")
    async def group_dm_remove_recipient(self, channel_id: Snowflake, user_id: Snowflake) -> None:
        """
        Removes a recipient from a Group DM.
        """

    @route(method="POST", path="/channels/{channel_id}/messages/{message_id}/threads")
    async def start_thread_from_message(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        name: str = None,
        auto_archive_duration: Optional[int] = None,
        rate_limit_per_user: Optional[Nullable[int]] = UNSET,
    ) -> Channel:
        """
        When called on a `GUILD_TEXT` channel, creates a `PUBLIC_THREAD`.
        When called on a `GUILD_ANNOUNCEMENT` channel, creates a `ANNOUNCEMENT_THREAD`.
        Does not work on a [GUILD_FORUM](https://discord.com/developers/docs/resources/channel#start_thread_in_forum_or_media_channel) or a GUILD_MEDIA channel.
        The id of the created thread will be the same as the id of the source message, and as such a message can only have a single thread created from it.

        Parameters
        ----------
        name:
            1-100 character channel name
        auto_archive_duration:
            the thread will stop showing in the channel list after `auto_archive_duration` minutes of inactivity, can be set to: 60, 1440, 4320, 10080
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        """

    @route(method="POST", path="/channels/{channel_id}/threads")
    async def start_thread_without_message(
        self,
        channel_id: Snowflake,
        name: str = None,
        auto_archive_duration: Optional[int] = None,
        type: Channel_Types = None,
        invitable: Optional[bool] = None,
        rate_limit_per_user: Optional[Nullable[int]] = UNSET,
        reason: str = None,
    ) -> Channel:
        """
        Creates a new thread that is not connected to an existing message.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) on success, and a 400 BAD REQUEST on invalid parameters.
        Fires a [Thread Create](https://discord.com/developers/docs/topics/gateway_events#thread_create) Gateway event.

        Parameters
        ----------
        name:
            1-100 character channel name
        auto_archive_duration:
            the thread will stop showing in the channel list after `auto_archive_duration` minutes of inactivity, can be set to: 60, 1440, 4320, 10080
        type:
            Type_Of_Thread
        invitable:
            whether non-moderators can add other non-moderators to a thread; only available when creating a private thread
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        """

    @route(method="POST", path="/channels/{channel_id}/threads")
    async def start_thread_in_forum_or_media_channel(
        self,
        channel_id: Snowflake,
        name: str = None,
        auto_archive_duration: int = None,
        content: str = UNSET,
        embeds: list["Embed"] = UNSET,
        allowed_mentions: "Allowed_Mentions" = Allowed_Mentions(parse=[]),
        components: list["Component"] = UNSET,
        sticker_ids: list[Snowflake] = UNSET,
        attachments: list["Attachment"] = UNSET,
        flags: Message_Flags = UNSET,
        rate_limit_per_user: Optional[Nullable[int]] = UNSET,
        applied_tags: Optional[list[Snowflake]] = None,
        reason: str = None,
    ):
        """
        _ Files must be attached using a multipart/form_data body as described in [Uploading Files](https://discord.com/developers/docs/reference#uploading_files).

        Forum and Media Thread Message Params Object
        > info
        > When sending a message, apps must provide a value for **at least one of** `content`, `embeds`, `sticker_ids`, `components`, or `files[n]`.
        | Field             | Type                                                                                         | Description                                                                                                                                                                                              |
        |-------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | content?\*        | string                                                                                       | Message contents (up to 2000 characters)                                                                                                                                                                 |
        | embeds?\*         | array of [embed](https://discord.com/developers/docs/resources/channel#embed-object) objects                               | Up to 10 `rich` embeds (up to 6000 characters)                                                                                                                                                           |
        | allowed_mentions? | [allowed mention object](https://discord.com/developers/docs/resources/channel#allowed-mentions-object)                    | Allowed mentions for the message                                                                                                                                                                         |
        | components?\*     | array of [message component](https://discord.com/developers/docs/interactions/message_components#component-object) objects | Components to include with the message                                                                                                                                                                   |
        | sticker_ids?\*    | array of snowflakes                                                                          | IDs of up to 3 [stickers](https://discord.com/developers/docs/resources/sticker#sticker-object) in the server to send in the message                                                                                                   |
        | attachments?      | array of partial [attachment](https://discord.com/developers/docs/resources/channel#attachment-object) objects             | Attachment objects with `filename` and `description`.
        See [Uploading Files](https://discord.com/developers/docs/reference#uploading-files)                                                                                             |
        | flags?            | integer                                                                                      | [Message flags](https:#/discord.com/developers/docs/resources/channel#message-object-message-flags) combined as a [bitfield](https:#/en.wikipedia.org/wiki/Bit_field) (only `SUPPRESS_EMBEDS` and `SUPPRESS_NOTIFICATIONS` can be set) |
        \* At least one of `content`, `embeds`, `sticker_ids`, `components`, or `files[n]` is required.

        Parameters
        ----------
        name:
            1-100 character channel name
        auto_archive_duration:
            duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
        message:
            contents of the first message in the forum/media thread
        files[n]:
            Uploading_Files
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        applied_tags:
            the IDs of the set of tags that have been applied to a thread in a `GUILD_FORUM`
        payload_json:
            Uploading_Files
        """

    @route(method="PUT", path="/channels/{channel_id}/thread-members/@me")
    async def join_thread(self, channel_id: Snowflake, reason: str = None) -> None:
        """
        Adds the current user to a thread.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway_events#thread_members_update) and a [Thread Create](https://discord.com/developers/docs/topics/gateway_events#thread_create) Gateway event.
        """

    @route(method="PUT", path="/channels/{channel_id}/thread-members/{user_id}")
    async def add_thread_member(self, channel_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Adds another member to a thread.
        Requires the ability to send messages in the thread.
        Also requires the thread is not archived.
        Returns a 204 empty response if the member is successfully added or was already a member of the thread.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway_events#thread_members_update) Gateway event.
        """

    @route(method="DELETE", path="/channels/{channel_id}/thread-members/@me")
    async def leave_thread(self, channel_id: Snowflake, reason: str = None) -> None:
        """
        Removes the current user from a thread.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway_events#thread_members_update) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_THREADS)
    @route(method="DELETE", path="/channels/{channel_id}/thread-members/{user_id}")
    async def remove_thread_member(self, channel_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Removes another member from a thread.
        Requires the MANAGE_THREADS permission, or the creator of the thread if it is a PRIVATE_THREAD.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway_events#thread_members_update) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/thread-members/{user_id}")
    async def get_thread_member(
        self, channel_id: Snowflake, user_id: Snowflake, *, with_member: Optional[bool] = None
    ) -> Thread_Member:
        """
        When with_member is set to true, the thread member object will include a member field containing a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) object.

        Parameters
        ----------
        with_member:
            Guild_Member
        """

    @route(method="GET", path="/channels/{channel_id}/thread-members")
    async def list_thread_members(
        self,
        channel_id: Snowflake,
        *,
        with_member: Optional[bool] = None,
        after: Optional[Snowflake] = None,
        limit: Optional[int] = None,
    ) -> list[Thread_Member]:
        """
        > This endpoint is restricted according to whether the GUILD_MEMBERS [Privileged Intent](https://discord.com/developers/docs/topics/gateway#privileged_intents) is enabled for your application.
        > warn.

        Parameters
        ----------
        with_member:
            Guild_Member
        after:
            Get thread members after this user ID
        limit:
            Max number of thread members to return
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/threads/archived/public")
    async def list_public_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[datetime] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are public.
        When called on a GUILD_TEXT channel, returns threads of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) PUBLIC_THREAD.
        When called on a GUILD_ANNOUNCEMENT channel returns threads of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) ANNOUNCEMENT_THREAD.
        Threads are ordered by archive_timestamp, in descending order.
        Requires the READ_MESSAGE_HISTORY permission.

        Parameters
        ----------
        before:
            returns threads archived before this timestamp
        limit:
            optional maximum number of threads to return
        """

    @route(method="GET", path="/channels/{channel_id}/threads/archived/private")
    async def list_private_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[datetime] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) PRIVATE_THREAD.
        Threads are ordered by archive_timestamp, in descending order.
        Requires both the READ_MESSAGE_HISTORY and MANAGE_THREADS permissions.

        Parameters
        ----------
        before:
            returns threads archived before this timestamp
        limit:
            optional maximum number of threads to return
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/users/@me/threads/archived/private")
    async def list_joined_private_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[Snowflake] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) PRIVATE_THREAD, and the user has joined.
        Threads are ordered by their id, in descending order.
        Requires the `READ_MESSAGE_HISTORY` permission.

        Parameters
        ----------
        before:
            returns threads before this id
        limit:
            optional maximum number of threads to return
        """

    @route(method="GET", path="/guilds/{guild_id}/emojis")
    async def list_guild_emojis(self, guild_id: Snowflake) -> list[Emoji]:
        """
        Returns a list of [emoji](https://discord.com/developers/docs/resources/emoji#emoji_object) objects for the given guild.
        Includes user fields if the bot has the CREATE_GUILD_EXPRESSIONS or MANAGE_GUILD_EXPRESSIONS permission.
        """

    @route(method="GET", path="/guilds/{guild_id}/emojis/{emoji_id}")
    async def get_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> Emoji:
        """
        Returns an [emoji](https://discord.com/developers/docs/resources/emoji#emoji_object) object for the given guild and emoji IDs.
        Includes the user field if the bot has the MANAGE_GUILD_EXPRESSIONS permission, or if the bot created the emoji and has the the CREATE_GUILD_EXPRESSIONS permission.
        """

    @permissions(Bitwise_Permission_Flags.CREATE_GUILD_EXPRESSIONS)
    @route(method="POST", path="/guilds/{guild_id}/emojis")
    async def create_guild_emoji(
        self,
        guild_id: Snowflake,
        name: str = None,
        image: str = None,
        roles: list[Snowflake] = None,
        reason: str = None,
    ) -> Emoji:
        """
        > Emojis and animated emojis have a maximum file size of 256 KiB.
        Attempting to upload an emoji larger than this limit will fail and return 400 Bad Request and an error message, but not a [JSON status code](https://discord.com/developers/docs/topics/opcodes_and_status_codes#json).

        Parameters
        ----------
        name:
            name of the emoji
        image:
            the 128x128 emoji image
        roles:
            roles allowed to use this emoji
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD_EXPRESSIONS)
    @route(method="PATCH", path="/guilds/{guild_id}/emojis/{emoji_id}")
    async def modify_guild_emoji(
        self,
        guild_id: Snowflake,
        emoji_id: Snowflake,
        name: str = None,
        roles: Nullable[list[Snowflake]] = UNSET,
        reason: str = None,
    ) -> Emoji:
        """
        Modify the given emoji.
        For emojis created by the current user, requires either the `CREATE_GUILD_EXPRESSIONS` or `MANAGE_GUILD_EXPRESSIONS` permission.
        For other emojis, requires the `MANAGE_GUILD_EXPRESSIONS` permission.
        Returns the updated [emoji](https://discord.com/developers/docs/resources/emoji#emoji_object) object on success.
        Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway_events#guild_emojis_update) Gateway event.

        Parameters
        ----------
        name:
            name of the emoji
        roles:
            roles allowed to use this emoji
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD_EXPRESSIONS)
    @route(method="DELETE", path="/guilds/{guild_id}/emojis/{emoji_id}")
    async def delete_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, reason: str = None) -> None:
        """
        Delete the given emoji.
        For emojis created by the current user, requires either the `CREATE_GUILD_EXPRESSIONS` or `MANAGE_GUILD_EXPRESSIONS` permission.
        For other emojis, requires the `MANAGE_GUILD_EXPRESSIONS` permission.
        Returns 204 No Content on success.
        Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway_events#guild_emojis_update) Gateway event.
        """

    @route(method="POST", path="/guilds")
    async def create_guild(
        self,
        name: str = None,
        region: Optional[Nullable[str]] = UNSET,
        icon: Optional[str] = None,
        verification_level: Optional[Verification_Level] = None,
        default_message_notifications: Optional[Default_Message_Notification_Level] = None,
        explicit_content_filter: Optional[Explicit_Content_Filter_Level] = None,
        roles: Optional[list[Role]] = None,
        channels: Optional[list[Channel]] = None,
        afk_channel_id: Optional[Snowflake] = None,
        afk_timeout: Optional[int] = None,
        system_channel_id: Optional[Snowflake] = None,
        system_channel_flags: Optional[System_Channel_Flags] = None,
    ) -> Guild:
        """
        Create a new guild.
        Returns a [guild](https://discord.com/developers/docs/resources/guild#guild_object) object on success.
        Fires a [Guild Create](https://discord.com/developers/docs/topics/gateway_events#guild_create) Gateway event.

        Parameters
        ----------
        name:
            name of the guild
        region:
            Voice_Region
        icon:
            base64 128x128 image for the guild icon
        verification_level:
            Verification_Level
        default_message_notifications:
            Message_Notification_Level
        explicit_content_filter:
            Explicit_Content_Filter_Level
        roles:
            new guild roles
        channels:
            new guild's channels
        afk_channel_id:
            id for afk channel
        afk_timeout:
            afk timeout in seconds, can be set to: 60, 300, 900, 1800, 3600
        system_channel_id:
            the id of the channel where guild notices such as welcome messages and boost events are posted
        system_channel_flags:
            System_Channel_Flags
        """

    @route(method="GET", path="/guilds/{guild_id}")
    async def get_guild(self, guild_id: Snowflake, *, with_counts: Optional[bool] = False) -> Guild:
        """
        Returns the [guild](https://discord.com/developers/docs/resources/guild#guild_object) object for the given id.
        If with_counts is set to true, this endpoint will also return approximate_member_count and approximate_presence_count for the guild.

        Parameters
        ----------
        with_counts:
            when `true`, will return approximate member and presence counts for the guild
        """

    @route(method="GET", path="/guilds/{guild_id}/preview")
    async def get_guild_preview(self, guild_id: Snowflake) -> Guild_Preview:
        """
        If the user is not in the guild, then the guild must be [discoverable](https://discord.com/developers/docs/resources/guild#guild_object_guild_features).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}")
    async def modify_guild(
        self,
        guild_id: Snowflake,
        name: str = None,
        region: Nullable[str] = UNSET,
        verification_level: Nullable[Verification_Level] = UNSET,
        default_message_notifications: Nullable[Default_Message_Notification_Level] = UNSET,
        explicit_content_filter: Nullable[Explicit_Content_Filter_Level] = UNSET,
        afk_channel_id: Nullable[Snowflake] = UNSET,
        afk_timeout: int = None,
        icon: Nullable[str] = UNSET,
        owner_id: Snowflake = None,
        splash: Nullable[str] = UNSET,
        discovery_splash: Nullable[str] = UNSET,
        banner: Nullable[str] = UNSET,
        system_channel_id: Nullable[Snowflake] = UNSET,
        system_channel_flags: System_Channel_Flags = None,
        premium_progress_bar_enabled: bool = None,
        rules_channel_id: Nullable[Snowflake] = UNSET,
        public_updates_channel_id: Nullable[Snowflake] = UNSET,
        preferred_locale: Nullable[Locales] = UNSET,
        features: list[Guild_Features] = None,
        description: Nullable[str] = UNSET,
        safety_alerts_channel_id: Nullable[Snowflake] = UNSET,
        reason: str = None,
    ) -> Guild:
        """
        > Attempting to add or remove the COMMUNITY [guild feature](https://discord.com/developers/docs/resources/guild#guild_object_guild_features) requires the ADMINISTRATOR permission.

        Parameters
        ----------
        name:
            guild name
        region:
            Voice_Region
        verification_level:
            Verification_Level
        default_message_notifications:
            Message_Notification_Level
        explicit_content_filter:
            Explicit_Content_Filter_Level
        afk_channel_id:
            id for afk channel
        afk_timeout:
            afk timeout in seconds, can be set to: 60, 300, 900, 1800, 3600
        icon:
            base64 1024x1024 png/jpeg/gif image for the guild icon
        owner_id:
            user id to transfer guild ownership to
        splash:
            base64 16:9 png/jpeg image for the guild splash
        discovery_splash:
            base64 16:9 png/jpeg image for the guild discovery splash
        banner:
            base64 16:9 png/jpeg image for the guild banner
        system_channel_id:
            the id of the channel where guild notices such as welcome messages and boost events are posted
        system_channel_flags:
            System_Channel_Flags
        rules_channel_id:
            the id of the channel where Community guilds display rules and/or guidelines
        public_updates_channel_id:
            the id of the channel where admins and moderators of Community guilds receive notices from Discord
        preferred_locale:
            the preferred locale of a Community guild used in server discovery and notices from Discord; defaults to "en-US"
        features:
            enabled guild features
        description:
            the description for the guild
        premium_progress_bar_enabled:
            whether the guild's boost progress bar should be enabled
        safety_alerts_channel_id:
            the id of the channel where admins and moderators of Community guilds receive safety alerts from Discord
        """

    @route(method="DELETE", path="/guilds/{guild_id}")
    async def delete_guild(self, guild_id: Snowflake) -> None:
        """
        Delete a guild permanently.
        User must be owner.
        Returns `204 No Content` on success.
        Fires a [Guild Delete](https://discord.com/developers/docs/topics/gateway_events#guild_delete) Gateway event.
        """

    @route(method="GET", path="/guilds/{guild_id}/channels")
    async def get_guild_channels(self, guild_id: Snowflake) -> list[Channel]:
        """
        Returns a list of guild [channel](https://discord.com/developers/docs/resources/channel#channel_object) objects.
        Does not include threads.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="POST", path="/guilds/{guild_id}/channels")
    async def create_guild_channel(
        self,
        guild_id: Snowflake,
        name: str = None,
        type: Channel_Types = None,
        topic: str = None,
        bitrate: int = None,
        user_limit: int = None,
        rate_limit_per_user: int = None,
        position: int = None,
        permission_overwrites: list[Overwrite] = None,
        parent_id: Snowflake = None,
        nsfw: bool = None,
        rtc_region: str = None,
        video_quality_mode: Video_Quality_Modes = None,
        default_auto_archive_duration: int = None,
        default_reaction_emoji: Default_Reaction = None,
        available_tags: Forum_Tag = None,
        default_sort_order: Sort_Order_Types = None,
        default_forum_layout: Layout_Type = None,
        default_thread_rate_limit_per_user: int = None,
        reason: str = None,
    ) -> Channel:
        """
        Create a new [channel](https://discord.com/developers/docs/resources/channel#channel_object) object for the guild.
        Requires the `MANAGE_CHANNELS` permission.
        If setting permission overwrites, only permissions your bot has in the guild can be allowed/denied.
        Setting `MANAGE_ROLES` permission in channels is only possible for guild administrators.
        Returns the new [channel](https://discord.com/developers/docs/resources/channel#channel_object) object on success.
        Fires a [Channel Create](https://discord.com/developers/docs/topics/gateway_events#channel_create) Gateway event.

        Parameters
        ----------
        name:
            channel name
        type:
            Type_Of_Channel
        topic:
            channel topic
        bitrate:
            the bitrate
        user_limit:
            the user limit of the voice channel
        rate_limit_per_user:
            amount of seconds a user has to wait before sending another message
        position:
            sorting position of the channel
        permission_overwrites:
            the channel's permission overwrites
        parent_id:
            id of the parent category for a channel
        nsfw:
            whether the channel is nsfw
        rtc_region:
            Voice_Region
        video_quality_mode:
            Video_Quality_Mode
        default_auto_archive_duration:
            the default duration that the clients use
        default_reaction_emoji:
            emoji to show in the add reaction button on a thread in a `GUILD_FORUM`
        available_tags:
            set of tags that can be used in a `GUILD_FORUM`
        default_sort_order:
            Default_Sort_Order_Type
        default_forum_layout:
            Default_Forum_Layout_View
        default_thread_rate_limit_per_user:
            the initial `rate_limit_per_user` to set on newly created threads in a channel. this field is copied to the thread at creation time and does not live update.
        """

    @route(method="PATCH", path="/guilds/{guild_id}/channels")
    async def modify_guild_channel_positions(
        self,
        guild_id: Snowflake,
        id: Snowflake = None,
        position: Optional[Nullable[int]] = UNSET,
        lock_permissions: Optional[Nullable[bool]] = UNSET,
        parent_id: Optional[Nullable[Snowflake]] = UNSET,
        reason: str = None,
    ) -> None:
        """
        Modify the positions of a set of [channel](https://discord.com/developers/docs/resources/channel#channel_object) objects for the guild.
        Requires `MANAGE_CHANNELS` permission.
        Returns a 204 empty response on success.
        Fires multiple [Channel Update](https://discord.com/developers/docs/topics/gateway_events#channel_update) Gateway events.

        Parameters
        ----------
        id:
            channel id
        position:
            sorting position of the channel
        lock_permissions:
            syncs the permission overwrites with the new parent, if moving to a new category
        parent_id:
            the new parent ID for the channel that is moved
        """

    @route(method="GET", path="/guilds/{guild_id}/threads/active")
    async def list_active_guild_threads(self, guild_id: Snowflake) -> list[Channel]:
        """
        Returns all active threads in the guild, including public and private threads.
        Threads are ordered by their `id`, in descending order.
        """

    @route(method="GET", path="/guilds/{guild_id}/members/{user_id}")
    async def get_guild_member(self, guild_id: Snowflake, user_id: Snowflake) -> Guild_Member:
        """
        Returns a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) object for the specified user.
        """

    @route(method="GET", path="/guilds/{guild_id}/members")
    async def list_guild_members(
        self, guild_id: Snowflake, *, limit: int = 1, after: Snowflake = 0
    ) -> list[Guild_Member]:
        """
        > This endpoint is restricted according to whether the GUILD_MEMBERS [Privileged Intent](https://discord.com/developers/docs/topics/gateway#privileged_intents) is enabled for your application.

        Parameters
        ----------
        limit:
            max number of members to return
        after:
            the highest user id in the previous page
        """

    @route(method="GET", path="/guilds/{guild_id}/members/search")
    async def search_guild_members(
        self, guild_id: Snowflake, *, query: str = None, limit: int = 1
    ) -> list[Guild_Member]:
        """
        Returns a list of [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) objects whose username or nickname starts with a provided string.

        Parameters
        ----------
        query:
            Query string to match username
        limit:
            max number of members to return
        """

    @route(method="PUT", path="/guilds/{guild_id}/members/{user_id}")
    async def add_guild_member(
        self,
        guild_id: Snowflake,
        user_id: Snowflake,
        access_token: str = None,
        nick: str = None,
        roles: list[Snowflake] = None,
        mute: bool = None,
        deaf: bool = None,
    ) -> Optional[Guild_Member]:
        """
        For guilds with [Membership Screening](https://discord.com/developers/docs/resources/guild#membership_screening_object) enabled, this endpoint will default to adding new members as pending in the [guild member object](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Members that are pending will have to complete membership screening before they become full members that can talk.

        Parameters
        ----------
        access_token:
            an oauth2 access token granted with the `guilds.join` to the bot's application for the user you want to add to the guild
        nick:
            value to set user's nickname to
        roles:
            role ids the member is assigned
        mute:
            whether the user is muted in voice channels
        deaf:
            whether the user is deafened in voice channels
        """

    @route(method="PATCH", path="/guilds/{guild_id}/members/{user_id}")
    async def modify_guild_member(
        self,
        guild_id: Snowflake,
        user_id: Snowflake,
        nick: str = None,
        roles: list[Snowflake] = None,
        mute: bool = None,
        deaf: bool = None,
        channel_id: Nullable[Snowflake] = UNSET,
        communication_disabled_until: datetime = None,
        flags: Guild_Member_Flags = None,
        reason: str = None,
    ) -> Guild_Member:
        """
        Modify attributes of a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Returns a 200 OK with the [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) as the body.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway_events#guild_member_update) Gateway event.
        If the channel_id is set to null, this will force the target user to be disconnected from voice.

        Parameters
        ----------
        nick:
            value to set user's nickname to
        roles:
            role ids the member is assigned
        mute:
            whether the user is muted in voice channels. Will throw a 400 error if the user is not in a voice channel
        deaf:
            whether the user is deafened in voice channels. Will throw a 400 error if the user is not in a voice channel
        channel_id:
            id of channel to move user to
        communication_disabled_until:
            Timeout
        flags:
            Guild_Member_Flags
        """

    @permissions(Bitwise_Permission_Flags.CHANGE_NICKNAME)
    @route(method="PATCH", path="/guilds/{guild_id}/members/@me")
    async def modify_current_member(
        self, guild_id: Snowflake, nick: Optional[Nullable[str]] = UNSET, reason: str = None
    ) -> Guild_Member:
        """
        Modifies the current member in a guild.
        Returns a 200 with the updated member object on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway_events#guild_member_update) Gateway event.

        Parameters
        ----------
        nick:
            value to set user's nickname to
        """

    @route(method="PATCH", path="/guilds/{guild_id}/members/@me/nick")
    async def modify_current_user_nick(self, guild_id: Snowflake, nick: Nullable[str], reason: str = None) -> str:
        """
        Modifies the nickname of the current user in a guild.
        Returns a 200 with the nickname on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway_events#guild_member_update) Gateway event.

        Parameters
        ----------
        nick:
            value to set user's nickname to
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PUT", path="/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    async def add_guild_member_role(
        self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, reason: str = None
    ) -> None:
        """
        Adds a role to a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Requires the `MANAGE_ROLES` permission.
        Returns a `204 empty response` on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway_events#guild_member_update) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="DELETE", path="/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    async def remove_guild_member_role(
        self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, reason: str = None
    ) -> None:
        """
        Removes a role from a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Requires the MANAGE_ROLES permission.
        Returns a 204 empty response on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway_events#guild_member_update) Gateway event.
        """

    @route(method="DELETE", path="/guilds/{guild_id}/members/{user_id}")
    async def remove_guild_member(self, guild_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Remove a member from a guild.
        Requires KICK_MEMBERS permission.
        Returns a 204 empty response on success.
        Fires a [Guild Member Remove](https://discord.com/developers/docs/topics/gateway_events#guild_member_remove) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="GET", path="/guilds/{guild_id}/bans")
    async def get_guild_bans(
        self,
        guild_id: Snowflake,
        *,
        limit: Optional[float] = 1000,
        before: Optional[Snowflake] = UNSET,
        after: Optional[Snowflake] = UNSET,
    ) -> list[Ban]:
        """
        Returns a list of [ban](https://discord.com/developers/docs/resources/guild#ban_object) objects for the users banned from this guild.
        Requires the BAN_MEMBERS permission.

        Parameters
        ----------
        limit:
            number of users to return
        before:
            consider only users before given user id
        after:
            consider only users after given user id
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="GET", path="/guilds/{guild_id}/bans/{user_id}")
    async def get_guild_ban(self, guild_id: Snowflake, user_id: Snowflake) -> Ban:
        """
        Returns a [ban](https://discord.com/developers/docs/resources/guild#ban_object) object for the given user or a 404 not found if the ban cannot be found.
        Requires the BAN_MEMBERS permission.
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="PUT", path="/guilds/{guild_id}/bans/{user_id}")
    async def create_guild_ban(
        self,
        guild_id: Snowflake,
        user_id: Snowflake,
        delete_message_days: Optional[int] = 0,
        delete_message_seconds: Optional[int] = 0,
        reason: Optional[str] = None,
    ) -> None:
        """
        Create a guild ban, and optionally delete previous messages sent by the banned user.
        Requires the `BAN_MEMBERS` permission.
        Returns a `204 empty response` on success.
        Fires a [Guild Ban Add](https://discord.com/developers/docs/topics/gateway_events#guild_ban_add) Gateway event.

        Parameters
        ----------
        delete_message_days:
            number of days to delete messages for
        delete_message_seconds:
            number of seconds to delete messages for, between 0 and 604800
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="DELETE", path="/guilds/{guild_id}/bans/{user_id}")
    async def remove_guild_ban(self, guild_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Remove the ban for a user.
        Requires the `BAN_MEMBERS` permissions.
        Returns a `204 empty response` on success.
        Fires a [Guild Ban Remove](https://discord.com/developers/docs/topics/gateway_events#guild_ban_remove) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS, Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/bulk-ban")
    async def bulk_guild_ban(
        self, guild_id: Snowflake, user_ids: list[Snowflake] = None, delete_message_seconds: Optional[int] = 0
    ) -> dict[str, list[Snowflake]]:
        """
        Ban up to 200 users from a guild, and optionally delete previous messages sent by the banned users.
        Requires both the `BAN_MEMBERS` and `MANAGE_GUILD` permissions.
        Returns a 200 response on success, including the fields `banned_users` with the IDs of the banned users and `failed_users` with IDs that could not be banned or were already banned.

        Parameters
        ----------
        user_ids:
            list of user ids to ban
        delete_message_seconds:
            number of seconds to delete messages for, between 0 and 604800
        """

    @route(method="GET", path="/guilds/{guild_id}/roles")
    async def get_guild_roles(self, guild_id: Snowflake) -> list[Role]:
        """
        Returns a list of [role](https://discord.com/developers/docs/topics/permissions#role_object) objects for the guild.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="POST", path="/guilds/{guild_id}/roles")
    async def create_guild_role(
        self,
        guild_id: Snowflake,
        name: str = "New Role",
        permissions: Bitwise_Permission_Flags = None,
        color: int = None,
        hoist: bool = False,
        icon: Nullable[str] = UNSET,
        unicode_emoji: Nullable[str] = UNSET,
        mentionable: bool = False,
        reason: str = None,
    ) -> Role:
        """
        Create a new [role](https://discord.com/developers/docs/topics/permissions#role_object) for the guild.
        Requires the MANAGE_ROLES permission.
        Returns the new [role](https://discord.com/developers/docs/topics/permissions#role_object) object on success.
        Fires a [Guild Role Create](https://discord.com/developers/docs/topics/gateway_events#guild_role_create) Gateway event.
        All JSON params are optional.

        Parameters
        ----------
        name:
            name of the role, max 100 characters
        permissions:
            bitwise value of the enabled/disabled permissions
        color:
            RGB color value
        hoist:
            whether the role should be displayed separately in the sidebar
        icon:
            the role's icon image
        unicode_emoji:
            Standard_Emoji
        mentionable:
            whether the role should be mentionable
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PATCH", path="/guilds/{guild_id}/roles")
    async def modify_guild_role_positions(
        self, guild_id: Snowflake, id: Snowflake = None, position: Nullable[int] = UNSET, reason: str = None
    ) -> list[Role]:
        """
        Modify the positions of a set of [role](https://discord.com/developers/docs/topics/permissions#role_object) objects for the guild.
        Requires the `MANAGE_ROLES` permission.
        Returns a list of all of the guild's [role](https://discord.com/developers/docs/topics/permissions#role_object) objects on success.
        Fires multiple [Guild Role Update](https://discord.com/developers/docs/topics/gateway_events#guild_role_update) Gateway events.

        Parameters
        ----------
        id:
            role
        position:
            sorting position of the role
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PATCH", path="/guilds/{guild_id}/roles/{role_id}")
    async def modify_guild_role(
        self,
        guild_id: Snowflake,
        role_id: Snowflake,
        name: str = None,
        permissions: str = None,
        color: int = None,
        hoist: bool = None,
        icon: str = None,
        unicode_emoji: str = None,
        mentionable: bool = None,
        reason: str = None,
    ) -> Role:
        """
        Modify a guild role.
        Requires the `MANAGE_ROLES` permission.
        Returns the updated [role](https://discord.com/developers/docs/topics/permissions#role_object) on success.
        Fires a [Guild Role Update](https://discord.com/developers/docs/topics/gateway_events#guild_role_update) Gateway event.

        Parameters
        ----------
        name:
            name of the role, max 100 characters
        permissions:
            bitwise value of the enabled/disabled permissions
        color:
            RGB color value
        hoist:
            whether the role should be displayed separately in the sidebar
        icon:
            the role's icon image
        unicode_emoji:
            Standard_Emoji
        mentionable:
            whether the role should be mentionable
        """

    @route(method="POST", path="/guilds/{guild_id}/mfa")
    async def modify_guild_mfa_level(self, guild_id: Snowflake, level: MFA_Level = None) -> MFA_Level:
        """
        Modify a guild's MFA level.
        Requires guild ownership.
        Returns the updated [level](https://discord.com/developers/docs/resources/guild#guild_object_mfa_level) on success.
        Fires a [Guild Update](https://discord.com/developers/docs/topics/gateway_events#guild_update) Gateway event.

        Parameters
        ----------
        level:
            MFA_Level
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="DELETE", path="/guilds/{guild_id}/roles/{role_id}")
    async def delete_guild_role(self, guild_id: Snowflake, role_id: Snowflake, reason: str = None) -> None:
        """
        Delete a guild role.
        Requires the `MANAGE_ROLES` permission.
        Returns a 204 empty response on success.
        Fires a [Guild Role Delete](https://discord.com/developers/docs/topics/gateway_events#guild_role_delete) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD, Bitwise_Permission_Flags.KICK_MEMBERS)
    @route(method="GET", path="/guilds/{guild_id}/prune")
    async def get_guild_prune_count(
        self, guild_id: Snowflake, *, days: int = 7, include_roles: list[Snowflake] = None
    ) -> dict[str, int]:
        """
        Returns an object with one `pruned` key indicating the number of members that would be removed in a prune operation.
        Requires the `MANAGE_GUILD` and `KICK_MEMBERS` permissions.

        Parameters
        ----------
        days:
            number of days to count prune for
        include_roles:
            role
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD, Bitwise_Permission_Flags.KICK_MEMBERS)
    @route(method="POST", path="/guilds/{guild_id}/prune")
    async def begin_guild_prune(
        self,
        guild_id: Snowflake,
        days: int = 7,
        compute_prune_count: bool = True,
        include_roles: list[Snowflake] = None,
        reason: Optional[str] = None,
    ):
        """
        Begin a prune operation.
        Requires the `MANAGE_GUILD` and `KICK_MEMBERS` permissions.
        Returns an object with one `pruned` key indicating the number of members that were removed in the prune operation.
        For large guilds it's recommended to set the compute_prune_count option to false, forcing pruned to null.
        Fires multiple [Guild Member Remove](https://discord.com/developers/docs/topics/gateway_events#guild_member_remove) Gateway events.

        Parameters
        ----------
        days:
            number of days to prune
        compute_prune_count:
            whether `pruned` is returned, discouraged for large guilds
        include_roles:
            role
        reason:
            reason for the prune
        """

    @route(method="GET", path="/guilds/{guild_id}/regions")
    async def get_guild_voice_regions(self, guild_id: Snowflake) -> list[Voice_Region]:
        """
        Returns a list of [voice region](https://discord.com/developers/docs/resources/voice#voice_region_object) objects for the guild.
        Unlike the similar /voice route, this returns VIP servers when the guild is VIP_enabled.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/invites")
    async def get_guild_invites(self, guild_id: Snowflake) -> list[Invite]:
        """
        Returns a list of [invite](https://discord.com/developers/docs/resources/invite#invite_object) objects (with [invite metadata](https://discord.com/developers/docs/resources/invite#invite_metadata_object)) for the guild.
        Requires the MANAGE_GUILD permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/integrations")
    async def get_guild_integrations(self, guild_id: Snowflake) -> list[Integration]:
        """
        Returns a list of [integration](https://discord.com/developers/docs/resources/guild#integration_object) objects for the guild.
        Requires the MANAGE_GUILD permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/integrations")
    async def create_guild_integration(self, guild_id: Snowflake, type: str, id: Snowflake) -> None:
        """
        Attach an [integration](https://discord.com/developers/docs/resources/guild#integration-object) object from the current user to the guild. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success. Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild-integrations-update) Gateway event.

        Params:
            :type: the integration type
            :id: the integration id
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/integrations")
    async def modify_guild_integration(
        self,
        guild_id: Snowflake,
        integration_id: Snowflake,
        expire_behavior: int = None,
        expire_grace_period: int = None,
        enable_emoticons: bool = None,
    ) -> None:
        """
        Modify the behavior and settings of an [integration](https://discord.com/developers/docs/resources/guild#integration-object) object for the guild. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success. Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild-integrations-update) Gateway event.
        > info
        > All parameters to this endpoint are optional and nullable.

        Params:
            :expire_behavior: Integration_Expire_Behaviors
            :expire_grace_period: period
            :enable_emoticons: whether emoticons should be synced for this integration
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="DELETE", path="/guilds/{guild_id}/integrations/{integration_id}")
    async def delete_guild_integration(
        self, guild_id: Snowflake, integration_id: Snowflake, reason: str = None
    ) -> None:
        """
        Delete the attached [integration](https://discord.com/developers/docs/resources/guild#integration_object) object for the guild.
        Deletes any associated webhooks and kicks the associated bot if there is one.
        Requires the `MANAGE_GUILD` permission.
        Returns a 204 empty response on success.
        Fires [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway_events#guild_integrations_update) and [Integration Delete](https://discord.com/developers/docs/topics/gateway_events#integration_delete) Gateway events.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/integrations/{integration_id}/sync")
    async def sync_guild_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> None:
        """Syncs guidl integrations"""

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/widget")
    async def get_guild_widget_settings(self, guild_id: Snowflake) -> Guild_Widget_Settings:
        """
        Returns a [guild widget settings](https://discord.com/developers/docs/resources/guild#guild_widget_settings_object) object.
        Requires the `MANAGE_GUILD` permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/widget")
    async def modify_guild_widget(
        self, guild_id: Snowflake, guild_widget: Guild_Widget_Settings, reason: str = None
    ) -> Guild_Widget_Settings:
        """
        Modify a [guild widget settings](https://discord.com/developers/docs/resources/guild#guild_widget_settings_object) object for the guild.
        All attributes may be passed in with JSON and modified.
        Requires the `MANAGE_GUILD` permission.
        Returns the updated [guild widget settings](https://discord.com/developers/docs/resources/guild#guild_widget_settings_object) object.
        Fires a [Guild Update](https://discord.com/developers/docs/topics/gateway_events#guild_update) Gateway event.
        """

    @route(method="GET", path="/guilds/{guild_id}/widget.json")
    async def get_guild_widget(self, guild_id: Snowflake) -> Guild_Widget:
        """
        Returns the [widget](https://discord.com/developers/docs/resources/guild#guild_widget_object) for the guild.
        Fires an [Invite Create](https://discord.com/developers/docs/topics/gateway_events#invite_create) Gateway event when an invite channel is defined and a new [Invite](https://discord.com/developers/docs/resources/invite#invite_object) is generated.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/vanity-url")
    async def get_guild_vanity_url(self, guild_id: Snowflake) -> Invite:
        """
        Returns a partial [invite](https://discord.com/developers/docs/resources/invite#invite_object) object for guilds with that feature enabled.
        Requires the `MANAGE_GUILD` permission.
        `code` will be null if a vanity url for the guild is not set.
        """

    @route(method="GET", path="/guilds/{guild_id}/widget.png")
    async def get_guild_widget_image(self, guild_id: Snowflake, *, style: str = "shield") -> bytes:
        """
        Returns a PNG image widget for the guild.
        Requires no permissions or authentication.
        Widget Style Options
        | Value   | Description                                                                                                                                                    | Example                                                                              |
        |---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
        | shield  | shield style widget with Discord icon and guild members online count                                                                                           | [Example](https:#/discord.com/api/guilds/81384788765712384/widget.png?style=shield)  |
        | banner1 | large image with guild icon, name and online count.
        'POWERED BY DISCORD' as the footer of the widget                                                           | [Example](https:#/discord.com/api/guilds/81384788765712384/widget.png?style=banner1) |
        | banner2 | smaller widget style with guild icon, name and online count.
        Split on the right with Discord logo                                                              | [Example](https:#/discord.com/api/guilds/81384788765712384/widget.png?style=banner2) |
        | banner3 | large image with guild icon, name and online count.
        In the footer, Discord logo on the left and 'Chat Now' on the right                                        | [Example](https:#/discord.com/api/guilds/81384788765712384/widget.png?style=banner3) |
        | banner4 | large Discord logo at the top of the widget.
        Guild icon, name and online count in the middle portion of the widget and a 'JOIN MY SERVER' button at the bottom | [Example](https:#/discord.com/api/guilds/81384788765712384/widget.png?style=banner4) |.

        Parameters
        ----------
        style:
            style of the widget image returned
        """

    @route(method="GET", path="/guilds/{guild_id}/welcome-screen")
    async def get_guild_welcome_screen(self, guild_id: Snowflake) -> Welcome_Screen:
        """
        Returns the [Welcome Screen](https://discord.com/developers/docs/resources/guild#welcome_screen_object) object for the guild.
        If the welcome screen is not enabled, the `MANAGE_GUILD` permission is required.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/welcome-screen")
    async def modify_guild_welcome_screen(
        self,
        guild_id: Snowflake,
        enabled: bool = None,
        welcome_channels: list[Welcome_Screen_Channel] = None,
        description: str = None,
    ) -> Welcome_Screen:
        """
        Modify the guild's [Welcome Screen](https://discord.com/developers/docs/resources/guild#welcome_screen_object).
        Requires the `MANAGE_GUILD` permission.
        Returns the updated [Welcome Screen](https://discord.com/developers/docs/resources/guild#welcome_screen_object) object.
        May fire a [Guild Update](https://discord.com/developers/docs/topics/gateway_events#guild_update) Gateway event.

        Parameters
        ----------
        enabled:
            whether the welcome screen is enabled
        welcome_channels:
            channels linked in the welcome screen and their display options
        description:
            the server description to show in the welcome screen
        """

    @route(method="GET", path="/guilds/{guild_id}/onboarding")
    async def get_guild_onboarding(self, guild_id: Snowflake) -> Guild_Onboarding:
        """
        Returns the [Onboarding](https://discord.com/developers/docs/resources/guild#guild_onboarding_object) object for the guild.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD, Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PUT", path="/guilds/{guild_id}/onboarding")
    async def modify_guild_onboarding(
        self,
        guild_id: Snowflake,
        prompts: list[Onboarding_Prompt] = None,
        default_channel_ids: list[Snowflake] = None,
        enabled: bool = None,
        mode: Onboarding_Mode = None,
    ) -> Guild_Onboarding:
        """
        Modifies the onboarding configuration of the guild.
        Returns a 200 with the [Onboarding](https://discord.com/developers/docs/resources/guild#guild_onboarding_object) object for the guild.
        Requires the `MANAGE_GUILD` and `MANAGE_ROLES` permissions.

        Parameters
        ----------
        prompts:
            Prompts shown during onboarding and in customize community
        default_channel_ids:
            Channel IDs that members get opted into automatically
        enabled:
            Whether onboarding is enabled in the guild
        mode:
            Current mode of onboarding
        """

    @route(method="PATCH", path="/guilds/{guild_id}/voice-states/@me")
    async def modify_current_user_voice_state(
        self,
        guild_id: Snowflake,
        channel_id: Optional[Snowflake] = None,
        suppress: Optional[bool] = None,
        request_to_speak_timestamp: Optional[Nullable[datetime]] = UNSET,
        reason: str = None,
    ) -> None:
        """
        Updates the current user's voice state.
        Returns `204 No Content` on success.
        Fires a [Voice State Update](https://discord.com/developers/docs/topics/gateway_events#voice_state_update) Gateway event.

        Caveats
        There are currently several caveats for this endpoint:
        - `channel_id` must currently point to a stage channel.
        - current user must already have joined `channel_id`.
        - You must have the `MUTE_MEMBERS` permission to unsuppress yourself.
        You can always suppress yourself.
        - You must have the `REQUEST_TO_SPEAK` permission to request to speak.
        You can always clear your own request to speak.
        - You are able to set `request_to_speak_timestamp` to any present or future time.

        Parameters
        ----------
        channel_id:
            the id of the channel the user is currently in
        suppress:
            toggles the user's suppress state
        request_to_speak_timestamp:
            sets the user's request to speak
        """

    @route(method="PATCH", path="/guilds/{guild_id}/voice-states/{user_id}")
    async def modify_user_voice_state(
        self,
        guild_id: Snowflake,
        user_id: Snowflake,
        channel_id: Snowflake = None,
        suppress: Optional[bool] = None,
        reason: str = None,
    ) -> None:
        """
        Updates another user's voice state.
        Fires a [Voice State Update](https://discord.com/developers/docs/topics/gateway_events#voice_state_update) Gateway event.

        Caveats
        There are currently several caveats for this endpoint:
        - `channel_id` must currently point to a stage channel.
        - User must already have joined `channel_id`.
        - You must have the `MUTE_MEMBERS` permission.
        (Since suppression is the only thing that is available currently.)
        - When unsuppressed, non-bot users will have their `request_to_speak_timestamp` set to the current time.
        Bot users will not.
        - When suppressed, the user will have their `request_to_speak_timestamp` removed.

        Parameters
        ----------
        channel_id:
            the id of the channel the user is currently in
        suppress:
            toggles the user's suppress state
        """

    @route(method="GET", path="/guilds/{guild_id}/scheduled-events")
    async def list_scheduled_events_for_guild(
        self, guild_id: Snowflake, *, with_user_count: Optional[bool] = None
    ) -> list[Guild_Scheduled_Event]:
        """
        Returns a list of [guild scheduled event](https://discord.com/developers/docs/resources/guild_scheduled_event#guild_scheduled_event_object) objects for the given guild.

        Parameters
        ----------
        with_user_count:
            include number of users subscribed to each event
        """

    @route(method="POST", path="/guilds/{guild_id}/scheduled-events")
    async def create_guild_scheduled_event(
        self,
        guild_id: Snowflake,
        channel_id: Snowflake = None,
        entity_metadata: Guild_Scheduled_Event_Entity_Metadata = None,
        name: str = None,
        privacy_level: Privacy_Level = None,
        scheduled_start_time: datetime = None,
        scheduled_end_time: datetime = None,
        entity_type: Guild_Scheduled_Event_Entity_Types = None,
        description: Optional[str] = None,
        image: Optional[str] = None,
    ) -> Guild_Scheduled_Event:
        """
        Create a guild scheduled event in the guild.
        Returns a [guild scheduled event](https://discord.com/developers/docs/resources/guild_scheduled_event#guild_scheduled_event_object) object on success.
        Fires a [Guild Scheduled Event Create](https://discord.com/developers/docs/topics/gateway_events#guild_scheduled_event_create) Gateway event.

        Parameters
        ----------
        channel_id:
            the channel id of the scheduled event.
        entity_metadata:
            the entity metadata of the scheduled event
        name:
            the name of the scheduled event
        privacy_level:
            the privacy level of the scheduled event
        scheduled_start_time:
            the time to schedule the scheduled event
        scheduled_end_time:
            the time when the scheduled event is scheduled to end
        entity_type:
            the entity type of the scheduled event
        description:
            the description of the scheduled event
        image:
            the cover image of the scheduled event
        """

    @route(method="GET", path="/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}")
    async def get_guild_scheduled_event(
        self, guild_id: Snowflake, guild_scheduled_event_id: str, *, with_user_count: Optional[bool] = None
    ) -> Guild_Scheduled_Event:
        """
        Get a guild scheduled event.
        Returns a [guild scheduled event](https://discord.com/developers/docs/resources/guild_scheduled_event#guild_scheduled_event_object) object on success.

        Parameters
        ----------
        with_user_count:
            include number of users subscribed to this event
        """

    @route(method="PATCH", path="/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}")
    async def modify_guild_scheduled_event(
        self,
        guild_id: Snowflake,
        guild_scheduled_event_id: str,
        scheduled_end_time: datetime = None,
        entity_type: Guild_Scheduled_Event_Entity_Types = None,
        channel_id: Nullable[Snowflake] = UNSET,
        entity_metadata: Optional[Nullable[Guild_Scheduled_Event_Entity_Metadata]] = UNSET,
        name: Optional[str] = None,
        privacy_level: Optional[Privacy_Level] = None,
        scheduled_start_time: Optional[datetime] = None,
        description: Optional[Nullable[str]] = UNSET,
        status: Optional[Guild_Scheduled_Event_Status] = None,
        image: Optional[str] = None,
    ) -> Guild_Scheduled_Event:
        """
        > To start or end an event, use this endpoint to modify the event's [status](https://discord.com/developers/docs/resources/guild_scheduled_event#guild_scheduled_event_object_guild_scheduled_event_status) field.

        Parameters
        ----------
        scheduled_end_time:
            the time when the scheduled event is scheduled to end
        entity_type:
            the entity type of the scheduled event
        channel_id:
            the channel id of the scheduled event, set to `null` if changing entity type to `EXTERNAL`
        entity_metadata:
            the entity metadata of the scheduled event
        name:
            the name of the scheduled event
        privacy_level:
            the privacy level of the scheduled event
        scheduled_start_time:
            the time to schedule the scheduled event
        description:
            the description of the scheduled event
        status:
            the status of the scheduled event
        image:
            the cover image of the scheduled event
        """

    @route(method="DELETE", path="/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}")
    async def delete_guild_scheduled_event(
        self, guild_id: Snowflake, guild_scheduled_event_id: str, reason: str = None
    ) -> None:
        """
        Delete a guild scheduled event.
        Returns a 204 on success.
        Fires a [Guild Scheduled Event Delete](https://discord.com/developers/docs/topics/gateway_events#guild_scheduled_event_delete) Gateway event.
        """

    @route(method="GET", path="/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}/users")
    async def get_guild_scheduled_event_users(
        self,
        guild_id: Snowflake,
        guild_scheduled_event_id: str,
        *,
        limit: Optional[float] = 100,
        with_member: Optional[bool] = False,
        before: Snowflake = "null",
        after: Snowflake = "null",
    ) -> Guild_Scheduled_Event_User:
        """
        Get a list of guild scheduled event users subscribed to a guild scheduled event.
        Returns a list of [guild scheduled event user](https://discord.com/developers/docs/resources/guild_scheduled_event#guild_scheduled_event_user_object) objects on success.
        Guild member data, if it exists, is included if the with_member query parameter is set.

        Parameters
        ----------
        limit:
            number of users to return
        with_member:
            include guild member data if it exists
        before:
            consider only users before given user id
        after:
            consider only users after given user id
        """

    @route(method="GET", path="/guilds/templates/{template_code}")
    async def get_guild_template(self, template_code: str) -> Guild_Template:
        """
        Returns a [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) object for the given code.
        """

    @route(method="POST", path="/guilds/templates/{template_code}")
    async def create_guild_from_guild_template(
        self, template_code: str, name: str = None, icon: Optional[str] = None
    ) -> Guild:
        """
        Create a new guild based on a template.
        Returns a [guild](https://discord.com/developers/docs/resources/guild#guild_object) object on success.
        Fires a [Guild Create](https://discord.com/developers/docs/topics/gateway_events#guild_create) Gateway event.

        Parameters
        ----------
        name:
            name of the guild
        icon:
            base64 128x128 image for the guild icon
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/templates")
    async def get_guild_templates(self, guild_id: Snowflake) -> Guild_Template:
        """
        Returns an array of [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) objects.
        Requires the `MANAGE_GUILD` permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/templates")
    async def create_guild_template(
        self, guild_id: Snowflake, name: str = None, description: Optional[Nullable[str]] = UNSET
    ) -> Guild_Template:
        """
        Creates a template for the guild.
        Requires the `MANAGE_GUILD` permission.
        Returns the created [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) object on success.

        Parameters
        ----------
        name:
            name of the template
        description:
            description for the template
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PUT", path="/guilds/{guild_id}/templates/{template_code}")
    async def sync_guild_template(self, guild_id: Snowflake, template_code: str) -> Guild_Template:
        """
        Syncs the template to the guild's current state.
        Requires the `MANAGE_GUILD` permission.
        Returns the [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) object on success.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/templates/{template_code}")
    async def modify_guild_template(
        self,
        guild_id: Snowflake,
        template_code: str,
        name: Optional[str] = None,
        description: Optional[Nullable[str]] = UNSET,
    ) -> Guild_Template:
        """
        Modifies the template's metadata.
        Requires the `MANAGE_GUILD` permission.
        Returns the [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) object on success.

        Parameters
        ----------
        name:
            name of the template
        description:
            description for the template
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="DELETE", path="/guilds/{guild_id}/templates/{template_code}")
    async def delete_guild_template(self, guild_id: Snowflake, template_code: str) -> Guild_Template:
        """
        Deletes the template.
        Requires the `MANAGE_GUILD` permission.
        Returns the deleted [guild template](https://discord.com/developers/docs/resources/guild_template#guild_template_object) object on success.
        """

    @route(method="GET", path="/invites/{invite_code}")
    async def get_invite(
        self,
        invite_code: str,
        *,
        with_counts: Optional[bool] = None,
        with_expiration: Optional[bool] = None,
        guild_scheduled_event_id: Optional[Snowflake] = None,
    ) -> Invite:
        """
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite_object) object for the given code.

        Parameters
        ----------
        with_counts:
            whether the invite should contain approximate member counts
        with_expiration:
            whether the invite should contain the expiration date
        guild_scheduled_event_id:
            the guild scheduled event to include with the invite
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="DELETE", path="/invites/{invite_code}")
    async def delete_invite(self, invite_code: str, reason: str = None) -> Invite:
        """
        Delete an invite.
        Requires the MANAGE_CHANNELS permission on the channel this invite belongs to, or MANAGE_GUILD to remove any invite across the guild.
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite_object) object on success.
        Fires an [Invite Delete](https://discord.com/developers/docs/topics/gateway_events#invite_delete) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/polls/{message_id}/answers/{answer_id}")
    async def get_answer_voters(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        answer_id: str,
        *,
        after: Optional[Snowflake] = None,
        limit: Optional[int] = 25,
    ) -> list[Poll_Answer]:
        """
        Get a list of users that voted for this specific answer.

        Parameters
        ----------
        after:
            Get users after this user ID
        limit:
            Max number of users to return
        """

    @route(method="POST", path="/channels/{channel_id}/polls/{message_id}/expire")
    async def end_poll(self, channel_id: Snowflake, message_id: Snowflake) -> Message:
        """
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object.
        Fires a [Message Update](https://discord.com/developers/docs/topics/gateway_events#message_update) Gateway event.
        Immediately ends the poll.
        You cannot end polls from other users.
        """

    @route(method="POST", path="/stage-instances")
    async def create_stage_instance(
        self,
        channel_id: Snowflake = None,
        topic: str = None,
        send_start_notification: bool = None,
        privacy_level: Optional[Privacy_Level] = None,
        guild_scheduled_event_id: Optional[Snowflake] = None,
        reason: str = None,
    ) -> Stage_Instance:
        """
        Creates a new Stage instance associated to a Stage channel.
        Returns that [Stage instance](https://discord.com/developers/docs/resources/stage_instance#stage_instance_object_stage_instance_structure).
        Fires a [Stage Instance Create](https://discord.com/developers/docs/topics/gateway_events#stage_instance_create) Gateway event.

        Parameters
        ----------
        channel_id:
            The id of the Stage channel
        topic:
            The topic of the Stage instance
        send_start_notification:
            Notify @everyone that a Stage instance has started
        privacy_level:
            Privacy_Level
        guild_scheduled_event_id:
            The guild scheduled event associated with this Stage instance
        """

    @route(method="GET", path="/stage-instances/{channel_id}")
    async def get_stage_instance(self, channel_id: Snowflake) -> Stage_Instance:
        """
        Gets the stage instance associated with the Stage channel, if it exists.
        """

    @route(method="PATCH", path="/stage-instances/{channel_id}")
    async def modify_stage_instance(
        self,
        channel_id: Snowflake,
        topic: Optional[str] = None,
        privacy_level: Optional[Privacy_Level] = None,
        reason: str = None,
    ) -> Stage_Instance:
        """
        Updates fields of an existing Stage instance.
        Returns the updated [Stage instance](https://discord.com/developers/docs/resources/stage_instance#stage_instance_object_stage_instance_structure).
        Fires a [Stage Instance Update](https://discord.com/developers/docs/topics/gateway_events#stage_instance_update) Gateway event.

        Parameters
        ----------
        topic:
            The topic of the Stage instance
        privacy_level:
            Privacy_Level
        """

    @route(method="DELETE", path="/stage-instances/{channel_id}")
    async def delete_stage_instance(self, channel_id: Snowflake, reason: str = None) -> None:
        """
        Deletes the Stage instance.
        Returns `204 No Content`.
        Fires a [Stage Instance Delete](https://discord.com/developers/docs/topics/gateway_events#stage_instance_delete) Gateway event.
        """

    @route(method="GET", path="/stickers/{sticker_id}")
    async def get_sticker(self, sticker_id: Snowflake) -> Sticker:
        """
        Returns a [sticker](https://discord.com/developers/docs/resources/sticker#sticker_object) object for the given sticker ID.
        """

    @route(method="GET", path="/sticker-packs")
    async def list_sticker_packs(self) -> list[Sticker_Pack]:
        """
        Returns a list of available sticker packs.
        """

    @route(method="GET", path="/guilds/{guild_id}/stickers")
    async def list_guild_stickers(self, guild_id: Snowflake) -> list[Sticker]:
        """
        Returns an array of [sticker](https://discord.com/developers/docs/resources/sticker#sticker_object) objects for the given guild.
        Includes user fields if the bot has the CREATE_GUILD_EXPRESSIONS or MANAGE_GUILD_EXPRESSIONS permission.
        """

    @route(method="GET", path="/guilds/{guild_id}/stickers/{sticker_id}")
    async def get_guild_sticker(self, guild_id: Snowflake, sticker_id: str) -> Sticker:
        """
        Returns a [sticker](https://discord.com/developers/docs/resources/sticker#sticker_object) object for the given guild and sticker IDs.
        Includes the user field if the bot has the CREATE_GUILD_EXPRESSIONS or MANAGE_GUILD_EXPRESSIONS permission.
        """

    @route(method="POST", path="/guilds/{guild_id}/stickers", json_as_form_data=True)
    async def create_guild_sticker(
        self, guild_id: Snowflake, name: str, description: str, tags: str, file: bytes
    ) -> Sticker:
        """
        > Lottie stickers can only be uploaded on guilds that have either the VERIFIED and/or the PARTNERED [guild feature](https://discord.com/developers/docs/resources/guild#guild_object_guild_features).

        Form Params
        | Field       | Type          | Description                                                                            |
        |-------------|---------------|----------------------------------------------------------------------------------------|
        | name        | string        | name of the sticker (2-30 characters)                                                  |
        | description | string        | description of the sticker (empty or 2-100 characters)                                 |
        | tags        | string        | autocomplete/suggestion tags for the sticker (max 200 characters)                      |
        | file        | file contents | the sticker file to upload, must be a PNG, APNG, GIF, or Lottie JSON file, max 512 KiB |.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD_EXPRESSIONS)
    @route(method="PATCH", path="/guilds/{guild_id}/stickers/{sticker_id}")
    async def modify_guild_sticker(
        self,
        guild_id: Snowflake,
        sticker_id: str,
        name: str = None,
        tags: str = None,
        description: Nullable[str] = UNSET,
    ) -> Sticker:
        """
        Modify the given sticker.
        For stickers created by the current user, requires either the CREATE_GUILD_EXPRESSIONS or MANAGE_GUILD_EXPRESSIONS permission.
        For other stickers, requires the MANAGE_GUILD_EXPRESSIONS permission.
        Returns the updated [sticker](https://discord.com/developers/docs/resources/sticker#sticker_object) object on success.
        Fires a [Guild Stickers Update](https://discord.com/developers/docs/topics/gateway_events#guild_stickers_update) Gateway event.

        Parameters
        ----------
        name:
            name of the sticker
        tags:
            autocomplete/suggestion tags for the sticker
        description:
            description of the sticker
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD_EXPRESSIONS)
    @route(method="DELETE", path="/guilds/{guild_id}/stickers/{sticker_id}")
    async def delete_guild_sticker(self, guild_id: Snowflake, sticker_id: str, reason: str = None) -> None:
        """
        Delete the given sticker.
        For stickers created by the current user, requires either the `CREATE_GUILD_EXPRESSIONS` or `MANAGE_GUILD_EXPRESSIONS` permission.
        For other stickers, requires the `MANAGE_GUILD_EXPRESSIONS` permission.
        Returns `204 No Content` on success.
        Fires a [Guild Stickers Update](https://discord.com/developers/docs/topics/gateway_events#guild_stickers_update) Gateway event.
        """

    @route(method="GET", path="/users/@me")
    async def get_current_user(self) -> User:
        """
        Returns the [user](https://discord.com/developers/docs/resources/user#user_object) object of the requester's account.
        For OAuth2, this requires the identify scope, which will return the object _without_ an email, and optionally the email scope, which returns the object _with_ an email.
        """

    @route(method="GET", path="/users/{user_id}")
    async def get_user(self, user_id: Snowflake) -> User:
        """
        Returns a [user](https://discord.com/developers/docs/resources/user#user_object) object for a given user ID.
        """

    @route(method="PATCH", path="/users/@me")
    async def modify_current_user(
        self, username: str = None, avatar: Nullable[str] = UNSET, banner: Nullable[str] = UNSET
    ) -> User:
        """
        Modify the requester's user account settings.
        Returns a [user](https://discord.com/developers/docs/resources/user#user_object) object on success.
        Fires a [User Update](https://discord.com/developers/docs/topics/gateway_events#user_update) Gateway event.

        Parameters
        ----------
        username:
            user's username, if changed may cause the user's discriminator to be randomized.
        avatar:
            if passed, modifies the user's avatar
        banner:
            if passed, modifies the user's banner
        """

    @route(method="GET", path="/users/@me/guilds")
    async def get_current_user_guilds(
        self, *, before: Snowflake = None, after: Snowflake = None, limit: int = 200, with_counts: bool = False
    ) -> list[Guild]:
        """
        Returns a list of partial [guild](https://discord.com/developers/docs/resources/guild#guild_object) objects the current user is a member of.
        For OAuth2, requires the guilds scope.

        > info
        > This endpoint returns 200 guilds by default, which is the maximum number of guilds a non-bot user can join.
        Therefore, pagination is **not needed** for integrations that need to get a list of the users' guilds.

        Parameters
        ----------
        before:
            get guilds before this guild ID
        after:
            get guilds after this guild ID
        limit:
            max number of guilds to return
        with_counts:
            include approximate member and presence counts in response
        """

    @route(method="GET", path="/users/@me/guilds/{guild_id}/member")
    async def get_current_user_guild_member(self, guild_id: Snowflake) -> Guild_Member:
        """
        Returns a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) object for the current user.
        Requires the guilds.members.read OAuth2 scope.
        """

    @route(method="DELETE", path="/users/@me/guilds/{guild_id}")
    async def leave_guild(self, guild_id: Snowflake) -> None:
        """
        Leave a guild.
        Returns a `204 empty response` on success.
        Fires a [Guild Delete](https://discord.com/developers/docs/topics/gateway_events#guild_delete) Gateway event and a [Guild Member Remove](https://discord.com/developers/docs/topics/gateway_events#guild_member_remove) Gateway event.
        """

    @route(method="POST", path="/users/@me/channels")
    async def create_dm(self, recipient_id: Snowflake = None) -> Channel:
        """
        Create a new DM channel with a user.
        Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel_object) object (if one already exists, it will be returned instead).

        Parameters
        ----------
        recipient_id:
            the recipient to open a DM channel with
        """

    @route(method="POST", path="/users/@me/channels")
    async def create_group_dm(self, access_tokens: list[str] = None, nicks: dict[Snowflake, str] = None) -> Channel:
        """
        Create a new group DM channel with multiple users.
        Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel_object) object.
        This endpoint was intended to be used with the now_deprecated GameBridge SDK.
        Fires a [Channel Create](https://discord.com/developers/docs/topics/gateway_events#channel_create) Gateway event.

        Parameters
        ----------
        access_tokens:
            access tokens of users that have granted your app the `gdm.join` scope
        nicks:
            a dictionary of user ids to their respective nicknames
        """

    @route(method="GET", path="/users/@me/connections")
    async def get_current_user_connections(self) -> list[Connection]:
        """
        Returns a list of [connection](https://discord.com/developers/docs/resources/user#connection_object) objects.
        Requires the `connections` OAuth2 scope.
        """

    @route(method="GET", path="/users/@me/applications/{application_id}/role-connection")
    async def get_current_user_application_role_connection(
        self, application_id: Snowflake
    ) -> Application_Role_Connection:
        """
        Returns the [application role connection](https://discord.com/developers/docs/resources/user#application_role_connection_object) for the user.
        Requires an OAuth2 access token with role_connections.write scope for the application specified in the path.
        """

    @route(method="PUT", path="/users/@me/applications/{application_id}/role-connection")
    async def update_current_user_application_role_connection(
        self,
        application_id: Snowflake,
        platform_name: Optional[str] = None,
        platform_username: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Application_Role_Connection:
        """
        Updates and returns the [application role connection](https://discord.com/developers/docs/resources/user#application_role_connection_object) for the user.
        Requires an OAuth2 access token with role_connections.write scope for the application specified in the path.

        Parameters
        ----------
        platform_name:
            the vanity name of the platform a bot has connected
        platform_username:
            the username on the platform a bot has connected
        metadata:
            Application_Role_Connection_Metadata
        """

    @route(method="GET", path="/voice/regions")
    async def list_voice_regions(self) -> list[Voice_Region]:
        """
        Returns an array of [voice region](https://discord.com/developers/docs/resources/voice#voice_region_object) objects that can be used when setting a voice or stage channel's [rtc_region](https://discord.com/developers/docs/resources/channel#channel_object_channel_structure).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="POST", path="/channels/{channel_id}/webhooks")
    async def create_webhook(
        self, channel_id: Snowflake, name: str = None, avatar: Optional[Nullable[str]] = UNSET, reason: str = None
    ) -> Webhook:
        """
        Create a new webhook.
        Name follows the nickname guidelines in the [Usernames and Nicknames](https://discord.com/developers/docs/resources/user#usernames_and_nicknames) documentation, with an exception that webhook names can be up to 80 characters.

        Parameters
        ----------
        name:
            name of the webhook
        avatar:
            image for the default webhook avatar
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="GET", path="/channels/{channel_id}/webhooks")
    async def get_channel_webhooks(self, channel_id: Snowflake) -> list[Webhook]:
        """
        Returns a list of channel [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) objects.
        Requires the `MANAGE_WEBHOOKS` permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="GET", path="/guilds/{guild_id}/webhooks")
    async def get_guild_webhooks(self, guild_id: Snowflake) -> list[Webhook]:
        """
        Returns a list of guild [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) objects.
        Requires the `MANAGE_WEBHOOKS` permission.
        """

    @route(method="GET", path="/webhooks/{webhook_id}")
    async def get_webhook(self, webhook_id: Snowflake) -> Webhook:
        """
        Returns the new [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) object for the given id.
        """

    @route(method="GET", path="/webhooks/{webhook_id}/{webhook_token}")
    async def get_webhook_with_token(self, webhook_id: Snowflake, webhook_token: str) -> Webhook:
        """
        Same as above, except this call does not require authentication and returns no user in the webhook object.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="PATCH", path="/webhooks/{webhook_id}")
    async def modify_webhook(
        self,
        webhook_id: Snowflake,
        name: str = None,
        avatar: Nullable[str] = UNSET,
        channel_id: Snowflake = None,
        reason: str = None,
    ) -> Webhook:
        """
        Modify a webhook.
        Requires the `MANAGE_WEBHOOKS` permission.
        Returns the updated [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) object on success.
        Fires a [Webhooks Update](https://discord.com/developers/docs/topics/gateway_events#webhooks_update) Gateway event.

        Parameters
        ----------
        name:
            the default name of the webhook
        avatar:
            image for the default webhook avatar
        channel_id:
            the new channel id this webhook should be moved to
        """

    @route(method="PATCH", path="/webhooks/{webhook_id}/{webhook_token}")
    async def modify_webhook_with_token(
        self,
        webhook_id: Snowflake,
        webhook_token: str,
        name: str = None,
        avatar: Nullable[str] = UNSET,
        reason: str = None,
    ) -> Webhook:
        """
        Same as above, except this call does not require authentication, does not accept a `channel_id` parameter in the body, and does not return a user in the webhook object.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="DELETE", path="/webhooks/{webhook_id}")
    async def delete_webhook(self, webhook_id: Snowflake) -> None:
        """
        Delete a webhook permanently.
        Requires the `MANAGE_WEBHOOKS` permission.
        Returns a `204 No Content` response on success.
        Fires a [Webhooks Update](https://discord.com/developers/docs/topics/gateway_events#webhooks_update) Gateway event.
        """

    @route(method="DELETE", path="/webhooks/{webhook_id}/{webhook_token}")
    async def delete_webhook_with_token(self, webhook_id: Snowflake, webhook_token: str) -> None:
        """
        Same as above, except this call does not require authentication.
        """

    @route(method="POST", path="/webhooks/{webhook_id}/{webhook_token}")
    async def execute_webhook(
        self,
        webhook_id: Snowflake,
        webhook_token: str,
        content: str = None,
        username: str = None,
        avatar_url: str = None,
        tts: bool = None,
        embeds: list[Embed] = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        components: list[Component] = None,
        attachments: list[Attachment] = None,
        flags: Message_Flags = None,
        thread_name: str = None,
        applied_tags: list[Snowflake] = None,
        poll: Poll = None,
        *,
        wait: bool = None,
        thread_id: Snowflake = None,
    ) -> Optional[Message]:
        """
        Refer to [Uploading Files](https://discord.com/developers/docs/reference#uploading_files) for details on attachments and multipart/form_data requests.
        Returns a message or 204 No Content depending on the wait query parameter.

        Parameters
        ----------
        content:
            the message contents
        username:
            override the default username of the webhook
        avatar_url:
            override the default avatar of the webhook
        tts:
            true if this is a TTS message
        embeds:
            embedded `rich` content
        allowed_mentions:
            allowed mentions for the message
        components:
            the components to include with the message
        attachments:
            attachment s with filename and description
        flags:
            Message_Flags
        thread_name:
            name of thread to create
        applied_tags:
            tag ids to apply to the thread
        poll:
            A poll!
        wait:
            waits for server confirmation of message send before response, and returns the created message body
        thread_id:
            Send a message to the specified thread within a webhook's channel. The thread will automatically be unarchived.
        """

    @route(method="POST", path="/webhooks/{webhook_id}/{webhook_token}/slack")
    async def execute_slack_compatible_webhook(
        self, webhook_id: Snowflake, webhook_token: str, json: dict, *, thread_id: Snowflake = None, wait: bool = None
    ) -> Optional[Message]:
        """
        Refer to [Slack's documentation](https:##api.slack.com/incoming-webhooks) for more information.
        We do not support Slack's `channel`, `icon_emoji`, `mrkdwn`, or `mrkdwn_in` properties.

        Parameters
        ----------
        thread_id:
            id of the thread to send the message in
        wait:
            waits for server confirmation of message send before response
        """

    @route(method="POST", path="/webhooks/{webhook_id}/{webhook_token}/github")
    async def execute_github_compatible_webhook(
        self, webhook_id: Snowflake, webhook_token: str, json: dict, *, thread_id: Snowflake = None, wait: bool = None
    ) -> Optional[Message]:
        """
        [Add a new webhook](https:##support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to your GitHub repo (in the repo's settings), and use this endpoint as the 'Payload URL.' You can choose what events your Discord channel receives by choosing the 'Let me select individual events' option and selecting individual events for the new webhook you're configuring.
        The supported [events](https:##docs.github.com/en/webhooks/webhook-events-and-payloads) are `commit_comment`, `create`, `delete`, `fork`, `issue_comment`, `issues`, `member`, `public`, `pull_request`, `pull_request_review`, `pull_request_review_comment`, `push`, `release`, `watch`, `check_run`, `check_suite`, `discussion`, and `discussion_comment`.

        Parameters
        ----------
        thread_id:
            id of the thread to send the message in
        wait:
            waits for server confirmation of message send before response
        """

    @route(method="GET", path="/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    async def get_webhook_message(
        self, webhook_id: Snowflake, webhook_token: str, message_id: Snowflake, *, thread_id: Snowflake = None
    ) -> Message:
        """
        Returns a previously_sent webhook message from the same token.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object on success.

        Parameters
        ----------
        thread_id:
            id of the thread the message is in
        """

    @route(method="PATCH", path="/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    async def edit_webhook_message(
        self,
        webhook_id: Snowflake,
        webhook_token: str,
        message_id: Snowflake,
        content: str = None,
        embeds: list[Embed] = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        attachments: list[Attachment] = None,
        components: list[Component] = None,
        *,
        thread_id: Snowflake = None,
    ) -> Message:
        """
        Edits a previously_sent webhook message from the same token.
        Refer to [Uploading Files](https://discord.com/developers/docs/reference#uploading_files) for details on attachments and multipart/form_data requests.

        Parameters
        ----------
        content:
            the message contents
        embeds:
            embedded `rich` content
        payload_json:
            JSON encoded body of non-file params
        allowed_mentions:
            allowed mentions for the message
        attachments:
            attached files to keep and possible descriptions for new files
        components:
            the components to include with the message
        files[n]:
            the contents of the file being sent/edited
        thread_id:
            id of the thread the message is in
        """

    @route(method="DELETE", path="/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    async def delete_webhook_message(
        self,
        webhook_id: Snowflake,
        webhook_token: str,
        message_id: Snowflake,
        *,
        thread_id: Snowflake = None,
        reason: str = None,
    ) -> None:
        """
        Deletes a message that was created by the webhook.
        Returns a `204 No Content` response on success.

        Parameters
        ----------
        thread_id:
            id of the thread the message is in
        """

    @route(method="GET", path="/gateway")
    async def get_gateway(self) -> dict[str, str]:
        """
        Returns an object with a valid WSS URL which the app can use when [Connecting](https://discord.com/developers/docs/topics/gateway#connecting) to the Gateway.
        Apps should cache this value and only call this endpoint to retrieve a new URL when they are unable to properly establish a connection using the cached one.
        > info.
        """

    @route(method="GET", path="/gateway/bot")
    async def get_gateway_bot(self) -> Gateway_Bot:
        """
        Returns an object based on the information in [Get Gateway](https://discord.com/developers/docs/topics/gateway#get_gateway), plus additional metadata that can help during the operation of large or [sharded](https://discord.com/developers/docs/topics/gateway#sharding) bots.
        Unlike the [Get Gateway](https://discord.com/developers/docs/topics/gateway#get_gateway), this route should not be cached for extended periods of time as the value is not guaranteed to be the same per_call, and changes as the bot joins/leaves guilds.
        """

    @route(method="GET", path="/oauth2/applications/@me")
    async def get_current_bot_application_information(self) -> Application:
        """
        Returns the bot's [application](https://discord.com/developers/docs/resources/application#application_object) object.
        """

    @route(method="GET", path="/oauth2/@me")
    async def get_current_authorization_information(self) -> Authorization_Information:
        """
        Returns info about the current authorization.
        Requires authentication with a bearer token.
        """

    @route(method="GET", path="/applications/{application_id}/commands")
    async def get_global_application_commands(
        self, application_id: Snowflake, *, with_localizations: Optional[bool] = None
    ) -> list[Application_Command]:
        """
        Fetch all of the global commands for your application.
        Returns an array of [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) objects.
        > warn.

        Parameters
        ----------
        with_localizations:
            Whether to include full localization dictionaries
        """

    @route(method="POST", path="/applications/{application_id}/commands")
    async def create_global_application_command(
        self,
        application_id: Snowflake,
        name: str = None,
        name_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        description: Optional[str] = None,
        description_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        options: Optional[Application_Command_Option] = None,
        default_member_permissions: Optional[Nullable[Bitwise_Permission_Flags]] = UNSET,
        dm_permission: Optional[Nullable[bool]] = UNSET,
        default_permission: Optional[bool] = None,
        integration_types: Optional[list[Application_Integration_Types]] = None,
        contexts: Optional[list[Interaction_Context_Types]] = None,
        type: Optional[Application_Command_Type] = None,
        nsfw: Optional[bool] = None,
    ) -> Application_Command:
        """
        Create a new global command.
        Returns 201 if a command with the same name does not already exist, or a 200 if it does (in which case the previous command will be overwritten).
        Both responses include an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        > warn.

        Parameters
        ----------
        name:
            Name_Of_Command
        name_localizations:
            Localization dictionary for the `name` field. Values follow the same restrictions as `name`
        description:
            1-100 character description for `CHAT_INPUT` commands
        description_localizations:
            Localization dictionary for the `description` field. Values follow the same restrictions as `description`
        options:
            the parameters for the command, max of 25
        default_member_permissions:
            Permissions
        dm_permission:
            Deprecated
        default_permission:
            Replaced by `default_member_permissions` and will be deprecated in the future. Indicates whether the command is enabled by default when the app is added to a guild. Defaults to `true`
        integration_types:
            Installation_Context
        contexts:
            Interaction_Context
        type:
            Type of command, defaults `1` if not set
        nsfw:
            Age-restricted
        """

    @route(method="GET", path="/applications/{application_id}/commands/{command_id}")
    async def get_global_application_command(
        self, application_id: Snowflake, command_id: Snowflake
    ) -> Application_Command:
        """
        Fetch a global command for your application.
        Returns an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        """

    @route(method="PATCH", path="/applications/{application_id}/commands/{command_id}")
    async def edit_global_application_command(
        self,
        application_id: Snowflake,
        command_id: Snowflake,
        name: Optional[str] = UNSET,
        name_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        description: Optional[str] = UNSET,
        description_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        options: Optional[Application_Command_Option] = UNSET,
        default_member_permissions: Optional[Nullable[str]] = UNSET,
        dm_permission: Optional[Nullable[bool]] = UNSET,
        default_permission: Optional[bool] = UNSET,
        integration_types: Optional[list[Application_Integration_Types]] = UNSET,
        contexts: Optional[list[Interaction_Context_Types]] = UNSET,
        nsfw: Optional[bool] = UNSET,
    ) -> Application_Command:
        """
        Edit a global command.
        Returns 200 and an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        All fields are optional, but any fields provided will entirely overwrite the existing values of those fields.
        > info.

        Parameters
        ----------
        name:
            Name_Of_Command
        name_localizations:
            Localization dictionary for the `name` field. Values follow the same restrictions as `name`
        description:
            1-100 character description
        description_localizations:
            Localization dictionary for the `description` field. Values follow the same restrictions as `description`
        options:
            the parameters for the command
        default_member_permissions:
            Permissions
        dm_permission:
            Deprecated
        default_permission:
            Replaced by `default_member_permissions` and will be deprecated in the future. Indicates whether the command is enabled by default when the app is added to a guild. Defaults to `true`
        integration_types:
            In_Preview
        contexts:
            In_Preview
        nsfw:
            Age-restricted
        """

    @route(method="DELETE", path="/applications/{application_id}/commands/{command_id}")
    async def delete_global_application_command(self, application_id: Snowflake, command_id: Snowflake) -> None:
        """
        Deletes a global command.
        Returns `204 No Content` on success.
        """

    @route(method="PUT", path="/applications/{application_id}/commands")
    async def bulk_overwrite_global_application_commands(
        self, application_id: Snowflake, *, payload: list[Application_Command]
    ) -> list[Application_Command]:
        """
        Takes a list of application commands, overwriting the existing global command list for this application.
        Returns 200 and a list of [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) objects.
        Commands that do not already exist will count toward daily application command create limits.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def get_guild_application_commands(
        self, application_id: Snowflake, guild_id: Snowflake, *, with_localizations: Optional[bool] = None
    ) -> list[Application_Command]:
        """
        Fetch all of the guild commands for your application for a specific guild.
        Returns an array of [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) objects.

        Parameters
        ----------
        with_localizations:
            Whether to include full localization dictionaries
        """

    @route(method="POST", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def create_guild_application_command(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        name: str = UNSET,
        name_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        description: Optional[str] = UNSET,
        description_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        options: Optional[Application_Command_Option] = UNSET,
        default_member_permissions: Optional[Nullable[Bitwise_Permission_Flags]] = UNSET,
        default_permission: Optional[bool] = UNSET,
        type: Optional[Application_Command_Type] = UNSET,
        nsfw: Optional[bool] = UNSET,
    ) -> Application_Command:
        """
        Create a new guild command.
        New guild commands will be available in the guild immediately.
        Returns 201 if a command with the same name does not already exist, or a 200 if it does (in which case the previous command will be overwritten).
        Both responses include an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        > danger.

        Parameters
        ----------
        name:
            Name_Of_Command
        name_localizations:
            Localization dictionary for the `name` field. Values follow the same restrictions as `name`
        description:
            1-100 character description for `CHAT_INPUT` commands
        description_localizations:
            Localization dictionary for the `description` field. Values follow the same restrictions as `description`
        options:
            Parameters for the command, max of 25
        default_member_permissions:
            Permissions
        default_permission:
            Replaced by `default_member_permissions` and will be deprecated in the future. Indicates whether the command is enabled by default when the app is added to a guild. Defaults to `true`
        type:
            Type of command, defaults `1` if not set
        nsfw:
            Age-restricted
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def get_guild_application_command(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> Application_Command:
        """
        Fetch a guild command for your application.
        Returns an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        """

    @route(method="PATCH", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def edit_guild_application_command(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        command_id: Snowflake,
        name: Optional[str] = UNSET,
        name_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        description: Optional[str] = UNSET,
        description_localizations: Optional[Nullable[dict[Locales, str]]] = UNSET,
        options: Optional[Application_Command_Option] = UNSET,
        default_member_permissions: Optional[Nullable[Bitwise_Permission_Flags]] = UNSET,
        default_permission: Optional[bool] = UNSET,
        nsfw: Optional[bool] = UNSET,
    ) -> Application_Command:
        """
        Edit a guild command.
        Updates for guild commands will be available immediately.
        Returns 200 and an [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) object.
        All fields are optional, but any fields provided will entirely overwrite the existing values of those fields.
        > info.

        Parameters
        ----------
        name:
            Name_Of_Command
        name_localizations:
            Localization dictionary for the `name` field. Values follow the same restrictions as `name`
        description:
            1-100 character description
        description_localizations:
            Localization dictionary for the `description` field. Values follow the same restrictions as `description`
        options:
            Parameters for the command, max of  25
        default_member_permissions:
            Permissions
        default_permission:
            Replaced by `default_member_permissions` and will be deprecated in the future. Indicates whether the command is enabled by default when the app is added to a guild. Defaults to `true`
        nsfw:
            Age-restricted
        """

    @route(method="DELETE", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def delete_guild_application_command(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> None:
        """
        Delete a guild command.
        Returns `204 No Content` on success.
        """

    @route(method="PUT", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def bulk_overwrite_guild_application_commands(
        self, application_id: Snowflake, guild_id: Snowflake, *, payload: list[Application_Command]
    ) -> list[Application_Command]:
        """
        Takes a list of application commands, overwriting the existing command list for this application for the targeted guild.
        Returns `200` and a list of [application command](https://discord.com/developers/docs/interactions/application_commands#application_command_object) objects.

        Parameters
        ----------
        name:
            Name_Of_Command
        description:
            1-100 character description
        integration_types:
            In_Preview
        contexts:
            In_Preview
        id:
            ID of the command, if known
        name_localizations:
            Localization dictionary for the `name` field. Values follow the same restrictions as `name`
        description_localizations:
            Localization dictionary for the `description` field. Values follow the same restrictions as `description`
        options:
            Parameters for the command
        default_member_permissions:
            Permissions
        dm_permission:
            Deprecated
        default_permission:
            Replaced by `default_member_permissions` and will be deprecated in the future. Indicates whether the command is enabled by default when the app is added to a guild. Defaults to `true`
        type:
            Type of command, defaults `1` if not set
        nsfw:
            Age-restricted
        """

    @route(method="POST", path="/interactions/{interaction_id}/{interaction_token}/callback")
    async def create_interaction_response(
        self,
        interaction_id: Snowflake,
        interaction_token: str,
        type: Interaction_Callback_Type,
        data: Optional[Interaction_Application_Command_Callback_Data] = None,
    ) -> None:
        """
        This endpoint also supports file attachments similar to the webhook endpoints.
        Refer to [Uploading Files](https://discord.com/developers/docs/reference#uploading_files) for details on uploading files and multipart/form_data requests.
        """

    @route(method="GET", path="/webhooks/{application_id}/{interaction_token}/messages/@original")
    async def get_original_interaction_response(self, application_id: Snowflake, interaction_token: str) -> Message:
        """
        Returns the initial Interaction response.
        Functions the same as [Get Webhook Message](https://discord.com/developers/docs/resources/webhook#get_webhook_message).
        """

    @route(method="PATCH", path="/webhooks/{application_id}/{interaction_token}/messages/@original")
    async def edit_original_interaction_response(
        self,
        application_id: Snowflake,
        interaction_token: str,
        content: str = None,
        embeds: list[Embed] = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        components: list[Component] = None,
        attachments: list[Attachment] = None,
        flags: int = None,
    ) -> Message:
        """
        Edits the initial Interaction response.
        Functions the same as [Edit Webhook Message](https://discord.com/developers/docs/resources/webhook#edit_webhook_message).
        """

    @route(method="DELETE", path="/webhooks/{application_id}/{interaction_token}/messages/@original")
    async def delete_original_interaction_response(self, application_id: Snowflake, interaction_token: str) -> None:
        """
        Deletes the initial Interaction response.
        Returns `204 No Content` on success.
        """

    @route(method="POST", path="/webhooks/{application_id}/{interaction_token}")
    async def create_followup_message(
        self,
        application_id: Snowflake,
        interaction_token: str,
        wait: bool = False,
        content: str = None,
        username: str = None,
        avatar_url: str = None,
        tts: bool = None,
        embeds: list[Embed] = None,
        payload_json: str = None,
        allowed_mentions: Allowed_Mentions = [],
        components: list[Component] = None,
        attachments: list[Attachment] = None,
        flags: Message_Flags = None,
    ) -> Message:
        """
        Create a followup message for an Interaction.
        Functions the same as [Execute Webhook](https://discord.com/developers/docs/resources/webhook#execute_webhook), but wait is always true.
        The thread_id, avatar_url, and username parameters are not supported when using this endpoint for interaction followups.
        """

    @route(method="GET", path="/webhooks/{application_id}/{interaction_token}/messages/{message_id}")
    async def get_followup_message(
        self, application_id: Snowflake, interaction_token: str, message_id: Snowflake
    ) -> Message:
        """
        Returns a followup message for an Interaction.
        Functions the same as [Get Webhook Message](https://discord.com/developers/docs/resources/webhook#get_webhook_message).
        """

    @route(method="PATCH", path="/webhooks/{application_id}/{interaction_token}/messages/{message_id}")
    async def edit_followup_message(
        self,
        application_id: Snowflake,
        interaction_token: str,
        message_id: Snowflake,
        content: str = None,
        embeds: list[Embed] = None,
        allowed_mentions: Allowed_Mentions = [],
        components: list[Component] = None,
        attachments: list[Attachment] = None,
    ) -> Message:
        """
        Edits a followup message for an Interaction.
        Functions the same as [Edit Webhook Message](https://discord.com/developers/docs/resources/webhook#edit_webhook_message).
        """

    @route(method="DELETE", path="/webhooks/{application_id}/{interaction_token}/messages/{message_id}")
    async def delete_followup_message(
        self, application_id: Snowflake, interaction_token: str, message_id: Snowflake
    ) -> None:
        """
        Deletes a followup message for an Interaction.
        Returns `204 No Content` on success.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/permissions")
    async def get_guild_application_command_permissions(
        self, application_id: Snowflake, guild_id: Snowflake
    ) -> list[Guild_Application_Command_Permissions]:
        """
        Fetches permissions for all commands for your application in a guild.
        Returns an array of [guild application command permissions](https://discord.com/developers/docs/interactions/application_commands#application_command_permissions_object_guild_application_command_permissions_structure) objects.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions")
    async def get_application_command_permissions(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> Guild_Application_Command_Permissions:
        """
        Fetches permissions for a specific command for your application in a guild.
        Returns a [guild application command permissions](https://discord.com/developers/docs/interactions/application_commands#application_command_permissions_object_guild_application_command_permissions_structure) object.
        """

    @route(method="PUT", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions")
    async def edit_application_command_permissions(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        command_id: Snowflake,
        permissions: list[Application_Command_Permissions] = None,
    ) -> Guild_Application_Command_Permissions:
        """
        > This endpoint requires authentication with a Bearer token that has permission to manage the guild and its roles.
        For more information, read above about [application command permissions](https://discord.com/developers/docs/interactions/application_commands#permissions).
        > warn.

        Parameters
        ----------
        permissions:
            Permissions for the command in the guild
        """

    @route(method="PUT", path="/applications/{application_id}/guilds/{guild_id}/commands/permissions")
    async def batch_edit_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake):
        """
        > This endpoint has been disabled with [updates to command permissions (Permissions v2)](https://discord.com/developers/docs/change/log#updated_command_permissions).
        Instead, you can [edit each application command permissions](https://discord.com/developers/docs/interactions/application_commands#edit_application_command_permissions) (though you should be careful to handle any potential [rate limits](#DOCS_TOPICS_RATE_LIMITS)).
        > danger.
        """

    @route(method="GET", path="/applications/{application_id}/entitlements")
    async def list_entitlements(
        self,
        application_id: Snowflake,
        *,
        user_id: Snowflake = UNSET,
        sku_ids: list[Snowflake] = UNSET,
        before: Snowflake = UNSET,
        after: Snowflake = UNSET,
        limit: int = UNSET,
        guild_id: Snowflake = UNSET,
        exclude_ended: bool = UNSET,
    ) -> dict[Any, Any]:
        """
        Returns all entitlements for a given app, active and expired.

        Parameters
        ----------
        user_id:
            User ID to look up entitlements for
        sku_ids:
            Optional list of SKU IDs to check entitlements for
        before:
            Retrieve entitlements before this entitlement ID
        after:
            Retrieve entitlements after this entitlement ID
        limit:
            Number of entitlements to return, 1-100, default 100
        guild_id:
            Guild ID to look up entitlements for
        exclude_ended:
            Whether or not ended entitlements should be omitted
        """

    @route(method="POST", path="/applications/{application_id}/entitlements/{entitlement_id}/consume")
    async def consume_an_entitlement(self, application_id: Snowflake, entitlement_id: str) -> None:
        """
        For One_Time Purchase consumable SKUs, marks a given entitlement for the user as consumed.
        The entitlement will have consumed: true when using [List Entitlements](https://discord.com/developers/docs/monetization/entitlements#list_entitlements).
        """

    @route(method="POST", path="/applications/{application_id}/entitlements")
    async def create_test_entitlement(
        self, application_id: Snowflake, sku_id: str, owner_id: Snowflake, owner_type: Entitlement_Subscription_Types
    ) -> Entitlement:
        """
        Creates a test entitlement to a given SKU for a given guild or user.
        Discord will act as though that user or guild has entitlement to your premium offering.

        Parameters
        ----------
        None:
            ID of the SKU to grant the entitlement to
        """

    @route(method="DELETE", path="/applications/{application_id}/entitlements/{entitlement_id}")
    async def delete_test_entitlement(self, application_id: Snowflake, entitlement_id: str) -> None:
        """
        Deletes a currently-active test entitlement.
        Discord will act as though that user or guild _no longer has_ entitlement to your premium offering.
        """

    @route(method="GET", path="/applications/{application_id}/skus")
    async def list_skus(self, application_id: Snowflake) -> list[SKU]:
        """
        Returns all SKUs for a given application.
        """
