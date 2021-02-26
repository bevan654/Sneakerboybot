from discord_webhook import DiscordWebhook, DiscordEmbed
from openD import openData as openData

options = openData('options.json')

webhook = DiscordWebhook(url=options['data']['webhook'])

# create embed object for webhook
embed = DiscordEmbed(title='SNKRLab AU', description=None, color=242424)
embed.add_embed_field(name='STATUS',value='WEBHOOK READY')
embed.set_footer(text='SNKRLab CLI - Helping members make money',icon_url='https://media.discordapp.net/attachments/782532739001614347/787653010142396446/SNKRLAB_21.png')
embed.set_timestamp()

webhook.add_embed(embed)

response = webhook.execute()