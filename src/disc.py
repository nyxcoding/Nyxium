import discord
from discord.ext import commands
from discord import app_commands
import re


client = None

syncAsk = False
events = []
commands_list = []
slash_commands = []

requested_intents = []


def setIntents(*intent_names):

    global requested_intents

    requested_intents = list(intent_names)


def create_client():

    global client

    intents = discord.Intents.default()

    # Keep the current Nyxium behaviour
    intents.message_content = True

    for intent in requested_intents:

        if intent == "members":
            intents.members = True

        elif intent == "messageContent":
            intents.message_content = True

        elif intent == "presences":
            intents.presences = True

        elif intent == "guilds":
            intents.guilds = True

        elif intent == "messages":
            intents.messages = True

        elif intent == "reactions":
            intents.reactions = True

        elif intent == "voiceStates":
            intents.voice_states = True

        elif intent == "typing":
            intents.typing = True

    client = commands.Bot(
        command_prefix="!",
        intents=intents,
        help_command=None
    )


# --------------------------------
# MESSAGE PROCESSING
# --------------------------------

def process_message(message):

    embeds = []

    # ------------------------------
    # IMAGES
    # ------------------------------

    image_pattern = r"\{image\[(.*?)\]\}"

    image_matches = re.findall(
        image_pattern,
        message
    )

    for image_url in image_matches:

        embed = discord.Embed()

        embed.set_image(
            url=image_url
        )

        embeds.append(embed)

    message = re.sub(
        image_pattern,
        "",
        message
    )

    # ------------------------------
    # EMBEDS
    # ------------------------------

    embed_pattern = r"\{embed\[(.*?)\]\}"

    embed_matches = re.findall(
        embed_pattern,
        message
    )

    for embed_data in embed_matches:

        parts = [
            part.strip()
            for part in embed_data.split(";")
        ]

        if len(parts) < 2:
            continue

        title = parts[0]
        description = parts[1]

        embed = discord.Embed(
            title=title,
            description=description
        )

        if len(parts) >= 3:

            image_url = parts[2]

            if image_url:
                embed.set_image(
                    url=image_url
                )

        embeds.append(embed)

    message = re.sub(
        embed_pattern,
        "",
        message
    )

    message = message.strip()

    return message, embeds


# --------------------------------
# BOT HANDLE
# --------------------------------

def handle(token):

    global syncAsk

    create_client()

    @client.event
    async def on_ready():

        if syncAsk:
            await client.tree.sync()

        for name, channelId, respond in events:

            if name == "onReady":

                channel = client.get_channel(
                    int(channelId)
                )

                if channel:

                    response, embeds = process_message(
                        respond
                    )

                    if embeds:

                        await channel.send(
                            response,
                            embeds=embeds
                        )

                    else:

                        await channel.send(
                            response
                        )

    @client.event
    async def on_member_join(member):

        for name, channelId, respond in events:

            if name == "memberJoin":

                response = respond

                if "{member}" in response:

                    response = response.replace(
                        "{member}",
                        member.mention
                    )

                channel = client.get_channel(
                    int(channelId)
                )

                if channel:

                    response, embeds = process_message(
                        response
                    )

                    if embeds:

                        await channel.send(
                            response,
                            embeds=embeds
                        )

                    else:

                        await channel.send(
                            response
                        )

    # --------------------------------
    # COMMANDS
    # --------------------------------

    for (
        name,
        message
    ) in commands_list:

        def make_command(response_message):

            async def command(ctx):

                userid = ctx.author.id

                response = response_message.replace(
                    "{userid}",
                    f"<@{userid}>"
                )

                response, embeds = process_message(
                    response
                )

                if embeds:

                    await ctx.send(
                        response,
                        embeds=embeds
                    )

                else:

                    await ctx.send(
                        response
                    )

            return command

        client.command(
            name=name
        )(
            make_command(message)
        )

    # --------------------------------
    # SLASH COMMANDS
    # --------------------------------

    for (
        name,
        description,
        message
    ) in slash_commands:

        def make_slash_command(response_message):

            async def command(
                interaction: discord.Interaction
            ):

                userid = interaction.user.id

                response = response_message.replace(
                    "{userid}",
                    f"<@{userid}>"
                )

                response, embeds = process_message(
                    response
                )

                if embeds:

                    await interaction.response.send_message(
                        response,
                        embeds=embeds
                    )

                else:

                    await interaction.response.send_message(
                        response
                    )

            return command

        command = make_slash_command(
            message
        )

        client.tree.add_command(
            app_commands.Command(
                name=name,
                description=description,
                callback=command
            )
        )

    client.run(token)


# --------------------------------
# COMMAND REGISTRATION
# --------------------------------

def clientCommand(
    name,
    message
):

    commands_list.append(
        (
            name,
            message
        )
    )


def applicationCommand(
    name,
    description,
    message
):

    slash_commands.append(
        (
            name,
            description,
            message
        )
    )


def sync():

    global syncAsk

    syncAsk = True


def event(
    name,
    channelId,
    respond
):

    events.append(
        (
            name,
            channelId,
            respond
        )
    )