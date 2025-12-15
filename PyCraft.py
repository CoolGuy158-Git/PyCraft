from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()
WORLD_WIDTH = 20
WORLD_DEPTH = 10
GROUND_LEVEL = 0
COBBLE_DEPTH = 10
RESPAWN_HEIGHT = 5
VOID_LEVEL = -COBBLE_DEPTH - 10

block_textures = {
    'grass': 'grass.jpg',
    'cobblestone': 'cobble.jpeg',
    'bedrock': 'bedrock.jpeg'
}

blocks = []
for x in range(WORLD_WIDTH):
    for z in range(WORLD_DEPTH):
        blocks.append(Entity(model='cube', texture=block_textures['grass'],
                             position=(x, GROUND_LEVEL, z), collider='box'))
        for y in range(1, COBBLE_DEPTH + 1):
            blocks.append(Entity(model='cube', texture=block_textures['cobblestone'],
                                 position=(x, -y, z), collider='box'))
        blocks.append(Entity(model='cube', texture=block_textures['bedrock'],
                             position=(x, -COBBLE_DEPTH - 1, z), collider='box'))
current_block = 'grass'
def input(key):
    global current_block
    if hasattr(mouse, 'hovered_entity') and mouse.hovered_entity in blocks:
        block = mouse.hovered_entity
        if key == 'left mouse down':
            new_block = Entity(
                model='cube',
                texture=block_textures[current_block],
                position=block.position + mouse.normal,
                collider='box'
            )
            blocks.append(new_block)
        if key == 'right mouse down':
            if hasattr(block, 'collider') and block.texture.name != 'bedrock.jpeg':
                blocks.remove(block)
                destroy(block)
    if key == '1':
        current_block = 'grass'
    if key == '2':
        current_block = 'cobblestone'

    if key == 'escape':
        application.quit()
def update():
    if player.y < VOID_LEVEL:
        player.position = (WORLD_WIDTH // 2, GROUND_LEVEL + RESPAWN_HEIGHT, WORLD_DEPTH // 2)
        player.velocity_y = 0
app.run()

