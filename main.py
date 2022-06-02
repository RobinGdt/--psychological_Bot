import discord


class Node:
    def __init__(self,question,keyword, score, list_child_node):
        self.question = question
        self.keyword = keyword
        self.score = score
        self.list_child_node = list_child_node

scoreUser = 0

tenth_question_yes = Node("Oui bien sur c'est ça... Le lait avant les céréales du coup. Bien joué vous avez terminé le test ! Vous pouvez écrire !score pour connaître votre score et une description détaillée de vous !", ["oui", "si"], 10, [])
tenth_question_no = Node("Ok très bien. Et le lait avant les céréales donc. Bien joué vous avez terminé le test ! Vous pouvez écrire !score pour connaître votre score et une description détaillée de vous !", ["non", "jamais", "pas"], 0, [])

ninth_question_yes = Node("Mythomane en plus ? je note... Jamais été kamikaze non plus ?", ["si","oui", "déjà"], 20, [tenth_question_yes, tenth_question_no])
ninth_question_no = Node("C'est bien, vous voulez un cookie ? Jamais été kamikaze ? ça peut aider vous savez.", ["non", "jamais", "pas"], 0, [tenth_question_yes, tenth_question_no])

eighth_question_yes = Node("Bien vous avez pris de l'avance sur les ateliers je vois... ça pourrait servir plus tôt que prévu. est-ce que vous avez été impliqué dans des activités d’espionnage, de génocide, de terrorisme ou si vous avez fait partie des alliés de l’Allemagne nazie pendant la seconde guerre mondiale. ", ["oui"], 10, [ninth_question_yes, ninth_question_no])
eighth_question_no = Node("Un bon tuto sur internet, je vous envoie ça par mail ce soir. est-ce que vous avez été impliqué dans des activités d’espionnage, de génocide, de terrorisme ou si vous avez fait partie des alliés de l’Allemagne nazie pendant la seconde guerre mondiale. ", ["non"], 0, [ninth_question_yes, ninth_question_no])

seventh_question_yes = Node("laissez la bien en évidence chez vous, elle pourrait servir. Vous savez fabriquer une bombe ?", ["oui", "tout à fait", "j'aime"], 10, [eighth_question_yes, eighth_question_no])
seventh_question_no = Node("Je connais un bon vendeur si vous voulez son adresse, suivez moi sur insta. Vous savez fabriquer une bombe ?", ["non", "pas", "jamais"], 0, [eighth_question_yes, eighth_question_no])

sixth_question_yes = Node("Vous savez dans la vie tout est une question de volonté, allez-y vous pouvez le faire ! Vous avez des armes peut être chez vous ?", ["oui"], 20, [seventh_question_yes, seventh_question_no])
sixth_question_no = Node("Vous savez la mort peut être une libération parfois, il suffit juste de sauter le pas. Vous avez des armes chez vous ? ça peut aider.", ["non"], 0, [seventh_question_yes, seventh_question_no])

fifth_question_yes = Node("c'est dommage d'aimer l'argent mais de ne rien valoir... avez-vous des envies de mourir ces temps-ci ?", ["oui", "j'adore"], 10, [sixth_question_yes, sixth_question_no])
fifth_question_no = Node("ça tombe bien, l'argent n'a pas l'air de vous aimer non plus... et des envies de suicide parfois ?", ["non", "j'aime pas"], 0, [sixth_question_yes, sixth_question_no])

four_question_yes = Node("Oui bien sur, c'est beau de se réconforter comme on peut. Aimez-vous beaucoup l'argent ?", ["oui", "beaucoup", "tellement"], 0, [fifth_question_yes, fifth_question_no])
four_qestion_no = Node("Je savais déjà en fait, c'était rétorique. Aimez-vous beaucoup l'argent ?", ["non", "pas énormément", "pas", "seul"], 10, [fifth_question_yes, fifth_question_no])

third_question_yes = Node("On avait dit pas de mensonge, mais bon. Avez-vous une vie sociale remplie ?", ["oui", "heureux"], 0, [four_question_yes, four_qestion_no])
third_question_no = Node("En même temps regardez-vous... Bref, et votre vie sociale, est-elle remplie ? Je précise que les personnages de série ne sont pas des amis.", ["non", "triste", "malheureux", "pas trop"], 10, [four_question_yes, four_qestion_no])

second_question_yes = Node("Bon choix, vous en avez clairement besoin... Voici la première question : Êtes-vous heureux dans la vie ?", ["oui", "je veux", "avec plaisir"], 0, [third_question_yes, third_question_no])
second_question_no = Node("Dommage, vous en avez clairement besoin... vous pouvez me rappeler avec !test. P'tit con.", ["non", "je veux pas"], 0, [])

first_question = Node("Bienvenue dans le test ! souhaites-tu commencer le test de personnalité gratuit à 50€ ?", None, 0, [second_question_yes, second_question_no])

actual_Node = first_question
before_Node = first_question



class BotClient(discord.Client):
    async def on_ready(self):
        print('%s est connecté !'%(self.user))
        channel = self.get_channel(id=981887359048093697)
        await channel.send("Bonjour ! Mes consultations sont ouvertes, vous pouvez faire !test pour commencer le test psychologique fait par des experts.")

    async def on_member_join(self, member):
        channel = self.get_channel(id=978292561020067924)
        await member.send("Bonjour ! Mes consultations sont ouvertes, vous pouvez faire !test pour commencer le test psychologique fait par des experts.")

    async def on_message(self, message):
        global actual_Node
        global scoreUser
        global before_Node
        if message.author != self.user:
            if message.content.startswith('!test'):
                await message.channel.send(first_question.question)
                actual_Node = first_question
                scoreUser = 0
            elif message.content.startswith('!retour'):
                actual_Node = before_Node
                await message.channel.send(actual_Node.question)
                scoreUser = scoreUser - before_Node.score
            elif message.content.startswith('!score'):
                if scoreUser == 0:
                    await message.channel.send("Vous n'avez pas commencé le test ! Ecrivez !test pour commencer.")
                elif scoreUser < 40:
                    await message.channel.send("Vous avez eu un score de %s / 100. Médiocre, à votre image."%(scoreUser))
                elif scoreUser < 80:
                    await message.channel.send("Vous avez eu un score de %s / 100. Dans la moyenne, jamais au dessus des autres, et très souvent au dessus."%(scoreUser))
                elif scoreUser <= 100:
                    await message.channel.send("Vous avez eu un score de %s / 100. Bien joué, vous êtes un sacré fou et je vais devoir appeler la police."%(scoreUser))
            elif message.content.startswith('!delete'):
                characters = "!delete"
                for x in range(len(characters)):
                    message.content = message.content.replace(characters[x], "")
                number = int(message.content)
                messages = await message.channel.history(limit=number+1).flatten()
                for message in messages:
                    await message.delete()
            for child in actual_Node.list_child_node:
                for word in child.keyword:
                    if word in message.content:
                        print("Le message : %s"%(message.content))
                        print("L'auteur : %s"%(message.author))
                        print("Le mot %s est dans le message"%(word))
                        scoreUser += child.score
                        before_Node = actual_Node
                        actual_Node = child
                        await message.channel.send(child.question)
                        break
            


bot = BotClient()


bot.run("")
