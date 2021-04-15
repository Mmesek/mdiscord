# -*- coding: utf-8 -*-
'''
Discord Types
----------

Model overrides with additional convinience methods.

:copyright: (c) 2021 Mmesek

'''

from __future__ import annotations
from .models import * # noqa: F401

class UserID(Snowflake):
    '''Snowflake representing UserID'''
    def __str__(self):
        return "users"

class ChannelID(Snowflake):
    '''Snowflake representing ChannelID'''
    def __str__(self):
        return "channels"

class RoleID(Snowflake):
    '''Snowflake representing RoleID'''
    def __str__(self):
        return "roles"

class GuildID(Snowflake):
    '''Snowflake representing GuildID'''
    pass

#class CDN_Endpoints(CDN_Endpoints):
#    @classmethod
#    def cdn(cls, value):
#        return CDN_URL + cls.value

class Discord_Paths(Enum):
    MessageLink = "channels/{guild_id}/{channel_id}/{message_id}"
    @property
    def link(self) -> str:
        return BASE_URL + self.value

from typing import Dict

@dataclass
class Application_Command_Interaction_Data(Application_Command_Interaction_Data):
    resolved: Resolved = None

@dataclass
class Resolved(DiscordObject):
    members: Dict[Snowflake, Guild_Member] = dict
    users: Dict[Snowflake, User] = dict
    roles: Dict[Snowflake, Role] = dict
    channels: Dict[Snowflake, Channel] = dict

@dataclass
class Embed(Embed):
    def setTitle(self, title: str) -> Embed:
        '''Sets Embed's Title respecting title limit if it's not above total limit'''
        title = str(title)[:Limits.TITLE]
        if self.total_characters + len(str(title)) <= Limits.TOTAL:
            self.title = title
        return self

    def setDescription(self, description:str) -> Embed:
        '''Sets Embed's Description respecting description limit if it's not above total limit'''
        description = str(description)[:Limits.DESCRIPTION]
        if self.total_characters + len(str(description)) <= Limits.TOTAL:
            self.description = description
        return self

    def setColor(self, color) -> Embed:
        '''Set's Embed's Color. 

        Params
        -------
        color:
            Accepts HEX string, RGB Tuple or final Integer'''
        if type(color) == str and '#' in color:
            color = int(color.lstrip('#'), 16)
        elif type(color) == tuple:
            color = (color[0]<<16) + (color[1]<<8) + color[2]
        self.color = color
        return self

    def setUrl(self, url:str) -> Embed:
        self.url = url
        return self

    def setImage(self, url:str, proxy_url:str=None, height:int=None, width:int=None) -> Embed:
        '''Sets Embed's Image'''
        self.image = Embed_Image(url=url, proxy_url=proxy_url, height=height, width=width)
        return self

    def setThumbnail(self, url:str, proxy_url:str=None, height:int=None, width:int=None) -> Embed:
        '''Sets Embed's Thumbnail'''
        self.thumbnail = Embed_Thumbnail(url=url, proxy_url=proxy_url, height=height, width=width)
        return self

    def setFooter(self, text:str='', icon_url:str=None, proxy_icon_url:str=None) -> Embed:
        '''Sets Embed's Footer respecting footer's text limit'''
        text = str(text)[:Limits.FOOTER_TEXT]
        if self.total_characters + len(str(text)) <= Limits.TOTAL:
            self.footer = Embed_Footer(text=text, icon_url=icon_url, proxy_icon_url=proxy_icon_url)
        return self

    def setTimestamp(self, timestamp) -> Embed:
        self.timestamp = timestamp
        return self

    def setAuthor(self, name:str='', url:str=None, icon_url:str=None, proxy_icon_url:str=None) -> Embed:
        '''Sets Embed's Author respecting author's name limit if it's not above total limit'''
        name = str(name)[:Limits.AUTHOR_NAME]
        if self.total_characters + len(str(name)) <= Limits.TOTAL:
            self.author = Embed_Author(name=name, url=url, icon_url=icon_url, proxy_icon_url=proxy_icon_url)
        return self

    def addField(self, name:str, value:str, inline:bool=False) -> Embed:
        '''Adds single field respecting limits if it's not above total limit'''
        name = str(name)[:Limits.FIELD_NAME]
        value = str(value)[:Limits.FIELD_VALUE]
        value = str(value)[:Limits.TOTAL - self.total_characters]

        if self.total_characters + len(str(name)) + len(str(value)) <= Limits.TOTAL:
            self.fields.append(Embed_Field(name=name, value=value, inline=inline))
        return self
    
    def addFields(self, title: str, text: str, inline:bool=False) -> Embed:
        '''
        Adds as many fields as neccessary to store whole text 
        while respecting limits and as long as it's not above total Embed's limit'''
        from textwrap import wrap
        for x, chunk in enumerate(wrap(text, Limits.FIELD_VALUE, replace_whitespace=False)):
            if len(self.fields) == Limits.FIELDS:
                break
            if x == 0:
                self.addField(title, chunk, inline)
            else:
                self.addField('\u200b', chunk, inline)
        return self

    @property
    def total_characters(self) -> int:
        return len(self.title or "") + len(self.description or "") + len(self.author.name or "" if self.author else "") + len(self.footer.text or "" if self.footer else "") + sum([len(field.name) + len(field.value) for field in self.fields])

@dataclass
class Message(Message):
    embeds: List[Embed] = list
    async def reply(self, content="", embed=None, file: bytes = None, filename: str="file.txt") -> Message:
        '''Creates replay message'''
        return await self._Client.create_message(self.channel_id,
        content=content if content != "" else self.content,
        embed=embed if embed else self.embeds[0] if self.embeds != [] else None, 
        filename=filename, file=file,
        message_reference=Message_Reference(message_id=self.id, channel_id=self.channel_id, guild_id=self.guild_id if self.guild_id != 0 else None))
    
    async def delete(self) -> None:
        '''Deletes message'''
        return await self._Client.delete_message(self.channel_id, self.id)
    
    async def edit(self) -> Message:
        '''Edits message'''
        return await self._Client.edit_message(self.channel_id, self.id, self.content, self.embeds[0], self.flags, self.allowed_mentions)
    
    async def send(self) -> Message:
        '''Creates new message'''
        return await self._Client.create_message(self.channel_id, content=self.content, embed=self.embeds[0])
    
    async def webhook(self, webhook_id: Snowflake, webhook_token: int, username: str = None, avatar_url: str = None, file: bytes = None) -> Message:
        '''Sends message as a webhook'''
        return await self._Client.execute_webhook(webhook_id, webhook_token, content=self.content, username=username, avatar_url=avatar_url, file=file, embeds=self.embeds, allowed_mentions=self.allowed_mentions)
    
    async def webhook_edit(self, webhook_id, webhook_token, content: str = None, embeds: List[Embed] = None, allowed_mentions: Allowed_Mentions = None) -> None:
        '''Edits webhook message'''
        return await self._Client.edit_webhook_message(webhook_id, webhook_token, self.id, content, embeds, allowed_mentions)
    
    async def get(self) -> Message:
        '''Fetches message'''
        return await self._Client.get_channel_message(self.channel_id, self.id)

    async def react(self, reaction) -> None:
        '''Reacts to message'''
        return await self._Client.create_reaction(self.channel_id, self.id, reaction)
    
    async def get_reactions(self, emoji, users=[], last_id=0, limit=100):
        #for chunk in range(int(count / 100) + (count % 100 > 0)): #Alternative pagination method
        r = await self._Client.get_reactions(self.channel_id, self.id, emoji, after=last_id, limit=limit)
        if len(r) < limit or len(r) == 0:
            return [i for i in users+r if i.id != self._Client.user_id]
        return await self.get_reactions(emoji, users=users+r, last_id=r[-1].id)

    async def delete_reaction(self, reaction) -> None:
        '''Deletes reaction'''
        return await self._Client.delete_own_reaction(self.channel_id, self.id, reaction)
    
    async def publish(self) -> Message:
        '''Publishes Message'''
        return await self._Client.crosspost_message(self.channel_id, self.id)

@dataclass
class Guild(Guild):
    def get_icon(self) -> str:
        return CDN_URL+CDN_Endpoints.Guild_Icon.value.format(guild_id=self.id, guild_icon=self.icon)
    def get_splash(self) -> str:
        return CDN_URL+CDN_Endpoints.Guild_Splash.value.format(guild_id=self.id, guild_splash=self.splash)
    def get_discovery_splash(self) -> str:
        return CDN_URL+CDN_Endpoints.Guild_Discovery_Splash.value.format(guild_id=self.id, guild_discovery_splash=self.discovery_splash)
        

@dataclass
class User(User):
    def get_avatar(self) -> str:
        if self.avatar:
            return CDN_URL+CDN_Endpoints.User_Avatar.value.format(user_id=self.id, user_avatar=self.avatar)
        return CDN_URL+CDN_Endpoints.Default_User_Avatar.value.format(user_discriminator=self.discriminator % 5)


@dataclass
class Interaction(Interaction):
    data: Application_Command_Interaction_Data = None
    async def pong(self):
        '''Pongs'''
        response = Interaction_Response(
            type=Interaction_Response_Type.PONG,
            data=None
        )
        return await self._Client.create_interaction_response(self.id, self.token, response)
    async def ack(self):
        '''Sends ACK message to Discord to prevent token from expiring.
        Use it if processing takes more than 3 seconds'''
        response = Interaction_Response(
            type=Interaction_Response_Type.ACKNOWLEDGE,
            data=None
        )
        return await self._Client.create_interaction_response(self.id, self.token, response)
    async def respond_private(self, content: str=None, embeds: List[Embed]=None, flags: int=64):
        return await self._Client.create_interaction_response(self.id, self.token, Interaction_Response(
            type=Interaction_Response_Type.CHANNELMESSAGEWITHSOURCE, data=Interaction_Application_Command_Callback_Data(content=content, embeds=embeds, allowed_mentions=Allowed_Mentions(parse=[]), flags=flags)
            )
        )
    async def deffered_message(self):
        '''Acknowledges Interaction with Source'''
        return await self._Client.create_interaction_response(self.id, self.token, Interaction_Response(
            type=Interaction_Response_Type.DEFFERED_CHANNEL_MESSAGE_WITH_SOURCE, data=Interaction_Application_Command_Callback_Data(flags=64))
        )
    async def send(self, content: str=None, embeds: List[Embed]=None):
        '''Responds to Channel with Source'''
        return await self._Client.create_interaction_response(self.id, self.token, 
            Interaction_Response(
                type=Interaction_Response_Type.CHANNELMESSAGEWITHSOURCE, 
                data=Interaction_Application_Command_Callback_Data(
                    content=content, 
                    embeds=embeds, 
                    allowed_mentions=Allowed_Mentions(parse=[]))
                )
            )
    async def respond(self, response: Interaction_Response):
        '''Responds to a message'''
        return await self._Client.create_interaction_response(self.id, self.token, response)
    async def edit_response(self, content: str = None, embeds: List[Embed] = None, allowed_mentions: Allowed_Mentions = None):
        '''Edits response'''
        return await self._Client.edit_original_interaction_response(self._Client.application.id, self.token, content, embeds, allowed_mentions)
    async def delete_response(self):
        '''Deletes response'''
        return await self._Client.delete_original_interaction_response(self._Client.application.id, self.token)
    async def reply(self, content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, file: bytes = None, filename=None, embeds: List[Embed] = None, payload_json: str = None, allowed_mentions: Allowed_Mentions = [], wait: bool = False):
        '''Creates followup message'''
        return await self._Client.create_followup_message(self._Client.application.id, self.token, wait=wait, content=content, username=username, avatar_url=avatar_url, tts=tts, file=file, filename=filename, embeds=embeds, payload_json=payload_json, allowed_mentions=allowed_mentions)
    async def edit(self, message_id, content: str = None, embeds: List[Embed] = None, allowed_mentions: Allowed_Mentions = []):
        '''Edits followup message'''
        return await self._Client.edit_followup_message(self._Client.application.id, self.token, message_id, content, embeds, allowed_mentions)
    async def delete(self, message_id):
        '''Deletes followup message'''
        return await self._Client.delete_followup_message(self._Client.application.id, self.token, message_id)


class Gateway_Events(Events):
    '''
    Params:
        :Hello: defines the heartbeat interval
        :Ready: contains the initial state information
        :Resumed: Resume
        :Reconnect: server is going away, client should reconnect to gateway and resume
        :Invalid_Session: Identify
        :Channel_Create: new guild channel created
        :Channel_Update: channel was updated
        :Channel_Delete: channel was deleted
        :Channel_Pins_Update: message was pinned
        :Guild_Create: lazy-load for unavailable guild, guild became available,
        :Guild_Update: guild was updated
        :Guild_Delete: guild became unavailable,
        :Guild_Ban_Add: user was banned from a guild
        :Guild_Ban_Remove: user was unbanned from a guild
        :Guild_Emojis_Update: guild emojis were updated
        :Guild_Integrations_Update: guild integration was updated
        :Guild_Member_Add: new user joined a guild
        :Guild_Member_Remove: user was removed from a guild
        :Guild_Member_Update: guild member was updated
        :Guild_Members_Chunk: Request_Guild_Members
        :Guild_Role_Create: guild role was created
        :Guild_Role_Update: guild role was updated
        :Guild_Role_Delete: guild role was deleted
        :Invite_Create: invite to a channel was created
        :Invite_Delete: invite to a channel was deleted
        :Message_Create: message was created
        :Message_Update: message was edited
        :Message_Delete: message was deleted
        :Message_Delete_Bulk: multiple messages were deleted at once
        :Message_Reaction_Add: user reacted to a message
        :Message_Reaction_Remove: user removed a reaction from a message
        :Message_Reaction_Remove_All: all reactions were explicitly removed from a message
        :Message_Reaction_Remove_Emoji: all reactions for a given emoji were explicitly removed from a message
        :Presence_Update: user was updated
        :Typing_Start: user started typing in a channel
        :User_Update: properties about the user changed
        :Voice_State_Update: someone joined, left,
        :Voice_Server_Update: guild's voice server was updated
        :Webhooks_Update: guild channel webhook was created, update,
        :Interaction_Create: Slash_Command
    '''
    Hello = staticmethod(Hello)
    Ready = staticmethod(Ready)
    Resumed = staticmethod(Resume)
    Reconnect = staticmethod(dict)
    Invalid_Session = staticmethod(bool)
    Channel_Create = staticmethod(Channel)
    Channel_Update = staticmethod(Channel)
    Channel_Delete = staticmethod(Channel)
    Channel_Pins_Update = staticmethod(Channel_Pins_Update)
    Guild_Create = staticmethod(Guild)
    Guild_Update = staticmethod(Guild)
    Guild_Delete = staticmethod(dict)
    Guild_Ban_Add = staticmethod(Guild_Ban_Add)
    Guild_Ban_Remove = staticmethod(Guild_Ban_Remove)
    Guild_Emojis_Update = staticmethod(Guild_Emojis_Update)
    Guild_Integrations_Update = staticmethod(Guild_Integrations_Update)
    Guild_Member_Add = staticmethod(Guild_Member_Add)
    Guild_Member_Remove = staticmethod(Guild_Member_Remove)
    Guild_Member_Update = staticmethod(Guild_Member_Update)
    Guild_Members_Chunk = staticmethod(Guild_Members_Chunk)
    Guild_Role_Create = staticmethod(Guild_Role_Create)
    Guild_Role_Update = staticmethod(Guild_Role_Update)
    Guild_Role_Delete = staticmethod(Guild_Role_Delete)
    Invite_Create = staticmethod(Invite_Create)
    Invite_Delete = staticmethod(Invite_Delete)
    Message_Create = staticmethod(Message)
    Message_Update = staticmethod(Message)
    Message_Delete = staticmethod(Message_Delete)
    Message_Delete_Bulk = staticmethod(Message_Delete_Bulk)
    Message_Reaction_Add = staticmethod(Message_Reaction_Add)
    Message_Reaction_Remove = staticmethod(Message_Reaction_Remove)
    Message_Reaction_Remove_All = staticmethod(Message_Reaction_Remove_All)
    Message_Reaction_Remove_Emoji = staticmethod(Message_Reaction_Remove_Emoji)
    Presence_Update = staticmethod(Presence_Update)
    Typing_Start = staticmethod(Typing_Start)
    User_Update = staticmethod(User)
    Voice_State_Update = staticmethod(Voice_State)
    Voice_Server_Update = staticmethod(Voice_Server_Update)
    Webhooks_Update = staticmethod(Webhook_Update)
    Interaction_Create = staticmethod(Interaction)
