# -*- coding: utf-8 -*-
"""
Discord Endpoints
----------

Discord API endpoints.

:copyright: (c) 2021-2024 Mmesek
:version: 2024/06/10 20:45
"""

from datetime import datetime
from typing import Optional

from msgspec import UnsetType, UNSET

from mdiscord.utils import Permissions as permissions
from mdiscord.routes import route
from mdiscord.types import (
    Snowflake,
    Channel,
    Bitwise_Permission_Flags,
    Message,
    Audit_Log,
    Overwrite,
    Embed,
    Attachment,
    Component,
    Allowed_Mentions,
    Message_Reference,
    Followed_Channel,
    Audit_Log_Events,
    Thread_List,
    Thread_Member,
    Channel_Types,
    Gateway_Bot,
    Welcome_Screen_Channel,
    User,
    Invite,
    Emoji,
    Role,
    Guild,
    Ban,
    Webhook,
    Guild_Preview,
    Guild_Member,
    Guild_Widget,
    Voice_Region,
    Connection,
    Guild_Features,
    Guild_Application_Command_Permissions,
    Application_Command_Permissions,
    Welcome_Screen,
    Integration,
    Application,
    Application_Command,
    Application_Command_Option,
    Interaction_Response,
    Application_Command_Type,
    Stage_Instance,
    Privacy_Level,
)


class Endpoints:
    @permissions(Bitwise_Permission_Flags.VIEW_AUDIT_LOG)
    @route(method="GET", path="/guilds/{guild_id}/audit-logs")
    async def get_guild_audit_log(
        self,
        guild_id: Snowflake,
        *,
        user_id: Snowflake = None,
        action_type: Audit_Log_Events = None,
        before: Snowflake = None,
        limit: int = None,
    ) -> Audit_Log:
        """
        Returns an [audit log](https://discord.com/developers/docs/resources/audit_log#audit_log_object) object for the guild.
        Requires the 'VIEW_AUDIT_LOG' permission.

        Parameters
        ----------
        user_id:
            filter the log for actions made by a user
        action_type:
            Audit_Log_Event
        before:
            filter the log before a certain entry id
        limit:
            how many entries are returned
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
        position: int | UnsetType = UNSET,
        topic: str | UnsetType = UNSET,
        nsfw: bool | UnsetType = UNSET,
        rate_limit_per_user: int | UnsetType = UNSET,
        bitrate: int | UnsetType = UNSET,
        user_limit: int | UnsetType = UNSET,
        permission_overwrites: list[Overwrite] | UnsetType = UNSET,
        parent_id: Snowflake | UnsetType = UNSET,
        rtc_region: str | UnsetType = UNSET,
        video_quality_mode: int | UnsetType = UNSET,
        *,
        reason: str = None,
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
            whether the channel is archived
        auto_archive_duration:
            duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
        locked:
            when a thread is locked, only users with MANAGE_THREADS can unarchive it
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
            the user limit of the voice channel; 0 refers to no limit, 1 to 99 refers to a user limit
        permission_overwrites:
            channel
        parent_id:
            id of the new parent category for a channel
        rtc_region:
            Voice_Region
        video_quality_mode:
            Video_Quality_Mode
        default_auto_archive_duration:
            the default duration for newly created threads in the channel, in minutes, to automatically archive the thread after recent activity
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
        Deleting a category does not delete its child channels; they will have their parent_id removed and a [Channel Update](https://discord.com/developers/docs/topics/gateway#channel_update) Gateway event will fire for each of them.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) object on success.
        Fires a [Channel Delete](https://discord.com/developers/docs/topics/gateway#channel_delete) Gateway event (or [Thread Delete](https://discord.com/developers/docs/topics/gateway#thread_delete) if the channel was a thread).
        """

    @permissions(Bitwise_Permission_Flags.VIEW_CHANNEL)
    @route(method="GET", path="/channels/{channel_id}/messages")
    async def get_channel_messages(
        self,
        channel_id: Snowflake,
        *,
        around: Snowflake = None,
        before: Snowflake = None,
        after: Snowflake = None,
        limit: int = 50,
    ) -> list[Message]:
        """
        Returns the messages for a channel.
        If operating on a guild channel, this endpoint requires the VIEW_CHANNEL permission to be present on the current user.
        If the current user is missing the 'READ_MESSAGE_HISTORY' permission in the channel then this will return no messages (since they cannot read the message history).
        Returns an array of [message](https://discord.com/developers/docs/resources/channel#message_object) objects on success.

        Parameters
        ----------
        around:
            get messages around this message ID
        before:
            get messages before this message ID
        after:
            get messages after this message ID
        limit:
            max number of messages to return
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/messages/{message_id}")
    async def get_channel_message(self, channel_id: Snowflake, message_id: Snowflake) -> Message:
        """
        Returns a specific message in the channel.
        If operating on a guild channel, this endpoint requires the 'READ_MESSAGE_HISTORY' permission to be present on the current user.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object on success.
        """

    @permissions(Bitwise_Permission_Flags.SEND_MESSAGES, Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="POST", path="/channels/{channel_id}/messages")
    async def create_message(
        self,
        channel_id: Snowflake,
        content: str = None,
        nonce: int = None,
        tts: bool = None,
        embeds: list[Embed] = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        message_reference: Message_Reference = None,
        components: list[Component] = None,
        attachments: list[Attachment] = None,
    ) -> Message:
        """
        Post a message to a guild text or DM channel.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object.
        Fires a [Message Create](https://discord.com/developers/docs/topics/gateway#message_create) Gateway event.
        See [message formatting](https://discord.com/developers/docs/reference#message_formatting) for more information on how to properly format messages.
        > warn
        Limitations
        - When operating on a guild channel, the current user must have the `SEND_MESSAGES` permission.
        - When sending a message with `tts` (text-to-speech) set to `true`, the current user must have the `SEND_TTS_MESSAGES` permission.
        - When creating a message as a reply to another message, the current user must have the `READ_MESSAGE_HISTORY` permission.
        - The referenced message must exist and cannot be a system message.
        - The maximum request size when sending a message is **8MB**
        - For the embed object, you can set every field except `type` (it will be `rich` regardless of if you try to set it), `provider`, `video`, and any `height`, `width`, or `proxy_url` values for images.
        - **Files can only be uploaded when using the `multipart/form-data` content type.**
        You may create a message as a reply to another message.
        To do so, include a [`message_reference`](https://discord.com/developers/docs/resources/channel#message-reference-object-message-reference-structure) with a `message_id`.
        The `channel_id` and `guild_id` in the `message_reference` are optional, but will be validated if provided.
        > info
        > Note that when sending a message, you must provide a value for at **least one of** `content`, `embeds`, or `file`.
        > info
        > For a `file` attachment, the `Content-Disposition` subpart header MUST contain a `filename` parameter.
        > warn
        > This endpoint supports both `application/json` and `multipart/form-data` bodies.
        When uploading files the `multipart/form-data` content type must be used.
        > Note that in multipart form data, the `embeds` and `allowed_mentions` fields cannot be used.
        You can pass a stringified JSON body as a form value as `payload_json` instead.
        > **If you supply a `payload_json` form value, all fields except for `file` fields will be ignored in the form data**.

        Parameters
        ----------
        content:
            the message contents
        tts:
            true if this is a TTS message
        embeds:
            embedded `rich` content
        payload_json:
            JSON encoded body of non-file params
        allowed_mentions:
            allowed mentions for the message
        message_reference:
            include to make your message a reply
        components:
            the components to include with the message
        attachments:
            attachment objects with filename, content of file and description
        """

    @permissions(Bitwise_Permission_Flags.SEND_MESSAGES)
    @route(method="POST", path="/channels/{channel_id}/messages/{message_id}/crosspost")
    async def crosspost_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> Message:
        """
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object.
        Crosspost a message in a News Channel to following channels.
        This endpoint requires the 'SEND_MESSAGES' permission, if the current user sent the message, or additionally the 'MANAGE_MESSAGES' permission, for all other messages, to be present for the current user.
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY | Bitwise_Permission_Flags.ADD_REACTIONS)
    @route(method="PUT", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me")
    async def create_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> None:
        """
        Create a reaction for the message.
        This endpoint requires the 'READ_MESSAGE_HISTORY' permission to be present on the current user.
        Additionally, if nobody else has reacted to the message using this emoji, this endpoint requires the 'ADD_REACTIONS' permission to be present on the current user.
        Returns a 204 empty response on success.
        """

    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me")
    async def delete_own_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> None:
        """
        Delete a reaction the current user has made for the message.
        Returns a 204 empty response on success.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}")
    async def delete_user_reaction(
        self, channel_id: Snowflake, message_id: Snowflake, emoji: str, user_id: Snowflake, reason: str = None
    ) -> None:
        """
        Deletes another user's reaction.
        This endpoint requires the 'MANAGE_MESSAGES' permission to be present on the current user.
        Returns a 204 empty response on success.
        """

    @route(method="GET", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}")
    async def get_reactions(
        self, channel_id: Snowflake, message_id: Snowflake, emoji: str, *, after: Snowflake = None, limit: int = 25
    ) -> list[User]:
        """
        Get a list of users that reacted with this emoji.
        Returns an array of [user](https://discord.com/developers/docs/resources/user#user_object) objects on success.

        Parameters
        ----------
        after:
            get users after this user ID
        limit:
            max number of users to return
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions")
    async def delete_all_reactions(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Deletes all reactions on a message.
        This endpoint requires the 'MANAGE_MESSAGES' permission to be present on the current user.
        Fires a [Message Reaction Remove All](https://discord.com/developers/docs/topics/gateway#message_reaction_remove_all) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}/reactions/{emoji}")
    async def delete_all_reactions_for_emoji(
        self, channel_id: Snowflake, message_id: Snowflake, emoji: str, reason: str = None
    ) -> None:
        """
        Deletes all the reactions for a given emoji on a message.
        This endpoint requires the MANAGE_MESSAGES permission to be present on the current user.
        Fires a [Message Reaction Remove Emoji](https://discord.com/developers/docs/topics/gateway#message_reaction_remove_emoji) Gateway event.
        """

    @route(method="PATCH", path="/channels/{channel_id}/messages/{message_id}")
    async def edit_message(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        content: str = None,
        embeds: list[Embed] = None,
        flags: int = None,
        allowed_mentions: Allowed_Mentions = Allowed_Mentions(parse=[]),
        attachments: list[Attachment] = None,
        components: list[Component] = None,
    ) -> Message:
        """
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object.
        Fires a [Message Update](https://discord.com/developers/docs/topics/gateway#message_update) Gateway event.
        Edit a previously sent message.
        The fields `content`, `embeds`, and `flags` can be edited by the original message author.
        Other users can only edit `flags` and only if they have the `MANAGE_MESSAGES` permission in the corresponding channel.
        When specifying flags, ensure to include all previously set flags/bits in addition to ones that you are modifying.
        Only `flags` documented in the table below may be modified by users (unsupported flag changes are currently ignored without error).

        Parameters
        ----------
        content:
            the message contents
        embeds:
            embedded `rich` content
        embed:
            embedded `rich` content, deprecated in favor of `embeds`
        flags:
            Flags
        payload_json:
            JSON encoded body of non-file params
        allowed_mentions:
            allowed mentions for the message
        attachments:
            attached files to keep/add
        components:
            the components to include with the message
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/messages/{message_id}")
    async def delete_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Delete a message.
        If operating on a guild channel and trying to delete a message that was not sent by the current user, this endpoint requires the MANAGE_MESSAGES permission.
        Returns a 204 empty response on success.
        Fires a [Message Delete](https://discord.com/developers/docs/topics/gateway#message_delete) Gateway event.
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
        Fires a [Message Delete Bulk](https://discord.com/developers/docs/topics/gateway#message_delete_bulk) Gateway event.

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
        allow: str = None,
        deny: str = None,
        type: int = None,
        reason: str = None,
    ) -> None:
        """
        Edit the channel permission overwrites for a user or role in a channel.
        Only usable for guild channels.
        Requires the MANAGE_ROLES permission.
        Only permissions your bot has in the guild or channel can be allowed/denied (unless your bot has a MANAGE_ROLES overwrite in the channel).
        Returns a 204 empty response on success.
        For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions).

        Parameters
        ----------
        allow:
            the bitwise value of all allowed permissions
        deny:
            the bitwise value of all disallowed permissions
        type:
            0 for a role
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
        Fires an [Invite Create](https://discord.com/developers/docs/topics/gateway#invite_create) Gateway event.

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
        For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="POST", path="/channels/{channel_id}/followers")
    async def follow_news_channel(
        self, channel_id: Snowflake, webhook_channel_id: Snowflake = None, reason: str = None
    ) -> Followed_Channel:
        """
        Follow a News Channel to send messages to a target channel.
        Requires the MANAGE_WEBHOOKS permission in the target channel.
        Returns a [followed channel](https://discord.com/developers/docs/resources/channel#followed_channel_object) object.

        Parameters
        ----------
        webhook_channel_id:
            id of target channel
        """

    @route(method="POST", path="/channels/{channel_id}/typing")
    async def trigger_typing_indicator(self, channel_id: Snowflake) -> None:
        """
        Post a typing indicator for the specified channel.
        Generally bots should **not** implement this route.
        However, if a bot is responding to a command and expects the computation to take a few seconds, this endpoint may be called to let the user know that the bot is processing their message.
        Returns a 204 empty response on success.
        Fires a [Typing Start](https://discord.com/developers/docs/topics/gateway#typing_start) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/pins")
    async def get_pinned_messages(self, channel_id: Snowflake) -> Message:
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
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_MESSAGES)
    @route(method="DELETE", path="/channels/{channel_id}/pins/{message_id}")
    async def unpin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: str = None) -> None:
        """
        Unpin a message in a channel.
        Requires the `MANAGE_MESSAGES` permission.
        Returns a 204 empty response on success.
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
    async def start_thread_with_message(
        self,
        channel_id: Snowflake,
        message_id: Snowflake,
        name: str = None,
        auto_archive_duration: int = None,
        reason: str = None,
    ) -> Channel:
        """
        Creates a new thread from an existing message.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) on success, and a 400 BAD REQUEST on invalid parameters.
        Fires a [Thread Create](https://discord.com/developers/docs/topics/gateway#thread_create) Gateway event.

        Parameters
        ----------
        name:
            1-100 character channel name
        auto_archive_duration:
            duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
        """

    @route(method="POST", path="/channels/{channel_id}/threads")
    async def start_thread_without_message(
        self,
        channel_id: Snowflake,
        name: str = None,
        auto_archive_duration: int = None,
        type: Channel_Types = None,
        reason: str = None,
    ) -> Channel:
        """
        Creates a new thread that is not connected to an existing message.
        The created thread defaults to a GUILD_PRIVATE_THREAD*.
        Returns a [channel](https://discord.com/developers/docs/resources/channel#channel_object) on success, and a 400 BAD REQUEST on invalid parameters.
        Fires a [Thread Create](https://discord.com/developers/docs/topics/gateway#thread_create) Gateway event.

        Parameters
        ----------
        name:
            1-100 character channel name
        auto_archive_duration:
            duration in minutes to automatically archive the thread after recent activity, can be set to: 60, 1440, 4320, 10080
        type:
            Type_Of_Thread
        """

    @route(method="POST", path="/channels/{channel_id}/threads")
    async def start_thread_in_forum_channel(
        self,
        channel_id: Snowflake,
        name: str = None,
        auto_archive_duration: int = None,
        rate_limit_per_user: int = None,
        message: Message = None,
        applied_tags: list[Snowflake] = None,
        reason: str = None,
    ):
        pass

    @route(method="PUT", path="/channels/{channel_id}/thread-members/@me")
    async def join_thread(self, channel_id: Snowflake, reason: str = None) -> None:
        """
        Adds the current user to a thread.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway#thread_members_update) Gateway event.
        """

    @route(method="PUT", path="/channels/{channel_id}/thread-members/{user_id}")
    async def add_thread_member(self, channel_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Adds another member to a thread.
        Requires the ability to send messages in the thread.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway#thread_members_update) Gateway event.
        """

    @route(method="DELETE", path="/channels/{channel_id}/thread-members/@me")
    async def leave_thread(self, channel_id: Snowflake, reason: str = None) -> None:
        """
        Removes the current user from a thread.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway#thread_members_update) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_THREADS)
    @route(method="DELETE", path="/channels/{channel_id}/thread-members/{user_id}")
    async def remove_thread_member(self, channel_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Removes another member from a thread.
        Requires the MANAGE_THREADS permission, or the creator of the thread if it is a GUILD_PRIVATE_THREAD.
        Also requires the thread is not archived.
        Returns a 204 empty response on success.
        Fires a [Thread Members Update](https://discord.com/developers/docs/topics/gateway#thread_members_update) Gateway event.
        """

    @route(method="GET", path="/channels/{channel_id}/thread-members")
    async def list_thread_members(self, channel_id: Snowflake) -> list[Thread_Member]:
        """
        > This endpoint is restricted according to whether the GUILD_MEMBERS [Privileged Intent](https://discord.com/developers/docs/topics/gateway#privileged_intents) is enabled for your application.
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/threads/active")
    async def list_active_threads(self, channel_id: Snowflake) -> list[Thread_List]:
        """
        Returns all active threads in the channel, including public and private threads.
        Threads are ordered by their `id`, in descending order.
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/threads/archived/public")
    async def list_public_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[datetime] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are public.
        When called on a GUILD_TEXT channel, returns threads of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) GUILD_PUBLIC_THREAD.
        When called on a GUILD_NEWS channel returns threads of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) GUILD_NEWS_THREAD.
        Threads are ordered by archive_timestamp, in descending order.
        Requires the READ_MESSAGE_HISTORY permission.

        Parameters
        ----------
        before:
            returns threads before this timestamp
        limit:
            optional maximum number of threads to return
        """

    @route(method="GET", path="/channels/{channel_id}/threads/archived/private")
    async def list_private_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[datetime] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) GUILD_PRIVATE_THREAD.
        Threads are ordered by archive_timestamp, in descending order.
        Requires both the READ_MESSAGE_HISTORY and MANAGE_THREADS permissions.

        Parameters
        ----------
        before:
            returns threads before this timestamp
        limit:
            optional maximum number of threads to return
        """

    @permissions(Bitwise_Permission_Flags.READ_MESSAGE_HISTORY)
    @route(method="GET", path="/channels/{channel_id}/users/@me/threads/archived/private")
    async def list_joined_private_archived_threads(
        self, channel_id: Snowflake, *, before: Optional[Snowflake] = None, limit: Optional[int] = None
    ) -> list[Thread_List]:
        """
        Returns archived threads in the channel that are of [type](https://discord.com/developers/docs/resources/channel#channel_object_channel_types) GUILD_PRIVATE_THREAD, and the user has joined.
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
        """

    @route(method="GET", path="/guilds/{guild_id}/emojis/{emoji_id}")
    async def get_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> Emoji:
        """
        Returns an [emoji](https://discord.com/developers/docs/resources/emoji#emoji_object) object for the given guild and emoji IDs.
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
        > Emojis and animated emojis have a maximum file size of 256kb.
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
        roles: list[Snowflake] | UnsetType = UNSET,
        reason: str = None,
    ) -> Emoji:
        """
        Modify the given emoji.
        Requires the MANAGE_EMOJIS permission.
        Returns the updated [emoji](https://discord.com/developers/docs/resources/emoji#emoji_object) object on success.
        Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway#guild_emojis_update) Gateway event.

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
        Requires the MANAGE_EMOJIS permission.
        Returns 204 No Content on success.
        Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway#guild_emojis_update) Gateway event.
        """

    @route(method="POST", path="/guilds")
    async def create_guild(
        self,
        name: str = None,
        region: Optional[str | UnsetType] = UNSET,
        icon: Optional[str] = None,
        verification_level: Optional[int] = None,
        default_message_notifications: Optional[int] = None,
        explicit_content_filter: Optional[int] = None,
        roles: Optional[list[Role]] = None,
        channels: Optional[list[Channel]] = None,
        afk_channel_id: Optional[Snowflake] = None,
        afk_timeout: Optional[int] = None,
        system_channel_id: Optional[Snowflake] = None,
        system_channel_flags: Optional[int] = None,
    ) -> Guild:
        """
        Create a new guild.
        Returns a [guild](https://discord.com/developers/docs/resources/guild#guild_object) object on success.
        Fires a [Guild Create](https://discord.com/developers/docs/topics/gateway#guild_create) Gateway event.

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
            afk timeout in seconds
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
        Returns the [guild preview](https://discord.com/developers/docs/resources/guild#guild_preview_object) object for the given id.
        If the user is not in the guild, then the guild must be lurkable (it must be Discoverable or have a [live public stage](https://discord.com/developers/docs/resources/stage_instance#definitions)).
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}")
    async def modify_guild(
        self,
        guild_id: Snowflake,
        name: str = None,
        region: str | UnsetType = UNSET,
        verification_level: int | UnsetType = UNSET,
        default_message_notifications: int | UnsetType = UNSET,
        explicit_content_filter: int | UnsetType = UNSET,
        afk_channel_id: Snowflake | UnsetType = UNSET,
        afk_timeout: int = None,
        icon: str | UnsetType = UNSET,
        owner_id: Snowflake = None,
        splash: str | UnsetType = UNSET,
        discovery_splash: str | UnsetType = UNSET,
        banner: str | UnsetType = UNSET,
        system_channel_id: Snowflake | UnsetType = UNSET,
        system_channel_flags: int = None,
        rules_channel_id: Snowflake | UnsetType = UNSET,
        public_updates_channel_id: Snowflake | UnsetType = UNSET,
        preferred_locale: str | UnsetType = UNSET,
        features: list[Guild_Features] = None,
        description: str | UnsetType = UNSET,
        reason: str = None,
    ) -> Guild:
        """
        Modify a guild's settings.
        Requires the `MANAGE_GUILD` permission.
        Returns the updated [guild](https://discord.com/developers/docs/resources/guild#guild_object) object on success.
        Fires a [Guild Update](https://discord.com/developers/docs/topics/gateway#guild_update) Gateway event.

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
            afk timeout in seconds
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
            the description for the guild, if the guild is discoverable
        """

    @route(method="DELETE", path="/guilds/{guild_id}")
    async def delete_guild(self, guild_id: Snowflake) -> None:
        """
        Delete a guild permanently.
        User must be owner.
        Returns `204 No Content` on success.
        Fires a [Guild Delete](https://discord.com/developers/docs/topics/gateway#guild_delete) Gateway event.
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
        type: int = None,
        topic: str = None,
        bitrate: int = None,
        user_limit: int = None,
        rate_limit_per_user: int = None,
        position: int = None,
        permission_overwrites: list[Overwrite] = None,
        parent_id: Snowflake = None,
        nsfw: bool = None,
        reason: str = None,
    ) -> Channel:
        """
        Create a new [channel](https://discord.com/developers/docs/resources/channel#channel_object) object for the guild.
        Requires the `MANAGE_CHANNELS` permission.
        If setting permission overwrites, only permissions your bot has in the guild can be allowed/denied.
        Setting `MANAGE_ROLES` permission in channels is only possible for guild administrators.
        Returns the new [channel](https://discord.com/developers/docs/resources/channel#channel_object) object on success.
        Fires a [Channel Create](https://discord.com/developers/docs/topics/gateway#channel_create) Gateway event.

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
        """

    @route(method="PATCH", path="/guilds/{guild_id}/channels")
    async def modify_guild_channel_positions(
        self,
        guild_id: Snowflake,
        id: Snowflake = None,
        position: int | UnsetType = UNSET,
        lock_permissions: bool | UnsetType = UNSET,
        parent_id: Snowflake | UnsetType = UNSET,
        reason: str = None,
    ) -> None:
        """
        Modify the positions of a set of [channel](https://discord.com/developers/docs/resources/channel#channel_object) objects for the guild.
        Requires `MANAGE_CHANNELS` permission.
        Returns a 204 empty response on success.
        Fires multiple [Channel Update](https://discord.com/developers/docs/topics/gateway#channel_update) Gateway events.

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
    ) -> Guild_Member | None:
        """
        For guilds with [Membership Screening](https://discord.com/developers/docs/resources/guild#membership_screening_object) enabled, this endpoint will default to adding new members as pending in the [guild member object](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Members that are pending will have to complete membership screening before they become full members that can talk.

        Parameters
        ----------
        access_token:
            an oauth2 access token granted with the `guilds.join` to the bot's application for the user you want to add to the guild
        nick:
            value to set users nickname to
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
        channel_id: Snowflake | UnsetType = UNSET,
        communication_disabled_until: datetime = None,
        reason: str = None,
    ) -> Guild_Member:
        """
        Modify attributes of a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Returns a 200 OK with the [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object) as the body.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild_member_update) Gateway event.
        If the channel_id is set to null, this will force the target user to be disconnected from voice.

        Parameters
        ----------
        nick:
            value to set users nickname to
        roles:
            role ids the member is assigned
        mute:
            whether the user is muted in voice channels. Will throw a 400 if the user is not in a voice channel
        deaf:
            whether the user is deafened in voice channels. Will throw a 400 if the user is not in a voice channel
        channel_id:
            id of channel to move user to
        """

    @route(method="PATCH", path="/guilds/{guild_id}/members/@me/nick")
    async def modify_current_user_nick(self, guild_id: Snowflake, nick: str = None, reason: str = None) -> str:
        """
        Modifies the nickname of the current user in a guild.
        Returns a 200 with the nickname on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild_member_update) Gateway event.

        Parameters
        ----------
        nick:
            value to set users nickname to
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PUT", path="/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    async def add_guild_member_role(
        self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, reason: str = None
    ) -> None:
        """
        Adds a role to a [guild member](https://discord.com/developers/docs/resources/guild#guild_member_object).
        Requires the MANAGE_ROLES permission.
        Returns a 204 empty response on success.
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild_member_update) Gateway event.
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
        Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild_member_update) Gateway event.
        """

    @route(method="DELETE", path="/guilds/{guild_id}/members/{user_id}")
    async def remove_guild_member(self, guild_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Remove a member from a guild.
        Requires KICK_MEMBERS permission.
        Returns a 204 empty response on success.
        Fires a [Guild Member Remove](https://discord.com/developers/docs/topics/gateway#guild_member_remove) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="GET", path="/guilds/{guild_id}/bans")
    async def get_guild_bans(self, guild_id: Snowflake) -> list[Ban]:
        """
        Returns a list of [ban](https://discord.com/developers/docs/resources/guild#ban_object) objects for the users banned from this guild.
        Requires the BAN_MEMBERS permission.
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
        delete_message_days: Optional[int] = None,
        reason: Optional[str] = None,
    ) -> None:
        """
        Create a guild ban, and optionally delete previous messages sent by the banned user.
        Requires the BAN_MEMBERS permission.
        Returns a 204 empty response on success.
        Fires a [Guild Ban Add](https://discord.com/developers/docs/topics/gateway#guild_ban_add) Gateway event.

        Parameters
        ----------
        delete_message_days:
            number of days to delete messages for
        reason:
            reason for the ban
        """

    @permissions(Bitwise_Permission_Flags.BAN_MEMBERS)
    @route(method="DELETE", path="/guilds/{guild_id}/bans/{user_id}")
    async def remove_guild_ban(self, guild_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        """
        Remove the ban for a user.
        Requires the BAN_MEMBERS permissions.
        Returns a 204 empty response on success.
        Fires a [Guild Ban Remove](https://discord.com/developers/docs/topics/gateway#guild_ban_remove) Gateway event.
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
        permissions: str = None,
        color: int = None,
        hoist: bool = False,
        icon: str = None,
        unicode_emoji: str = None,
        mentionable: bool = False,
        reason: str = None,
    ) -> Role:
        """
        Create a new [role](https://discord.com/developers/docs/topics/permissions#role_object) for the guild.
        Requires the MANAGE_ROLES permission.
        Returns the new [role](https://discord.com/developers/docs/topics/permissions#role_object) object on success.
        Fires a [Guild Role Create](https://discord.com/developers/docs/topics/gateway#guild_role_create) Gateway event.
        All JSON params are optional.

        Parameters
        ----------
        name:
            name of the role
        permissions:
            bitwise value of the enabled/disabled permissions
        color:
            RGB color value
        hoist:
            whether the role should be displayed separately in the sidebar
        mentionable:
            whether the role should be mentionable
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="PATCH", path="/guilds/{guild_id}/roles")
    async def modify_guild_role_positions(
        self, guild_id: Snowflake, id: Snowflake = None, position: int = None, reason: str = None
    ) -> list[Role]:
        """
        Modify the positions of a set of [role](https://discord.com/developers/docs/topics/permissions#role_object) objects for the guild.
        Requires the MANAGE_ROLES permission.
        Returns a list of all of the guild's [role](https://discord.com/developers/docs/topics/permissions#role_object) objects on success.
        Fires multiple [Guild Role Update](https://discord.com/developers/docs/topics/gateway#guild_role_update) Gateway events.

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
        Fires a [Guild Role Update](https://discord.com/developers/docs/topics/gateway#guild_role_update) Gateway event.

        Parameters
        ----------
        name:
            name of the role
        permissions:
            bitwise value of the enabled/disabled permissions
        color:
            RGB color value
        hoist:
            whether the role should be displayed separately in the sidebar
        mentionable:
            whether the role should be mentionable
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_ROLES)
    @route(method="DELETE", path="/guilds/{guild_id}/roles/{role_id}")
    async def delete_guild_role(self, guild_id: Snowflake, role_id: Snowflake, reason: str = None) -> None:
        """
        Delete a guild role.
        Requires the `MANAGE_ROLES` permission.
        Returns a 204 empty response on success.
        Fires a [Guild Role Delete](https://discord.com/developers/docs/topics/gateway#guild_role_delete) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.KICK_MEMBERS)
    @route(method="GET", path="/guilds/{guild_id}/prune")
    async def get_guild_prune_count(
        self, guild_id: Snowflake, *, days: int = 7, include_roles: list[Snowflake] = None
    ) -> dict:
        """
        Returns an object with one 'pruned' key indicating the number of members that would be removed in a prune operation.
        Requires the `KICK_MEMBERS` permission.

        Parameters
        ----------
        days:
            number of days to count prune for
        include_roles:
            role
        """

    @permissions(Bitwise_Permission_Flags.KICK_MEMBERS)
    @route(method="POST", path="/guilds/{guild_id}/prune")
    async def begin_guild_prune(
        self,
        guild_id: Snowflake,
        days: int = 7,
        compute_prune_count: bool = True,
        include_roles: list[Snowflake] = None,
        reason: Optional[str] = None,
    ) -> dict:
        """
        Begin a prune operation.
        Requires the KICK_MEMBERS permission.
        Returns an object with one 'pruned' key indicating the number of members that were removed in the prune operation.
        For large guilds it's recommended to set the compute_prune_count option to false, forcing 'pruned' to null.
        Fires multiple [Guild Member Remove](https://discord.com/developers/docs/topics/gateway#guild_member_remove) Gateway events.

        Parameters
        ----------
        days:
            number of days to prune
        compute_prune_count:
            whether 'pruned' is returned, discouraged for large guilds
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
        await self.api_call(path=f"/guilds/{guild_id}/integrations", method="POST", json={"type": type, "id": id})

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
        Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild_integrations_update) Gateway event.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="POST", path="/guilds/{guild_id}/integrations/{integration_id}/sync")
    async def sync_guild_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> None:
        pass

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="GET", path="/guilds/{guild_id}/widget")
    async def get_guild_widget_settings(self, guild_id: Snowflake) -> Guild_Widget:
        """
        Returns a [guild widget](https://discord.com/developers/docs/resources/guild#guild_widget_object) object.
        Requires the MANAGE_GUILD permission.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_GUILD)
    @route(method="PATCH", path="/guilds/{guild_id}/widget")
    async def modify_guild_widget(
        self, guild_id: Snowflake, guild_widget: Guild_Widget = None, reason: str = None
    ) -> Guild_Widget:
        """
        Modify a [guild widget](https://discord.com/developers/docs/resources/guild#guild_widget_object) object for the guild.
        All attributes may be passed in with JSON and modified.
        Requires the MANAGE_GUILD permission.
        Returns the updated [guild widget](https://discord.com/developers/docs/resources/guild#guild_widget_object) object.
        """

    @route(method="GET", path="/guilds/{guild_id}/widget.json")
    async def get_guild_widget(self, guild_id: Snowflake) -> Guild_Widget:
        """
        Returns the widget for the guild.
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
    async def get_guild_widget_image(self, guild_id: Snowflake, *, style: str = "shield") -> dict:
        """
        Returns a PNG image widget for the guild.
        Requires no permissions or authentication.
        Widget Style Options
        | Value   | Description                                                                                                                                                    | Example                                                                              |
        | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
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
        Requires the MANAGE_GUILD permission.
        Returns the updated [Welcome Screen](https://discord.com/developers/docs/resources/guild#welcome_screen_object) object.

        Parameters
        ----------
        enabled:
            whether the welcome screen is enabled
        welcome_channels:
            channels linked in the welcome screen and their display options
        description:
            the server description to show in the welcome screen
        """

    @route(method="PATCH", path="/guilds/{guild_id}/voice-states/@me")
    async def modify_current_user_voice_state(
        self,
        guild_id: Snowflake,
        channel_id: Snowflake = None,
        suppress: Optional[bool] = None,
        request_to_speak_timestamp: Optional[datetime | UnsetType] = UNSET,
        reason: str = None,
    ) -> None:
        """
        Updates the current user's voice state.
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

    @route(method="GET", path="/invites/{invite_code}")
    async def get_invite(
        self, invite_code: str, *, with_counts: Optional[bool] = None, with_expiration: Optional[bool] = None
    ) -> Invite:
        """
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite_object) object for the given code.

        Parameters
        ----------
        with_counts:
            whether the invite should contain approximate member counts
        with_expiration:
            whether the invite should contain the expiration date
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_CHANNELS)
    @route(method="DELETE", path="/invites/{invite_code}")
    async def delete_invite(self, invite_code: str, reason: str = None) -> Invite:
        """
        Delete an invite.
        Requires the MANAGE_CHANNELS permission on the channel this invite belongs to, or MANAGE_GUILD to remove any invite across the guild.
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite_object) object on success.
        Fires a [Invite Delete](https://discord.com/developers/docs/topics/gateway#invite_delete) Gateway event.
        """

    @route(method="POST", path="/stage-instances")
    async def create_stage_instance(
        self, channel_id: Snowflake = None, topic: str = None, privacy_level: Optional[Privacy_Level] = None
    ) -> Stage_Instance:
        """
        Creates a new Stage instance associated to a Stage channel.

        Parameters
        ----------
        channel_id:
            The id of the Stage channel
        topic:
            The topic of the Stage instance
        privacy_level:
            Privacy_Level
        """

    @route(method="GET", path="/stage-instances/{channel_id}")
    async def get_stage_instance(self, channel_id: Snowflake) -> Stage_Instance:
        """
        Gets the stage instance associated with the Stage channel, if it exists.
        """

    @route(method="PATCH", path="/stage-instances/{channel_id}")
    async def modify_stage_instance(
        self, channel_id: Snowflake, topic: Optional[str] = None, privacy_level: Optional[Privacy_Level] = None
    ) -> Stage_Instance:
        """
        Updates fields of an existing Stage instance.

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
    async def modify_current_user(self, username: str = None, avatar: str | UnsetType = UNSET) -> User:
        """
        Modify the requester's user account settings.
        Returns a [user](https://discord.com/developers/docs/resources/user#user_object) object on success.

        Parameters
        ----------
        username:
            user's username, if changed may cause the user's discriminator to be randomized.
        avatar:
            if passed, modifies the user's avatar
        """

    @route(method="GET", path="/users/@me/guilds")
    async def get_current_user_guilds(
        self, *, before: Snowflake = None, after: Snowflake = None, limit: int = 200
    ) -> list[Guild]:
        """
        Returns a list of partial [guild](https://discord.com/developers/docs/resources/guild#guild_object) objects the current user is a member of.
        Requires the guilds OAuth2 scope.

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
        """

    @route(method="DELETE", path="/users/@me/guilds/{guild_id}")
    async def leave_guild(self, guild_id: Snowflake) -> None:
        """
        Leave a guild.
        Returns a 204 empty response on success.
        """

    @route(method="POST", path="/users/@me/channels")
    async def create_dm(self, recipient_id: Snowflake = None) -> Channel:
        """
        Create a new DM channel with a user.
        Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel_object) object.

        Parameters
        ----------
        recipient_id:
            the recipient to open a DM channel with
        """

    @route(method="POST", path="/users/@me/channels")
    async def create_group_dm(self, access_tokens: list[str] = None, nicks: dict = dict) -> Channel:
        """
        Create a new group DM channel with multiple users.
        Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel_object) object.
        This endpoint was intended to be used with the now_deprecated GameBridge SDK.
        DMs created with this endpoint will not be shown in the Discord client.

        Parameters
        ----------
        access_tokens:
            access tokens of users that have granted your app the `gdm.join` scope
        nicks:
            a dictionary of user ids to their respective nicknames
        """

    @route(method="GET", path="/users/@me/connections")
    async def get_user_connections(self) -> list[Connection]:
        """
        Returns a list of [connection](https://discord.com/developers/docs/resources/user#connection_object) objects.
        Requires the `connections` OAuth2 scope.
        """

    @route(method="GET", path="/voice/regions")
    async def list_voice_regions(self) -> list[Voice_Region]:
        """
        Returns an array of [voice region](https://discord.com/developers/docs/resources/voice#voice_region_object) objects that can be used when creating servers.
        """

    @permissions(Bitwise_Permission_Flags.MANAGE_WEBHOOKS)
    @route(method="POST", path="/channels/{channel_id}/webhooks")
    async def create_webhook(
        self, channel_id: Snowflake, name: str = None, avatar: Optional[str | UnsetType] = UNSET, reason: str = None
    ) -> Webhook:
        """
        Create a new webhook.
        Requires the `MANAGE_WEBHOOKS` permission.
        Returns a [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) object on success.
        Webhook names follow our naming restrictions that can be found in our [Usernames and Nicknames](https://discord.com/developers/docs/resources/user#usernames_and_nicknames) documentation, with the following additional stipulations:.

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
        avatar: str | UnsetType = UNSET,
        channel_id: Snowflake = None,
        reason: str = None,
    ) -> Webhook:
        """
        Modify a webhook.
        Requires the `MANAGE_WEBHOOKS` permission.
        Returns the updated [webhook](https://discord.com/developers/docs/resources/webhook#webhook_object) object on success.

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
        avatar: str | UnsetType = UNSET,
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
        Returns a 204 NO CONTENT response on success.
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
        *,
        wait: bool = None,
        thread_id: Snowflake = None,
    ) -> Message | None:
        """
        > info.

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
        wait:
            waits for server confirmation of message send before response, and returns the created message body
        thread_id:
            Send a message to the specified thread within a webhook's channel. The thread will automatically be unarchived.
        attachments:
            attachment objects with filename, content of file and description
        """

    @route(method="POST", path="/webhooks/{webhook_id}/{webhook_token}/slack")
    async def execute_slack_compatible_webhook(
        self, webhook_id: Snowflake, webhook_token: str, json: dict, *, wait: bool = None
    ) -> Webhook | None:
        """
        Refer to [Slack's documentation](https:##api.slack.com/incoming-webhooks) for more information.
        We do not support Slack's `channel`, `icon_emoji`, `mrkdwn`, or `mrkdwn_in` properties.

        Parameters
        ----------
        wait:
            waits for server confirmation of message send before response
        """

    @route(method="POST", path="/webhooks/{webhook_id}/{webhook_token}/github")
    async def execute_github_compatible_webhook(
        self, webhook_id: Snowflake, webhook_token: str, json: dict, *, wait: bool = None
    ) -> Message | None:
        """
        Add a new webhook to your GitHub repo (in the repo's settings), and use this endpoint as the 'Payload URL.' You can choose what events your Discord channel receives by choosing the 'Let me select individual events' option and selecting individual events for the new webhook you're configuring.

        Parameters
        ----------
        wait:
            waits for server confirmation of message send before response
        """

    @route(method="GET", path="/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    async def get_webhook_message(self, webhook_id: Snowflake, webhook_token: str, message_id: Snowflake) -> Message:
        """
        Returns a previously-sent webhook message from the same token.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message-object) object on success.
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
    ) -> Message:
        """
        Edits a previously_sent webhook message from the same token.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message_object) object on success.

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
            attached files to keep/add
        components:
            the components to include with the message
        """

    @route(method="DELETE", path="/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    async def delete_webhook_message(
        self, webhook_id: Snowflake, webhook_token: str, message_id: Snowflake, reason: str = None
    ) -> None:
        """
        Deletes a message that was created by the webhook.
        Returns a 204 NO CONTENT response on success.
        """

    @route(method="GET", path="/gateway")
    async def get_gateway(self) -> dict:
        """
        Returns an object with a single valid WSS URL, which the client can use for [Connecting](https://discord.com/developers/docs/topics/gateway#connecting).
        Clients **should** cache this value and only call this endpoint to retrieve a new URL if they are unable to properly establish a connection using the cached version of the URL.
        > info.
        """

    @route(method="GET", path="/gateway/bot")
    async def get_gateway_bot(self) -> Gateway_Bot:
        """
        Returns an object based on the information in [Get Gateway](https://discord.com/developers/docs/topics/gateway#get_gateway), plus additional metadata that can help during the operation of large or [sharded](https://discord.com/developers/docs/topics/gateway#sharding) bots.
        Unlike the [Get Gateway](https://discord.com/developers/docs/topics/gateway#get_gateway), this route should not be cached for extended periods of time as the value is not guaranteed to be the same per_call, and changes as the bot joins/leaves guilds.
        > warn.

        Parameters
        ----------
        url:
            The WSS URL that can be used for connecting to the gateway
        shards:
            Shards
        session_start_limit:
            Information on the current session start limit
        """

    @route(method="GET", path="/oauth2/applications/@me")
    async def get_current_bot_application_information(self) -> Application:
        """
        Returns the bot's [application](https://discord.com/developers/docs/resources/application#application_object) object without flags.
        """

    @route(method="GET", path="/oauth2/@me")
    async def get_current_authorization_information(self) -> dict:
        """
        Returns info about the current authorization.
        Requires authentication with a bearer token.
        Example Authorization Information
        ```json
        {
        'application': {
        'id': '159799960412356608',
        'name': 'AIRHORN SOLUTIONS',
        'icon': 'f03590d3eb764081d154a66340ea7d6d',
        'description': '',
        'summary': '',
        'hook': true,
        'bot_public': true,
        'bot_require_code_grant': false,
        'verify_key': 'c8cde6a3c8c6e49d86af3191287b3ce255872be1fff6dc285bdb420c06a2c3c8'
        },
        'scopes': [
        'guilds.join',
        'identify'
        ],
        'expires': '2021-01-23T02:33:17.017000+00:00',
        'user': {
        'id': '268473310986240001',
        'username': 'Discord',
        'avatar': 'f749bb0cbeeb26ef21eca719337d20f1',
        'discriminator': '0001',
        'public_flags': 131072
        }
        }
        ```.
        """

    @route(method="GET", path="/applications/{application_id}/commands")
    async def get_global_application_commands(
        self, application_id: Snowflake, *, with_localizations: bool = False
    ) -> list[Application_Command]:
        """
        Fetch all of the global commands for your application.
        Returns an array of [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) objects.
        """

    @route(method="POST", path="/applications/{application_id}/commands")
    async def create_global_application_command(
        self,
        application_id: Snowflake,
        name: str = None,
        description: str = None,
        options: Optional[Application_Command_Option] = None,
        default_permission: Optional[bool] = None,
        type: Application_Command_Type = Application_Command_Type.CHAT_INPUT,
    ) -> Application_Command:
        """
        Create a new global command.
        New global commands will be available in all guilds after 1 hour.
        Returns 201 and an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        > danger.

        Parameters
        ----------
        name:
            1-32 lowercase character name matching `^[\\w-]{1,32}$`
        description:
            1-100 character description
        options:
            the parameters for the command
        default_permission:
            whether the command is enabled by default when the app is added to a guild
        """

    @route(method="GET", path="/applications/{application_id}/commands/{command_id}")
    async def get_global_application_command(
        self, application_id: Snowflake, command_id: Snowflake
    ) -> Application_Command:
        """
        Fetch a global command for your application.
        Returns an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        """

    @route(method="PATCH", path="/applications/{application_id}/commands/{command_id}")
    async def edit_global_application_command(
        self,
        application_id: Snowflake,
        command_id: Snowflake,
        name: str = None,
        description: str = None,
        options: Optional[list[Application_Command_Option]] = None,
        default_permission: Optional[bool] = None,
    ) -> Application_Command:
        """
        Edit a global command.
        Updates will be available in all guilds after 1 hour.
        Returns 200 and an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        > info.

        Parameters
        ----------
        name:
            1-32 lowercase character name matching `^[\\w-]{1,32}$`
        description:
            1-100 character description
        options:
            the parameters for the command
        default_permission:
            whether the command is enabled by default when the app is added to a guild
        """

    @route(method="DELETE", path="/applications/{application_id}/commands/{command_id}")
    async def delete_global_application_command(self, application_id: Snowflake, command_id: Snowflake) -> None:
        """
        Deletes a global command.
        Returns `204`.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def get_guild_application_commands(
        self, application_id: Snowflake, guild_id: Snowflake, *, with_localizations: bool = False
    ) -> list[Application_Command]:
        """
        Fetch all of the guild commands for your application for a specific guild.
        Returns an array of [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) objects.
        """

    @route(method="PUT", path="/applications/{application_id}/commands")
    async def bulk_overwrite_global_application_commands(
        self, application_id: Snowflake, application_commands: list[Application_Command]
    ) -> list[Application_Command]:
        """
        Takes a list of application commands, overwriting existing commands that are registered globally for this application.
        Updates will be available in all guilds after 1 hour.
        Returns 200 and a list of [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) objects.
        Commands that do not already exist will count toward daily application command create limits.
        """

    @route(method="POST", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def create_guild_application_command(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        name: str = None,
        description: str = None,
        options: Optional[list[Application_Command_Option]] = None,
        default_permission: Optional[bool] = None,
        type: Application_Command_Type = Application_Command_Type.CHAT_INPUT,
    ) -> Application_Command:
        """
        Create a new guild command.
        New guild commands will be available in the guild immediately.
        Returns 201 and an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        If the command did not already exist, it will count toward daily application command create limits.
        > danger.

        Parameters
        ----------
        name:
            1-32 lowercase character name matching `^[\\w-]{1,32}$`
        description:
            1-100 character description
        options:
            the parameters for the command
        default_permission:
            whether the command is enabled by default when the app is added to a guild
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def get_guild_application_command(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> Application_Command:
        """
        Fetch a guild command for your application.
        Returns an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        """

    @route(method="PATCH", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def edit_guild_application_command(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        command_id: Snowflake,
        name: str = None,
        description: str = None,
        options: Optional[list[Application_Command_Option]] = None,
        default_permission: Optional[bool] = None,
    ) -> Application_Command:
        """
        Edit a guild command.
        Updates for guild commands will be available immediately.
        Returns 200 and an [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) object.
        > info.

        Parameters
        ----------
        name:
            1-32 lowercase character name matching `^[\\w-]{1,32}$`
        description:
            1-100 character description
        options:
            the parameters for the command
        default_permission:
            whether the command is enabled by default when the app is added to a guild
        """

    @route(method="DELETE", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}")
    async def delete_guild_application_command(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> None:
        """
        Delete a guild command.
        Returns `204` on success.
        """

    @route(method="PUT", path="/applications/{application_id}/guilds/{guild_id}/commands")
    async def bulk_overwrite_guild_application_commands(
        self, application_id: Snowflake, guild_id: Snowflake, application_commands: list[Application_Command]
    ) -> list[Application_Command]:
        """
        Takes a list of application commands, overwriting existing commands for the guild.
        Returns `200` and a list of [application command](https://discord.com/developers/docs/interactions/slash_commands#application_command_object) objects.
        """

    @route(method="POST", path="/interactions/{interaction_id}/{interaction_token}/callback")
    async def create_interaction_response(
        self, interaction_id: Snowflake, interaction_token: str, response: Interaction_Response
    ) -> None:
        """
        Create a response to an Interaction from the gateway.
        Takes an [interaction response](https://discord.com/developers/docs/interactions/slash_commands#interaction_response_object).
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
        Returns `204` on success.
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
        flags: int = None,
    ) -> Message:
        """
        Create a followup message for an Interaction.
        Functions the same as [Execute Webhook](https://discord.com/developers/docs/resources/webhook#execute_webhook), but wait is always true, and flags can be set to 64 in the body to send an ephemeral message.
        The thread_id query parameter is not required (and is furthermore ignored) when using this endpoint for interaction followups.
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
        Returns `204` on success.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/permissions")
    async def get_guild_application_command_permissions(
        self, application_id: Snowflake, guild_id: Snowflake
    ) -> list[Guild_Application_Command_Permissions]:
        """
        Fetches command permissions for all commands for your application in a guild.
        Returns an array of [guild application command permissions](https://discord.com/developers/docs/interactions/slash_commands#application_command_permissions_object_guild_application_command_permissions_structure) objects.
        """

    @route(method="GET", path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions")
    async def get_application_command_permissions(
        self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake
    ) -> Guild_Application_Command_Permissions:
        """
        Fetches command permissions for a specific command for your application in a guild.
        Returns a [guild application command permissions](https://discord.com/developers/docs/interactions/slash_commands#application_command_permissions_object_guild_application_command_permissions_structure) object.
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
        Returns a [Guild_Application_Command_Permissions](https://discord.com/developers/docs/interactions/slash_commands#application_command_permissions_object_guild_application_command_permissions_structure) object.
        > warn.

        Parameters
        ----------
        permissions:
            the permissions for the command in the guild
        """

    @route(method="PUT", path="/applications/{application_id}/guilds/{guild_id}/commands/permissions")
    async def batch_edit_application_command_permissions(
        self,
        application_id: Snowflake,
        guild_id: Snowflake,
        command_permissions: list[Guild_Application_Command_Permissions],
        reason: str = None,
    ) -> list[Guild_Application_Command_Permissions]:
        """
        Returns an array of [Guild_Application_Command_Permissions](https://discord.com/developers/docs/interactions/slash_commands#application_command_permissions_object_guild_application_command_permissions_structure) objects.
        """
