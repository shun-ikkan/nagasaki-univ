#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("cv1.progrape.jp")
#mc = minecraft.Minecraft.create("bes-master.cis.nagasaki-u.ac.jp")
pos = mc.player.getPos()

#please your current position
pos.x = -2384;
pos.y = 4;
pos.z = -260;

pos.x += 1931
pos.y += -4
pos.z += 899

#mc.setBlock(pos.x, pos.y, pos.z-1, block.FLOWING_WATER.id)

for i in range(0, 120):
 for j in range(0, 6):
  for k in range(0, 6):
     mc.setBlock(pos.x+j, pos.y+i, pos.z+k, block.IRON_BLOCK.id);

for i in range(0, 120):
 for j in range(0, 6):
  for k in range(0, 6):
     mc.setBlock(pos.x+j+19, pos.y+i, pos.z+k, block.IRON_BLOCK.id);

for i in range(0, 120):
 for j in range(0, 6):
  for k in range(0, 6):
     mc.setBlock(pos.x+j, pos.y+i, pos.z+k+19, block.IRON_BLOCK.id);

for i in range(0, 120):
 for j in range(0, 6):
  for k in range(0, 6):
     mc.setBlock(pos.x+j+19, pos.y+i, pos.z+k+19, block.IRON_BLOCK.id);

for i in range(0, 118):
 for j in range(0, 23):
  for k in range(0, 23):
     if i % 5 == 0:
        mc.setBlock(pos.x+j+1, pos.y+i, pos.z+k+1, block.SANDSTONE.id);
     else:
        mc.setBlock(pos.x+j+1, pos.y+i, pos.z+k+1, block.GLASS.id);
