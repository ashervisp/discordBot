from discord.ext import process_commands

class Test:

    @commands.command()
    async def add(self):
        self.counter += 1
        await self.bot.say('Counter is now %d' % self.counter)

def setup(bot):
    bot.add_cog(TestCog(bot))
