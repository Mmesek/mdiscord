# -*- coding: utf-8 -*-
"""
Discord Types
----------

Model overrides with additional convinience methods.

:copyright: (c) 2021 Mmesek

"""

from __future__ import annotations

from typing import Union, Tuple
from datetime import datetime

from .models import *  # noqa: F401


class Attachment(Attachment):
    file: bytes = None

    def __init__(
        self,
        id: Snowflake = None,
        filename: str = "file",
        description: str = None,
        content_type: str = None,
        size: int = None,
        url: str = None,
        proxy_url: str = None,
        height: int = None,
        width: int = None,
        *,
        spoiler: bool = False,
        file: bytes = None,
        _Client=None,
    ):
        if spoiler and not filename.startswith("SPOILER_"):
            filename = "SPOILER_" + filename
        super().__init__(
            _Client=_Client,
            id=id,
            filename=filename,
            description=description,
            content_type=content_type,
            size=size,
            url=url,
            proxy_url=proxy_url,
            height=height,
            width=width,
        )
        self.file = file


class UserID(Snowflake):
    """Snowflake representing UserID"""

    def __str__(self):
        return "users"


class ChannelID(Snowflake):
    """Snowflake representing ChannelID"""

    def __str__(self):
        return "channels"


class RoleID(Snowflake):
    """Snowflake representing RoleID"""

    def __str__(self):
        return "roles"


class GuildID(Snowflake):
    """Snowflake representing GuildID"""

    pass


# class CDN_Endpoints(CDN_Endpoints):
#    @classmethod
#    def cdn(cls, value):
#        return CDN_URL + cls.value


class Discord_Paths(Enum):
    MessageLink = "channels/{guild_id}/{channel_id}/{message_id}"

    @property
    def link(self) -> str:
        return BASE_URL + self.value


@dataclass
class Embed(Embed):
    def set_title(self, title: str) -> Embed:
        """Sets Embed's Title respecting title limit if it's not above total limit"""
        title = str(title)[: Limits.TITLE]
        if self.total_characters + len(str(title)) <= Limits.TOTAL:
            self.title = title
        return self

    setTitle = set_title

    def set_description(self, description: str) -> Embed:
        """Sets Embed's Description respecting description limit if it's not above total limit"""
        description = str(description)[: Limits.DESCRIPTION]
        if self.total_characters + len(str(description)) <= Limits.TOTAL:
            self.description = description
        return self

    setDescription = set_description

    def set_color(self, color: Union[str, Tuple[int, int, int], int]) -> Embed:
        """Set's Embed's Color.

        Parameters
        ----------
        color:
            Accepts HEX string, RGB Tuple or final Integer"""
        if type(color) == str and "#" in color:
            color = int(color.lstrip("#"), 16)
        elif type(color) == tuple:
            color = (color[0] << 16) + (color[1] << 8) + color[2]
        self.color = color
        return self

    setColor = set_color

    def set_url(self, url: str) -> Embed:
        """Sets URL."""
        self.url = url
        return self

    setUrl = set_url

    def set_image(self, url: str, proxy_url: str = None, height: int = None, width: int = None) -> Embed:
        """Sets Embed's Image"""
        self.image = Embed_Image(url=url, proxy_url=proxy_url, height=height, width=width)
        return self

    setImage = set_image

    def set_thumbnail(self, url: str, proxy_url: str = None, height: int = None, width: int = None) -> Embed:
        """Sets Embed's Thumbnail"""
        self.thumbnail = Embed_Thumbnail(url=url, proxy_url=proxy_url, height=height, width=width)
        return self

    setThumbnail = set_thumbnail

    def set_footer(self, text: str = "", icon_url: str = None, proxy_icon_url: str = None) -> Embed:
        """Sets Embed's Footer respecting footer's text limit"""
        text = str(text)[: Limits.FOOTER_TEXT]
        if self.total_characters + len(str(text)) <= Limits.TOTAL:
            self.footer = Embed_Footer(text=text, icon_url=icon_url, proxy_icon_url=proxy_icon_url)
        return self

    setFooter = set_footer

    def set_timestamp(self, timestamp: datetime) -> Embed:
        """Sets Timestamp.

        Parameters
        ----------
        timestamp:
            Accepts direct ISO string, datetime object or POSIX float"""
        if type(timestamp) is datetime:
            timestamp = timestamp.isoformat()
        elif type(timestamp) is float:
            timestamp = datetime.fromtimestamp(timestamp).isoformat()
        self.timestamp = timestamp
        return self

    setTimestamp = set_timestamp

    def set_author(self, name: str = "", url: str = None, icon_url: str = None, proxy_icon_url: str = None) -> Embed:
        """Sets Embed's Author respecting author's name limit if it's not above total limit"""
        name = str(name)[: Limits.AUTHOR_NAME]
        if self.total_characters + len(str(name)) <= Limits.TOTAL:
            self.author = Embed_Author(name=name, url=url, icon_url=icon_url, proxy_icon_url=proxy_icon_url)
        return self

    setAuthor = set_author

    def add_field(self, name: str, value: str, inline: bool = False) -> Embed:
        """Adds single field respecting limits if it's not above total limit"""
        name = str(name)[: Limits.FIELD_NAME]
        value = str(value)[: Limits.FIELD_VALUE]
        value = str(value)[: Limits.TOTAL - self.total_characters]

        if self.total_characters + len(str(name)) + len(str(value)) <= Limits.TOTAL:
            self.fields.append(Embed_Field(name=name, value=value, inline=inline))
        return self

    addField = add_field

    def add_fields(self, title: str, text: str, inline: bool = False) -> Embed:
        """
        Adds as many fields as neccessary to store whole text
        while respecting limits and as long as it's not above total Embed's limit"""
        from textwrap import wrap

        for x, chunk in enumerate(wrap(text, Limits.FIELD_VALUE, replace_whitespace=False)):
            if len(self.fields) == Limits.FIELDS:
                break
            if x == 0:
                self.addField(title, chunk, inline)
            else:
                self.addField("\u200b", chunk, inline)
        return self

    addFields = add_fields

    @property
    def total_characters(self) -> int:
        """Counts total characters"""
        return (
            len(str(self.title) or "")
            + len(str(self.description) or "")
            + len(str(self.author.name) or "" if self.author else "")
            + len(str(self.footer.text) or "" if self.footer else "")
            + sum([len(str(field.name)) + len(str(field.value)) for field in self.fields])
        )


class Sendable:
    @property
    def is_dm(self) -> bool:
        raise NotImplementedError

    @property
    def in_thread(self) -> bool:
        raise NotImplementedError

    @property
    def is_reply(self) -> bool:
        raise NotImplementedError

    @property
    def is_empty(self) -> bool:
        raise NotImplementedError

    @property
    def is_bot(self) -> bool:
        raise NotImplementedError

    async def typing(self, channel_id: Snowflake = None, private: bool = False) -> None:
        """Shows in channel that Bot is Typing. Useful for signalising loading state"""
        raise NotImplementedError

    async def reply(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        private: bool = False,
    ) -> Message:
        """Creates reply message.
        Basically a wrapper around `send` method.

        Parameters
        ----------
        content:
            Message to send
        embeds:
            List of embeds to send
        components:
            List of components to send
        attachments:
            List of attachments to send
        allowed_mentions:
            Allowed Mentions structure
        message_reference:
            Message_Reference object message is a reply to
        private:
            Whether message should be send as ephemeral response for interaction (or DM for message) or not
        """
        raise NotImplementedError

    async def send(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        reply: bool = False,
        private: bool = False,
        channel_id: Snowflake = None,
    ) -> Message:
        """Sends message

        Parameters
        ----------
        content:
            Message to send
        embeds:
            List of embeds to send
        components:
            List of components to send
        attachments:
            List of attachments to send
        allowed_mentions:
            Allowed Mentions structure
        message_reference:
            Message_Reference object message is a reply to
        reply:
            Whether this message should attach to original message and reply to it
        private:
            Whether message should be send as ephemeral response for interaction (or DM for message) or not"""
        raise NotImplementedError

    async def edit(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        flags: Message_Flags = None,
    ) -> Message:
        """Edits message

        Parameters
        ----------
        content:
            Message to send
        embeds:
            List of embeds to send
        components:
            List of components to send
        attachments:
            List of attachments to keep
        flags:
            Flags message should be send with
        allowed_mentions:
            Allowed Mentions structure"""
        raise NotImplementedError

    async def delete(self, message_id: Snowflake = None, reason: str = None) -> None:
        """Deletes message"""
        raise NotImplementedError

    async def get(self, channel_id: Snowflake = None, message_id: Snowflake = None) -> Message:
        """Fetches message"""
        raise NotImplementedError

    async def publish(self) -> Message:
        """Publishes message if in announcement channel"""
        raise NotImplementedError

    async def send_followup(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        allowed_mentions: Allowed_Mentions = [],
        tts: bool = None,
        attachments: List[Attachment] = None,
        username: str = None,
        avatar_url: str = None,
        flags: Message_Flags = None,
        wait: bool = False,
        thread_id: Snowflake = None,
    ) -> Union[Message, None]:
        """Creates followup message. (Replies to previous message)
        Basically a wrapper around `send_webhook` method.

        Parameters
        ----------
        content:
            Message to send
        embeds:
            List of embeds to send
        components:
            List of components to include
        attachments:
            List of attachments to send
        allowed_mentions:
            Allowed Mentions structure
        username:
            Username message should be send with (Works only with interactions or webhooks)
        avatar_url:
            Avatar message should be send with (Works only with interactions or webhooks)
        flags:
            Flags message should be send with (Works only with interactions)
        wait:
            Whether should return Message (Not used with interactions)
        thread_id:
            Whether Message should be part of a thread (Not used with interactions)
        """
        raise NotImplementedError

    async def edit_followup(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = [],
        flags: Message_Flags = None,
    ) -> Union[Message, None]:
        """Edits last followup message. (Edits last reply)
        Basically a wrapper around `edit_webhook` method.

        Parameters
        ----------
        content:
            Message to send
        embeds:
            List of embeds to send
        components:
            List of components to include
        allowed_mentions:
            Allowed Mentions structure
        attachments:
            List of attachments to keep
        flags:
            Flags message should be send with
        """
        raise NotImplementedError

    async def delete_followup(self, message_id: Snowflake = None) -> None:
        """Deletes last followup message. (Deletes last reply)
        Basically a wrapper around `delete_webhook` method."""
        raise NotImplementedError


@dataclass
class Message(Message, Sendable):
    embeds: List[Embed] = list

    @property
    def is_private(self) -> bool:
        return self.guild_id == 0

    @property
    def is_thread(self) -> bool:
        return self.thread is not None

    @property
    def is_reply(self) -> bool:
        return self.referenced_message is not None

    @property
    def is_webhook(self) -> bool:
        return self.webhook_id or False

    @property
    def is_empty(self) -> bool:
        return self.content == ""

    @property
    def is_bot(self) -> bool:
        return self.author and self.author.bot or self.webhook_id

    async def typing(self, channel_id: Snowflake = None, private: bool = False) -> None:
        return await self._Client.trigger_typing_indicator(channel_id or self.channel_id)

    async def reply(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        private: bool = None,
    ) -> Message:
        return await self.send(
            content=content,
            embeds=embeds,
            components=components,
            attachments=attachments,
            allowed_mentions=allowed_mentions,
            message_reference=message_reference
            or Message_Reference(
                message_id=self.id, channel_id=self.channel_id, guild_id=self.guild_id if self.guild_id != 0 else None
            )
            if self.id
            else None,
            reply=True,
            private=private,
        )

    async def send(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        reply: bool = False,
        private: bool = False,
        channel_id: Snowflake = None,
    ) -> Message:
        return await self._Client.create_message(
            channel_id or self.channel_id,
            content=content,  # if content != "" else self.content,
            embeds=embeds,  # if embeds else self.embeds,
            components=components,  # if components else self.components,
            attachments=attachments,
            allowed_mentions=allowed_mentions,
            message_reference=message_reference,
        )

    async def edit(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        flags: Message_Flags = None,
    ) -> Message:
        return await self._Client.edit_message(
            channel_id=self.channel_id,
            message_id=self.id,
            content=content or self.content,
            embeds=embeds or self.embeds,
            components=components or self.components,
            attachments=attachments or self.attachments,
            flags=flags or self.flags,
            allowed_mentions=allowed_mentions,
        )

    async def delete(self, message_id: Snowflake = None, reason: str = None) -> None:
        return await self._Client.delete_message(
            channel_id=self.channel_id, message_id=message_id or self.id, reason=reason
        )

    async def webhook(
        self, webhook_id: Snowflake, webhook_token: int, username: str = None, avatar_url: str = None
    ) -> Message:
        """Sends message as a webhook"""
        return await self._Client.execute_webhook(
            webhook_id,
            webhook_token,
            content=self.content,
            username=username,
            avatar_url=avatar_url,
            embeds=self.embeds,
            allowed_mentions=self.allowed_mentions,
            attachments=self.attachments,
        )

    async def webhook_edit(
        self,
        webhook_id,
        webhook_token,
        content: str = None,
        embeds: List[Embed] = None,
        allowed_mentions: Allowed_Mentions = None,
    ) -> None:
        """Edits webhook message"""
        return await self._Client.edit_webhook_message(
            webhook_id, webhook_token, self.id, content, embeds, allowed_mentions
        )

    async def get(self) -> Message:
        return await self._Client.get_channel_message(self.channel_id, self.id)

    async def react(self, reaction: str) -> None:
        """Reacts to message"""
        return await self._Client.create_reaction(self.channel_id, self.id, reaction)

    async def get_reactions(
        self, emoji: str, users: List[User] = [], last_id: Snowflake = 0, limit: Snowflake = 100
    ) -> List[User]:
        """Retrieves all users that reacted to this message"""
        # for chunk in range(int(count / 100) + (count % 100 > 0)): #Alternative pagination method
        r = await self._Client.get_reactions(self.channel_id, self.id, emoji, after=last_id, limit=limit)
        if len(r) < limit or len(r) == 0:
            return [i for i in users + r if i.id != self._Client.user_id]
        return await self.get_reactions(emoji, users=users + r, last_id=r[-1].id)

    async def delete_reaction(self, reaction: str) -> None:
        """Deletes reaction"""
        return await self._Client.delete_own_reaction(self.channel_id, self.id, reaction)

    async def publish(self) -> Message:
        return await self._Client.crosspost_message(self.channel_id, self.id)

    def attachments_as_embed(self, embed=None, title_attachments="Attachments", title_image="Image"):
        """Returns Attachments as URLs listed in an Embed"""
        if len(self.attachments) == 0:
            return embed
        if embed is None:
            embed = Embed()
        embed.setImage(self.attachments[0].url)
        if self.attachments[0].url[-3:] not in ["png", "jpg", "jpeg", "webp", "gif"] or len(self.attachments) > 1:
            filename = "\n".join([f"[{i.filename}]({i.url})" for i in self.attachments])
            embed.addFields(title_attachments, filename, True)
        else:
            embed.addField(title_image, self.attachments[0].filename, True)
        return embed

    @property
    def message_link(self):
        return Discord_Paths.MessageLink.link.format(self.guild_id or "@me", self.channel_id, self.id)

    deferred = typing


@dataclass
class Guild(Guild):
    def get_icon(self) -> str:
        return CDN_URL + CDN_Endpoints.Guild_Icon.value.format(guild_id=self.id, guild_icon=self.icon)

    def get_splash(self) -> str:
        return CDN_URL + CDN_Endpoints.Guild_Splash.value.format(guild_id=self.id, guild_splash=self.splash)

    def get_discovery_splash(self) -> str:
        return CDN_URL + CDN_Endpoints.Guild_Discovery_Splash.value.format(
            guild_id=self.id, guild_discovery_splash=self.discovery_splash
        )


@dataclass
class Channel(Channel):
    async def get_messages(self, before_id: Snowflake = None, messages: List[Message] = [], limit: int = 100):
        if limit < 1:
            return messages
        r = await self._Client.get_channel_messages(self.id, before=before_id, limit=min(limit, 100))
        if not r:
            return messages
        return await self.get_messages(r[-1].id, messages=messages + r, limit=limit - len(r))


@dataclass
class User(User):
    def __str__(self):
        return f"{self.username}#{self.discriminator}"

    def get_avatar(self) -> str:
        if self.avatar:
            return CDN_URL + CDN_Endpoints.User_Avatar.value.format(user_id=self.id, user_avatar=self.avatar)
        return CDN_URL + CDN_Endpoints.Default_User_Avatar.value.format(user_discriminator=self.discriminator % 5)


@dataclass
class Interaction(Interaction):
    data: Application_Command_Interaction_Data = None
    _deferred = False
    _replied = False
    _followup_id = None

    @property
    def is_private(self) -> bool:
        return self.guild_id == 0

    @property
    def is_thread(self) -> bool:
        return False

    @property
    def is_reply(self) -> bool:
        return False

    @property
    def is_webhook(self) -> bool:
        return False

    @property
    def is_empty(self) -> bool:
        return False

    @property
    def is_bot(self) -> bool:
        return False

    async def deferred(self, private: bool = False) -> None:
        """Acknowledges Interaction with Source"""
        if self._deferred:
            return await self._Client.edit_original_interaction_response(
                self.application_id,
                self.token,
                content="Processing...",
                flags=Message_Flags.EPHEMERAL if private else None,
            )
        self._deferred = True
        self._replied = True
        return await self._Client.create_interaction_response(
            self.id,
            self.token,
            Interaction_Response(
                type=Interaction_Callback_Type.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE,
                data=Interaction_Application_Command_Callback_Data(flags=Message_Flags.EPHEMERAL if private else None),
            ),
        )

    async def reply(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        private: bool = None,
    ) -> Message:
        if self._deferred:
            _f = self.edit
            kw = {}
        else:
            _f = self.send
            kw = {"message_reference": None, "reply": True}
        r = await _f(
            content=content,
            embeds=embeds,
            components=components,
            attachments=attachments,
            allowed_mentions=allowed_mentions,
            private=private,
            **kw,
        )
        self._replied = True
        return r

    async def send(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        message_reference: Message_Reference = None,
        reply: bool = None,
        private: bool = None,
        channel_id: Snowflake = None,
        custom_id: str = None,
        title: str = None,
    ) -> Message:
        flags = Message_Flags.EPHEMERAL if private else None
        if channel_id:
            return await self._Client.create_message(
                channel_id,
                content,
                embeds=embeds,
                components=components,
                attachments=attachments,
                allowed_mentions=allowed_mentions,
            )
        if self._replied:
            return await self.send_followup(
                content=content,
                embeds=embeds,
                components=components,
                allowed_mentions=allowed_mentions,
                attachments=attachments,
                flags=flags,
            )
        return await self._Client.create_interaction_response(
            self.id,
            self.token,
            Interaction_Response(
                type=Interaction_Callback_Type.CHANNEL_MESSAGE_WITH_SOURCE
                if not custom_id
                else Interaction_Callback_Type.MODAL,
                data=Interaction_Application_Command_Callback_Data(
                    content=content,
                    embeds=embeds,
                    components=components,
                    allowed_mentions=allowed_mentions,
                    flags=flags,
                    custom_id=custom_id,
                    title=title,
                ),
            ),
        )

    async def update(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        private: bool = False,
    ):
        flags = Message_Flags.EPHEMERAL if private else None
        return await self._Client.create_interaction_response(
            self.id,
            self.token,
            Interaction_Response(
                type=Interaction_Callback_Type.UPDATE_MESSAGE,
                data=Interaction_Application_Command_Callback_Data(
                    content=content,
                    embeds=embeds,
                    components=components,
                    attachments=attachments,
                    allowed_mentions=allowed_mentions,
                    flags=flags,
                ),
            ),
        )

    async def send_followup(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        allowed_mentions: Allowed_Mentions = None,
        tts: bool = None,
        attachments: List[Attachment] = None,
        username: str = None,
        avatar_url: str = None,
        flags: Message_Flags = None,
        wait: bool = None,
        thread_id: Snowflake = None,
    ) -> Union[Message, None]:
        m = await self._Client.create_followup_message(
            self._Client.application.id,
            self.token,
            wait=wait,
            content=content,
            username=username,
            avatar_url=avatar_url,
            tts=tts,
            attachments=attachments,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            flags=flags,
        )
        self._followup_id = m.id
        return m

    async def edit(
        self,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        attachments: List[Attachment] = None,
        allowed_mentions: Allowed_Mentions = None,
        flags: Message_Flags = None,
        private: bool = False,
    ) -> Message:
        return await self._Client.edit_original_interaction_response(
            self._Client.application.id,
            self.token,
            content=content,
            embeds=embeds,
            components=components,
            attachments=attachments,
            allowed_mentions=allowed_mentions,
            flags=Message_Flags.EPHEMERAL if private else None,
        )

    async def edit_followup(
        self,
        message_id: Snowflake = None,
        content: str = None,
        embeds: List[Embed] = None,
        components: List[Component] = None,
        allowed_mentions: Allowed_Mentions = None,
        attachments: List[Attachment] = None,
        flags: Message_Flags = None,
    ) -> Union[Message, None]:
        return await self._Client.edit_followup_message(
            self._Client.application.id,
            self.token,
            message_id or self._followup_id,
            content=content,
            embeds=embeds,
            components=components,
            attachments=attachments,
            allowed_mentions=allowed_mentions,
        )

    async def delete(self, message_id: Snowflake = None) -> None:
        return await self._Client.delete_original_interaction_response(self._Client.application.id, self.token)

    async def delete_followup(self, message_id: Snowflake = None) -> None:
        return await self._Client.delete_followup_message(
            self._Client.application.id, self.token, message_id or self._followup_id
        )


class Gateway_Events(Events):
    """Mapping of received Event name from Gateway with coresponding Type and description"""

    Hello = Hello
    """Defines the heartbeat interval"""
    Ready = Ready
    """Contains the initial state information"""
    Resumed = Resume
    """Resume"""
    Reconnect = dict
    """Server is going away, client should reconnect to gateway and resume"""
    Invalid_Session = bool
    """Identify"""
    Application_Command_Create = Application_Command_Create
    Application_Command_Update = Application_Command_Update
    Application_Command_Delete = Application_Command_Delete
    Channel_Create = Channel
    """New guild channel created"""
    Channel_Update = Channel
    """Channel was updated"""
    Channel_Delete = Channel
    """Channel was deleted"""
    Channel_Pins_Update = Channel_Pins_Update
    """Message was pinned"""
    Thread_Create = Channel
    Thread_Update = Channel
    Thread_Delete = Channel
    Thread_List_Sync = Thread_List_Sync
    Thread_Member_Update = Thread_Member
    Thread_Members_Update = Thread_Members_Update
    Guild_Create = Guild
    """Lazy-load for unavailable guild, guild became available,"""
    Guild_Update = Guild
    """Guild was updated"""
    Guild_Delete = dict
    """Guild became unavailable,"""
    Guild_Ban_Add = Guild_Ban_Add
    """User was banned from a guild"""
    Guild_Ban_Remove = Guild_Ban_Remove
    """User was unbanned from a guild"""
    Guild_Emojis_Update = Guild_Emojis_Update
    """Guild emojis were updated"""
    Guild_Integrations_Update = Guild_Integrations_Update
    """Guild integration was updated"""
    Guild_Member_Add = Guild_Member_Add
    """New user joined a guild"""
    Guild_Member_Remove = Guild_Member_Remove
    """User was removed from a guild"""
    Guild_Member_Update = Guild_Member_Update
    """Guild member was updated"""
    Guild_Members_Chunk = Guild_Members_Chunk
    """Request_Guild_Members"""
    Guild_Role_Create = Guild_Role_Create
    """Guild role was created"""
    Guild_Role_Update = Guild_Role_Update
    """Guild role was updated"""
    Guild_Role_Delete = Guild_Role_Delete
    """Guild role was deleted"""
    Invite_Create = Invite_Create
    """Invite to a channel was created"""
    Invite_Delete = Invite_Delete
    """Invite to a channel was deleted"""
    Message_Create = Message
    """Message was created"""
    Message_Update = Message
    """Message was edited"""
    Message_Delete = Message_Delete
    """Message was deleted"""
    Message_Delete_Bulk = Message_Delete_Bulk
    """Multiple messages were deleted at once"""
    Message_Reaction_Add = Message_Reaction_Add
    """User reacted to a message"""
    Message_Reaction_Remove = Message_Reaction_Remove
    """User removed a reaction from a message"""
    Message_Reaction_Remove_All = Message_Reaction_Remove_All
    """All reactions were explicitly removed from a message"""
    Message_Reaction_Remove_Emoji = Message_Reaction_Remove_Emoji
    """All reactions for a given emoji were explicitly removed from a message"""
    Presence_Update = Presence_Update
    """User was updated"""
    Typing_Start = Typing_Start
    """User started typing in a channel"""
    User_Update = User
    """Properties about the user changed"""
    Voice_State_Update = Voice_State
    """Someone joined, left,"""
    Voice_Server_Update = Voice_Server_Update
    """Guild's voice server was updated"""
    Webhooks_Update = Webhook_Update
    """Guild channel webhook was created, update,"""
    Interaction_Create = Interaction
    """Slash_Command"""
