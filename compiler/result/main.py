import asyncio


class Generate_角色1(scgame.Sprite):

    async def event_whenflagclicked_1(self):
        for _ in range(1234):  # repeat 1234 times.
            await self.glide_to(0, 0, secs=100)  # gilde to (0, 0) in 100s.
            await asyncio.sleep(0)  # [DO NOT DEL] yield to other coroutines.
        while True:  # infinity loop.
            if game.var('我的变量', '`jEk@4|i[#Fk?(8x)AV.-my variable') == '50':
                if game.is_keypressed('space'):
                    await self.think_bubble('嗯……', secs=222)  # think '嗯……' for 222s.
                else:
                    await self.think_bubble('嗯……', secs=333)  # think '嗯……' for 333s.
            await asyncio.sleep(0)  # [DO NOT DEL] yield to other coroutines.

    async def event_whenflagclicked_2(self):
        await self.move_forward(scgame.random(1, 10))  # move forward for scgame.random(1, 10) steps.
        await self.move_forward(10)  # move forward for 10 steps.
        game.stop('all')  # stop all.

    async def event_whenflagclicked(self):
        await self.event_whenflagclicked_1()
        await self.event_whenflagclicked_2()
