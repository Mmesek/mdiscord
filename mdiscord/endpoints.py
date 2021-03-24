# -*- coding: utf-8 -*-
'''
Discord Endpoints
----------

Discord API Endpoint call functions.

:copyright: (c) 2021 Mmesek

'''

from typing import List
from .types import (Snowflake, Channel, Message, Audit_Log, Overwrite, Embed, 
    Allowed_Mentions, Message_Reference, Followed_Channel, 
    User, Invite, Emoji, Role, Guild, Ban, Webhook, 
    Guild_Preview, Guild_Member, Guild_Widget, Voice_Region, Connection, 
    Integration, Application, Application_Command, Application_Command_Option, Interaction_Response)
from .utils import Permissions
from .serializer import as_dict

class Endpoints:
    async def api_call(self, path: str, method: str = "GET", reason: str = None, **kwargs):
        raise NotImplementedError
    
    @Permissions("VIEW_AUDIT_LOG")
    async def get_guild_audit_log(self, guild_id: Snowflake, user_id: Snowflake = None, action_type: int = None, before: int = None, limit: int = None) -> Audit_Log:
        '''
        Returns an [audit log](https://discord.com/developers/docs/resources/audit_log#audit-log-object) object for the guild. Requires the 'VIEW_AUDIT_LOG' permission.

        Params:
            :user_id: filter the log for actions made by a user
            :action_type: Audit_Log_Event
            :before: filter the log before a certain entry id
            :limit: how many entries are returned
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/audit-logs", method = "GET", params = {"user_id": user_id, "action_type": action_type, "before": before, "limit": limit})
        return Audit_Log(**r)

    async def get_channel(self, channel_id: Snowflake) -> Channel:
        '''
        Get a channel by ID. Returns a [channel](https://discord.com/developers/docs/resources/channel#channel-object) object.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}", method = "GET")
        return Channel(**r)

    @Permissions("MANAGE_CHANNELS")
    async def modify_channel(self, channel_id: Snowflake, name: str=None, type: int=None, position: int=None, topic: str=None, nsfw: bool=None, rate_limit_per_user: int=None, bitrate: int=None, user_limit: int=None, permission_overwrites: List[Overwrite]=None, parent_id: Snowflake=None, reason: str=None) -> Channel:
        '''
        Update a channel's settings. Requires the `MANAGE_CHANNELS` permission for the guild. Returns a [channel](https://discord.com/developers/docs/resources/channel#channel-object) on success, and a 400 BAD REQUEST on invalid parameters. Fires a [Channel Update](https://discord.com/developers/docs/topics/gateway#channel-update) Gateway event. If modifying a category, individual [Channel Update](https://discord.com/developers/docs/topics/gateway#channel-update) events will fire for each child channel that also changes. All JSON parameters are optional.

        Params:
            :name: 2-100 character channel name
            :type: Type_Of_Channel
            :position: the position of the channel in the left-hand listing
            :topic: 0-1024 character channel topic
            :nsfw: whether the channel is nsfw
            :rate_limit_per_user: amount of seconds a user has to wait before sending another message
            :bitrate: the bitrate
            :user_limit: the user limit of the voice channel; 0 refers to no limit, 1 to 99 refers to a user limit
            :permission_overwrites: channel
            :parent_id: id of the new parent category for a channel
        '''
        r = await self.api_call(path = f"/channels/{channel_id}", method = "PATCH", json = {"name": name, "type": type, "position": position, "topic": topic, "nsfw": nsfw, "rate_limit_per_user": rate_limit_per_user, "bitrate": bitrate, "user_limit": user_limit, "permission_overwrites": permission_overwrites, "parent_id": parent_id}, reason=reason)
        return Channel(**r)

    @Permissions("MANAGE_CHANNELS")
    async def delete_close_channel(self, channel_id: Snowflake) -> Channel:
        '''
        Delete a channel, or close a private message. Requires the `MANAGE_CHANNELS` permission for the guild. Deleting a category does not delete its child channels; they will have their `parent_id` removed and a [Channel Update](https://discord.com/developers/docs/topics/gateway#channel-update) Gateway event will fire for each of them. Returns a [channel](https://discord.com/developers/docs/resources/channel#channel-object) object on success. Fires a [Channel Delete](https://discord.com/developers/docs/topics/gateway#channel-delete) Gateway event.
        > warn
        > Deleting a guild channel cannot be undone. Use this with caution, as it is impossible to undo this action when performed on a guild channel. In contrast, when used with a private message, it is possible to undo the action by opening a private message with the recipient again.
        > info
        > For Community guilds, the Rules or Guidelines channel and the Community Updates channel cannot be deleted.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}", method = "DELETE")
        return Channel(**r)

    @Permissions("VIEW_CHANNEL")
    async def get_channel_messages(self, channel_id: Snowflake, around: int=None, before: int=None, after: int=None, limit: int=50) -> List[Message]:
        '''
        Returns the messages for a channel. If operating on a guild channel, this endpoint requires the `VIEW_CHANNEL` permission to be present on the current user. If the current user is missing the 'READ_MESSAGE_HISTORY' permission in the channel then this will return no messages (since they cannot read the message history). Returns an array of [message](https://discord.com/developers/docs/resources/channel#message-object) objects on success.
        > info
        > The before, after, and around keys are mutually exclusive, only one may be passed at a time.

        Params:
            :around: get messages around this message ID
            :before: get messages before this message ID
            :after: get messages after this message ID
            :limit: max number of messages to return
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/messages", method = "GET", params = {"around": around, "before": before, "after": after, "limit": limit})
        return [Message(**i) for i in r]

    @Permissions("READ_MESSAGE_HISTORY")
    async def get_channel_message(self, channel_id: Snowflake, message_id: Snowflake) -> Message:
        '''
        Returns a specific message in the channel. If operating on a guild channel, this endpoint requires the 'READ_MESSAGE_HISTORY' permission to be present on the current user. Returns a [message](https://discord.com/developers/docs/resources/channel#message-object) object on success.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}", method = "GET")
        return Message(**r)

    @Permissions("SEND_MESSAGES", "READ_MESSAGE_HISTORY")
    async def create_message(self, channel_id: Snowflake=None, content: str=None, nonce: int=None, tts: bool=None, file: bytes=None, filename: str="file.txt", embed: Embed=None, payload_json: str=None, allowed_mentions: Allowed_Mentions=Allowed_Mentions(parse=[]), message_reference: Message_Reference=None) -> Message:
        '''
        > warn
        > Before using this endpoint, you must connect to and identify with a [gateway](https://discord.com/developers/docs/topics/gateway#gateways) at least once.
        > warn
        > Discord may strip certain characters from message content, like invalid unicode characters or characters which cause unexpected message formatting. If you are passing user-generated strings into message content, consider sanitizing the data to prevent unexpected behavior and utilizing `allowed_mentions` to prevent unexpected mentions.
        Post a message to a guild text or DM channel. If operating on a guild channel, this endpoint requires the `SEND_MESSAGES` permission to be present on the current user. If the `tts` field is set to `true`, the `SEND_TTS_MESSAGES` permission is required for the message to be spoken. Returns a [message](https://discord.com/developers/docs/resources/channel#message-object) object. Fires a [Message Create](https://discord.com/developers/docs/topics/gateway#message-create) Gateway event. See [message formatting](https://discord.com/developers/docs/reference#message-formatting) for more information on how to properly format messages.
        The maximum request size when sending a message is 8MB.
        This endpoint supports requests with `Content-Type`s of both `application/json` and `multipart/form-data`. You must however use `multipart/form-data` when uploading files. Note that when sending `multipart/form-data` requests the `embed` field cannot be used, however you can pass a JSON encoded body as form value for `payload_json`, where additional request parameters such as `embed` can be set.
        > info
        > Note that when sending `application/json` you must send at least one of `content` or `embed`, and when sending `multipart/form-data`, you must send at least one of `content`, `embed` or `file`. For a `file` attachment, the `Content-Disposition` subpart header MUST contain a `filename` parameter.
        You may create a message as a reply to another message. To do so, include a [`message_reference`](https://discord.com/developers/docs/resources/channel#message-object-message-reference-structure) with a `message_id`. This requires the `READ_MESSAGE_HISTORY` permission, and the referenced message must exist and cannot be a system message. The `channel_id` and `guild_id` in the `message_reference` are optional, but will be validated if provided.

        Params:
            :content: the message contents
            :nonce: a nonce that can be used for optimistic message sending
            :tts: true if this is a TTS message
            :file: the contents of the file being sent
            :embed: embedded `rich` content
            :payload_json: JSON encoded body of any additional request fields.
            :allowed_mentions: allowed mentions for a message
            :message_reference: include to make your message a reply
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/messages", method = "POST", json = {"content": content, "nonce": nonce, "tts": tts, "embed": embed, "payload_json": payload_json, "allowed_mentions": allowed_mentions, "message_reference": message_reference}, file=file, filename=filename)
        return Message(**r)

    @Permissions("SEND_MESSAGES")
    async def crosspost_message(self, channel_id: Snowflake, message_id: Snowflake) -> Message:
        '''
        Crosspost a message in a News Channel to following channels. This endpoint requires the 'SEND_MESSAGES' permission, if the current user sent the message, or additionally the 'MANAGE_MESSAGES' permission, for all other messages, to be present for the current user.
        Returns a [message](https://discord.com/developers/docs/resources/channel#message-object) object.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/crosspost", method = "POST")
        return Message(**r)
    
    @Permissions("READ_MESSAGE_HISTORY", "ADD_REACTIONS")
    async def create_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> None:
        '''
        Create a reaction for the message. This endpoint requires the 'READ_MESSAGE_HISTORY' permission to be present on the current user. Additionally, if nobody else has reacted to the message using this emoji, this endpoint requires the 'ADD_REACTIONS' permission to be present on the current user. Returns a 204 empty response on success.
        The `emoji` must be [URL Encoded](https:#/en.wikipedia.org/wiki/Percent-encoding) or the request will fail with `10014: Unknown Emoji`.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", method = "PUT")
    
    async def delete_own_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: int) -> None:
        '''
        Delete a reaction the current user has made for the message. Returns a 204 empty response on success.
        The `emoji` must be [URL Encoded](https:#/en.wikipedia.org/wiki/Percent-encoding) or the request will fail with `10014: Unknown Emoji`.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", method = "DELETE")
    
    @Permissions("MANAGE_MESSAGES")
    async def delete_user_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: int, user_id: Snowflake) -> None:
        '''
        Deletes another user's reaction. This endpoint requires the 'MANAGE_MESSAGES' permission to be present on the current user. Returns a 204 empty response on success.
        The `emoji` must be [URL Encoded](https:#/en.wikipedia.org/wiki/Percent-encoding) or the request will fail with `10014: Unknown Emoji`.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}", method = "DELETE")
    
    async def get_reactions(self, channel_id: Snowflake, message_id: Snowflake, emoji: int, before: int=None, after: int=None, limit: int=25) -> List[User]:
        '''
        Get a list of users that reacted with this emoji. Returns an array of [user](https://discord.com/developers/docs/resources/user#user-object) objects on success.
        The `emoji` must be [URL Encoded](https:#/en.wikipedia.org/wiki/Percent-encoding) or the request will fail with `10014: Unknown Emoji`.

        Params:
            :before: get users before this user ID
            :after: get users after this user ID
            :limit: max number of users to return
        '''
        params = {'limit': limit}
        if before:
            params['before'] = before
        else:
            params['after'] = after
        r = await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}", method = "GET", params = params)
        return [User(**i) for i in r]

    @Permissions("MANAGE_MESSAGES")
    async def delete_all_reactions(self, channel_id: Snowflake, message_id: Snowflake) -> None:
        '''
        Deletes all reactions on a message. This endpoint requires the 'MANAGE_MESSAGES' permission to be present on the current user. Fires a [Message Reaction Remove All](https://discord.com/developers/docs/topics/gateway#message-reaction-remove-all) Gateway event.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions", method = "DELETE")

    @Permissions("MANAGE_MESSAGES")
    async def delete_all_reactions_for_emoji(self, channel_id: Snowflake, message_id: Snowflake, emoji: int) -> None:
        '''
        Deletes all the reactions for a given emoji on a message. This endpoint requires the `MANAGE_MESSAGES` permission to be present on the current user. Fires a [Message Reaction Remove Emoji](https://discord.com/developers/docs/topics/gateway#message-reaction-remove-emoji) Gateway event.
        The `emoji` must be [URL Encoded](https:#/en.wikipedia.org/wiki/Percent-encoding) or the request will fail with `10014: Unknown Emoji`.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}", method = "DELETE")

    async def edit_message(self, channel_id: Snowflake, message_id: Snowflake, content: str, embed: Embed, flags: int, allowed_mentions: Allowed_Mentions) -> Message:
        '''
        Edit a previously sent message. The fields `content`, `embed`, `allowed_mentions` and `flags` can be edited by the original message author. Other users can only edit `flags` and only if they have the `MANAGE_MESSAGES` permission in the corresponding channel. When specifying flags, ensure to include all previously set flags/bits in addition to ones that you are modifying. Only `flags` documented in the table below may be modified by users (unsupported flag changes are currently ignored without error).
        Returns a [message](https://discord.com/developers/docs/resources/channel#message-object) object. Fires a [Message Update](https://discord.com/developers/docs/topics/gateway#message-update) Gateway event.
        > info
        > All parameters to this endpoint are optional and nullable.

        Params:
            :content: the new message contents
            :embed: embedded `rich` content
            :flags: Flags
            :allowed_mentions: allowed mentions for the message
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}", method = "PATCH", json = {"content": content, "embed": embed, "flags": flags, "allowed_mentions": allowed_mentions})
        return Message(**r)

    @Permissions("MANAGE_MESSAGES")
    async def delete_message(self, channel_id: Snowflake, message_id: Snowflake) -> None:
        '''
        Delete a message. If operating on a guild channel and trying to delete a message that was not sent by the current user, this endpoint requires the `MANAGE_MESSAGES` permission. Returns a 204 empty response on success. Fires a [Message Delete](https://discord.com/developers/docs/topics/gateway#message-delete) Gateway event.
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/{message_id}", method = "DELETE")

    @Permissions("MANAGE_MESSAGES")
    async def bulk_delete_messages(self, channel_id: Snowflake, messages: List[int]) -> None:
        '''
        Delete multiple messages in a single request. This endpoint can only be used on guild channels and requires the `MANAGE_MESSAGES` permission. Returns a 204 empty response on success. Fires a [Message Delete Bulk](https://discord.com/developers/docs/topics/gateway#message-delete-bulk) Gateway event.
        Any message IDs given that do not exist or are invalid will count towards the minimum and maximum message count (currently 2 and 100 respectively).
        > warn
        > This endpoint will not delete messages older than 2 weeks, and will fail with a 400 BAD REQUEST if any message provided is older than that or if any duplicate message IDs are provided.

        Params:
            :messages: an  message ids to delete
        '''
        await self.api_call(path = f"/channels/{channel_id}/messages/bulk-delete", method = "POST", json = {"messages": messages})

    @Permissions("MANAGE_ROLES")
    async def edit_channel_permissions(self, channel_id: Snowflake, overwrite_id: Snowflake, allow: str, deny: str, type: int) -> None:
        '''
        Edit the channel permission overwrites for a user or role in a channel. Only usable for guild channels. Requires the `MANAGE_ROLES` permission. Returns a 204 empty response on success. For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions).
        
        Params:
            :allow: the bitwise value of all allowed permissions
            :deny: the bitwise value of all disallowed permissions
            :type: 0 for a role
        '''
        await self.api_call(path = f"/channels/{channel_id}/permissions/{overwrite_id}", method = "PUT", json = {"allow": allow, "deny": deny, "type": type})
    
    @Permissions("MANAGE_CHANNELS")
    async def get_channel_invites(self, channel_id: Snowflake) -> List[Invite]:
        '''
        Returns a list of [invite](https://discord.com/developers/docs/resources/invite#invite-object) objects (with [invite metadata](https://discord.com/developers/docs/resources/invite#invite-metadata-object)) for the channel. Only usable for guild channels. Requires the `MANAGE_CHANNELS` permission.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/invites", method = "GET")
        return [Invite(**i) for i in r]
    
    @Permissions("CREATE_INSTANT_INVITE")
    async def create_channel_invite(self, channel_id: Snowflake, max_age: int=86400, max_uses: int=0, temporary: bool=False, unique: bool=False, target_user: str=None, target_user_type: int=None) -> Invite:
        '''
        Create a new [invite](https://discord.com/developers/docs/resources/invite#invite-object) object for the channel. Only usable for guild channels. Requires the `CREATE_INSTANT_INVITE` permission. All JSON parameters for this route are optional, however the request body is not. If you are not sending any fields, you still have to send an empty JSON object (`{}`). Returns an [invite](https://discord.com/developers/docs/resources/invite#invite-object) object. Fires an [Invite Create](https://discord.com/developers/docs/topics/gateway#invite-create) Gateway event.
        
        Params:
            :max_age: duration of invite in seconds before expiry,
            :max_uses: max number of uses
            :temporary: whether this invite only grants temporary membership
            :unique: if true, don't try to reuse a similar invite
            :target_user: the target user id for this invite
            :target_user_type: the type of target user for this invite
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/invites", method = "POST", json = {"max_age": max_age, "max_uses": max_uses, "temporary": temporary, "unique": unique, "target_user": target_user, "target_user_type": target_user_type})
        return Invite(**r)
    
    @Permissions("MANAGE_ROLES")
    async def delete_channel_permission(self, channel_id: Snowflake, overwrite_id: Snowflake) -> None:
        '''
        Delete a channel permission overwrite for a user or role in a channel. Only usable for guild channels. Requires the `MANAGE_ROLES` permission. Returns a 204 empty response on success. For more information about permissions, see [permissions](https://discord.com/developers/docs/topics/permissions#permissions)
        '''
        await self.api_call(path = f"/channels/{channel_id}/permissions/{overwrite_id}", method = "DELETE")
    
    @Permissions("MANAGE_WEBHOOKS")
    async def follow_news_channel(self, channel_id: Snowflake, webhook_channel_id: Snowflake) -> Followed_Channel:
        '''
        Follow a News Channel to send messages to a target channel. Requires the `MANAGE_WEBHOOKS` permission in the target channel. Returns a [followed channel](https://discord.com/developers/docs/resources/channel#followed-channel-object) object.
        
        Params:
            :webhook_channel_id: id of target channel
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/followers", method = "POST", json = {"webhook_channel_id": webhook_channel_id})
        return Followed_Channel(**r)
    
    async def trigger_typing_indicator(self, channel_id: Snowflake) -> None:
        '''
        Post a typing indicator for the specified channel. Generally bots should **not** implement this route. However, if a bot is responding to a command and expects the computation to take a few seconds, this endpoint may be called to let the user know that the bot is processing their message. Returns a 204 empty response on success. Fires a [Typing Start](https://discord.com/developers/docs/topics/gateway#typing-start) Gateway event.
        '''
        await self.api_call(path = f"/channels/{channel_id}/typing", method = "POST")
    
    async def get_pinned_messages(self, channel_id: Snowflake) -> Message:
        '''
        Returns all pinned messages in the channel as an array of [message](https://discord.com/developers/docs/resources/channel#message-object) objects.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/pins", method = "GET")
        return Message(**r)
    
    @Permissions("MANAGE_MESSAGES")
    async def add_pinned_channel_message(self, channel_id: Snowflake, message_id: Snowflake) -> None:
        '''
        Pin a message in a channel. Requires the `MANAGE_MESSAGES` permission. Returns a 204 empty response on success.
        > warn
        > The max pinned messages is 50.
        '''
        await self.api_call(path = f"/channels/{channel_id}/pins/{message_id}", method = "PUT")
    
    @Permissions("MANAGE_MESSAGES")
    async def delete_pinned_channel_message(self, channel_id: Snowflake, message_id: Snowflake) -> None:
        '''
        Delete a pinned message in a channel. Requires the `MANAGE_MESSAGES` permission. Returns a 204 empty response on success.
        '''
        await self.api_call(path = f"/channels/{channel_id}/pins/{message_id}", method = "DELETE")
    
    async def group_dm_add_recipient(self, channel_id: Snowflake, user_id: Snowflake, access_token: str, nick: str) -> None:
        '''
        Adds a recipient to a Group DM using their access token
        
        Params:
            :access_token: access token of a user that has granted your app the `gdm.join` scope
            :nick: nickname of the user being added
        '''
        await self.api_call(path = f"/channels/{channel_id}/recipients/{user_id}", method = "PUT", json = {"access_token": access_token, "nick": nick})
    
    async def group_dm_remove_recipient(self, channel_id: Snowflake, user_id: Snowflake) -> None:
        '''
        Removes a recipient from a Group DM
        '''
        await self.api_call(path = f"/channels/{channel_id}/recipients/{user_id}", method = "DELETE")
    
    async def list_guild_emojis(self, guild_id: Snowflake) -> List[Emoji]:
        '''
        Returns a list of [emoji](https://discord.com/developers/docs/resources/emoji#emoji-object) objects for the given guild.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/emojis", method = "GET")
        return [Emoji(**i) for i in r]
    
    async def get_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> Emoji:
        '''
        Returns an [emoji](https://discord.com/developers/docs/resources/emoji#emoji-object) object for the given guild and emoji IDs.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/emojis/{emoji_id}", method = "GET")
        return Emoji(**r)
    
    @Permissions("MANAGE_EMOJIS")
    async def create_guild_emoji(self, guild_id: Snowflake, name: str, image: str, roles: List[int]) -> Emoji:
        '''
        Create a new emoji for the guild. Requires the `MANAGE_EMOJIS` permission. Returns the new [emoji](https://discord.com/developers/docs/resources/emoji#emoji-object) object on success. Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway#guild-emojis-update) Gateway event.
        > warn
        > Emojis and animated emojis have a maximum file size of 256kb. Attempting to upload an emoji larger than this limit will fail and return 400 Bad Request and an error message, but not a [JSON status code](https://discord.com/developers/docs/topics/opcodes_and_status_codes#json).
        
        Params:
            :name: name of the emoji
            :image: the 128x128 emoji image
            :roles: roles for which this emoji will be whitelisted
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/emojis", method = "POST", json = {"name": name, "image": image, "roles": roles})
        return Emoji(**r)
    
    @Permissions("MANAGE_EMOJIS")
    async def modify_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, name: str, roles: List[int]=None) -> Emoji:
        '''
        Modify the given emoji. Requires the `MANAGE_EMOJIS` permission. Returns the updated [emoji](https://discord.com/developers/docs/resources/emoji#emoji-object) object on success. Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway#guild-emojis-update) Gateway event.
        > info
        > All parameters to this endpoint are optional.
        
        Params:
            :name: name of the emoji
            :roles: roles to which this emoji will be whitelisted
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/emojis/{emoji_id}", method = "PATCH", json = {"name": name, "roles": roles})
        return Emoji(**r)
    
    @Permissions("MANAGE_EMOJIS")
    async def delete_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> None:
        '''
        Delete the given emoji. Requires the `MANAGE_EMOJIS` permission. Returns `204 No Content` on success. Fires a [Guild Emojis Update](https://discord.com/developers/docs/topics/gateway#guild-emojis-update) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/emojis/{emoji_id}", method = "DELETE")
    
    async def create_guild(self, name: str, region: str=None, icon: str=None, verification_level: int=None, default_message_notifications: int=None, explicit_content_filter: int=None, roles: List[Role]=None, channels: List[Channel]=None, afk_channel_id: Snowflake=None, afk_timeout: int=None, system_channel_id: Snowflake=None) -> Guild:
        '''
        Create a new guild. Returns a [guild](https://discord.com/developers/docs/resources/guild#guild-object) object on success. Fires a [Guild Create](https://discord.com/developers/docs/topics/gateway#guild-create) Gateway event.
        > warn
        > This endpoint can be used only by bots in less than 10 guilds.
        
        Params:
            :name: name of the guild
            :region: Voice_Region
            :icon: base64 128x128 image for the guild icon
            :verification_level: Verification_Level
            :default_message_notifications: Message_Notification_Level
            :explicit_content_filter: Explicit_Content_Filter_Level
            :roles: new guild roles
            :channels: new guild's channels
            :afk_channel_id: id for afk channel
            :afk_timeout: afk timeout in seconds
            :system_channel_id: the id of the channel where guild notices such as welcome messages and boost events are posted
        '''
        r = await self.api_call(path = f"/guilds", method = "POST", json = {"name": name, "region": region, "icon": icon, "verification_level": verification_level, "default_message_notifications": default_message_notifications, "explicit_content_filter": explicit_content_filter, "roles": roles, "channels": channels, "afk_channel_id": afk_channel_id, "afk_timeout": afk_timeout, "system_channel_id": system_channel_id})
        return Guild(**r)
    
    async def get_guild(self, guild_id: Snowflake, with_counts: bool=False) -> Guild:
        '''
        Returns the [guild](https://discord.com/developers/docs/resources/guild#guild-object) object for the given id. If `with_counts` is set to `true`, this endpoint will also return `approximate_member_count` and `approximate_presence_count` for the guild.
        
        Params:
            :with_counts: when `true`, will return approximate member and presence counts for the guild
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}", method = "GET", params = {"with_counts": with_counts})
        return Guild(**r)
    
    async def get_guild_preview(self, guild_id: Snowflake) -> Guild_Preview:
        '''
        Returns the [guild preview](https://discord.com/developers/docs/resources/guild#guild-preview-object) object for the given id. If the user is not in the guild, then the guild must be Discoverable.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/preview", method = "GET")
        return Guild_Preview(**r)
    
    @Permissions("MANAGE_GUILD")
    async def modify_guild(self, guild_id: Snowflake, name: str, afk_timeout: int, icon: str, owner_id: Snowflake, splash: str, banner: str, region: str=None, verification_level: int=None, default_message_notifications: int=None, explicit_content_filter: int=None, afk_channel_id: Snowflake=None, system_channel_id: Snowflake=None, rules_channel_id: Snowflake=None, public_updates_channel_id: Snowflake=None, preferred_locale: str=None) -> Guild:
        '''
        Modify a guild's settings. Requires the `MANAGE_GUILD` permission. Returns the updated [guild](https://discord.com/developers/docs/resources/guild#guild-object) object on success. Fires a [Guild Update](https://discord.com/developers/docs/topics/gateway#guild-update) Gateway event.
        > info
        > All parameters to this endpoint are optional
        
        Params:
            :name: guild name
            :region: Voice_Region
            :verification_level: Verification_Level
            :default_message_notifications: Message_Notification_Level
            :explicit_content_filter: Explicit_Content_Filter_Level
            :afk_channel_id: id for afk channel
            :afk_timeout: afk timeout in seconds
            :icon: base64 1024x1024 png/jpeg/gif image for the guild icon
            :owner_id: user id to transfer guild ownership to
            :splash: base64 16:9 png/jpeg image for the guild splash
            :banner: base64 16:9 png/jpeg image for the guild banner
            :system_channel_id: the id of the channel where guild notices such as welcome messages and boost events are posted
            :rules_channel_id: the id of the channel where Community guilds display rules and/or guidelines
            :public_updates_channel_id: the id of the channel where admins and moderators of Community guilds receive notices from Discord
            :preferred_locale: the preferred locale of a Community guild used in server discovery and notices from Discord; defaults to "en-US"
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}", method = "PATCH", json = {"name": name, "region": region, "verification_level": verification_level, "default_message_notifications": default_message_notifications, "explicit_content_filter": explicit_content_filter, "afk_channel_id": afk_channel_id, "afk_timeout": afk_timeout, "icon": icon, "owner_id": owner_id, "splash": splash, "banner": banner, "system_channel_id": system_channel_id, "rules_channel_id": rules_channel_id, "public_updates_channel_id": public_updates_channel_id, "preferred_locale": preferred_locale})
        return Guild(**r)
    
    async def delete_guild(self, guild_id: Snowflake) -> None:
        '''
        Delete a guild permanently. User must be owner. Returns `204 No Content` on success. Fires a [Guild Delete](https://discord.com/developers/docs/topics/gateway#guild-delete) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}", method = "DELETE")
    
    async def get_guild_channels(self, guild_id: Snowflake) -> List[Channel]:
        '''
        Returns a list of guild [channel](https://discord.com/developers/docs/resources/channel#channel-object) objects.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/channels", method = "GET")
        return [Channel(**i) for i in r]
    
    @Permissions("MANAGE_CHANNELS")
    async def create_guild_channel(self, guild_id: Snowflake, name: str, type: int, topic: str, bitrate: int, user_limit: int, rate_limit_per_user: int, position: int, permission_overwrites: List[Overwrite], parent_id: Snowflake, nsfw: bool) -> Channel:
        '''
        Create a new [channel](https://discord.com/developers/docs/resources/channel#channel-object) object for the guild. Requires the `MANAGE_CHANNELS` permission. Returns the new [channel](https://discord.com/developers/docs/resources/channel#channel-object) object on success. Fires a [Channel Create](https://discord.com/developers/docs/topics/gateway#channel-create) Gateway event.
        > info
        > All parameters to this endpoint are optional excluding 'name'
        
        Params:
            :name: channel name
            :type: Type_Of_Channel
            :topic: channel topic
            :bitrate: the bitrate
            :user_limit: the user limit of the voice channel
            :rate_limit_per_user: amount of seconds a user has to wait before sending another message
            :position: sorting position of the channel
            :permission_overwrites: the channel's permission overwrites
            :parent_id: id of the parent category for a channel
            :nsfw: whether the channel is nsfw
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/channels", method = "POST", json = {"name": name, "type": type, "topic": topic, "bitrate": bitrate, "user_limit": user_limit, "rate_limit_per_user": rate_limit_per_user, "position": position, "permission_overwrites": permission_overwrites, "parent_id": parent_id, "nsfw": nsfw})
        return Channel(**r)

    async def modify_guild_channel_positions(self, guild_id: Snowflake, id: Snowflake, position: int=None) -> None:
        '''
        Modify the positions of a set of [channel](https://discord.com/developers/docs/resources/channel#channel-object) objects for the guild. Requires `MANAGE_CHANNELS` permission. Returns a 204 empty response on success. Fires multiple [Channel Update](https://discord.com/developers/docs/topics/gateway#channel-update) Gateway events.
        > info
        > Only channels to be modified are required, with the minimum being a swap between at least two channels.
        This endpoint takes a JSON array of parameters in the following format:

        Params:
            :id: channel id
            :position: sorting position of the channel
        '''
        await self.api_call(path = f"/guilds/{guild_id}/channels", method = "PATCH", json = {"id": id, "position": position})

    async def get_guild_member(self, guild_id: Snowflake, user_id: Snowflake) -> Guild_Member:
        '''
        Returns a [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object) object for the specified user.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}", method = "GET")
        return Guild_Member(**r)

    async def list_guild_members(self, guild_id: Snowflake, limit: int=1, after: int=0) -> List[Guild_Member]:
        '''
        Returns a list of [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object) objects that are members of the guild.
        > warn
        > In the future, this endpoint will be restricted in line with our [Privileged Intents](https://discord.com/developers/docs/topics/gateway#privileged-intents)
        > info
        > All parameters to this endpoint are optional

        Params:
            :limit: max number of members to return
            :after: the highest user id in the previous page
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/members", method = "GET", params = {"limit": limit, "after": after})
        return [Guild_Member(**i) for i in r]

    async def add_guild_member(self, guild_id: Snowflake, user_id: Snowflake, access_token: str, nick: str, roles: List[int], mute: bool, deaf: bool) -> Guild_Member:
        '''
        Adds a user to the guild, provided you have a valid oauth2 access token for the user with the `guilds.join` scope. Returns a 201 Created with the [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object) as the body, or 204 No Content if the user is already a member of the guild. Fires a [Guild Member Add](https://discord.com/developers/docs/topics/gateway#guild-member-add) Gateway event.
        > info
        > All parameters to this endpoint except for `access_token` are optional.
        > info
        > The Authorization header must be a Bot token (belonging to the same application used for authorization), and the bot must be a member of the guild with `CREATE_INSTANT_INVITE` permission.

        Params:
            :access_token: an oauth2 access token granted with the `guilds.join` to the bot's application for the user you want to add to the guild
            :nick: value to set users nickname to
            :roles: role ids the member is assigned
            :mute: whether the user is muted in voice channels
            :deaf: whether the user is deafened in voice channels
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}", method = "PUT", json = {"access_token": access_token, "nick": nick, "roles": roles, "mute": mute, "deaf": deaf})
        return Guild_Member(**r)

    async def modify_guild_member(self, guild_id: Snowflake, user_id: Snowflake, nick: str, roles: List[int], mute: bool, deaf: bool, channel_id: Snowflake) -> None:
        '''
        Modify attributes of a [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object). Returns a 204 empty response on success. Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild-member-update) Gateway event. If the `channel_id` is set to null, this will force the target user to be disconnected from voice.
        > info
        > All parameters to this endpoint are optional and nullable. When moving members to channels, the API user _must_ have permissions to both connect to the channel and have the `MOVE_MEMBERS` permission.

        Params:
            :nick: value to set users nickname to
            :roles: role ids the member is assigned
            :mute: whether the user is muted in voice channels. Will throw a 400 if the user is not in a voice channel
            :deaf: whether the user is deafened in voice channels. Will throw a 400 if the user is not in a voice channel
            :channel_id: id of channel to move user to
        '''
        await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}", method = "PATCH", json = {"nick": nick, "roles": roles, "mute": mute, "deaf": deaf, "channel_id": channel_id})

    async def modify_current_user_nick(self, guild_id: Snowflake, nick: str=None) -> str:
        '''
        Modifies the nickname of the current user in a guild. Returns a 200 with the nickname on success. Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild-member-update) Gateway event.

        Params:
            :nick: value to set users nickname to
        '''
        return await self.api_call(path = f"/guilds/{guild_id}/members/@me/nick", method = "PATCH", json = {"nick": nick})

    @Permissions("MANAGE_ROLES")
    async def add_guild_member_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, reason: str = None) -> None:
        '''
        Adds a role to a [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object). Requires the `MANAGE_ROLES` permission. Returns a 204 empty response on success. Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild-member-update) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", method = "PUT", reason=reason)

    @Permissions("MANAGE_ROLES")
    async def remove_guild_member_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, reason: str = None) -> None:
        '''
        Removes a role from a [guild member](https://discord.com/developers/docs/resources/guild#guild-member-object). Requires the `MANAGE_ROLES` permission. Returns a 204 empty response on success. Fires a [Guild Member Update](https://discord.com/developers/docs/topics/gateway#guild-member-update) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", method = "DELETE", reason=reason)

    async def remove_guild_member(self, guild_id: Snowflake, user_id: Snowflake, reason: str = None) -> None:
        '''
        Remove a member from a guild. Requires `KICK_MEMBERS` permission. Returns a 204 empty response on success. Fires a [Guild Member Remove](https://discord.com/developers/docs/topics/gateway#guild-member-remove) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/members/{user_id}", method = "DELETE", reason=reason)

    @Permissions("BAN_MEMBERS")
    async def get_guild_bans(self, guild_id: Snowflake) -> List[Ban]:
        '''
        Returns a list of [ban](https://discord.com/developers/docs/resources/guild#ban-object) objects for the users banned from this guild. Requires the `BAN_MEMBERS` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/bans", method = "GET")
        return [Ban(**i) for i in r]

    @Permissions("BAN_MEMBERS")
    async def get_guild_ban(self, guild_id: Snowflake, user_id: Snowflake) -> Ban:
        '''
        Returns a [ban](https://discord.com/developers/docs/resources/guild#ban-object) object for the given user or a 404 not found if the ban cannot be found. Requires the `BAN_MEMBERS` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/bans/{user_id}", method = "GET")
        return Ban(**r)

    @Permissions("BAN_MEMBERS")
    async def create_guild_ban(self, guild_id: Snowflake, user_id: Snowflake, delete_message_days: int=None, reason: str=None) -> None:
        '''
        Create a guild ban, and optionally delete previous messages sent by the banned user. Requires the `BAN_MEMBERS` permission. Returns a 204 empty response on success. Fires a [Guild Ban Add](https://discord.com/developers/docs/topics/gateway#guild-ban-add) Gateway event.

        Params:
            :delete_message_days: number of days to delete messages for
            :reason: reason for the ban
        '''
        await self.api_call(path = f"/guilds/{guild_id}/bans/{user_id}", method = "PUT", json = {"delete_message_days": delete_message_days, "reason": reason})

    @Permissions("BAN_MEMBERS")
    async def remove_guild_ban(self, guild_id: Snowflake, user_id: Snowflake) -> None:
        '''
        Remove the ban for a user. Requires the `BAN_MEMBERS` permissions. Returns a 204 empty response on success. Fires a [Guild Ban Remove](https://discord.com/developers/docs/topics/gateway#guild-ban-remove) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/bans/{user_id}", method = "DELETE")

    async def get_guild_roles(self, guild_id: Snowflake) -> List[Role]:
        '''
        Returns a list of [role](https://discord.com/developers/docs/topics/permissions#role-object) objects for the guild.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/roles", method = "GET")
        return [Role(**i) for i in r]

    @Permissions("MANAGE_ROLES")
    async def create_guild_role(self, guild_id: Snowflake, name: str="new_role", permissions: str="@everyone_permissions_in_guild", color: int=0, hoist: bool=False, mentionable: bool=False) -> Role:
        '''
        Create a new [role](https://discord.com/developers/docs/topics/permissions#role-object) for the guild. Requires the `MANAGE_ROLES` permission. Returns the new [role](https://discord.com/developers/docs/topics/permissions#role-object) object on success. Fires a [Guild Role Create](https://discord.com/developers/docs/topics/gateway#guild-role-create) Gateway event. All JSON params are optional.

        Params:
            :name: name of the role
            :permissions: bitwise value of the enabled/disabled permissions
            :color: RGB color value
            :hoist: whether the role should be displayed separately in the sidebar
            :mentionable: whether the role should be mentionable
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/roles", method = "POST", json = {"name": name, "permissions": permissions, "color": color, "hoist": hoist, "mentionable": mentionable})
        return Role(**r)

    @Permissions("MANAGE_ROLES")
    async def modify_guild_role_positions(self, guild_id: Snowflake, id: Snowflake, position: int=None) -> List[Role]:
        '''
        Modify the positions of a set of [role](https://discord.com/developers/docs/topics/permissions#role-object) objects for the guild. Requires the `MANAGE_ROLES` permission. Returns a list of all of the guild's [role](https://discord.com/developers/docs/topics/permissions#role-object) objects on success. Fires multiple [Guild Role Update](https://discord.com/developers/docs/topics/gateway#guild-role-update) Gateway events.
        This endpoint takes a JSON array of parameters in the following format:

        Params:
            :id: role
            :position: sorting position of the role
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/roles", method = "PATCH", json = {"id": id, "position": position})
        return [Role(**i) for i in r]

    @Permissions("MANAGE_ROLES")
    async def modify_guild_role(self, guild_id: Snowflake, role_id: Snowflake, name: str, permissions: str, color: int, hoist: bool, mentionable: bool) -> Role:
        '''
        Modify a guild role. Requires the `MANAGE_ROLES` permission. Returns the updated [role](https://discord.com/developers/docs/topics/permissions#role-object) on success. Fires a [Guild Role Update](https://discord.com/developers/docs/topics/gateway#guild-role-update) Gateway event.
        > info
        > All parameters to this endpoint are optional and nullable.

        Params:
            :name: name of the role
            :permissions: bitwise value of the enabled/disabled permissions
            :color: RGB color value
            :hoist: whether the role should be displayed separately in the sidebar
            :mentionable: whether the role should be mentionable
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/roles/{role_id}", method = "PATCH", json = {"name": name, "permissions": permissions, "color": color, "hoist": hoist, "mentionable": mentionable})
        return Role(**r)

    @Permissions("MANAGE_ROLES")
    async def delete_guild_role(self, guild_id: Snowflake, role_id: Snowflake) -> None:
        '''
        Delete a guild role. Requires the `MANAGE_ROLES` permission. Returns a 204 empty response on success. Fires a [Guild Role Delete](https://discord.com/developers/docs/topics/gateway#guild-role-delete) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/roles/{role_id}", method = "DELETE")

    @Permissions("KICK_MEMBERS")
    async def get_guild_prune_count(self, guild_id: Snowflake, days: int=7, include_roles: List[int]=None) -> dict:
        '''
        Returns an object with one 'pruned' key indicating the number of members that would be removed in a prune operation. Requires the `KICK_MEMBERS` permission.
        By default, prune will not remove users with roles. You can optionally include specific roles in your prune by providing the `include_roles` parameter. Any inactive user that has a subset of the provided role(s) will be counted in the prune and users with additional roles will not.

        Params:
            :days: number of days to count prune for
            :include_roles: role
        '''
        return await self.api_call(path = f"/guilds/{guild_id}/prune", method = "GET", params = {"days": days, "include_roles": include_roles})

    @Permissions("KICK_MEMBERS")
    async def begin_guild_prune(self, guild_id: Snowflake, days: int=7, compute_prune_count: bool=True, include_roles: List[int]=None) -> None:
        '''
        Begin a prune operation. Requires the `KICK_MEMBERS` permission. Returns an object with one 'pruned' key indicating the number of members that were removed in the prune operation. For large guilds it's recommended to set the `compute_prune_count` option to `false`, forcing 'pruned' to `null`. Fires multiple [Guild Member Remove](https://discord.com/developers/docs/topics/gateway#guild-member-remove) Gateway events.
        By default, prune will not remove users with roles. You can optionally include specific roles in your prune by providing the `include_roles` parameter. Any inactive user that has a subset of the provided role(s) will be included in the prune and users with additional roles will not.

        Params:
            :days: number of days to prune
            :compute_prune_count: whether 'pruned' is returned, discouraged for large guilds
            :include_roles: role
        '''
        await self.api_call(path = f"/guilds/{guild_id}/prune", method = "POST", json = {"days": days, "compute_prune_count": compute_prune_count, "include_roles": include_roles})

    async def get_guild_voice_regions(self, guild_id: Snowflake) -> List[Voice_Region]:
        '''
        Returns a list of [voice region](https://discord.com/developers/docs/resources/voice#voice-region-object) objects for the guild. Unlike the similar `/voice` route, this returns VIP servers when the guild is VIP-enabled.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/regions", method = "GET")
        return [Voice_Region(**i) for i in r]

    @Permissions("MANAGE_GUILD")
    async def get_guild_invites(self, guild_id: Snowflake) -> List[Invite]:
        '''
        Returns a list of [invite](https://discord.com/developers/docs/resources/invite#invite-object) objects (with [invite metadata](https://discord.com/developers/docs/resources/invite#invite-metadata-object)) for the guild. Requires the `MANAGE_GUILD` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/invites", method = "GET")
        return [Invite(**i) for i in r]

    @Permissions("MANAGE_GUILD")
    async def get_guild_integrations(self, guild_id: Snowflake) -> List[Integration]:
        '''
        Returns a list of [integration](https://discord.com/developers/docs/resources/guild#integration-object) objects for the guild. Requires the `MANAGE_GUILD` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/integrations", method = "GET")
        return [Integration(**i) for i in r]

    @Permissions("MANAGE_GUILD")
    async def create_guild_integration(self, guild_id: Snowflake, type: str, id: Snowflake) -> None:
        '''
        Attach an [integration](https://discord.com/developers/docs/resources/guild#integration-object) object from the current user to the guild. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success. Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild-integrations-update) Gateway event.

        Params:
            :type: the integration type
            :id: the integration id
        '''
        await self.api_call(path = f"/guilds/{guild_id}/integrations", method = "POST", json = {"type": type, "id": id})

    @Permissions("MANAGE_GUILD")
    async def modify_guild_integration(self, guild_id: Snowflake, integration_id: Snowflake, expire_behavior: int, expire_grace_period: int, enable_emoticons: bool) -> None:
        '''
        Modify the behavior and settings of an [integration](https://discord.com/developers/docs/resources/guild#integration-object) object for the guild. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success. Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild-integrations-update) Gateway event.
        > info
        > All parameters to this endpoint are optional and nullable.

        Params:
            :expire_behavior: Integration_Expire_Behaviors
            :expire_grace_period: period
            :enable_emoticons: whether emoticons should be synced for this integration
        '''
        await self.api_call(path = f"/guilds/{guild_id}/integrations/{integration_id}", method = "PATCH", json = {"expire_behavior": expire_behavior, "expire_grace_period": expire_grace_period, "enable_emoticons": enable_emoticons})

    @Permissions("MANAGE_GUILD")
    async def delete_guild_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> None:
        '''
        Delete the attached [integration](https://discord.com/developers/docs/resources/guild#integration-object) object for the guild. Deletes any associated webhooks and kicks the associated bot if there is one. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success. Fires a [Guild Integrations Update](https://discord.com/developers/docs/topics/gateway#guild-integrations-update) Gateway event.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/integrations/{integration_id}", method = "DELETE")

    @Permissions("MANAGE_GUILD")
    async def sync_guild_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> None:
        '''
        Sync an integration. Requires the `MANAGE_GUILD` permission. Returns a 204 empty response on success.
        '''
        await self.api_call(path = f"/guilds/{guild_id}/integrations/{integration_id}/sync", method = "POST")

    @Permissions("MANAGE_GUILD")
    async def get_guild_widget_settings(self, guild_id: Snowflake) -> Guild_Widget:
        '''
        Returns a [guild widget](https://discord.com/developers/docs/resources/guild#guild-widget-object) object. Requires the `MANAGE_GUILD` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/widget", method = "GET")
        return Guild_Widget(**r)

    @Permissions("MANAGE_GUILD")
    async def modify_guild_widget(self, guild_id: Snowflake) -> Guild_Widget:
        '''
        Modify a [guild widget](https://discord.com/developers/docs/resources/guild#guild-widget-object) object for the guild. All attributes may be passed in with JSON and modified. Requires the `MANAGE_GUILD` permission. Returns the updated [guild widget](https://discord.com/developers/docs/resources/guild#guild-widget-object) object.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/widget", method = "PATCH")
        return Guild_Widget(**r)

    async def get_guild_widget(self, guild_id: Snowflake) -> Guild_Widget:
        '''
        Returns the widget for the guild.
        '''
        r = await self.api_call(path=f"/guilds/{guild_id}/widget_json", method="GET")
        return Guild_Widget(**r)

    @Permissions("MANAGE_GUILD")
    async def get_guild_vanity_url(self, guild_id: Snowflake) -> Invite:
        '''
        Returns a partial [invite](https://discord.com/developers/docs/resources/invite#invite-object) object for guilds with that feature enabled. Requires the `MANAGE_GUILD` permission. `code` will be null if a vanity url for the guild is not set.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/vanity-url", method = "GET")
        return Invite(**r)

    async def get_guild_widget_image(self, guild_id: Snowflake, style: str="shield") -> str:
        '''
        Returns a PNG image widget for the guild. Requires no permissions or authentication.
        > info
        > All parameters to this endpoint are optional.

        Params:
            :style: style of the widget image returned
        '''
        return await self.api_call(path = f"/guilds/{guild_id}/widget_png", method = "GET", params = {"style": style})

    async def get_invite(self, invite_code: int, with_counts: bool=None) -> Invite:
        '''
        Returns an [invite](https://discord.com/developers/docs/resources/invite#invite-object) object for the given code.

        Params:
            :with_counts: whether the invite should contain approximate member counts
        '''
        r = await self.api_call(path = f"/invites/{invite_code}", method = "GET", json = {"with_counts": with_counts})
        return Invite(**r)

    @Permissions("MANAGE_CHANNELS")
    async def delete_invite(self, invite_code: int) -> Invite:
        '''
        Delete an invite. Requires the `MANAGE_CHANNELS` permission on the channel this invite belongs to, or `MANAGE_GUILD` to remove any invite across the guild. Returns an [invite](https://discord.com/developers/docs/resources/invite#invite-object) object on success. Fires a [Invite Delete](https://discord.com/developers/docs/topics/gateway#invite-delete) Gateway event.
        '''
        r = await self.api_call(path = f"/invites/{invite_code}", method = "DELETE")
        return Invite(**r)

    async def get_current_user(self) -> User:
        '''
        Returns the [user](https://discord.com/developers/docs/resources/user#user-object) object of the requester's account. For OAuth2, this requires the `identify` scope, which will return the object _without_ an email, and optionally the `email` scope, which returns the object _with_ an email.
        '''
        r = await self.api_call(path = f"/users/@me", method = "GET")
        return User(**r)

    async def get_user(self, user_id: Snowflake) -> User:
        '''
        Returns a [user](https://discord.com/developers/docs/resources/user#user-object) object for a given user ID.
        '''
        r = await self.api_call(path = f"/users/{user_id}", method = "GET")
        return User(**r)

    async def modify_current_user(self, username: str, avatar: str) -> User:
        '''
        Modify the requester's user account settings. Returns a [user](https://discord.com/developers/docs/resources/user#user-object) object on success.
        > info
        > All parameters to this endpoint are optional.

        Params:
            :username: user's username, if changed may cause the user's discriminator to be randomized.
            :avatar: if passed, modifies the user's avatar
        '''
        r = await self.api_call(path = f"/users/@me", method = "PATCH", json = {"username": username, "avatar": avatar})
        return User(**r)

    async def get_current_user_guilds(self) -> List[Guild]:
        '''
        Returns a list of partial [guild](https://discord.com/developers/docs/resources/guild#guild-object) objects the current user is a member of. Requires the `guilds` OAuth2 scope.
        '''
        r = await self.api_call(path = f"/users/@me/guilds", method = "GET")
        return [Guild(**i) for i in r]

    async def leave_guild(self, guild_id: Snowflake) -> None:
        '''
        Leave a guild. Returns a 204 empty response on success.
        '''
        await self.api_call(path = f"/users/@me/guilds/{guild_id}", method = "DELETE")

    async def get_user_dms(self) -> List[Channel]:
        '''
        Returns a list of [DM channel](https://discord.com/developers/docs/resources/channel#channel-object) objects. For bots, this is no longer a supported method of getting recent DMs, and will return an empty array.
        '''
        r = await self.api_call(path = f"/users/@me/channels", method = "GET")
        return [Channel(**i) for i in r]

    async def create_dm(self, recipient_id: Snowflake) -> Channel:
        '''
        Create a new DM channel with a user. Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel-object) object.
        > warn
        > You should not use this endpoint to DM everyone in a server about something. DMs should generally be initiated by a user action. If you open a significant amount of DMs too quickly, your bot may be rate limited or blocked from opening new ones.

        Params:
            :recipient_id: the recipient to open a DM channel with
        '''
        r = await self.api_call(path = f"/users/@me/channels", method = "POST", json = {"recipient_id": recipient_id})
        return Channel(**r)

    async def create_group_dm(self, access_tokens: List[str], nicks: dict) -> Channel:
        '''
        Create a new group DM channel with multiple users. Returns a [DM channel](https://discord.com/developers/docs/resources/channel#channel-object) object. This endpoint was intended to be used with the now-deprecated GameBridge SDK. DMs created with this endpoint will not be shown in the Discord client
        > warn
        > This endpoint is limited to 10 active group DMs.

        Params:
            :access_tokens: access tokens of users that have granted your app the `gdm.join` scope
            :nicks: a dictionary of user ids to their respective nicknames
        '''
        r = await self.api_call(path = f"/users/@me/channels", method = "POST", json = {"access_tokens": access_tokens, "nicks": nicks})
        return Channel(**r)

    async def get_user_connections(self) -> List[Connection]:
        '''
        Returns a list of [connection](https://discord.com/developers/docs/resources/user#connection-object) objects. Requires the `connections` OAuth2 scope.
        '''
        r = await self.api_call(path = f"/users/@me/connections", method = "GET")
        return [Connection(**i) for i in r]

    async def list_voice_regions(self) -> List[Voice_Region]:
        '''
        Returns an array of [voice region](https://discord.com/developers/docs/resources/voice#voice-region-object) objects that can be used when creating servers.
        '''
        r = await self.api_call(path = f"/voice/regions", method = "GET")
        return [Voice_Region(**i) for i in r]

    @Permissions("MANAGE_WEBHOOKS")
    async def create_webhook(self, channel_id: Snowflake, name: str, avatar: str) -> Webhook:
        '''
        Create a new webhook. Requires the `MANAGE_WEBHOOKS` permission. Returns a [webhook](https://discord.com/developers/docs/resources/webhook#webhook-object) object on success. Webhook names follow our naming restrictions that can be found in our [Usernames and Nicknames](https://discord.com/developers/docs/resources/user#usernames-and-nicknames) documentation, with the following additional stipulations:
        - Webhook names cannot be: 'clyde'

        Params:
            :name: name of the webhook
            :avatar: image for the default webhook avatar
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/webhooks", method = "POST", json = {"name": name, "avatar": avatar})
        return Webhook(**r)

    @Permissions("MANAGE_WEBHOOKS")
    async def get_channel_webhooks(self, channel_id: Snowflake) -> List[Webhook]:
        '''
        Returns a list of channel [webhook](https://discord.com/developers/docs/resources/webhook#webhook-object) objects. Requires the `MANAGE_WEBHOOKS` permission.
        '''
        r = await self.api_call(path = f"/channels/{channel_id}/webhooks", method = "GET")
        return [Webhook(**i) for i in r]

    @Permissions("MANAGE_WEBHOOKS")
    async def get_guild_webhooks(self, guild_id: Snowflake) -> List[Webhook]:
        '''
        Returns a list of guild [webhook](https://discord.com/developers/docs/resources/webhook#webhook-object) objects. Requires the `MANAGE_WEBHOOKS` permission.
        '''
        r = await self.api_call(path = f"/guilds/{guild_id}/webhooks", method = "GET")
        return [Webhook(**i) for i in r]

    async def get_webhook(self, webhook_id: Snowflake) -> Webhook:
        '''
        Returns the new [webhook](https://discord.com/developers/docs/resources/webhook#webhook-object) object for the given id.
        '''
        r = await self.api_call(path = f"/webhooks/{webhook_id}", method = "GET")
        return Webhook(**r)

    async def get_webhook_with_token(self, webhook_id: Snowflake, webhook_token: int) -> None:
        '''
        Same as above, except this call does not require authentication and returns no user in the webhook object.
        '''
        r = await self.api_call(path=f"/webhooks/{webhook_id}/{webhook_token}", method="GET")
        return Webhook(**r)

    @Permissions("MANAGE_WEBHOOKS")
    async def modify_webhook(self, webhook_id: Snowflake, name: str, avatar: str, channel_id: Snowflake) -> Webhook:
        '''
        Modify a webhook. Requires the `MANAGE_WEBHOOKS` permission. Returns the updated [webhook](https://discord.com/developers/docs/resources/webhook#webhook-object) object on success.
        > info
        > All parameters to this endpoint are optional

        Params:
            :name: the default name of the webhook
            :avatar: image for the default webhook avatar
            :channel_id: the new channel id this webhook should be moved to
        '''
        r = await self.api_call(path = f"/webhooks/{webhook_id}", method = "PATCH", json = {"name": name, "avatar": avatar, "channel_id": channel_id})
        return Webhook(**r)

    async def modify_webhook_with_token(self, webhook_id: Snowflake, webhook_token: int) -> None:
        '''
        Same as above, except this call does not require authentication, does not accept a `channel_id` parameter in the body, and does not return a user in the webhook object.
        '''
        r = await self.api_call(path=f"/webhooks/{webhook_id}/{webhook_token}", method="PATCH")
        return Webhook(**r)

    @Permissions("MANAGE_WEBHOOKS")
    async def delete_webhook(self, webhook_id: Snowflake) -> None:
        '''
        Delete a webhook permanently. Requires the `MANAGE_WEBHOOKS` permission. Returns a 204 NO CONTENT response on success.
        '''
        await self.api_call(path = f"/webhooks/{webhook_id}", method = "DELETE")

    async def delete_webhook_with_token(self, webhook_id: Snowflake, webhook_token: int) -> None:
        '''
        Same as above, except this call does not require authentication.
        '''
        await self.api_call(path = f"/webhooks/{webhook_id}/{webhook_token}", method = "DELETE")

    async def execute_webhook(self, webhook_id: Snowflake, webhook_token: int, wait: bool = False, content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, file: bytes = None, embeds: List[Embed] = None, payload_json: str = None, allowed_mentions: Allowed_Mentions = None) -> Message:
        '''
        > warn
        > This endpoint supports both JSON and form data bodies. It does require multipart/form-data requests instead of the normal JSON request type when uploading files. Make sure you set your `Content-Type` to `multipart/form-data` if you're doing that. Note that in that case, the `embeds` field cannot be used, but you can pass an url-encoded JSON body as a form value for `payload_json`.

        Params:
            :wait: waits for server confirmation of message send before response, and returns the created message body
            :content: the message contents
            :username: override the default username of the webhook
            :avatar_url: override the default avatar of the webhook
            :tts: true if this is a TTS message
            :file: the contents of the file being sent
            :embeds: embedded `rich` content
            :payload_json: Message_Create
            :allowed_mentions: allowed mentions for the message
        '''
        r = await self.api_call(path = f"/webhooks/{webhook_id}/{webhook_token}", method = "POST", params = {"wait": wait}, json = {"content": content, "username": username, "avatar_url": avatar_url, "tts": tts, "file": file, "embeds": embeds, "payload_json": payload_json, "allowed_mentions": allowed_mentions})
        return Message(**r) if wait else None

    async def execute_slack_compatible_webhook(self, webhook_id: Snowflake, webhook_token: int, wait: bool) -> None:
        '''
        Params:
            :wait: waits for server confirmation of message send before response
        '''
        await self.api_call(path = f"/webhooks/{webhook_id}/{webhook_token}/slack", method = "POST", params = {"wait": wait})

    async def execute_github_compatible_webhook(self, webhook_id: Snowflake, webhook_token: int, wait: bool) -> None:
        '''
        Params:
            :wait: waits for server confirmation of message send before response
        '''
        await self.api_call(path = f"/webhooks/{webhook_id}/{webhook_token}/github", method = "POST", params = {"wait": wait})

    async def edit_webhook_message(self, webhook_id: Snowflake, webhook_token: int, message_id: Snowflake, content: str, embeds: List[Embed], allowed_mentions: Allowed_Mentions) -> None:
        '''
        Edits a previously-sent webhook message from the same token.
        > info
        > All parameters to this endpoint are optional and nullable.

        Params:
            :content: the message contents
            :embeds: embedded `rich` content
            :allowed_mentions: allowed mentions for the message
        '''
        await self.api_call(path = f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}", method = "PATCH", json = {"content": content, "embeds": embeds, "allowed_mentions": allowed_mentions})

    async def get_gateway(self) -> dict:
        '''
        > info
        > This endpoint does not require authentication.
        Returns an object with a single valid WSS URL, which the client can use for [Connecting](https://discord.com/developers/docs/topics/gateway#connecting). selfs **should** cache this value and only call this endpoint to retrieve a new URL if they are unable to properly establish a connection using the cached version of the URL.
        '''
        return await self.api_call(path = f"/gateway", method = "GET")

    async def get_gateway_bot(self) -> dict:
        '''
        > warn
        > This endpoint requires authentication using a valid bot token.
        Returns an object based on the information in [Get Gateway](https://discord.com/developers/docs/topics/gateway#get-gateway), plus additional metadata that can help during the operation of large or [sharded](https://discord.com/developers/docs/topics/gateway#sharding) bots. Unlike the [Get Gateway](https://discord.com/developers/docs/topics/gateway#get-gateway), this route should not be cached for extended periods of time as the value is not guaranteed to be the same per-call, and changes as the bot joins/leaves guilds.
        '''
        return await self.api_call(path = f"/gateway/bot", method = "GET")

    async def get_current_application_information(self) -> None:
        '''
        Returns the bot's OAuth2 [application object](https://discord.com/developers/docs/topics/oauth2#application-object) without `flags`.
        '''
        r = await self.api_call(path=f"/oauth2/applications/@me", method="GET")
        return Application(**r)

    async def get_global_application_commands(self, application_id: Snowflake) -> List[Application_Command]:
        '''
        Fetch all of the global commands for your application. Returns an array of [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) objects.
        '''
        r = await self.api_call(path = f"/applications/{application_id}/commands", method = "GET")
        return [Application_Command(**i) for i in r]

    async def create_global_application_command(self, application_id: Snowflake, name: str, description: str, options: List[Application_Command_Option]=None) -> Application_Command:
        '''
        > danger
        > Creating a command with the same name as an existing command for your application will overwrite the old command.
        Create a new global command. New global commands will be available in all guilds after 1 hour. Returns `201` and an [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) object.

        Params:
            :name: 3-32 character command name
            :description: 1-100 character description
            :options: the parameters for the command
        '''
        r = await self.api_call(path = f"/applications/{application_id}/commands", method = "POST", json = {"name": name, "description": description, "options": options})
        return Application_Command(**r)

    async def edit_global_application_command(self, application_id: Snowflake, command_id: Snowflake, name: str, description: str, options: List[Application_Command_Option]=None) -> Application_Command:
        '''
        Edit a global command. Updates will be available in all guilds after 1 hour. Returns `200` and an [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) object.

        Params:
            :name: 3-32 character command name
            :description: 1-100 character description
            :options: the parameters for the command
        '''
        r = await self.api_call(path = f"/applications/{application_id}/commands/{command_id}", method = "PATCH", json = {"name": name, "description": description, "options": options})
        return Application_Command(**r)

    async def delete_global_application_command(self, application_id: Snowflake, command_id: Snowflake) -> None:
        '''
        Deletes a global command. Returns `204`.
        '''
        await self.api_call(path = f"/applications/{application_id}/commands/{command_id}", method = "DELETE")

    async def get_guild_application_commands(self, application_id: Snowflake, guild_id: Snowflake) -> List[Application_Command]:
        '''
        Fetch all of the guild commands for your application for a specific guild. Returns an array of [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) objects.
        '''
        r = await self.api_call(path = f"/applications/{application_id}/guilds/{guild_id}/commands", method = "GET")
        return [Application_Command(**i) for i in r]

    async def create_guild_application_command(self, application_id: Snowflake, guild_id: Snowflake, name: str, description: str, options: List[Application_Command_Option]=[]) -> Application_Command:
        '''
        > danger
        > Creating a command with the same name as an existing command for your application will overwrite the old command.
        Create a new guild command. New guild commands will be available in the guild immediately. Returns `201` and an [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) object.

        Params:
            :name: 3-32 character command name
            :description: 1-100 character description
            :options: the parameters for the command
        '''
        r = await self.api_call(path = f"/applications/{application_id}/guilds/{guild_id}/commands", method = "POST", json = {"name": name, "description": description, "options": options})
        return Application_Command(**r)

    async def edit_guild_application_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake, name: str, description: str, options: List[Application_Command_Option]=[]) -> Application_Command:
        '''
        Edit a guild command. Updates for guild commands will be available immediately. Returns `200` and an [ApplicationCommand](https://discord.com/developers/docs/interactions/slash_commands#applicationcommand) object.

        Params:
            :name: 3-32 character command name
            :description: 1-100 character description
            :options: the parameters for the command
        '''
        r = await self.api_call(path = f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}", method = "PATCH", json = {"name": name, "description": description, "options": options})
        return Application_Command(**r)

    async def delete_guild_application_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> None:
        '''
        Delete a guild command. Returns `204` on success.
        '''
        await self.api_call(path = f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}", method = "DELETE")

    async def create_interaction_response(self, interaction_id: Snowflake, interaction_token: int, response: Interaction_Response) -> None:
        '''
        Create a response to an Interaction from the gateway. Takes an [Interaction response](https://discord.com/developers/docs/interactions/slash_commands#interaction-response).
        '''
        await self.api_call(path = f"/interactions/{interaction_id}/{interaction_token}/callback", method = "POST", json = as_dict(response))

    async def edit_original_interaction_response(self, application_id: Snowflake, interaction_token: int, content: str = None, embeds: List[Embed] = None, allowed_mentions: Allowed_Mentions = None) -> None:
        '''
        Edits the initial Interaction response. Functions the same as [Edit Webhook Message](https://discord.com/developers/docs/resources/webhook#edit-webhook-message).
        '''
        await self.api_call(path = f"/webhooks/{application_id}/{interaction_token}/messages/@original", method = "PATCH", json={"content":content, "embeds": embeds, "allowed_mentions": allowed_mentions})

    async def delete_original_interaction_response(self, application_id: Snowflake, interaction_token: int) -> None:
        '''
        Deletes the initial Interaction response. Returns `204` on success.
        '''
        await self.api_call(path = f"/webhooks/{application_id}/{interaction_token}/messages/@original", method = "DELETE")

    async def create_followup_message(self, application_id: Snowflake, interaction_token: int, wait: bool = False, content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, file: bytes = None, filename: str="file.txt", embeds: List[Embed] = None, payload_json: str = None, allowed_mentions: Allowed_Mentions = []) -> Message:
        '''
        Create a followup message for an Interaction. Functions the same as [Execute Webhook](https://discord.com/developers/docs/resources/webhook#execute-webhook)
        '''
        r = await self.api_call(path=f"/webhooks/{application_id}/{interaction_token}", method="POST", params={"wait": wait}, json={"content": content, "username": username, "avatar_url": avatar_url, "tts": tts, "embeds": embeds, "payload_json": payload_json, "allowed_mentions": allowed_mentions}, file=file, filename=filename)
        return Message(**r)

    async def edit_followup_message(self, application_id: Snowflake, interaction_token: int, message_id: Snowflake, content: str = None, embeds: List[Embed] = None, allowed_mentions: Allowed_Mentions = []) -> None:
        '''
        Edits a followup message for an Interaction. Functions the same as [Edit Webhook Message](https://discord.com/developers/docs/resources/webhook#edit-webhook-message).
        '''
        await self.api_call(path = f"/webhooks/{application_id}/{interaction_token}/messages/{message_id}", method = "PATCH", json={"content":content, "embeds": embeds, "allowed_mentions": allowed_mentions})

    async def delete_followup_message(self, application_id: Snowflake, interaction_token: int, message_id: Snowflake) -> None:
        '''
        Deletes a followup message for an Interaction. Returns `204` on success.
        '''
        await self.api_call(path=f"/webhooks/{application_id}/{interaction_token}/messages/{message_id}", method="DELETE")