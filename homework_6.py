class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"

class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return "Я светящийся и летающий стример!"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return "Снимаю трендовые тик-токи со своими суперсилами!"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return "Стримлю танцуя под все трендовые треки!"

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

characters = [GlowStreamer(),
              ViralCyborg(),
              DonateMage()
]

for character in characters:
    print(character.live())
    print(character.ultimate_content())

